package com.deliverypromise.calculator;

import com.deliverypromise.calculator.service.DeliveryService;
import jakarta.servlet.http.HttpSession;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

    private final DeliveryService deliveryService;

    public HomeController(DeliveryService deliveryService) {
        this.deliveryService = deliveryService;
    }

    @GetMapping("/")
    public String home(HttpSession session, Model model) {
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

        model.addAttribute("total", deliveryService.getTotalDeliveries());
        model.addAttribute("pending", deliveryService.getPendingDeliveries());
        model.addAttribute("delivered", deliveryService.getDeliveredDeliveries());
        model.addAttribute("slaRate", deliveryService.getOnTimeSlaRate());

        return "index";
    }
}

