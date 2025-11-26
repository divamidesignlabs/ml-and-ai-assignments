"""
Pytest tests for Assignment 5: ShipmentTracker Class
"""

import pytest

from python_basics.shipment_tracker_05 import ShipmentTracker


class TestShipmentTracker:
    """Test cases for ShipmentTracker class."""
    
    def test_class_attribute_carrier(self):
        """Test that carrier is a class attribute with default value."""
        assert hasattr(ShipmentTracker, 'carrier')
        assert ShipmentTracker.carrier == 'Standard Logistics'
    
    def test_instance_attributes(self):
        """Test instance attributes are set correctly."""
        tracker = ShipmentTracker('SHIP001', 'New York', 'Los Angeles')
        
        assert tracker.shipment_id == 'SHIP001'
        assert tracker.origin == 'New York'
        assert tracker.destination == 'Los Angeles'
    
    def test_events_starts_empty(self):
        """Test that events list starts empty."""
        tracker = ShipmentTracker('SHIP001', 'A', 'B')
        
        assert isinstance(tracker.events, list)
        assert len(tracker.events) == 0
    
    def test_add_event(self):
        """Test adding events to shipment."""
        tracker = ShipmentTracker('SHIP001', 'A', 'B')
        
        tracker.add_event('Package picked up')
        assert len(tracker.events) == 1
        assert 'Package picked up' in tracker.events
        
        tracker.add_event('In transit')
        assert len(tracker.events) == 2
    
    def test_events_isolated_between_instances(self):
        """Test that events lists are not shared between instances."""
        tracker1 = ShipmentTracker('SHIP001', 'A', 'B')
        tracker2 = ShipmentTracker('SHIP002', 'C', 'D')
        
        tracker1.add_event('Event for tracker 1')
        
        assert len(tracker1.events) == 1
        assert len(tracker2.events) == 0
    
    def test_modify_carrier_on_instance(self):
        """Test that carrier can be modified on one instance."""
        tracker1 = ShipmentTracker('SHIP001', 'A', 'B')
        tracker2 = ShipmentTracker('SHIP002', 'C', 'D')
        
        tracker2.carrier = 'Express Freight'
        
        assert tracker2.carrier == 'Express Freight'
        assert tracker1.carrier == 'Standard Logistics'
        assert ShipmentTracker.carrier == 'Standard Logistics'
    
    def test_str_contains_shipment_id(self):
        """Test __str__ contains shipment_id."""
        tracker = ShipmentTracker('SHIP001', 'New York', 'Los Angeles')
        str_output = str(tracker)
        
        assert 'SHIP001' in str_output
    
    def test_str_contains_origin(self):
        """Test __str__ contains origin."""
        tracker = ShipmentTracker('SHIP001', 'New York', 'Los Angeles')
        str_output = str(tracker)
        
        assert 'New York' in str_output
    
    def test_str_contains_destination(self):
        """Test __str__ contains destination."""
        tracker = ShipmentTracker('SHIP001', 'New York', 'Los Angeles')
        str_output = str(tracker)
        
        assert 'Los Angeles' in str_output
    
    def test_str_returns_string(self):
        """Test __str__ returns a string."""
        tracker = ShipmentTracker('SHIP001', 'A', 'B')
        assert isinstance(str(tracker), str)
    
    def test_multiple_events(self):
        """Test adding multiple events."""
        tracker = ShipmentTracker('SHIP001', 'A', 'B')
        
        events = [
            'Package picked up',
            'In transit - Hub 1',
            'In transit - Hub 2',
            'Out for delivery',
            'Delivered'
        ]
        
        for event in events:
            tracker.add_event(event)
        
        assert len(tracker.events) == 5
        for event in events:
            assert event in tracker.events
