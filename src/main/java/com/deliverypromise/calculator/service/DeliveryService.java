package com.deliverypromise.calculator.service;

import com.deliverypromise.calculator.model.Delivery;
import com.deliverypromise.calculator.repository.DeliveryRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.util.List;

@Service
public class DeliveryService {

    private final DeliveryRepository deliveryRepository;

    public DeliveryService(DeliveryRepository deliveryRepository) {
        this.deliveryRepository = deliveryRepository;
    }

    public Delivery createDelivery(Delivery delivery) {
        delivery.setPromisedDate(
                LocalDate.now().plusDays(delivery.getDeliveryDays())
        );

        if (delivery.getStatus() == null || delivery.getStatus().isBlank()) {
            delivery.setStatus("PENDING");
        }

        return deliveryRepository.save(delivery);
    }

    public List<Delivery> getAllDeliveries() {
        return deliveryRepository.findAll();
    }

    public List<Delivery> searchDeliveries(String keyword) {
        if (keyword == null || keyword.isBlank()) {
            return getAllDeliveries();
        }

        return deliveryRepository
                .findByCustomerNameContainingIgnoreCaseOrProductNameContainingIgnoreCase(
                        keyword, keyword);
    }

    public Delivery updateStatus(Long id, String status) {
        Delivery delivery = deliveryRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("Delivery not found"));

        delivery.setStatus(status);
        return deliveryRepository.save(delivery);
    }

    public long getTotalDeliveries() {
        return deliveryRepository.count();
    }

    public long getPendingDeliveries() {
        return deliveryRepository.findAll().stream()
                .filter(d -> "PENDING".equalsIgnoreCase(d.getStatus()))
                .count();
    }

    public long getDeliveredDeliveries() {
        return deliveryRepository.findAll().stream()
                .filter(d -> "DELIVERED".equalsIgnoreCase(d.getStatus()))
                .count();
    }
}
