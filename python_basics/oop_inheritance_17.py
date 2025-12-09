"""
Assignment 17: Object-Oriented Programming - Inheritance and Polymorphism

Implement a multi-level inheritance hierarchy for a logistics system with
polymorphic behavior. Demonstrate method overriding, super() usage, and
polymorphic method dispatch.

Instructions:
- Implement base classes with abstract behavior
- Demonstrate single and multiple inheritance
- Use super() to call parent class methods
- Override methods to provide specialized behavior
- Implement polymorphic operations across different object types
"""

from typing import List, Dict, Any


class Vehicle:
    """
    Base class representing a vehicle in the logistics system.
    
    Attributes:
        registration_id: Vehicle registration number
        capacity: Maximum carrying capacity in units
        current_load: Current load in units
    """
    
    def __init__(self, registration_id: str, capacity: float):
        """
        Initialize a vehicle.
        
        Args:
            registration_id: Unique vehicle ID
            capacity: Maximum capacity
        """
        # TODO: Implement __init__
        pass
    
    def load_cargo(self, weight: float) -> bool:
        """
        Load cargo onto the vehicle.
        
        Args:
            weight: Weight to load
        
        Returns:
            True if cargo was loaded, False if it exceeds capacity
        """
        # TODO: Implement load_cargo
        pass
    
    def unload_cargo(self, weight: float) -> bool:
        """
        Unload cargo from the vehicle.
        
        Args:
            weight: Weight to unload
        
        Returns:
            True if cargo was unloaded, False if weight exceeds current load
        """
        # TODO: Implement unload_cargo
        pass
    
    def get_capacity_used(self) -> float:
        """Get the percentage of capacity used."""
        # TODO: Implement get_capacity_used
        pass
    
    def deliver_shipment(self) -> Dict[str, Any]:
        """
        Process a shipment delivery. To be overridden by subclasses.
        
        Returns:
            Dictionary with delivery details
        """
        return {
            'type': self.__class__.__name__,
            'registration_id': self.registration_id,
            'load_delivered': self.current_load
        }


class Truck(Vehicle):
    """
    Truck class extending Vehicle.
    
    Additional Attributes:
        axles: Number of axles on the truck
    """
    
    def __init__(self, registration_id: str, capacity: float, axles: int = 2):
        """
        Initialize a truck.
        
        Args:
            registration_id: Truck registration number
            capacity: Carrying capacity
            axles: Number of axles (default: 2)
        """
        # TODO: Implement __init__ using super()
        pass
    
    def deliver_shipment(self) -> Dict[str, Any]:
        """
        Override parent method to include truck-specific delivery info.
        
        Returns:
            Dictionary with truck-specific delivery details
        """
        # TODO: Implement deliver_shipment
        # Should call super().deliver_shipment() and add 'axles' and 'route_type'
        pass


class Van(Vehicle):
    """
    Van class extending Vehicle.
    
    Additional Attributes:
        refrigerated: Whether the van has refrigeration
    """
    
    def __init__(self, registration_id: str, capacity: float, refrigerated: bool = False):
        """
        Initialize a van.
        
        Args:
            registration_id: Van registration number
            capacity: Carrying capacity
            refrigerated: Whether van is refrigerated
        """
        # TODO: Implement __init__ using super()
        pass
    
    def deliver_shipment(self) -> Dict[str, Any]:
        """
        Override parent method to include van-specific delivery info.
        
        Returns:
            Dictionary with van-specific delivery details
        """
        # TODO: Implement deliver_shipment
        # Should call super().deliver_shipment() and add 'refrigerated' and 'cargo_type'
        pass


class Drone(Vehicle):
    """
    Drone class extending Vehicle.
    
    Additional Attributes:
        max_altitude: Maximum altitude in meters
        battery_level: Current battery percentage (0-100)
    """
    
    def __init__(self, registration_id: str, capacity: float, max_altitude: int = 500):
        """
        Initialize a drone.
        
        Args:
            registration_id: Drone ID
            capacity: Carrying capacity in kg
            max_altitude: Maximum flight altitude
        """
        # TODO: Implement __init__ using super()
        pass
    
    def charge_battery(self, amount: int) -> None:
        """
        Charge the drone's battery.
        
        Args:
            amount: Amount to charge (capped at 100)
        """
        # TODO: Implement charge_battery
        pass
    
    def deliver_shipment(self) -> Dict[str, Any]:
        """
        Override parent method to include drone-specific delivery info.
        
        Returns:
            Dictionary with drone-specific delivery details
        """
        # TODO: Implement deliver_shipment
        # Should call super().deliver_shipment() and add 'battery_level' and 'altitude'
        pass


class RefrigeratedTruck(Truck):
    """
    Specialized truck with refrigeration capability (multiple inheritance concept).
    Demonstrates multi-level inheritance: Vehicle -> Truck -> RefrigeratedTruck
    """
    
    def __init__(self, registration_id: str, capacity: float, axles: int = 2, temperature: float = 4.0):
        """
        Initialize a refrigerated truck.
        
        Args:
            registration_id: Truck registration number
            capacity: Carrying capacity
            axles: Number of axles
            temperature: Refrigeration temperature in Celsius
        """
        # TODO: Implement __init__ using super()
        pass
    
    def deliver_shipment(self) -> Dict[str, Any]:
        """
        Override parent method to include refrigeration details.
        
        Returns:
            Dictionary with refrigerated truck delivery details
        """
        # TODO: Implement deliver_shipment
        # Should call super().deliver_shipment() and add 'temperature'
        pass


class LogisticsFleet:
    """
    Container class that manages a fleet of vehicles and demonstrates polymorphism.
    """
    
    def __init__(self):
        """Initialize an empty fleet."""
        # TODO: Implement __init__
        pass
    
    def add_vehicle(self, vehicle: Vehicle) -> None:
        """Add a vehicle to the fleet."""
        # TODO: Implement add_vehicle
        pass
    
    def deliver_all_shipments(self) -> List[Dict[str, Any]]:
        """
        Deliver shipments from all vehicles (polymorphic operation).
        
        Implementation:
            - Iterate through all vehicles
            - Call deliver_shipment() on each (polymorphic method call)
            - Collect results
            - Unload all cargo after delivery
        
        Returns:
            List of delivery details from each vehicle
        """
        # TODO: Implement deliver_all_shipments
        pass
    
    def get_fleet_status(self) -> Dict[str, Any]:
        """
        Get overall fleet status.
        
        Returns:
            Dictionary with fleet statistics
        """
        # TODO: Implement get_fleet_status
        # Should include total_vehicles, total_capacity, total_load, vehicle_breakdown by type
        pass


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def run_tests():
    """Run test cases for OOP inheritance and polymorphism."""
    
    print("Test 1: Basic Vehicle functionality")
    truck = Truck('TRK-001', 5000.0, axles=3)
    truck.load_cargo(2000.0)
    truck.load_cargo(2000.0)
    print(f"  Truck capacity used: {truck.get_capacity_used():.1f}%")
    print(f"  Current load: {truck.current_load}\n")
    
    print("Test 2: Load exceeding capacity")
    success = truck.load_cargo(2000.0)
    print(f"  Loading 2000 units (capacity exceeded): {success}")
    print(f"  Current load: {truck.current_load}\n")
    
    print("Test 3: Unload cargo")
    truck.unload_cargo(1000.0)
    print(f"  Unloaded 1000 units")
    print(f"  Current load: {truck.current_load}\n")
    
    print("Test 4: Polymorphic delivery - Truck")
    delivery = truck.deliver_shipment()
    print(f"  Truck delivery: {delivery}\n")
    
    print("Test 5: Polymorphic delivery - Van")
    van = Van('VAN-001', 1500.0, refrigerated=True)
    van.load_cargo(1000.0)
    delivery = van.deliver_shipment()
    print(f"  Van delivery: {delivery}\n")
    
    print("Test 6: Polymorphic delivery - Drone")
    drone = Drone('DRN-001', 5.0, max_altitude=1000)
    drone.load_cargo(3.0)
    drone.charge_battery(50)
    delivery = drone.deliver_shipment()
    print(f"  Drone delivery: {delivery}\n")
    
    print("Test 7: Multi-level inheritance - RefrigeratedTruck")
    refrig_truck = RefrigeratedTruck('REF-TRK-001', 3000.0, axles=2, temperature=2.5)
    refrig_truck.load_cargo(2500.0)
    delivery = refrig_truck.deliver_shipment()
    print(f"  Refrigerated truck delivery: {delivery}\n")
    
    print("Test 8: Fleet management and polymorphic dispatch")
    fleet = LogisticsFleet()
    fleet.add_vehicle(Truck('TRK-002', 5000.0, axles=2))
    fleet.add_vehicle(Van('VAN-002', 1500.0, refrigerated=False))
    fleet.add_vehicle(Drone('DRN-002', 10.0, max_altitude=800))
    fleet.add_vehicle(RefrigeratedTruck('REF-TRK-002', 4000.0, axles=3, temperature=3.0))
    
    # Load cargo
    fleet.vehicles[0].load_cargo(3000.0)
    fleet.vehicles[1].load_cargo(1000.0)
    fleet.vehicles[2].load_cargo(5.0)
    fleet.vehicles[3].load_cargo(3000.0)
    
    print(f"  Fleet status: {fleet.get_fleet_status()}")
    
    # Deliver from all vehicles (polymorphic method call)
    deliveries = fleet.deliver_all_shipments()
    print(f"\n  Deliveries from all vehicles:")
    for delivery in deliveries:
        print(f"    {delivery}")
    print()


if __name__ == '__main__':
    run_tests()
