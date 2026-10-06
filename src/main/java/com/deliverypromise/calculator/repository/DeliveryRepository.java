package com.deliverypromise.calculator.repository;

import com.deliverypromise.calculator.model.Delivery;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface DeliveryRepository extends JpaRepository<Delivery, Long> {

    List<Delivery> findByCustomerNameContainingIgnoreCaseOrProductNameContainingIgnoreCase(
            String customerName, String productName);
}
