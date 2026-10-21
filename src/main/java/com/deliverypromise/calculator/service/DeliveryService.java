package com.deliverypromise.calculator.service;

import com.deliverypromise.calculator.model.Delivery;
import com.deliverypromise.calculator.repository.DeliveryRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Service
public class DeliveryService {

    private final DeliveryRepository deliveryRepository;

    public DeliveryService(DeliveryRepository deliveryRepository) {
        this.deliveryRepository = deliveryRepository;
    }

    public Delivery createDelivery(Delivery delivery) {
        if (delivery.getOrderDate() == null) {
            delivery.setOrderDate(LocalDate.now());
        }

        if (delivery.getShippingTier() == null || delivery.getShippingTier().isBlank()) {
            delivery.setShippingTier("STANDARD");
        }

        if (delivery.getPriority() == null || delivery.getPriority().isBlank()) {
            delivery.setPriority("NORMAL");
        }

        // Smart SLA Promise Calculation
        int days = delivery.getDeliveryDays() > 0 ? delivery.getDeliveryDays() : 3;
        LocalDate calculatedDate;
        String tier = delivery.getShippingTier().toUpperCase();

        if ("SAME_DAY".equals(tier)) {
            calculatedDate = delivery.getOrderDate();
        } else if ("EXPRESS".equals(tier)) {
            calculatedDate = delivery.getOrderDate().plusDays(Math.max(1, Math.min(days, 2)));
        } else if ("ECONOMY".equals(tier)) {
            calculatedDate = delivery.getOrderDate().plusDays(days + 2);
        } else {
            // STANDARD
            calculatedDate = delivery.getOrderDate().plusDays(days);
        }

        delivery.setPromisedDate(calculatedDate);

        if (delivery.getTrackingNumber() == null || delivery.getTrackingNumber().isBlank()) {
            delivery.setTrackingNumber("TRK-" + UUID.randomUUID().toString().substring(0, 8).toUpperCase());
        }

        if (delivery.getStatus() == null || delivery.getStatus().isBlank()) {
            delivery.setStatus("PENDING");
        }

        return deliveryRepository.save(delivery);
    }

    public List<Delivery> getAllDeliveries() {
        return deliveryRepository.findAll();
    }

    public Optional<Delivery> getDeliveryById(Long id) {
        return deliveryRepository.findById(id);
    }

    public Optional<Delivery> getDeliveryByTrackingNumber(String trackingNumber) {
        if (trackingNumber == null || trackingNumber.isBlank()) {
            return Optional.empty();
        }
        return deliveryRepository.findByTrackingNumber(trackingNumber.trim().toUpperCase());
    }

    public List<Delivery> searchDeliveries(String keyword) {
        if (keyword == null || keyword.isBlank()) {
            return getAllDeliveries();
        }
        String term = keyword.trim();
        return deliveryRepository
                .findByCustomerNameContainingIgnoreCaseOrProductNameContainingIgnoreCaseOrTrackingNumberContainingIgnoreCase(
                        term, term, term);
    }

    public List<Delivery> getDeliveriesByStatus(String status) {
        if (status == null || status.isBlank() || "ALL".equalsIgnoreCase(status)) {
            return getAllDeliveries();
        }
        return deliveryRepository.findByStatusIgnoreCase(status.trim());
    }

    public Delivery updateStatus(Long id, String status) {
        Delivery delivery = deliveryRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("Delivery not found with id: " + id));

        String upperStatus = status.trim().toUpperCase();
        delivery.setStatus(upperStatus);

        if ("DELIVERED".equals(upperStatus)) {
            delivery.setDeliveredDate(LocalDate.now());
        }

        return deliveryRepository.save(delivery);
    }

    public Delivery cancelDelivery(Long id) {
        Delivery delivery = deliveryRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("Delivery not found with id: " + id));

        if ("DELIVERED".equalsIgnoreCase(delivery.getStatus())) {
            throw new IllegalStateException("Delivered orders cannot be cancelled");
        }

        delivery.setStatus("CANCELLED");
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

    public long getProcessingDeliveries() {
        return deliveryRepository.findAll().stream()
                .filter(d -> "PROCESSING".equalsIgnoreCase(d.getStatus()))
                .count();
    }

    public long getShippedDeliveries() {
        return deliveryRepository.findAll().stream()
                .filter(d -> "SHIPPED".equalsIgnoreCase(d.getStatus()))
                .count();
    }

    public long getDeliveredDeliveries() {
        return deliveryRepository.findAll().stream()
                .filter(d -> "DELIVERED".equalsIgnoreCase(d.getStatus()))
                .count();
    }

    public long getCancelledDeliveries() {
        return deliveryRepository.findAll().stream()
                .filter(d -> "CANCELLED".equalsIgnoreCase(d.getStatus()))
                .count();
    }

    public double getOnTimeSlaRate() {
        long total = getTotalDeliveries();
        if (total == 0) return 100.0;
        long cancelled = getCancelledDeliveries();
        long activeOrDelivered = total - cancelled;
        if (activeOrDelivered <= 0) return 100.0;

        long onTimeCount = deliveryRepository.findAll().stream()
                .filter(d -> !"CANCELLED".equalsIgnoreCase(d.getStatus()))
                .filter(d -> {
                    LocalDate actual = d.getDeliveredDate() != null ? d.getDeliveredDate() : LocalDate.now();
                    return !actual.isAfter(d.getPromisedDate());
                })
                .count();

        return Math.round((onTimeCount * 100.0 / activeOrDelivered) * 10.0) / 10.0;
    }

    public double getAverageDeliveryDays() {
        List<Delivery> list = deliveryRepository.findAll();
        if (list.isEmpty()) return 3.0;
        double avg = list.stream().mapToInt(Delivery::getDeliveryDays).average().orElse(3.0);
        return Math.round(avg * 10.0) / 10.0;
    }

    public void seedDemoDeliveries() {
        if (deliveryRepository.count() > 0) {
            return;
        }

        LocalDate today = LocalDate.now();

        Delivery d1 = new Delivery();
        d1.setTrackingNumber("TRK-IN-9821");
        d1.setCustomerName("Rohan Deshmukh");
        d1.setDeliveryAddress("Flat 402, Rohan Viti, Baner Road, Pune, Maharashtra 411045");
        d1.setProductName("Apple MacBook Pro 16\" M3 Max (36GB RAM, 1TB SSD)");
        d1.setDeliveryDays(2);
        d1.setShippingTier("EXPRESS");
        d1.setPriority("URGENT");
        d1.setOrderDate(today.minusDays(1));
        d1.setStatus("SHIPPED");
        d1.setNotes("High-value electronics - Verified OTP required");
        createDelivery(d1);

        Delivery d2 = new Delivery();
        d2.setTrackingNumber("TRK-IN-4412");
        d2.setCustomerName("Pooja Sharma");
        d2.setDeliveryAddress("B-12, Godrej Woods, Sector 43, Noida, Uttar Pradesh 201303");
        d2.setProductName("Sony WH-1000XM5 Wireless Noise Cancelling Headphones");
        d2.setDeliveryDays(3);
        d2.setShippingTier("STANDARD");
        d2.setPriority("NORMAL");
        d2.setOrderDate(today.minusDays(2));
        d2.setStatus("PROCESSING");
        d2.setNotes("Contact customer before morning dispatch");
        createDelivery(d2);

        Delivery d3 = new Delivery();
        d3.setTrackingNumber("TRK-IN-8890");
        d3.setCustomerName("Ananya Iyer");
        d3.setDeliveryAddress("14/B, 3rd Cross, Indiranagar 1st Stage, Bengaluru, Karnataka 560038");
        d3.setProductName("Samsung 65\" Crystal 4K UHD Smart TV (2024 Model)");
        d3.setDeliveryDays(4);
        d3.setShippingTier("STANDARD");
        d3.setPriority("HIGH");
        d3.setOrderDate(today.minusDays(5));
        d3.setStatus("DELIVERED");
        d3.setDeliveredDate(today.minusDays(1));
        d3.setNotes("Installation and wall mount scheduled");
        createDelivery(d3);

        Delivery d4 = new Delivery();
        d4.setTrackingNumber("TRK-IN-1029");
        d4.setCustomerName("Aditya Verma");
        d4.setDeliveryAddress("204, Silver Oak Heights, Civil Lines, Nagpur, Maharashtra 440001");
        d4.setProductName("Apple iPhone 15 Pro Max 256GB Natural Titanium");
        d4.setDeliveryDays(1);
        d4.setShippingTier("SAME_DAY");
        d4.setPriority("URGENT");
        d4.setOrderDate(today.minusDays(2));
        d4.setStatus("DELIVERED");
        d4.setDeliveredDate(today.minusDays(1));
        d4.setNotes("Delivered in person with ID proof verified");
        createDelivery(d4);

        Delivery d5 = new Delivery();
        d5.setTrackingNumber("TRK-IN-6623");
        d5.setCustomerName("Meera Nair");
        d5.setDeliveryAddress("Villa 7, Skyline Riveria, Marine Drive, Kochi, Kerala 682031");
        d5.setProductName("Dyson V12 Detect Slim Cordless Vacuum Cleaner");
        d5.setDeliveryDays(5);
        d5.setShippingTier("STANDARD");
        d5.setPriority("NORMAL");
        d5.setOrderDate(today);
        d5.setStatus("PENDING");
        d5.setNotes("Package packed at central hub, ready for dispatch");
        createDelivery(d5);

        Delivery d6 = new Delivery();
        d6.setTrackingNumber("TRK-IN-7714");
        d6.setCustomerName("Karan Malhotra");
        d6.setDeliveryAddress("C-302, DLF Phase 5, Golf Course Road, Gurugram, Haryana 122002");
        d6.setProductName("LG 9 Kg AI Direct Drive Front Load Washing Machine");
        d6.setDeliveryDays(4);
        d6.setShippingTier("STANDARD");
        d6.setPriority("NORMAL");
        d6.setOrderDate(today.minusDays(1));
        d6.setStatus("SHIPPED");
        d6.setNotes("Fragile heavy appliance - Two-person delivery team");
        createDelivery(d6);

        Delivery d7 = new Delivery();
        d7.setTrackingNumber("TRK-IN-3329");
        d7.setCustomerName("Sneha Patel");
        d7.setDeliveryAddress("A-501, Iscon Platinum, Bopal-Ambli Road, Ahmedabad, Gujarat 380058");
        d7.setProductName("Bose QuietComfort 45 Bluetooth Headphones");
        d7.setDeliveryDays(2);
        d7.setShippingTier("EXPRESS");
        d7.setPriority("NORMAL");
        d7.setOrderDate(today.minusDays(4));
        d7.setStatus("DELIVERED");
        d7.setDeliveredDate(today.minusDays(2));
        d7.setNotes("Signed by security reception");
        createDelivery(d7);

        Delivery d8 = new Delivery();
        d8.setTrackingNumber("TRK-IN-5501");
        d8.setCustomerName("Vikramaditya Rao");
        d8.setDeliveryAddress("Plot 48, Jubilee Hills Road No. 36, Hyderabad, Telangana 500033");
        d8.setProductName("Sony PlayStation 5 Slim Digital Edition (1TB SSD)");
        d8.setDeliveryDays(3);
        d8.setShippingTier("STANDARD");
        d8.setPriority("HIGH");
        d8.setOrderDate(today);
        d8.setStatus("PENDING");
        d8.setNotes("Customer requested delivery after 5 PM");
        createDelivery(d8);

        Delivery d9 = new Delivery();
        d9.setTrackingNumber("TRK-IN-2219");
        d9.setCustomerName("Tanya Sengupta");
        d9.setDeliveryAddress("82/1A, Ballygunge Circular Road, Kolkata, West Bengal 700019");
        d9.setProductName("Kindle Paperwhite Signature Edition (32GB)");
        d9.setDeliveryDays(2);
        d9.setShippingTier("EXPRESS");
        d9.setPriority("NORMAL");
        d9.setOrderDate(today.minusDays(1));
        d9.setStatus("PROCESSING");
        d9.setNotes("Gift wrap and greeting card attached");
        createDelivery(d9);

        Delivery d10 = new Delivery();
        d10.setTrackingNumber("TRK-IN-9908");
        d10.setCustomerName("Rahul Kulkarni");
        d10.setDeliveryAddress("1102, Lodha Bellissimo, NM Joshi Marg, Lower Parel, Mumbai 400013");
        d10.setProductName("Philips HD9252 Digital Air Fryer (4.1 Liter)");
        d10.setDeliveryDays(5);
        d10.setShippingTier("ECONOMY");
        d10.setPriority("NORMAL");
        d10.setOrderDate(today.minusDays(3));
        d10.setStatus("CANCELLED");
        d10.setNotes("Customer cancelled due to incorrect delivery address");
        createDelivery(d10);
    }
}

