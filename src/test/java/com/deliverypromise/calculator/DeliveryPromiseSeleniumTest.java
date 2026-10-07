package com.deliverypromise.calculator;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

import static org.junit.jupiter.api.Assertions.assertTrue;

class DeliveryPromiseSeleniumTest {

    private static WebDriver driver;
    private static WebDriverWait wait;

    @BeforeAll
    static void setUp() {
        // Selenium Manager automatically locates/downloads the compatible ChromeDriver.
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    }

    @Test
    void deliveryManagementPageLoads() {
        driver.get("http://localhost:8765/deliveries");

        wait.until(ExpectedConditions.titleContains("Delivery Management"));

        assertTrue(driver.getTitle().contains("Delivery Management"));
        assertTrue(driver.findElement(By.tagName("h1"))
                .getText().contains("Delivery Management"));
        assertTrue(driver.findElement(By.name("keyword")).isDisplayed());
    }

    @Test
    void createDeliveryAndVerifyPromisedDate() {
        driver.get("http://localhost:8765/deliveries");

        String customer = "Selenium Customer " + System.currentTimeMillis();

        driver.findElement(By.name("customerName")).sendKeys(customer);
        driver.findElement(By.name("deliveryAddress")).sendKeys("Nagpur");
        driver.findElement(By.name("productName")).sendKeys("Selenium Test Product");
        driver.findElement(By.name("deliveryDays")).clear();
        driver.findElement(By.name("deliveryDays")).sendKeys("5");

        driver.findElement(By.cssSelector("button[type='submit']"))
                .click();

        wait.until(ExpectedConditions.urlContains("/deliveries"));

        assertTrue(driver.findElement(By.tagName("table"))
                .getText().contains(customer));

        assertTrue(driver.findElement(By.tagName("table"))
                .getText().contains("PENDING"));

        assertTrue(driver.findElement(By.tagName("table"))
                .getText().contains("Selenium Test Product"));
    }

    @Test
    void searchDelivery() {
        driver.get("http://localhost:8765/deliveries");

        String customer = "Search Selenium " + System.currentTimeMillis();

        driver.findElement(By.name("customerName")).sendKeys(customer);
        driver.findElement(By.name("deliveryAddress")).sendKeys("Nagpur");
        driver.findElement(By.name("productName")).sendKeys("Search Test Product");
        driver.findElement(By.name("deliveryDays")).clear();
        driver.findElement(By.name("deliveryDays")).sendKeys("3");
        driver.findElement(By.cssSelector("form[action='/deliveries'] button[type='submit']"))
                .click();

        wait.until(ExpectedConditions.urlContains("/deliveries"));

        driver.findElement(By.name("keyword")).sendKeys(customer);
        driver.findElement(By.cssSelector("form[action='/deliveries'][method='get'] button"))
                .click();

        wait.until(ExpectedConditions.urlContains("keyword"));

        assertTrue(driver.findElement(By.tagName("table"))
                .getText().contains(customer));
    }

    @AfterAll
    static void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
