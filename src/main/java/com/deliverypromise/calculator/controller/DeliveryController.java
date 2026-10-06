package com.deliverypromise.calculator.controller;

import com.deliverypromise.calculator.model.Delivery;
import com.deliverypromise.calculator.service.DeliveryService;
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
            Model model) {

        model.addAttribute("delivery", new Delivery());
        model.addAttribute("deliveries", deliveryService.searchDeliveries(keyword));
        model.addAttribute("keyword", keyword == null ? "" : keyword);
        model.addAttribute("total", deliveryService.getTotalDeliveries());
        model.addAttribute("pending", deliveryService.getPendingDeliveries());
        model.addAttribute("delivered", deliveryService.getDeliveredDeliveries());

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
            @RequestParam String status) {

        deliveryService.updateStatus(id, status);
        return "redirect:/deliveries";
    }
}
