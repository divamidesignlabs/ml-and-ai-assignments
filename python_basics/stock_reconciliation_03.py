"""
Assignment 3: Stock Reconciliation

Given two dicts 'system' and 'physical', classify each SKU as:
- surplus: physical > system (or SKU only in physical)
- deficit: physical < system (or SKU only in system)
- matched: physical == system

Return a dict containing lists of (sku, difference).

Instructions:
- Implement the reconcile_stock function
- Handle SKUs that appear in only one dict (treat missing as 0)
- difference = physical - system
- Return dict with keys 'surplus', 'deficit', 'matched'
"""


def reconcile_stock(system, physical):
    """
    Reconcile system inventory against physical count.
    
    Args:
        system: Dict mapping SKU to system quantity
        physical: Dict mapping SKU to physical count quantity
    
    Returns:
        Dict with keys 'surplus', 'deficit', 'matched', each containing
        a list of tuples (sku, difference) where difference = physical - system
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def run_tests():
    """Run test cases for stock reconciliation."""
    
    system_inventory = {
        'SKU001': 100,
        'SKU002': 50,
        'SKU003': 75,
        'SKU004': 30,
        'SKU005': 200,  # Only in system
    }
    
    physical_inventory = {
        'SKU001': 100,  # Matched
        'SKU002': 45,   # Deficit of 5
        'SKU003': 80,   # Surplus of 5
        'SKU004': 25,   # Deficit of 5
        'SKU006': 15,   # Only in physical - surplus
    }
    
    expected_result = {
        'surplus': [('SKU003', 5), ('SKU006', 15)],
        'deficit': [('SKU002', -5), ('SKU004', -5), ('SKU005', -200)],
        'matched': [('SKU001', 0)]
    }
    
    result = reconcile_stock(system_inventory, physical_inventory)
    
    assert result is not None, "Function not implemented - returns None"
    
    # Sort results for comparison (order may vary)
    for key in result:
        result[key] = sorted(result[key], key=lambda x: x[0])
    for key in expected_result:
        expected_result[key] = sorted(expected_result[key], key=lambda x: x[0])
    
    print("Reconciliation Results:")
    print("-" * 50)
    
    print("\nSurplus (physical > system):")
    for sku, diff in result.get('surplus', []):
        print(f"  {sku}: +{diff}")
    
    print("\nDeficit (physical < system):")
    for sku, diff in result.get('deficit', []):
        print(f"  {sku}: {diff}")
    
    print("\nMatched (physical == system):")
    for sku, diff in result.get('matched', []):
        print(f"  {sku}: {diff}")
    
    assert result == expected_result, \
        f"Reconciliation mismatch.\nExpected: {expected_result}\nGot: {result}"
    
    print("\n" + "="*50)
    print("✅ ALL TESTS PASSED!")
    print("="*50)


if __name__ == "__main__":
    run_tests()
