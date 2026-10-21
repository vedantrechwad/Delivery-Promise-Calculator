package com.deliverypromise.calculator.repository;

import com.deliverypromise.calculator.model.Delivery;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;

public interface DeliveryRepository extends JpaRepository<Delivery, Long> {

    List<Delivery> findByCustomerNameContainingIgnoreCaseOrProductNameContainingIgnoreCase(
            String customerName, String productName);

    List<Delivery> findByCustomerNameContainingIgnoreCaseOrProductNameContainingIgnoreCaseOrTrackingNumberContainingIgnoreCase(
            String customerName, String productName, String trackingNumber);

    Optional<Delivery> findByTrackingNumber(String trackingNumber);

    List<Delivery> findByStatusIgnoreCase(String status);
}

