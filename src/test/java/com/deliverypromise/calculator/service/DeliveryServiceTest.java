package com.deliverypromise.calculator.service;

import com.deliverypromise.calculator.model.Delivery;
import com.deliverypromise.calculator.repository.DeliveryRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
class DeliveryServiceTest {

    @Mock
    private DeliveryRepository deliveryRepository;

    @InjectMocks
    private DeliveryService deliveryService;

    private Delivery sampleDelivery;

    @BeforeEach
    void setUp() {
        sampleDelivery = new Delivery();
        sampleDelivery.setCustomerName("Vedant Rechwad");
        sampleDelivery.setDeliveryAddress("Nagpur, MH");
        sampleDelivery.setProductName("MacBook Pro");
        sampleDelivery.setDeliveryDays(4);
    }

    @Test
    void createDelivery_StandardTier_CalculatesPromisedDate() {
        when(deliveryRepository.save(any(Delivery.class))).thenAnswer(invocation -> invocation.getArgument(0));

        sampleDelivery.setShippingTier("STANDARD");
        Delivery created = deliveryService.createDelivery(sampleDelivery);

        assertNotNull(created.getPromisedDate());
        assertEquals(LocalDate.now().plusDays(4), created.getPromisedDate());
        assertEquals("PENDING", created.getStatus());
        assertTrue(created.getTrackingNumber().startsWith("TRK-"));
    }

    @Test
    void createDelivery_SameDayTier_SetsTodayPromisedDate() {
        when(deliveryRepository.save(any(Delivery.class))).thenAnswer(invocation -> invocation.getArgument(0));

        sampleDelivery.setShippingTier("SAME_DAY");
        Delivery created = deliveryService.createDelivery(sampleDelivery);

        assertEquals(LocalDate.now(), created.getPromisedDate());
    }

    @Test
    void createDelivery_ExpressTier_CapsTransitDays() {
        when(deliveryRepository.save(any(Delivery.class))).thenAnswer(invocation -> invocation.getArgument(0));

        sampleDelivery.setShippingTier("EXPRESS");
        sampleDelivery.setDeliveryDays(6);
        Delivery created = deliveryService.createDelivery(sampleDelivery);

        // Express caps days to 2
        assertEquals(LocalDate.now().plusDays(2), created.getPromisedDate());
    }

    @Test
    void createDelivery_EconomyTier_AddsBufferDays() {
        when(deliveryRepository.save(any(Delivery.class))).thenAnswer(invocation -> invocation.getArgument(0));

        sampleDelivery.setShippingTier("ECONOMY");
        sampleDelivery.setDeliveryDays(3);
        Delivery created = deliveryService.createDelivery(sampleDelivery);

        // Economy adds 2 buffer days = 3 + 2 = 5
        assertEquals(LocalDate.now().plusDays(5), created.getPromisedDate());
    }

    @Test
    void updateStatus_ToDelivered_SetsDeliveredDate() {
        sampleDelivery.setStatus("SHIPPED");
        when(deliveryRepository.findById(1L)).thenReturn(Optional.of(sampleDelivery));
        when(deliveryRepository.save(any(Delivery.class))).thenAnswer(invocation -> invocation.getArgument(0));

        Delivery updated = deliveryService.updateStatus(1L, "DELIVERED");

        assertEquals("DELIVERED", updated.getStatus());
        assertEquals(LocalDate.now(), updated.getDeliveredDate());
    }

    @Test
    void cancelDelivery_PendingOrder_Succeeds() {
        sampleDelivery.setStatus("PENDING");
        when(deliveryRepository.findById(1L)).thenReturn(Optional.of(sampleDelivery));
        when(deliveryRepository.save(any(Delivery.class))).thenAnswer(invocation -> invocation.getArgument(0));

        Delivery cancelled = deliveryService.cancelDelivery(1L);

        assertEquals("CANCELLED", cancelled.getStatus());
    }

    @Test
    void cancelDelivery_DeliveredOrder_ThrowsIllegalStateException() {
        sampleDelivery.setStatus("DELIVERED");
        when(deliveryRepository.findById(1L)).thenReturn(Optional.of(sampleDelivery));

        assertThrows(IllegalStateException.class, () -> deliveryService.cancelDelivery(1L));
    }

    @Test
    void searchDeliveries_ReturnsMatchingRecords() {
        when(deliveryRepository.findByCustomerNameContainingIgnoreCaseOrProductNameContainingIgnoreCaseOrTrackingNumberContainingIgnoreCase(
                "MacBook", "MacBook", "MacBook")).thenReturn(List.of(sampleDelivery));

        List<Delivery> results = deliveryService.searchDeliveries("MacBook");

        assertEquals(1, results.size());
        assertEquals("MacBook Pro", results.get(0).getProductName());
    }
}
