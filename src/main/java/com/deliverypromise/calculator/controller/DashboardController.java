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
    public String dashboard(Model model) {
        model.addAttribute("total", deliveryService.getTotalDeliveries());
        model.addAttribute("pending", deliveryService.getPendingDeliveries());
        model.addAttribute("delivered", deliveryService.getDeliveredDeliveries());
        return "dashboard";
    }
}
