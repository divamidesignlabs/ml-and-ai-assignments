"""
Assignment 8: SKU Comparison Class

Implement class SKU with:
- Case-insensitive __eq__: 'SKU001' == 'sku001'
- Sortable __lt__: For sorting SKUs alphabetically (case-insensitive)
- Clean __repr__: Developer-friendly representation
- __hash__: Required for use in sets (based on normalized SKU)

Create several SKUs, sort them, compare them, and place them in a set.

Instructions:
- Implement the SKU class with all comparison methods
- Normalize SKU codes (e.g., uppercase) for comparison
- Implement __hash__ to allow use in sets
"""


class SKU:
    """
    A SKU (Stock Keeping Unit) class with case-insensitive comparison.
    
    Supports equality checking, sorting, and use in sets.
    """
    
    def __init__(self, code):
        """
        Initialize SKU with a code.
        
        Args:
            code: SKU identifier string
        """
        # TODO: Store the original code and a normalized version
        pass
    
    def __eq__(self, other):
        """
        Case-insensitive equality comparison.
        
        Args:
            other: Another SKU or string to compare
        
        Returns:
            True if SKUs are equal (case-insensitive)
        """
        # TODO: Implement case-insensitive comparison
        pass
    
    def __lt__(self, other):
        """
        Less-than comparison for sorting (case-insensitive).
        
        Args:
            other: Another SKU to compare
        
        Returns:
            True if this SKU comes before other alphabetically
        """
        # TODO: Implement for sorting
        pass
    
    def __hash__(self):
        """
        Hash function for use in sets and dicts.
        
        Returns:
            Hash based on normalized SKU code
        """
        # TODO: Implement hash based on normalized code
        pass
    
    def __repr__(self):
        """
        Developer-friendly string representation.
        
        Returns:
            String like SKU('ABC123')
        """
        # TODO: Implement repr
        pass


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def run_tests():
    """Run test cases for SKU comparison class."""
    
    # Create SKUs
    sku1 = SKU('ABC123')
    sku2 = SKU('abc123')  # Same as sku1, different case
    sku3 = SKU('DEF456')
    sku4 = SKU('ABC100')
    sku5 = SKU('xyz789')
    
    # Test __eq__ (case-insensitive)
    assert sku1 == sku2, f"'ABC123' should equal 'abc123'"
    assert not (sku1 == sku3), f"'ABC123' should not equal 'DEF456'"
    
    print("Test 1: __eq__ (case-insensitive equality)")
    print(f"  SKU('ABC123') == SKU('abc123'): {sku1 == sku2}")
    print(f"  SKU('ABC123') == SKU('DEF456'): {sku1 == sku3}")
    print("  ✓ Passed")
    
    # Test __lt__ (sorting)
    assert sku4 < sku1, f"'ABC100' should be less than 'ABC123'"
    assert sku1 < sku3, f"'ABC123' should be less than 'DEF456'"
    
    print("\nTest 2: __lt__ (sorting)")
    print(f"  SKU('ABC100') < SKU('ABC123'): {sku4 < sku1}")
    print(f"  SKU('ABC123') < SKU('DEF456'): {sku1 < sku3}")
    print("  ✓ Passed")
    
    # Test sorting a list of SKUs
    sku_list = [sku5, sku3, sku1, sku4]
    sorted_skus = sorted(sku_list)
    expected_order = ['ABC100', 'ABC123', 'DEF456', 'XYZ789']
    sorted_codes = [s.code.upper() for s in sorted_skus]
    
    assert sorted_codes == expected_order, \
        f"Sorted order mismatch. Expected: {expected_order}, Got: {sorted_codes}"
    
    print("\nTest 3: Sorting SKUs")
    print(f"  Original: {[s.code for s in sku_list]}")
    print(f"  Sorted: {[s.code for s in sorted_skus]}")
    print("  ✓ Passed")
    
    # Test __hash__ (use in set)
    sku_set = {sku1, sku2, sku3, sku4, sku5}
    # sku1 and sku2 should be the same in set (case-insensitive)
    assert len(sku_set) == 4, \
        f"Set should have 4 unique SKUs (ABC123/abc123 are same), got: {len(sku_set)}"
    
    print("\nTest 4: __hash__ (use in set)")
    print(f"  Added 5 SKUs (2 with same code, different case)")
    print(f"  Set size: {len(sku_set)}")
    print(f"  Set contents: {sku_set}")
    print("  ✓ Passed")
    
    # Test __repr__
    repr_str = repr(sku1)
    assert 'SKU' in repr_str, f"__repr__ should contain 'SKU'"
    assert 'ABC123' in repr_str or 'abc123' in repr_str.lower(), \
        f"__repr__ should contain the SKU code"
    
    print("\nTest 5: __repr__")
    print(f"  repr(SKU('ABC123')) = {repr_str}")
    print("  ✓ Passed")
    
    # Test membership
    assert sku2 in sku_set, "SKU('abc123') should be found in set (case-insensitive)"
    print("\nTest 6: Set membership (case-insensitive)")
    print(f"  SKU('abc123') in set containing SKU('ABC123'): True")
    print("  ✓ Passed")
    
    print("\n" + "="*50)
    print("✅ ALL TESTS PASSED!")
    print("="*50)


if __name__ == "__main__":
    run_tests()
