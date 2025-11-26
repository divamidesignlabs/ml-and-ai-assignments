"""
Assignment 7: Naive Forecasting

For a list of daily demand values, compute:
- last_value: The last value in the list
- num_increases: Count of days where demand increased from previous day
- longest_streak: Longest consecutive upward streak

Return results in a dict.

Instructions:
- Implement the analyze_demand function
- Handle edge cases (empty list, single value)
- A streak of 1 increase counts as streak length 1
"""


def analyze_demand(demand_values):
    """
    Analyze daily demand values for forecasting metrics.
    
    Args:
        demand_values: List of numeric demand values (one per day)
    
    Returns:
        Dict with keys:
        - 'last_value': Last demand value (None if empty list)
        - 'num_increases': Count of day-over-day increases
        - 'longest_streak': Length of longest consecutive increase streak
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def run_tests():
    """Run test cases for naive forecasting."""
    
    # Test case 1: Normal demand pattern
    demand1 = [100, 105, 102, 110, 115, 120, 118, 125, 130, 128]
    result1 = analyze_demand(demand1)
    
    assert result1 is not None, "Function not implemented - returns None"
    
    expected1 = {
        'last_value': 128,
        'num_increases': 6,  # 105>100, 110>102, 115>110, 120>115, 125>118, 130>125
        'longest_streak': 3  # 110->115->120
    }
    
    assert result1['last_value'] == expected1['last_value'], \
        f"last_value mismatch. Expected: {expected1['last_value']}, Got: {result1['last_value']}"
    assert result1['num_increases'] == expected1['num_increases'], \
        f"num_increases mismatch. Expected: {expected1['num_increases']}, Got: {result1['num_increases']}"
    assert result1['longest_streak'] == expected1['longest_streak'], \
        f"longest_streak mismatch. Expected: {expected1['longest_streak']}, Got: {result1['longest_streak']}"
    
    print("Test 1: Normal demand pattern")
    print(f"  Demand: {demand1}")
    print(f"  Result: {result1}")
    print("  ✓ Passed")
    
    # Test case 2: Steady increase
    demand2 = [10, 20, 30, 40, 50]
    result2 = analyze_demand(demand2)
    
    expected2 = {
        'last_value': 50,
        'num_increases': 4,
        'longest_streak': 4
    }
    
    assert result2 == expected2, f"Mismatch. Expected: {expected2}, Got: {result2}"
    
    print("\nTest 2: Steady increase")
    print(f"  Demand: {demand2}")
    print(f"  Result: {result2}")
    print("  ✓ Passed")
    
    # Test case 3: Steady decrease
    demand3 = [50, 40, 30, 20, 10]
    result3 = analyze_demand(demand3)
    
    expected3 = {
        'last_value': 10,
        'num_increases': 0,
        'longest_streak': 0
    }
    
    assert result3 == expected3, f"Mismatch. Expected: {expected3}, Got: {result3}"
    
    print("\nTest 3: Steady decrease")
    print(f"  Demand: {demand3}")
    print(f"  Result: {result3}")
    print("  ✓ Passed")
    
    # Test case 4: Single value
    demand4 = [100]
    result4 = analyze_demand(demand4)
    
    expected4 = {
        'last_value': 100,
        'num_increases': 0,
        'longest_streak': 0
    }
    
    assert result4 == expected4, f"Mismatch. Expected: {expected4}, Got: {result4}"
    
    print("\nTest 4: Single value")
    print(f"  Demand: {demand4}")
    print(f"  Result: {result4}")
    print("  ✓ Passed")
    
    # Test case 5: Empty list
    demand5 = []
    result5 = analyze_demand(demand5)
    
    expected5 = {
        'last_value': None,
        'num_increases': 0,
        'longest_streak': 0
    }
    
    assert result5 == expected5, f"Mismatch. Expected: {expected5}, Got: {result5}"
    
    print("\nTest 5: Empty list")
    print(f"  Demand: {demand5}")
    print(f"  Result: {result5}")
    print("  ✓ Passed")
    
    print("\n" + "="*50)
    print("✅ ALL TESTS PASSED!")
    print("="*50)


if __name__ == "__main__":
    run_tests()
