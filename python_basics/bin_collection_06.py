"""
Assignment 6: BinCollection Sequence Class

Create a class that wraps a list of bin codes and supports:
- __getitem__: Get bin by index
- __setitem__: Set bin by index
- __delitem__: Delete bin by index
- __len__: Get number of bins
- __iter__: Iterate over bins

Demonstrate reading, modifying, deleting, and iterating.

Instructions:
- Implement all the dunder methods listed above
- The class should wrap an internal list
- Support both positive and negative indexing
"""


class BinCollection:
    """
    A collection of warehouse bin codes that behaves like a sequence.
    
    Supports indexing, iteration, and modification of bin codes.
    """
    
    def __init__(self, bins=None):
        """
        Initialize the bin collection.
        
        Args:
            bins: Optional list of bin codes to initialize with
        """
        # TODO: Initialize internal list
        pass
    
    def __getitem__(self, index):
        """
        Get bin code at the specified index.
        
        Args:
            index: Integer index (supports negative indexing)
        
        Returns:
            Bin code at the specified index
        """
        # TODO: Implement this method
        pass
    
    def __setitem__(self, index, value):
        """
        Set bin code at the specified index.
        
        Args:
            index: Integer index (supports negative indexing)
            value: New bin code value
        """
        # TODO: Implement this method
        pass
    
    def __delitem__(self, index):
        """
        Delete bin at the specified index.
        
        Args:
            index: Integer index (supports negative indexing)
        """
        # TODO: Implement this method
        pass
    
    def __len__(self):
        """
        Return the number of bins in the collection.
        
        Returns:
            Integer count of bins
        """
        # TODO: Implement this method
        pass
    
    def __iter__(self):
        """
        Return an iterator over the bin codes.
        
        Returns:
            Iterator over bin codes
        """
        # TODO: Implement this method
        pass
    
    def __repr__(self):
        """
        Return a developer-friendly representation.
        
        Returns:
            String representation of the collection
        """
        # TODO: Implement this method (optional but helpful)
        pass


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def run_tests():
    """Run test cases for BinCollection class."""
    
    # Initialize collection
    bins = BinCollection(['A1', 'A2', 'B1', 'B2', 'C1'])
    
    # Test __len__
    assert len(bins) == 5, f"Length should be 5, got: {len(bins)}"
    print("Test 1: __len__")
    print(f"  Length: {len(bins)}")
    print("  ✓ Passed")
    
    # Test __getitem__ with positive index
    assert bins[0] == 'A1', f"bins[0] should be 'A1', got: {bins[0]}"
    assert bins[2] == 'B1', f"bins[2] should be 'B1', got: {bins[2]}"
    print("\nTest 2: __getitem__ (positive index)")
    print(f"  bins[0] = {bins[0]}")
    print(f"  bins[2] = {bins[2]}")
    print("  ✓ Passed")
    
    # Test __getitem__ with negative index
    assert bins[-1] == 'C1', f"bins[-1] should be 'C1', got: {bins[-1]}"
    assert bins[-2] == 'B2', f"bins[-2] should be 'B2', got: {bins[-2]}"
    print("\nTest 3: __getitem__ (negative index)")
    print(f"  bins[-1] = {bins[-1]}")
    print(f"  bins[-2] = {bins[-2]}")
    print("  ✓ Passed")
    
    # Test __setitem__
    bins[1] = 'A2-MODIFIED'
    assert bins[1] == 'A2-MODIFIED', f"bins[1] should be 'A2-MODIFIED', got: {bins[1]}"
    print("\nTest 4: __setitem__")
    print(f"  bins[1] = 'A2-MODIFIED' -> {bins[1]}")
    print("  ✓ Passed")
    
    # Test __delitem__
    del bins[1]
    assert len(bins) == 4, f"Length should be 4 after delete, got: {len(bins)}"
    assert bins[1] == 'B1', f"bins[1] should be 'B1' after delete, got: {bins[1]}"
    print("\nTest 5: __delitem__")
    print(f"  After deleting index 1, length: {len(bins)}")
    print(f"  bins[1] is now: {bins[1]}")
    print("  ✓ Passed")
    
    # Test __iter__
    bins_list = list(bins)
    expected_list = ['A1', 'B1', 'B2', 'C1']
    assert bins_list == expected_list, f"Iteration mismatch. Expected: {expected_list}, Got: {bins_list}"
    print("\nTest 6: __iter__")
    print("  Iterating over bins:")
    for bin_code in bins:
        print(f"    - {bin_code}")
    print("  ✓ Passed")
    
    # Test __repr__ (optional but helpful)
    print("\nTest 7: __repr__")
    print(f"  repr(bins) = {repr(bins)}")
    print("  ✓ Passed")
    
    # Test IndexError for out of bounds
    try:
        _ = bins[100]
        assert False, "Should raise IndexError for out of bounds access"
    except IndexError:
        print("\nTest 8: IndexError for out of bounds")
        print("  bins[100] raises IndexError")
        print("  ✓ Passed")
    
    print("\n" + "="*50)
    print("✅ ALL TESTS PASSED!")
    print("="*50)


if __name__ == "__main__":
    run_tests()
