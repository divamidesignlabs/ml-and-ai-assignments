"""
Pytest tests for Assignment 7: Naive Forecasting
"""

import pytest

from python_basics.naive_forecasting_07 import analyze_demand


class TestAnalyzeDemand:
    """Test cases for naive forecasting function."""
    
    def test_last_value(self):
        """Test last_value extraction."""
        result = analyze_demand([10, 20, 30])
        assert result['last_value'] == 30
    
    def test_last_value_single_item(self):
        """Test last_value with single item."""
        result = analyze_demand([100])
        assert result['last_value'] == 100
    
    def test_last_value_empty_list(self):
        """Test last_value with empty list."""
        result = analyze_demand([])
        assert result['last_value'] is None
    
    def test_num_increases_all_increasing(self):
        """Test num_increases with steadily increasing values."""
        result = analyze_demand([10, 20, 30, 40, 50])
        assert result['num_increases'] == 4
    
    def test_num_increases_all_decreasing(self):
        """Test num_increases with steadily decreasing values."""
        result = analyze_demand([50, 40, 30, 20, 10])
        assert result['num_increases'] == 0
    
    def test_num_increases_mixed(self):
        """Test num_increases with mixed pattern."""
        result = analyze_demand([100, 105, 102, 110, 115])
        # Increases: 105>100, 110>102, 115>110 = 3
        assert result['num_increases'] == 3
    
    def test_num_increases_empty(self):
        """Test num_increases with empty list."""
        result = analyze_demand([])
        assert result['num_increases'] == 0
    
    def test_num_increases_single(self):
        """Test num_increases with single value."""
        result = analyze_demand([100])
        assert result['num_increases'] == 0
    
    def test_longest_streak_all_increasing(self):
        """Test longest_streak with all increasing."""
        result = analyze_demand([10, 20, 30, 40, 50])
        assert result['longest_streak'] == 4
    
    def test_longest_streak_all_decreasing(self):
        """Test longest_streak with all decreasing."""
        result = analyze_demand([50, 40, 30, 20, 10])
        assert result['longest_streak'] == 0
    
    def test_longest_streak_mixed(self):
        """Test longest_streak with mixed pattern."""
        # Pattern: 100 -> 105 (up) -> 102 (down) -> 110 (up) -> 115 (up) -> 120 (up) -> 118 (down)
        result = analyze_demand([100, 105, 102, 110, 115, 120, 118])
        # Longest streak: 110 -> 115 -> 120 = 3 consecutive increases
        assert result['longest_streak'] == 3
    
    def test_longest_streak_empty(self):
        """Test longest_streak with empty list."""
        result = analyze_demand([])
        assert result['longest_streak'] == 0
    
    def test_longest_streak_single(self):
        """Test longest_streak with single value."""
        result = analyze_demand([100])
        assert result['longest_streak'] == 0
    
    def test_full_sample_from_assignment(self):
        """Test with full sample from assignment."""
        demand = [100, 105, 102, 110, 115, 120, 118, 125, 130, 128]
        result = analyze_demand(demand)
        
        expected = {
            'last_value': 128,
            'num_increases': 6,
            'longest_streak': 3
        }
        
        assert result['last_value'] == expected['last_value']
        assert result['num_increases'] == expected['num_increases']
        assert result['longest_streak'] == expected['longest_streak']
    
    def test_result_structure(self):
        """Test that result has correct structure."""
        result = analyze_demand([10, 20, 30])
        
        assert 'last_value' in result
        assert 'num_increases' in result
        assert 'longest_streak' in result
    
    def test_equal_consecutive_values(self):
        """Test handling of equal consecutive values."""
        result = analyze_demand([10, 10, 10, 20, 20])
        # Only one increase: from 10 to 20
        assert result['num_increases'] == 1
        assert result['longest_streak'] == 1
