package com.deliverypromise.calculator.controller;

import jakarta.servlet.http.HttpSession;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class RoleController {

    @GetMapping("/role")
    public String setRole(
            @RequestParam String role,
            @RequestParam(required = false, defaultValue = "/deliveries") String redirect,
            @RequestParam(required = false, defaultValue = "false") boolean direct,
            HttpSession session) {

        String normalizedRole = role != null ? role.trim().toUpperCase() : "CUSTOMER";
        if (!normalizedRole.equals("ADMIN")
                && !normalizedRole.equals("OPERATIONS")
                && !normalizedRole.equals("CUSTOMER")) {
            normalizedRole = "CUSTOMER";
        }

        // Direct bypass option if called programmatically
        if (direct) {
            session.setAttribute("role", normalizedRole);
            if ("ADMIN".equals(normalizedRole)) {
                session.setAttribute("user", "admin");
                session.setAttribute("displayName", "Vedant Rechwad");
                session.setAttribute("avatar", "👤");
            } else if ("OPERATIONS".equals(normalizedRole)) {
                session.setAttribute("user", "operator");
                session.setAttribute("displayName", "Operations Lead");
                session.setAttribute("avatar", "🚚");
            } else {
                session.setAttribute("user", "customer");
                session.setAttribute("displayName", "Retail Customer");
                session.setAttribute("avatar", "👤");
            }
            return "redirect:" + (redirect.startsWith("/") ? redirect : "/deliveries");
        }

        // Default demonstration flow: redirect to login asking for credentials
        return "redirect:/login?role=" + normalizedRole.toLowerCase() + "&redirect=" + (redirect.startsWith("/") ? redirect : "/deliveries");
    }
}


