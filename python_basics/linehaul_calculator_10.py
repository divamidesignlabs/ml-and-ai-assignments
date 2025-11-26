"""
Assignment 10: Linehaul Time Calculator

Create a Leg class representing a transportation leg with:
- start: Starting location
- end: Ending location
- hours: Transit time in hours

Implement:
- total_transit_time(*legs): Sum all leg hours
- __str__ or __repr__: Readable route summary

Instructions:
- Implement the Leg class with proper dunder methods
- Implement the total_transit_time function
- Create a readable route summary showing the full journey
"""


class Leg:
    """
    Represents a single leg of a transportation route.
    
    Attributes:
        start: Starting location
        end: Ending location
        hours: Transit time in hours
    """
    
    def __init__(self, start, end, hours):
        """
        Initialize a transportation leg.
        
        Args:
            start: Starting location string
            end: Ending location string
            hours: Transit time as number (int or float)
        """
        # TODO: Initialize attributes
        pass
    
    def __str__(self):
        """
        Human-readable string representation.
        
        Returns:
            String like "New York -> Chicago (12.0 hrs)"
        """
        # TODO: Implement this method
        pass
    
    def __repr__(self):
        """
        Developer-friendly representation.
        
        Returns:
            String like "Leg('New York', 'Chicago', 12.0)"
        """
        # TODO: Implement this method
        pass


def total_transit_time(*legs):
    """
    Calculate total transit time across multiple legs.
    
    Args:
        *legs: Variable number of Leg objects
    
    Returns:
        Total hours as a number
    """
    # TODO: Implement this function
    pass


def route_summary(*legs):
    """
    Generate a readable summary of the entire route.
    
    Args:
        *legs: Variable number of Leg objects
    
    Returns:
        Multi-line string showing the route and total time
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def run_tests():
    """Run test cases for linehaul time calculator."""
    
    # Create legs
    leg1 = Leg('New York', 'Chicago', 12.0)
    leg2 = Leg('Chicago', 'Denver', 14.5)
    leg3 = Leg('Denver', 'Los Angeles', 16.0)
    
    # Test Leg attributes
    assert leg1.start == 'New York', f"start mismatch: {leg1.start}"
    assert leg1.end == 'Chicago', f"end mismatch: {leg1.end}"
    assert leg1.hours == 12.0, f"hours mismatch: {leg1.hours}"
    
    print("Test 1: Leg attributes")
    print(f"  Leg 1: start={leg1.start}, end={leg1.end}, hours={leg1.hours}")
    print("  ✓ Passed")
    
    # Test __str__
    str_output = str(leg1)
    assert str_output is not None, "__str__ not implemented"
    assert 'New York' in str_output, "start should be in __str__ output"
    assert 'Chicago' in str_output, "end should be in __str__ output"
    assert '12' in str_output, "hours should be in __str__ output"
    
    print("\nTest 2: __str__ method")
    print(f"  str(leg1) = {str_output}")
    print("  ✓ Passed")
    
    # Test __repr__
    repr_output = repr(leg1)
    assert repr_output is not None, "__repr__ not implemented"
    assert 'Leg' in repr_output, "'Leg' should be in __repr__ output"
    
    print("\nTest 3: __repr__ method")
    print(f"  repr(leg1) = {repr_output}")
    print("  ✓ Passed")
    
    # Test total_transit_time
    total = total_transit_time(leg1, leg2, leg3)
    expected_total = 42.5
    
    assert total is not None, "total_transit_time not implemented"
    assert abs(total - expected_total) < 0.01, \
        f"Total mismatch. Expected: {expected_total}, Got: {total}"
    
    print("\nTest 4: total_transit_time")
    print(f"  Legs: {leg1.hours} + {leg2.hours} + {leg3.hours} = {total} hrs")
    print("  ✓ Passed")
    
    # Test with single leg
    single_total = total_transit_time(leg1)
    assert single_total == 12.0, f"Single leg total should be 12.0, got: {single_total}"
    
    print("\nTest 5: total_transit_time with single leg")
    print(f"  Single leg: {single_total} hrs")
    print("  ✓ Passed")
    
    # Test with no legs
    empty_total = total_transit_time()
    assert empty_total == 0, f"Empty total should be 0, got: {empty_total}"
    
    print("\nTest 6: total_transit_time with no legs")
    print(f"  No legs: {empty_total} hrs")
    print("  ✓ Passed")
    
    # Test route_summary
    summary = route_summary(leg1, leg2, leg3)
    
    assert summary is not None, "route_summary not implemented"
    assert 'New York' in summary, "Route should include New York"
    assert 'Los Angeles' in summary, "Route should include Los Angeles"
    assert '42.5' in summary or '42' in summary, "Route should include total time"
    
    print("\nTest 7: route_summary")
    print("  Route Summary:")
    print(f"{summary}")
    print("  ✓ Passed")
    
    print("\n" + "="*50)
    print("✅ ALL TESTS PASSED!")
    print("="*50)


if __name__ == "__main__":
    run_tests()
