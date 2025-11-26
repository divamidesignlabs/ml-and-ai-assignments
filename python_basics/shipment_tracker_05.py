"""
Assignment 5: ShipmentTracker Class

Build a class with:
- Class attribute: carrier (default carrier name)
- Instance attributes: shipment_id, origin, destination, events (list)
- Method to add events
- Ability to modify carrier on one instance without affecting others
- __str__ method for readable output

Instructions:
- Implement the ShipmentTracker class
- Events should be stored as a list of strings or dicts
- The carrier can be changed per instance
"""


class ShipmentTracker:
    """
    Track shipments with carrier, route, and event information.
    
    Class Attributes:
        carrier: Default carrier name (shared across instances unless overridden)
    
    Instance Attributes:
        shipment_id: Unique identifier for the shipment
        origin: Origin location
        destination: Destination location
        events: List of tracking events
    """
    
    # TODO: Add class attribute 'carrier' with default value 'Standard Logistics'
    
    def __init__(self, shipment_id, origin, destination):
        """
        Initialize a new shipment tracker.
        
        Args:
            shipment_id: Unique identifier for the shipment
            origin: Origin location string
            destination: Destination location string
        """
        # TODO: Initialize instance attributes
        pass
    
    def add_event(self, event):
        """
        Add a tracking event to the shipment.
        
        Args:
            event: Event description string
        """
        # TODO: Implement this method
        pass
    
    def __str__(self):
        """
        Return a readable string representation of the shipment.
        
        Returns:
            Formatted string with shipment details
        """
        # TODO: Implement this method
        pass


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def run_tests():
    """Run test cases for ShipmentTracker class."""
    
    # Test class attribute
    assert hasattr(ShipmentTracker, 'carrier'), "Class should have 'carrier' class attribute"
    assert ShipmentTracker.carrier == 'Standard Logistics', \
        f"Default carrier should be 'Standard Logistics', got: {ShipmentTracker.carrier}"
    
    print("Test 1: Class attribute 'carrier'")
    print(f"  Default carrier: {ShipmentTracker.carrier}")
    print("  ✓ Passed")
    
    # Create shipments
    shipment1 = ShipmentTracker('SHIP001', 'New York', 'Los Angeles')
    shipment2 = ShipmentTracker('SHIP002', 'Chicago', 'Miami')
    
    # Test instance attributes
    assert shipment1.shipment_id == 'SHIP001', f"shipment_id mismatch: {shipment1.shipment_id}"
    assert shipment1.origin == 'New York', f"origin mismatch: {shipment1.origin}"
    assert shipment1.destination == 'Los Angeles', f"destination mismatch: {shipment1.destination}"
    assert isinstance(shipment1.events, list), "events should be a list"
    assert len(shipment1.events) == 0, "events should start empty"
    
    print("\nTest 2: Instance attributes")
    print(f"  Shipment ID: {shipment1.shipment_id}")
    print(f"  Origin: {shipment1.origin}")
    print(f"  Destination: {shipment1.destination}")
    print(f"  Events: {shipment1.events}")
    print("  ✓ Passed")
    
    # Test add_event
    shipment1.add_event('Package picked up')
    shipment1.add_event('In transit - Denver hub')
    shipment1.add_event('Out for delivery')
    
    assert len(shipment1.events) == 3, f"Should have 3 events, got: {len(shipment1.events)}"
    assert 'Package picked up' in shipment1.events, "First event missing"
    
    print("\nTest 3: Adding events")
    print(f"  Events: {shipment1.events}")
    print("  ✓ Passed")
    
    # Test modifying carrier on one instance
    shipment2.carrier = 'Express Freight'
    
    assert shipment2.carrier == 'Express Freight', \
        f"Shipment 2 carrier should be 'Express Freight', got: {shipment2.carrier}"
    assert shipment1.carrier == 'Standard Logistics', \
        f"Shipment 1 carrier should still be 'Standard Logistics', got: {shipment1.carrier}"
    assert ShipmentTracker.carrier == 'Standard Logistics', \
        f"Class carrier should still be 'Standard Logistics', got: {ShipmentTracker.carrier}"
    
    print("\nTest 4: Instance-specific carrier modification")
    print(f"  Shipment 1 carrier: {shipment1.carrier}")
    print(f"  Shipment 2 carrier: {shipment2.carrier}")
    print(f"  Class carrier: {ShipmentTracker.carrier}")
    print("  ✓ Passed")
    
    # Test __str__
    str_output = str(shipment1)
    assert str_output is not None, "__str__ not implemented"
    assert 'SHIP001' in str_output, "shipment_id should be in __str__ output"
    assert 'New York' in str_output, "origin should be in __str__ output"
    assert 'Los Angeles' in str_output, "destination should be in __str__ output"
    
    print("\nTest 5: __str__ method")
    print(f"  Output:\n{shipment1}")
    print("  ✓ Passed")
    
    print("\n" + "="*50)
    print("✅ ALL TESTS PASSED!")
    print("="*50)


if __name__ == "__main__":
    run_tests()
