"""
Pytest tests for Assignment 10: Linehaul Time Calculator
"""

import pytest

from python_basics.linehaul_calculator_10 import Leg, total_transit_time, route_summary


class TestLeg:
    """Test cases for Leg class."""
    
    def test_init_attributes(self):
        """Test Leg initialization."""
        leg = Leg('New York', 'Chicago', 12.0)
        
        assert leg.start == 'New York'
        assert leg.end == 'Chicago'
        assert leg.hours == 12.0
    
    def test_str_contains_start(self):
        """Test __str__ contains start location."""
        leg = Leg('New York', 'Chicago', 12.0)
        assert 'New York' in str(leg)
    
    def test_str_contains_end(self):
        """Test __str__ contains end location."""
        leg = Leg('New York', 'Chicago', 12.0)
        assert 'Chicago' in str(leg)
    
    def test_str_contains_hours(self):
        """Test __str__ contains hours."""
        leg = Leg('New York', 'Chicago', 12.0)
        assert '12' in str(leg)
    
    def test_repr_contains_leg(self):
        """Test __repr__ contains 'Leg'."""
        leg = Leg('New York', 'Chicago', 12.0)
        assert 'Leg' in repr(leg)
    
    def test_repr_is_string(self):
        """Test __repr__ returns string."""
        leg = Leg('A', 'B', 5.0)
        assert isinstance(repr(leg), str)


class TestTotalTransitTime:
    """Test cases for total_transit_time function."""
    
    def test_single_leg(self):
        """Test with single leg."""
        leg = Leg('A', 'B', 12.0)
        assert total_transit_time(leg) == 12.0
    
    def test_multiple_legs(self):
        """Test with multiple legs."""
        leg1 = Leg('A', 'B', 12.0)
        leg2 = Leg('B', 'C', 14.5)
        leg3 = Leg('C', 'D', 16.0)
        
        total = total_transit_time(leg1, leg2, leg3)
        assert abs(total - 42.5) < 0.01
    
    def test_no_legs(self):
        """Test with no legs."""
        assert total_transit_time() == 0
    
    def test_integer_hours(self):
        """Test with integer hours."""
        leg1 = Leg('A', 'B', 10)
        leg2 = Leg('B', 'C', 20)
        
        assert total_transit_time(leg1, leg2) == 30
    
    def test_decimal_hours(self):
        """Test with decimal hours."""
        leg1 = Leg('A', 'B', 1.5)
        leg2 = Leg('B', 'C', 2.5)
        
        assert abs(total_transit_time(leg1, leg2) - 4.0) < 0.01


class TestRouteSummary:
    """Test cases for route_summary function."""
    
    def test_contains_all_locations(self):
        """Test summary contains all locations."""
        leg1 = Leg('New York', 'Chicago', 12.0)
        leg2 = Leg('Chicago', 'Los Angeles', 20.0)
        
        summary = route_summary(leg1, leg2)
        
        assert 'New York' in summary
        assert 'Chicago' in summary
        assert 'Los Angeles' in summary
    
    def test_contains_total_time(self):
        """Test summary contains total time."""
        leg1 = Leg('A', 'B', 10.0)
        leg2 = Leg('B', 'C', 15.0)
        
        summary = route_summary(leg1, leg2)
        
        assert '25' in summary
    
    def test_single_leg_summary(self):
        """Test summary with single leg."""
        leg = Leg('Start', 'End', 5.0)
        
        summary = route_summary(leg)
        
        assert 'Start' in summary
        assert 'End' in summary
        assert '5' in summary
    
    def test_returns_string(self):
        """Test that summary returns a string."""
        leg = Leg('A', 'B', 10.0)
        
        assert isinstance(route_summary(leg), str)


class TestFullIntegration:
    """Integration tests for linehaul calculator."""
    
    def test_full_sample_from_assignment(self):
        """Test with full sample from assignment."""
        leg1 = Leg('New York', 'Chicago', 12.0)
        leg2 = Leg('Chicago', 'Denver', 14.5)
        leg3 = Leg('Denver', 'Los Angeles', 16.0)
        
        # Test attributes
        assert leg1.start == 'New York'
        assert leg1.end == 'Chicago'
        assert leg1.hours == 12.0
        
        # Test total time
        total = total_transit_time(leg1, leg2, leg3)
        assert abs(total - 42.5) < 0.01
        
        # Test summary
        summary = route_summary(leg1, leg2, leg3)
        assert 'New York' in summary
        assert 'Los Angeles' in summary
        assert '42' in summary
    
    def test_leg_objects_independent(self):
        """Test that Leg objects are independent."""
        leg1 = Leg('A', 'B', 10.0)
        leg2 = Leg('C', 'D', 20.0)
        
        leg1.hours = 15.0
        
        assert leg2.hours == 20.0
