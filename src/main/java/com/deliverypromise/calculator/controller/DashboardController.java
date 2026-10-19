package com.deliverypromise.calculator.controller;

import com.deliverypromise.calculator.service.DeliveryService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class DashboardController {

    private final DeliveryService deliveryService;

    public DashboardController(DeliveryService deliveryService) {
        this.deliveryService = deliveryService;
    }

    @GetMapping("/dashboard")
    public String dashboard(jakarta.servlet.http.HttpSession session, Model model) {
        Object role = session.getAttribute("role");
        model.addAttribute("role", role == null ? "CUSTOMER" : role.toString());
        model.addAttribute("total", deliveryService.getTotalDeliveries());
        model.addAttribute("pending", deliveryService.getPendingDeliveries());
        model.addAttribute("delivered", deliveryService.getDeliveredDeliveries());
        return "dashboard";
    }
}
