"""
Pytest tests for Assignment 8: SKU Comparison Class
"""

import pytest

from python_basics.sku_comparison_08 import SKU


class TestSKU:
    """Test cases for SKU comparison class."""
    
    def test_init_stores_code(self):
        """Test that SKU stores the code."""
        sku = SKU('ABC123')
        assert hasattr(sku, 'code')
        assert sku.code.upper() == 'ABC123'
    
    def test_eq_same_case(self):
        """Test equality with same case."""
        sku1 = SKU('ABC123')
        sku2 = SKU('ABC123')
        assert sku1 == sku2
    
    def test_eq_different_case(self):
        """Test case-insensitive equality."""
        sku1 = SKU('ABC123')
        sku2 = SKU('abc123')
        assert sku1 == sku2
    
    def test_eq_different_skus(self):
        """Test inequality for different SKUs."""
        sku1 = SKU('ABC123')
        sku2 = SKU('DEF456')
        assert not (sku1 == sku2)
    
    def test_lt_basic(self):
        """Test less-than comparison."""
        sku1 = SKU('ABC123')
        sku2 = SKU('DEF456')
        assert sku1 < sku2
    
    def test_lt_case_insensitive(self):
        """Test case-insensitive less-than."""
        sku1 = SKU('abc123')
        sku2 = SKU('DEF456')
        assert sku1 < sku2
    
    def test_lt_same_prefix(self):
        """Test less-than with same prefix."""
        sku1 = SKU('ABC100')
        sku2 = SKU('ABC123')
        assert sku1 < sku2
    
    def test_sorting(self):
        """Test sorting list of SKUs."""
        skus = [
            SKU('xyz789'),
            SKU('DEF456'),
            SKU('ABC123'),
            SKU('abc100')
        ]
        
        sorted_skus = sorted(skus)
        sorted_codes = [s.code.upper() for s in sorted_skus]
        
        assert sorted_codes == ['ABC100', 'ABC123', 'DEF456', 'XYZ789']
    
    def test_hash_same_case(self):
        """Test hash for same case SKUs."""
        sku1 = SKU('ABC123')
        sku2 = SKU('ABC123')
        assert hash(sku1) == hash(sku2)
    
    def test_hash_different_case(self):
        """Test hash is case-insensitive."""
        sku1 = SKU('ABC123')
        sku2 = SKU('abc123')
        assert hash(sku1) == hash(sku2)
    
    def test_hash_different_skus(self):
        """Test different SKUs have different hashes (usually)."""
        sku1 = SKU('ABC123')
        sku2 = SKU('DEF456')
        # This should be true for any reasonable hash
        assert hash(sku1) != hash(sku2)
    
    def test_set_membership(self):
        """Test SKU can be used in a set."""
        sku1 = SKU('ABC123')
        sku2 = SKU('abc123')  # Same as sku1
        sku3 = SKU('DEF456')
        
        sku_set = {sku1, sku2, sku3}
        
        # sku1 and sku2 should be deduplicated
        assert len(sku_set) == 2
    
    def test_set_lookup(self):
        """Test finding SKU in a set (case-insensitive)."""
        sku_set = {SKU('ABC123'), SKU('DEF456')}
        
        # Should find lowercase version
        lookup = SKU('abc123')
        assert lookup in sku_set
    
    def test_repr(self):
        """Test __repr__ returns valid string."""
        sku = SKU('ABC123')
        repr_str = repr(sku)
        
        assert 'SKU' in repr_str
        assert 'ABC123' in repr_str or 'abc123' in repr_str.lower()
    
    def test_full_sample_from_assignment(self):
        """Test full sample from assignment."""
        sku1 = SKU('ABC123')
        sku2 = SKU('abc123')
        sku3 = SKU('DEF456')
        sku4 = SKU('ABC100')
        sku5 = SKU('xyz789')
        
        # Test equality
        assert sku1 == sku2
        assert not (sku1 == sku3)
        
        # Test sorting
        sku_list = [sku5, sku3, sku1, sku4]
        sorted_skus = sorted(sku_list)
        expected_order = ['ABC100', 'ABC123', 'DEF456', 'XYZ789']
        assert [s.code.upper() for s in sorted_skus] == expected_order
        
        # Test set
        sku_set = {sku1, sku2, sku3, sku4, sku5}
        assert len(sku_set) == 4  # sku1 and sku2 are same
