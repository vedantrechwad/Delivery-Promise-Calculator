package com.deliverypromise.calculator.controller;

import jakarta.servlet.http.HttpSession;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class RoleController {

    @GetMapping("/role")
    public String setRole(@RequestParam String role, HttpSession session) {
        String normalizedRole = role.toUpperCase();

        if (!normalizedRole.equals("ADMIN")
                && !normalizedRole.equals("OPERATIONS")
                && !normalizedRole.equals("CUSTOMER")) {
            normalizedRole = "CUSTOMER";
        }

        session.setAttribute("role", normalizedRole);
        return "redirect:/deliveries";
    }
}
