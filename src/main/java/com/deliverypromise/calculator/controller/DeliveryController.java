package com.deliverypromise.calculator.controller;

import com.deliverypromise.calculator.model.Delivery;
import com.deliverypromise.calculator.service.DeliveryService;
import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class DeliveryController {

    private final DeliveryService deliveryService;

    public DeliveryController(DeliveryService deliveryService) {
        this.deliveryService = deliveryService;
    }

    @GetMapping("/deliveries")
    public String deliveries(
            @RequestParam(required = false) String keyword,
            @RequestParam(required = false) String error,
            HttpSession session,
            Model model) {

        String role = getRole(session);

        model.addAttribute("delivery", new Delivery());
        model.addAttribute("deliveries", deliveryService.searchDeliveries(keyword));
        model.addAttribute("keyword", keyword == null ? "" : keyword);
        model.addAttribute("total", deliveryService.getTotalDeliveries());
        model.addAttribute("pending", deliveryService.getPendingDeliveries());
        model.addAttribute("delivered", deliveryService.getDeliveredDeliveries());
        model.addAttribute("role", role);
        model.addAttribute("canUpdateStatus",
                role.equals("ADMIN") || role.equals("OPERATIONS"));
        model.addAttribute("error", error);

        return "deliveries";
    }

    @PostMapping("/deliveries")
    public String createDelivery(@Valid @ModelAttribute Delivery delivery) {
        deliveryService.createDelivery(delivery);
        return "redirect:/deliveries";
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
        return "redirect:/deliveries";
    }

    private String getRole(HttpSession session) {
        Object role = session.getAttribute("role");

        if (role == null) {
            session.setAttribute("role", "CUSTOMER");
            return "CUSTOMER";
        }

        return role.toString();
    }
}
