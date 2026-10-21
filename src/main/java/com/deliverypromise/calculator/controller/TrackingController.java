package com.deliverypromise.calculator.controller;

import com.deliverypromise.calculator.model.Delivery;
import com.deliverypromise.calculator.service.DeliveryService;
import jakarta.servlet.http.HttpSession;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;

import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.List;
import java.util.Optional;

@Controller
public class TrackingController {

    private final DeliveryService deliveryService;

    public TrackingController(DeliveryService deliveryService) {
        this.deliveryService = deliveryService;
    }

    @GetMapping("/track")
    public String track(
            @RequestParam(required = false) String code,
            HttpSession session,
            Model model) {

        attachSessionInfo(session, model);

        if (code != null && !code.isBlank()) {
            String trimmed = code.trim();
            Optional<Delivery> byTracking = deliveryService.getDeliveryByTrackingNumber(trimmed);

            Delivery delivery = null;
            if (byTracking.isPresent()) {
                delivery = byTracking.get();
            } else {
                List<Delivery> matches = deliveryService.searchDeliveries(trimmed);
                if (!matches.isEmpty()) {
                    delivery = matches.get(0);
                }
            }

            if (delivery != null) {
                model.addAttribute("trackedDelivery", delivery);
                model.addAttribute("currentStage", calculateStage(delivery.getStatus()));
                model.addAttribute("countdownDays", calculateCountdown(delivery));
            } else {
                model.addAttribute("notFound", true);
            }
            model.addAttribute("searchCode", trimmed);
        }

        return "track";
    }

    @GetMapping("/track/{trackingNumber}")
    public String trackDirect(
            @PathVariable String trackingNumber,
            HttpSession session,
            Model model) {
        return track(trackingNumber, session, model);
    }

    private int calculateStage(String status) {
        if (status == null) return 1;
        return switch (status.toUpperCase()) {
            case "PENDING" -> 1;
            case "PROCESSING" -> 2;
            case "SHIPPED" -> 3;
            case "DELIVERED" -> 4;
            default -> 1;
        };
    }

    private long calculateCountdown(Delivery delivery) {
        if ("DELIVERED".equalsIgnoreCase(delivery.getStatus()) || "CANCELLED".equalsIgnoreCase(delivery.getStatus())) {
            return 0;
        }
        LocalDate today = LocalDate.now();
        if (delivery.getPromisedDate() == null) return 0;
        return ChronoUnit.DAYS.between(today, delivery.getPromisedDate());
    }

    private void attachSessionInfo(HttpSession session, Model model) {
        Object role = session.getAttribute("role");
        if (role == null) {
            session.setAttribute("role", "CUSTOMER");
            session.setAttribute("user", "guest");
            session.setAttribute("displayName", "Guest Customer");
            session.setAttribute("avatar", "👤");
        }
        model.addAttribute("role", session.getAttribute("role").toString());
        model.addAttribute("user", session.getAttribute("user").toString());
        model.addAttribute("displayName", session.getAttribute("displayName").toString());
        model.addAttribute("avatar", session.getAttribute("avatar").toString());
    }
}
