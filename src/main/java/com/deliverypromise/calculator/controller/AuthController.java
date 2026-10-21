package com.deliverypromise.calculator.controller;

import jakarta.servlet.http.HttpSession;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class AuthController {

    public static final String DEFAULT_ROLE = "CUSTOMER";

    @GetMapping("/login")
    public String login(
            @RequestParam(required = false) String role,
            @RequestParam(required = false) String error,
            @RequestParam(required = false) String logout,
            @RequestParam(required = false, defaultValue = "/deliveries") String redirect,
            HttpSession session,
            Model model) {

        // If a specific role switch is requested (e.g. ?role=admin), display the login screen
        // so the presenter can demonstrate the credentials flow.
        // Only redirect if no specific role switch was requested and user is already authenticated.
        if ((role == null || role.isBlank())
                && error == null
                && logout == null
                && session.getAttribute("user") != null
                && !"guest".equals(session.getAttribute("user"))) {
            return "redirect:" + (redirect.startsWith("/") ? redirect : "/deliveries");
        }

        String targetRole = role != null ? role.trim().toLowerCase() : "";
        model.addAttribute("targetRole", targetRole);
        model.addAttribute("error", error);
        model.addAttribute("logout", logout);
        model.addAttribute("redirect", redirect);
        return "login";
    }

    @PostMapping("/login")
    public String doLogin(
            @RequestParam String username,
            @RequestParam String password,
            @RequestParam(required = false, defaultValue = "/deliveries") String redirect,
            HttpSession session) {

        String u = username != null ? username.trim().toLowerCase() : "";
        String p = password != null ? password.trim() : "";

        String role = null;
        String displayName = null;
        String avatar = null;

        if ("admin".equals(u) && "admin123".equals(p)) {
            role = "ADMIN";
            displayName = "Vedant Rechwad";
            avatar = "👤";
        } else if ("operator".equals(u) && "ops123".equals(p)) {
            role = "OPERATIONS";
            displayName = "Operations Lead";
            avatar = "🚚";
        } else if ("customer".equals(u) && "customer123".equals(p)) {
            role = "CUSTOMER";
            displayName = "Retail Customer";
            avatar = "👤";
        }

        if (role == null) {
            return "redirect:/login?error=Invalid%20username%20or%20password.%20See%20demo%20credentials%20below.&redirect=" + redirect;
        }

        session.setAttribute("user", u);
        session.setAttribute("role", role);
        session.setAttribute("displayName", displayName);
        session.setAttribute("avatar", avatar);

        return "redirect:" + (redirect.startsWith("/") ? redirect : "/deliveries");
    }

    @GetMapping("/logout")
    public String logout(HttpSession session) {
        session.invalidate();
        return "redirect:/login?logout=true";
    }

    public static String getActiveRole(HttpSession session) {
        Object role = session.getAttribute("role");
        if (role == null) {
            session.setAttribute("role", DEFAULT_ROLE);
            session.setAttribute("user", "guest");
            session.setAttribute("displayName", "Guest Customer");
            session.setAttribute("avatar", "👤");
            return DEFAULT_ROLE;
        }
        return role.toString();
    }
}
