package com.deliverypromise.calculator;

import com.deliverypromise.calculator.service.DeliveryService;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class DeliveryPromiseCalculatorApplication {

    public static void main(String[] args) {
        SpringApplication.run(DeliveryPromiseCalculatorApplication.class, args);
    }

    @Bean
    CommandLineRunner initDatabase(DeliveryService deliveryService) {
        return args -> {
            if (deliveryService.getTotalDeliveries() == 0) {
                deliveryService.seedDemoDeliveries();
            }
        };
    }
}

