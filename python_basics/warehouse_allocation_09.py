"""
Assignment 9: Warehouse Allocation Simulator

Given a dict of bin capacities and a list of (sku, qty) items:
- Place each SKU into the first bin with sufficient remaining capacity
- Track remaining capacity in each bin
- Produce final allocations and a list of unplaced SKUs

Instructions:
- Implement the allocate_to_bins function
- Process items in order, placing in first available bin
- Return dict of allocations and list of unplaced items
"""


def allocate_to_bins(bin_capacities, items):
    """
    Allocate SKUs to warehouse bins based on capacity.
    
    Args:
        bin_capacities: Dict mapping bin code to max capacity
        items: List of tuples (sku, qty) to allocate
    
    Returns:
        Tuple of (allocations, unplaced)
        - allocations: Dict mapping bin code to list of (sku, qty) placed there
        - unplaced: List of (sku, qty) that couldn't fit in any bin
    
    Algorithm:
        For each item, find the first bin with remaining capacity >= qty.
        Place the item and reduce the remaining capacity.
        If no bin has sufficient capacity, add to unplaced list.
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def run_tests():
    """Run test cases for warehouse allocation simulator."""
    
    # Test case 1: Basic allocation
    bin_capacities = {
        'BIN-A': 100,
        'BIN-B': 50,
        'BIN-C': 75,
    }
    
    items = [
        ('SKU001', 30),  # Fits in BIN-A (70 remaining)
        ('SKU002', 40),  # Fits in BIN-A (30 remaining)
        ('SKU003', 50),  # Fits in BIN-B (0 remaining)
        ('SKU004', 35),  # Fits in BIN-C (40 remaining)
        ('SKU005', 25),  # Fits in BIN-A (5 remaining)
        ('SKU006', 60),  # Doesn't fit anywhere - unplaced
        ('SKU007', 40),  # Fits in BIN-C (0 remaining)
    ]
    
    result = allocate_to_bins(bin_capacities, items)
    
    assert result is not None, "Function not implemented - returns None"
    
    allocations, unplaced = result
    
    print("Test 1: Basic allocation")
    print(f"  Bin Capacities: {bin_capacities}")
    print(f"  Items to allocate: {items}")
    print()
    
    print("  Allocations:")
    for bin_code, allocated_items in allocations.items():
        print(f"    {bin_code}: {allocated_items}")
    
    print(f"\n  Unplaced items: {unplaced}")
    
    # Verify allocations
    assert 'BIN-A' in allocations, "BIN-A should have allocations"
    assert 'BIN-B' in allocations, "BIN-B should have allocations"
    assert 'BIN-C' in allocations, "BIN-C should have allocations"
    
    # Check BIN-A contains expected items
    bin_a_skus = [sku for sku, qty in allocations['BIN-A']]
    assert 'SKU001' in bin_a_skus, "SKU001 should be in BIN-A"
    assert 'SKU002' in bin_a_skus, "SKU002 should be in BIN-A"
    assert 'SKU005' in bin_a_skus, "SKU005 should be in BIN-A"
    
    # Check BIN-B
    bin_b_skus = [sku for sku, qty in allocations['BIN-B']]
    assert 'SKU003' in bin_b_skus, "SKU003 should be in BIN-B"
    
    # Check BIN-C
    bin_c_skus = [sku for sku, qty in allocations['BIN-C']]
    assert 'SKU004' in bin_c_skus, "SKU004 should be in BIN-C"
    assert 'SKU007' in bin_c_skus, "SKU007 should be in BIN-C"
    
    # Check unplaced
    unplaced_skus = [sku for sku, qty in unplaced]
    assert 'SKU006' in unplaced_skus, "SKU006 should be unplaced"
    
    print("  ✓ Passed")
    
    # Test case 2: All items fit
    bin_capacities2 = {'BIN-X': 1000}
    items2 = [('A', 100), ('B', 200), ('C', 300)]
    
    allocations2, unplaced2 = allocate_to_bins(bin_capacities2, items2)
    
    assert len(unplaced2) == 0, "All items should fit"
    assert len(allocations2['BIN-X']) == 3, "All 3 items should be in BIN-X"
    
    print("\nTest 2: All items fit in one bin")
    print(f"  Allocations: {allocations2}")
    print(f"  Unplaced: {unplaced2}")
    print("  ✓ Passed")
    
    # Test case 3: No items fit
    bin_capacities3 = {'BIN-Y': 10}
    items3 = [('X', 50), ('Y', 60)]
    
    allocations3, unplaced3 = allocate_to_bins(bin_capacities3, items3)
    
    assert len(unplaced3) == 2, "No items should fit"
    
    print("\nTest 3: No items fit")
    print(f"  Allocations: {allocations3}")
    print(f"  Unplaced: {unplaced3}")
    print("  ✓ Passed")
    
    print("\n" + "="*50)
    print("✅ ALL TESTS PASSED!")
    print("="*50)


if __name__ == "__main__":
    run_tests()
