package com.deliverypromise.calculator.controller;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;
import org.springframework.web.servlet.view.InternalResourceViewResolver;

import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

class AuthControllerTest {

    private MockMvc mockMvc;

    @BeforeEach
    void setUp() {
        InternalResourceViewResolver viewResolver = new InternalResourceViewResolver();
        viewResolver.setPrefix("/templates/");
        viewResolver.setSuffix(".html");

        mockMvc = MockMvcBuilders.standaloneSetup(new AuthController())
                .setViewResolvers(viewResolver)
                .build();
    }

    @Test
    void loginPage_ReturnsOk() throws Exception {
        mockMvc.perform(get("/login"))
                .andExpect(status().isOk())
                .andExpect(view().name("login"));
    }

    @Test
    void doLogin_ValidAdmin_RedirectsToDeliveries() throws Exception {
        mockMvc.perform(post("/login")
                        .param("username", "admin")
                        .param("password", "admin123"))
                .andExpect(status().is3xxRedirection())
                .andExpect(redirectedUrl("/deliveries"))
                .andExpect(request().sessionAttribute("role", "ADMIN"))
                .andExpect(request().sessionAttribute("user", "admin"));
    }

    @Test
    void doLogin_ValidOperator_RedirectsToDeliveries() throws Exception {
        mockMvc.perform(post("/login")
                        .param("username", "operator")
                        .param("password", "ops123"))
                .andExpect(status().is3xxRedirection())
                .andExpect(redirectedUrl("/deliveries"))
                .andExpect(request().sessionAttribute("role", "OPERATIONS"));
    }

    @Test
    void doLogin_InvalidCredentials_RedirectsToLoginWithError() throws Exception {
        mockMvc.perform(post("/login")
                        .param("username", "wrong")
                        .param("password", "wrongpass"))
                .andExpect(status().is3xxRedirection())
                .andExpect(result -> {
                    String url = result.getResponse().getRedirectedUrl();
                    assertNotNull(url);
                    assertTrue(url.startsWith("/login?error="));
                });
    }

    @Test
    void logout_InvalidatesSessionAndRedirects() throws Exception {
        mockMvc.perform(get("/logout"))
                .andExpect(status().is3xxRedirection())
                .andExpect(redirectedUrl("/login?logout=true"));
    }
}
