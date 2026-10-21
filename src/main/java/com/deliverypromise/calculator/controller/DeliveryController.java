package com.deliverypromise.calculator.controller;

import com.deliverypromise.calculator.model.Delivery;
import com.deliverypromise.calculator.service.DeliveryService;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.List;

@Controller
public class DeliveryController {

    private final DeliveryService deliveryService;

    public DeliveryController(DeliveryService deliveryService) {
        this.deliveryService = deliveryService;
    }

    @GetMapping("/deliveries")
    public String deliveries(
            @RequestParam(required = false) String keyword,
            @RequestParam(required = false) String status,
            @RequestParam(required = false) String error,
            @RequestParam(required = false) String success,
            HttpSession session,
            Model model) {

        String role = getRole(session);

        List<Delivery> list;
        if (keyword != null && !keyword.isBlank()) {
            list = deliveryService.searchDeliveries(keyword);
        } else if (status != null && !status.isBlank() && !"ALL".equalsIgnoreCase(status)) {
            list = deliveryService.getDeliveriesByStatus(status);
        } else {
            list = deliveryService.getAllDeliveries();
        }

        model.addAttribute("delivery", new Delivery());
        model.addAttribute("deliveries", list);
        model.addAttribute("keyword", keyword == null ? "" : keyword);
        model.addAttribute("selectedStatus", status == null || status.isBlank() ? "ALL" : status.toUpperCase());

        model.addAttribute("total", deliveryService.getTotalDeliveries());
        model.addAttribute("pending", deliveryService.getPendingDeliveries());
        model.addAttribute("processing", deliveryService.getProcessingDeliveries());
        model.addAttribute("shipped", deliveryService.getShippedDeliveries());
        model.addAttribute("delivered", deliveryService.getDeliveredDeliveries());
        model.addAttribute("cancelled", deliveryService.getCancelledDeliveries());
        model.addAttribute("slaRate", deliveryService.getOnTimeSlaRate());
        model.addAttribute("avgDays", deliveryService.getAverageDeliveryDays());

        model.addAttribute("role", role);
        model.addAttribute("user", session.getAttribute("user") != null ? session.getAttribute("user").toString() : "guest");
        model.addAttribute("displayName", session.getAttribute("displayName") != null ? session.getAttribute("displayName").toString() : "Guest Customer");
        model.addAttribute("avatar", session.getAttribute("avatar") != null ? session.getAttribute("avatar").toString() : "👤");

        model.addAttribute("canUpdateStatus", role.equals("ADMIN") || role.equals("OPERATIONS"));
        model.addAttribute("error", error);
        model.addAttribute("success", success);

        return "deliveries";
    }

    @PostMapping("/deliveries")
    public String createDelivery(
            @Valid @ModelAttribute Delivery delivery,
            BindingResult bindingResult,
            HttpSession session,
            Model model) {

        if (bindingResult.hasErrors()) {
            return "redirect:/deliveries?error=Invalid%20input.%20Please%20verify%20all%20required%20fields.";
        }

        Delivery created = deliveryService.createDelivery(delivery);
        return "redirect:/deliveries?success=Delivery%20record%20created%20with%20Tracking%20" + created.getTrackingNumber();
    }

    @PostMapping("/deliveries/{id}/status")
    public String updateStatus(
            @PathVariable Long id,
            @RequestParam String status,
            HttpSession session) {

        String role = getRole(session);

        if (!role.equals("ADMIN") && !role.equals("OPERATIONS")) {
            return "redirect:/deliveries?error=Only%20Admin%20or%20Operations%20users%20can%20update%20delivery%20status";
        }

        deliveryService.updateStatus(id, status);
        return "redirect:/deliveries?success=Delivery%20status%20updated%20to%20" + status.toUpperCase();
    }

    @PostMapping("/deliveries/{id}/cancel")
    public String cancelDelivery(@PathVariable Long id) {
        try {
            deliveryService.cancelDelivery(id);
        } catch (IllegalStateException e) {
            return "redirect:/deliveries?error=" + URLEncoder.encode(e.getMessage(), StandardCharsets.UTF_8);
        }
        return "redirect:/deliveries?success=Delivery%20order%20cancelled%20successfully";
    }

    @GetMapping("/deliveries/seed")
    public String seedDeliveries() {
        deliveryService.seedDemoDeliveries();
        return "redirect:/deliveries?success=Sample%20logistics%20orders%20seeded%20successfully";
    }

    @GetMapping("/deliveries/export")
    public void exportDeliveriesToCsv(HttpServletResponse response) throws IOException {
        response.setContentType("text/csv; charset=UTF-8");
        response.setHeader("Content-Disposition", "attachment; filename=\"delivery_records.csv\"");

        PrintWriter writer = response.getWriter();
        writer.println("ID,TrackingNumber,CustomerName,Address,ProductName,ShippingTier,DeliveryDays,PromisedDate,Status,OrderDate");

        List<Delivery> deliveries = deliveryService.getAllDeliveries();
        for (Delivery d : deliveries) {
            writer.printf("%d,\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",%d,%s,%s,%s%n",
                    d.getId(),
                    d.getTrackingNumber() != null ? d.getTrackingNumber() : "",
                    d.getCustomerName().replace("\"", "\"\""),
                    d.getDeliveryAddress().replace("\"", "\"\""),
                    d.getProductName().replace("\"", "\"\""),
                    d.getShippingTier() != null ? d.getShippingTier() : "STANDARD",
                    d.getDeliveryDays(),
                    d.getPromisedDate(),
                    d.getStatus(),
                    d.getOrderDate() != null ? d.getOrderDate() : ""
            );
        }
        writer.flush();
    }

    private String getRole(HttpSession session) {
        Object role = session.getAttribute("role");

        if (role == null) {
            session.setAttribute("role", "CUSTOMER");
            session.setAttribute("user", "guest");
            session.setAttribute("displayName", "Guest Customer");
            session.setAttribute("avatar", "👤");
            return "CUSTOMER";
        }

        return role.toString();
    }
}

