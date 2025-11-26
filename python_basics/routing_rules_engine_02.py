"""
Assignment 2: Routing Rules Engine

Write assign_zone(sku, qty, loc) implementing realistic warehouse rules:
- Bulk zone: qty >= 100
- General zone: 20 <= qty < 100
- Pick-face zone: qty < 20
- Hazmat override: SKU starting with 'HAZ' always goes to 'hazmat' zone

Apply it to normalized inventory and return (sku, zone) pairs.

Instructions:
- Implement the assign_zone function
- Rules are applied in order: hazmat check first, then quantity-based rules
- Return the zone as a string
"""


def assign_zone(sku, qty, loc):
    """
    Assign a warehouse zone based on SKU, quantity, and location.
    
    Args:
        sku: SKU identifier string
        qty: Quantity as integer
        loc: Location code string
    
    Returns:
        Zone name as string ('hazmat', 'bulk', 'general', or 'pick-face')
    
    Rules:
        1. If SKU starts with 'HAZ', return 'hazmat' (override)
        2. If qty >= 100, return 'bulk'
        3. If qty >= 20, return 'general'
        4. Otherwise, return 'pick-face'
    """
    # TODO: Implement this function
    pass


def apply_routing_rules(inventory_records):
    """
    Apply routing rules to a list of inventory records.
    
    Args:
        inventory_records: List of tuples (sku, qty, loc)
    
    Returns:
        List of tuples (sku, zone)
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def run_tests():
    """Run test cases for routing rules engine."""
    
    # Test individual zone assignments
    test_cases = [
        # (sku, qty, loc, expected_zone)
        ('SKU001', 150, 'A1', 'bulk'),
        ('SKU002', 50, 'B2', 'general'),
        ('SKU003', 10, 'C3', 'pick-face'),
        ('HAZ001', 200, 'D4', 'hazmat'),  # Hazmat override
        ('HAZ002', 5, 'E5', 'hazmat'),    # Hazmat override even with low qty
        ('SKU004', 100, 'F6', 'bulk'),    # Boundary case
        ('SKU005', 20, 'G7', 'general'),  # Boundary case
        ('SKU006', 19, 'H8', 'pick-face'),
    ]
    
    print("Testing assign_zone function:")
    print("-" * 50)
    
    for sku, qty, loc, expected in test_cases:
        result = assign_zone(sku, qty, loc)
        assert result is not None, f"Function not implemented - returns None for ({sku}, {qty}, {loc})"
        assert result == expected, \
            f"Zone mismatch for ({sku}, {qty}, {loc}). Expected: {expected}, Got: {result}"
        print(f"  ({sku}, {qty}, {loc}) -> {result} ✓")
    
    # Test apply_routing_rules
    print("\nTesting apply_routing_rules function:")
    print("-" * 50)
    
    sample_inventory = [
        ('SKU001', 10, 'A1'),
        ('SKU002', 25, 'B2'),
        ('HAZ003', 5, 'C3'),
        ('SKU004', 150, 'D4'),
    ]
    
    expected_routing = [
        ('SKU001', 'pick-face'),
        ('SKU002', 'general'),
        ('HAZ003', 'hazmat'),
        ('SKU004', 'bulk'),
    ]
    
    routing_result = apply_routing_rules(sample_inventory)
    
    assert routing_result is not None, "apply_routing_rules not implemented - returns None"
    assert routing_result == expected_routing, \
        f"Routing mismatch.\nExpected: {expected_routing}\nGot: {routing_result}"
    
    for sku, zone in routing_result:
        print(f"  {sku} -> {zone}")
    
    print("\n" + "="*50)
    print("✅ ALL TESTS PASSED!")
    print("="*50)


if __name__ == "__main__":
    run_tests()
