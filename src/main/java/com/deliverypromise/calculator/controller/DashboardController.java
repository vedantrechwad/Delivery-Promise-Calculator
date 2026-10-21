package com.deliverypromise.calculator.controller;

import com.deliverypromise.calculator.model.Delivery;
import com.deliverypromise.calculator.service.DeliveryService;
import jakarta.servlet.http.HttpSession;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;

@Controller
public class DashboardController {

    private final DeliveryService deliveryService;

    public DashboardController(DeliveryService deliveryService) {
        this.deliveryService = deliveryService;
    }

    @GetMapping("/dashboard")
    public String dashboard(HttpSession session, Model model) {
        Object role = session.getAttribute("role");
        String roleStr = role == null ? "CUSTOMER" : role.toString();
        if (role == null) {
            session.setAttribute("role", "CUSTOMER");
            session.setAttribute("user", "guest");
            session.setAttribute("displayName", "Guest Customer");
            session.setAttribute("avatar", "👤");
        }

        List<Delivery> all = deliveryService.getAllDeliveries();

        long sameDayCount = all.stream().filter(d -> "SAME_DAY".equalsIgnoreCase(d.getShippingTier())).count();
        long expressCount = all.stream().filter(d -> "EXPRESS".equalsIgnoreCase(d.getShippingTier())).count();
        long standardCount = all.stream().filter(d -> d.getShippingTier() == null || "STANDARD".equalsIgnoreCase(d.getShippingTier())).count();
        long economyCount = all.stream().filter(d -> "ECONOMY".equalsIgnoreCase(d.getShippingTier())).count();

        // Recent deliveries (up to 5)
        List<Delivery> recent = all.stream()
                .sorted((a, b) -> Long.compare(b.getId() != null ? b.getId() : 0, a.getId() != null ? a.getId() : 0))
                .limit(6)
                .toList();

        model.addAttribute("role", roleStr);
        model.addAttribute("user", session.getAttribute("user") != null ? session.getAttribute("user").toString() : "guest");
        model.addAttribute("displayName", session.getAttribute("displayName") != null ? session.getAttribute("displayName").toString() : "Guest Customer");
        model.addAttribute("avatar", session.getAttribute("avatar") != null ? session.getAttribute("avatar").toString() : "👤");

        model.addAttribute("total", deliveryService.getTotalDeliveries());
        model.addAttribute("pending", deliveryService.getPendingDeliveries());
        model.addAttribute("processing", deliveryService.getProcessingDeliveries());
        model.addAttribute("shipped", deliveryService.getShippedDeliveries());
        model.addAttribute("delivered", deliveryService.getDeliveredDeliveries());
        model.addAttribute("cancelled", deliveryService.getCancelledDeliveries());

        model.addAttribute("slaRate", deliveryService.getOnTimeSlaRate());
        model.addAttribute("avgDays", deliveryService.getAverageDeliveryDays());

        model.addAttribute("sameDayCount", sameDayCount);
        model.addAttribute("expressCount", expressCount);
        model.addAttribute("standardCount", standardCount);
        model.addAttribute("economyCount", economyCount);

        model.addAttribute("recentDeliveries", recent);

        return "dashboard";
    }
}

