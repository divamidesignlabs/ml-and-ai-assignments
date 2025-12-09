"""
Pytest tests for Assignment 17: Object-Oriented Programming - Inheritance and Polymorphism
"""

import pytest
from python_basics.oop_inheritance_17 import (
    Vehicle, Truck, Van, Drone, RefrigeratedTruck, LogisticsFleet
)


class TestVehicleBaseClass:
    """Test cases for Vehicle base class."""
    
    def test_vehicle_initialization(self):
        """Test creating a vehicle."""
        vehicle = Vehicle('VEH001', 1000.0)
        
        assert vehicle.registration_id == 'VEH001'
        assert vehicle.capacity == 1000.0
        assert vehicle.current_load == 0.0
    
    def test_load_cargo(self):
        """Test loading cargo onto vehicle."""
        vehicle = Vehicle('VEH001', 1000.0)
        
        result = vehicle.load_cargo(500.0)
        
        assert result is True
        assert vehicle.current_load == 500.0
    
    def test_load_exceeding_capacity(self):
        """Test that loading exceeding capacity fails."""
        vehicle = Vehicle('VEH001', 1000.0)
        vehicle.load_cargo(800.0)
        
        result = vehicle.load_cargo(300.0)
        
        assert result is False
        assert vehicle.current_load == 800.0
    
    def test_unload_cargo(self):
        """Test unloading cargo from vehicle."""
        vehicle = Vehicle('VEH001', 1000.0)
        vehicle.load_cargo(500.0)
        
        result = vehicle.unload_cargo(200.0)
        
        assert result is True
        assert vehicle.current_load == 300.0
    
    def test_unload_exceeding_current_load(self):
        """Test that unloading more than current load fails."""
        vehicle = Vehicle('VEH001', 1000.0)
        vehicle.load_cargo(300.0)
        
        result = vehicle.unload_cargo(400.0)
        
        assert result is False
        assert vehicle.current_load == 300.0
    
    def test_get_capacity_used(self):
        """Test calculating capacity used percentage."""
        vehicle = Vehicle('VEH001', 1000.0)
        vehicle.load_cargo(500.0)
        
        capacity_used = vehicle.get_capacity_used()
        
        assert capacity_used == 50.0


class TestTruckSubclass:
    """Test cases for Truck subclass."""
    
    def test_truck_initialization(self):
        """Test creating a truck with inherited and new attributes."""
        truck = Truck('TRK001', 5000.0, axles=3)
        
        assert truck.registration_id == 'TRK001'
        assert truck.capacity == 5000.0
        assert truck.axles == 3
    
    def test_truck_inherits_vehicle_methods(self):
        """Test that truck inherits vehicle methods."""
        truck = Truck('TRK001', 5000.0)
        
        result = truck.load_cargo(2000.0)
        
        assert result is True
        assert truck.current_load == 2000.0
    
    def test_truck_deliver_shipment(self):
        """Test truck-specific delivery shipment."""
        truck = Truck('TRK001', 5000.0, axles=2)
        truck.load_cargo(3000.0)
        
        delivery = truck.deliver_shipment()
        
        assert delivery['registration_id'] == 'TRK001'
        assert delivery['load_delivered'] == 3000.0
        assert delivery['axles'] == 2
        assert 'route_type' in delivery
    
    def test_truck_default_axles(self):
        """Test truck with default axles."""
        truck = Truck('TRK002', 5000.0)
        
        assert truck.axles == 2


class TestVanSubclass:
    """Test cases for Van subclass."""
    
    def test_van_initialization(self):
        """Test creating a van with refrigeration option."""
        van = Van('VAN001', 1500.0, refrigerated=True)
        
        assert van.registration_id == 'VAN001'
        assert van.capacity == 1500.0
        assert van.refrigerated is True
    
    def test_van_deliver_shipment(self):
        """Test van-specific delivery shipment."""
        van = Van('VAN001', 1500.0, refrigerated=True)
        van.load_cargo(1000.0)
        
        delivery = van.deliver_shipment()
        
        assert delivery['registration_id'] == 'VAN001'
        assert delivery['load_delivered'] == 1000.0
        assert delivery['refrigerated'] is True
        assert 'cargo_type' in delivery
    
    def test_van_non_refrigerated(self):
        """Test van without refrigeration."""
        van = Van('VAN002', 1500.0, refrigerated=False)
        
        assert van.refrigerated is False


class TestDroneSubclass:
    """Test cases for Drone subclass."""
    
    def test_drone_initialization(self):
        """Test creating a drone."""
        drone = Drone('DRN001', 10.0, max_altitude=1000)
        
        assert drone.registration_id == 'DRN001'
        assert drone.capacity == 10.0
        assert drone.max_altitude == 1000
        assert drone.battery_level == 0.0
    
    def test_drone_charge_battery(self):
        """Test charging drone battery."""
        drone = Drone('DRN001', 10.0)
        
        drone.charge_battery(50)
        
        assert drone.battery_level == 50.0
    
    def test_battery_capped_at_100(self):
        """Test that battery level is capped at 100."""
        drone = Drone('DRN001', 10.0)
        
        drone.charge_battery(150)
        
        assert drone.battery_level == 100.0
    
    def test_drone_deliver_shipment(self):
        """Test drone-specific delivery shipment."""
        drone = Drone('DRN001', 10.0, max_altitude=1000)
        drone.load_cargo(5.0)
        drone.charge_battery(75)
        
        delivery = drone.deliver_shipment()
        
        assert delivery['registration_id'] == 'DRN001'
        assert delivery['load_delivered'] == 5.0
        assert delivery['battery_level'] == 75.0
        assert 'altitude' in delivery


class TestMultiLevelInheritance:
    """Test cases for multi-level inheritance."""
    
    def test_refrigerated_truck_initialization(self):
        """Test creating a refrigerated truck."""
        ref_truck = RefrigeratedTruck('REF-TRK001', 3000.0, axles=2, temperature=2.5)
        
        assert ref_truck.registration_id == 'REF-TRK001'
        assert ref_truck.capacity == 3000.0
        assert ref_truck.axles == 2
        assert ref_truck.temperature == 2.5
    
    def test_refrigerated_truck_inherits_from_truck(self):
        """Test that refrigerated truck inherits from truck."""
        ref_truck = RefrigeratedTruck('REF-TRK001', 3000.0)
        
        result = ref_truck.load_cargo(2000.0)
        
        assert result is True
        assert ref_truck.current_load == 2000.0
    
    def test_refrigerated_truck_deliver_shipment(self):
        """Test refrigerated truck delivery includes temperature."""
        ref_truck = RefrigeratedTruck('REF-TRK001', 3000.0, temperature=3.0)
        ref_truck.load_cargo(2500.0)
        
        delivery = ref_truck.deliver_shipment()
        
        assert delivery['registration_id'] == 'REF-TRK001'
        assert delivery['load_delivered'] == 2500.0
        assert delivery['temperature'] == 3.0


class TestPolymorphism:
    """Test cases for polymorphic behavior."""
    
    def test_polymorphic_deliver_method(self):
        """Test that different vehicle types have different delivery formats."""
        truck = Truck('TRK001', 5000.0)
        van = Van('VAN001', 1500.0)
        drone = Drone('DRN001', 10.0)
        
        truck.load_cargo(2000.0)
        van.load_cargo(1000.0)
        drone.load_cargo(5.0)
        
        truck_delivery = truck.deliver_shipment()
        van_delivery = van.deliver_shipment()
        drone_delivery = drone.deliver_shipment()
        
        # Each should have type-specific fields
        assert 'axles' in truck_delivery
        assert 'refrigerated' in van_delivery
        assert 'battery_level' in drone_delivery
    
    def test_polymorphic_method_call(self):
        """Test calling same method on different vehicle types."""
        vehicles = [
            Truck('TRK001', 5000.0),
            Van('VAN001', 1500.0),
            Drone('DRN001', 10.0),
        ]
        
        for vehicle in vehicles:
            delivery = vehicle.deliver_shipment()
            assert delivery['registration_id'] is not None


class TestLogisticsFleet:
    """Test cases for fleet management."""
    
    def test_create_empty_fleet(self):
        """Test creating an empty fleet."""
        fleet = LogisticsFleet()
        
        assert len(fleet.vehicles) == 0
    
    def test_add_vehicle_to_fleet(self):
        """Test adding vehicles to fleet."""
        fleet = LogisticsFleet()
        truck = Truck('TRK001', 5000.0)
        van = Van('VAN001', 1500.0)
        
        fleet.add_vehicle(truck)
        fleet.add_vehicle(van)
        
        assert len(fleet.vehicles) == 2
    
    def test_fleet_status(self):
        """Test getting fleet status."""
        fleet = LogisticsFleet()
        fleet.add_vehicle(Truck('TRK001', 5000.0))
        fleet.add_vehicle(Van('VAN001', 1500.0))
        
        status = fleet.get_fleet_status()
        
        assert status['total_vehicles'] == 2
        assert status['total_capacity'] == 6500.0
        assert 'total_load' in status
        assert 'vehicle_breakdown' in status
    
    def test_deliver_all_shipments(self):
        """Test delivering shipments from all vehicles."""
        fleet = LogisticsFleet()
        truck = Truck('TRK001', 5000.0)
        van = Van('VAN001', 1500.0)
        
        fleet.add_vehicle(truck)
        fleet.add_vehicle(van)
        
        truck.load_cargo(2000.0)
        van.load_cargo(1000.0)
        
        deliveries = fleet.deliver_all_shipments()
        
        assert len(deliveries) == 2
        # After delivery, all vehicles should have zero load
        for vehicle in fleet.vehicles:
            assert vehicle.current_load == 0.0
    
    def test_polymorphic_dispatch_in_fleet(self):
        """Test that different vehicle types are handled correctly in fleet."""
        fleet = LogisticsFleet()
        fleet.add_vehicle(Truck('TRK001', 5000.0))
        fleet.add_vehicle(Van('VAN001', 1500.0))
        fleet.add_vehicle(Drone('DRN001', 10.0))
        
        deliveries = fleet.deliver_all_shipments()
        
        assert len(deliveries) == 3
        
        # Check that each delivery type is present
        delivery_types = [d['type'] for d in deliveries]
        assert 'Truck' in delivery_types
        assert 'Van' in delivery_types
        assert 'Drone' in delivery_types
