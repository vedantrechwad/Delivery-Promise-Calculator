package com.deliverypromise.calculator.controller;

import com.deliverypromise.calculator.service.DeliveryService;
import jakarta.servlet.http.HttpSession;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.io.File;
import java.lang.management.ManagementFactory;
import java.lang.management.RuntimeMXBean;

@Controller
public class SystemController {

    private final DeliveryService deliveryService;

    @Value("${server.port:8765}")
    private String serverPort;

    @Value("${spring.application.name:delivery-promise-calculator}")
    private String appName;

    public SystemController(DeliveryService deliveryService) {
        this.deliveryService = deliveryService;
    }

    @GetMapping("/system")
    public String systemDiagnostics(HttpSession session, Model model) {
        attachSessionInfo(session, model);

        Runtime runtime = Runtime.getRuntime();
        long totalMemory = runtime.totalMemory() / (1024 * 1024);
        long freeMemory = runtime.freeMemory() / (1024 * 1024);
        long maxMemory = runtime.maxMemory() / (1024 * 1024);
        long usedMemory = totalMemory - freeMemory;
        double memUsagePercent = maxMemory > 0 ? (usedMemory * 100.0 / maxMemory) : 0;

        RuntimeMXBean mxBean = ManagementFactory.getRuntimeMXBean();
        long uptimeSeconds = mxBean.getUptime() / 1000;
        long uptimeMinutes = uptimeSeconds / 60;
        long uptimeHours = uptimeMinutes / 60;

        File dbFile = new File("delivery_promise.db");
        long dbSizeBytes = dbFile.exists() ? dbFile.length() : 0;
        double dbSizeKb = Math.round((dbSizeBytes / 1024.0) * 10.0) / 10.0;

        model.addAttribute("appName", appName);
        model.addAttribute("serverPort", serverPort);
        model.addAttribute("javaVersion", System.getProperty("java.version"));
        model.addAttribute("osName", System.getProperty("os.name") + " (" + System.getProperty("os.arch") + ")");
        model.addAttribute("usedMemory", usedMemory);
        model.addAttribute("maxMemory", maxMemory);
        model.addAttribute("freeMemory", freeMemory);
        model.addAttribute("memPercent", Math.round(memUsagePercent * 10.0) / 10.0);
        model.addAttribute("uptimeHours", uptimeHours);
        model.addAttribute("uptimeMinutes", uptimeMinutes % 60);
        model.addAttribute("uptimeSeconds", uptimeSeconds % 60);

        model.addAttribute("dbExists", dbFile.exists());
        model.addAttribute("dbSizeKb", dbSizeKb);
        model.addAttribute("totalRecords", deliveryService.getTotalDeliveries());

        // DevOps specs
        model.addAttribute("dockerImage", "delivery-promise-calculator:1.0");
        model.addAttribute("dockerDeployPort", "8766 -> 8765");
        model.addAttribute("jenkinsJob", "delivery-promise-pipeline");
        model.addAttribute("puppetManifest", "puppet/delivery_promise.pp");
        model.addAttribute("seleniumSuite", "DeliveryPromiseSeleniumTest");

        return "system";
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
