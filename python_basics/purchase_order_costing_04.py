"""
Assignment 4: Purchase Order Costing

Implement compute_po_cost(*line_items, tax_rate=0.05, **meta) where:
- Each line item is a tuple (qty, price)
- Compute subtotal = sum of (qty * price) for all line items
- tax = subtotal * tax_rate
- total = subtotal + tax
- Extract 'vendor' from meta (default to 'Unknown')

Return tuple (vendor, subtotal, tax, total).

Instructions:
- Use *args for variable number of line items
- Use keyword argument for tax_rate with default 0.05
- Use **kwargs to capture metadata including vendor
"""


def compute_po_cost(*line_items, tax_rate=0.05, **meta):
    """
    Compute purchase order cost from line items.
    
    Args:
        *line_items: Variable number of tuples (qty, price)
        tax_rate: Tax rate as decimal (default 0.05 = 5%)
        **meta: Metadata dict, should contain 'vendor' key
    
    Returns:
        Tuple of (vendor, subtotal, tax, total)
        - vendor: String from meta or 'Unknown'
        - subtotal: Sum of qty * price for all line items
        - tax: subtotal * tax_rate
        - total: subtotal + tax
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def run_tests():
    """Run test cases for purchase order costing."""
    
    # Test case 1: Basic PO with vendor
    result1 = compute_po_cost(
        (10, 25.00),   # 10 units at $25 = $250
        (5, 50.00),    # 5 units at $50 = $250
        (20, 10.00),   # 20 units at $10 = $200
        tax_rate=0.08,
        vendor='Acme Supplies',
        po_number='PO-2024-001'
    )
    
    assert result1 is not None, "Function not implemented - returns None"
    
    vendor1, subtotal1, tax1, total1 = result1
    
    expected_subtotal1 = 700.00
    expected_tax1 = 56.00
    expected_total1 = 756.00
    
    assert vendor1 == 'Acme Supplies', f"Vendor mismatch. Expected: 'Acme Supplies', Got: {vendor1}"
    assert abs(subtotal1 - expected_subtotal1) < 0.01, f"Subtotal mismatch. Expected: {expected_subtotal1}, Got: {subtotal1}"
    assert abs(tax1 - expected_tax1) < 0.01, f"Tax mismatch. Expected: {expected_tax1}, Got: {tax1}"
    assert abs(total1 - expected_total1) < 0.01, f"Total mismatch. Expected: {expected_total1}, Got: {total1}"
    
    print("Test Case 1: PO with vendor and custom tax rate")
    print(f"  Vendor: {vendor1}")
    print(f"  Subtotal: ${subtotal1:.2f}")
    print(f"  Tax (8%): ${tax1:.2f}")
    print(f"  Total: ${total1:.2f}")
    print("  ✓ Passed")
    
    # Test case 2: Default tax rate, no vendor
    result2 = compute_po_cost(
        (100, 5.00),   # 100 units at $5 = $500
        (50, 8.00),    # 50 units at $8 = $400
    )
    
    vendor2, subtotal2, tax2, total2 = result2
    
    expected_subtotal2 = 900.00
    expected_tax2 = 45.00  # 5% default
    expected_total2 = 945.00
    
    assert vendor2 == 'Unknown', f"Vendor should be 'Unknown' when not provided. Got: {vendor2}"
    assert abs(subtotal2 - expected_subtotal2) < 0.01, f"Subtotal mismatch. Expected: {expected_subtotal2}, Got: {subtotal2}"
    assert abs(tax2 - expected_tax2) < 0.01, f"Tax mismatch. Expected: {expected_tax2}, Got: {tax2}"
    assert abs(total2 - expected_total2) < 0.01, f"Total mismatch. Expected: {expected_total2}, Got: {total2}"
    
    print("\nTest Case 2: PO with default tax rate, no vendor")
    print(f"  Vendor: {vendor2}")
    print(f"  Subtotal: ${subtotal2:.2f}")
    print(f"  Tax (5%): ${tax2:.2f}")
    print(f"  Total: ${total2:.2f}")
    print("  ✓ Passed")
    
    # Test case 3: Empty PO
    result3 = compute_po_cost(vendor='Empty Vendor')
    
    vendor3, subtotal3, tax3, total3 = result3
    
    assert vendor3 == 'Empty Vendor', f"Vendor mismatch. Expected: 'Empty Vendor', Got: {vendor3}"
    assert subtotal3 == 0, f"Empty PO subtotal should be 0. Got: {subtotal3}"
    assert tax3 == 0, f"Empty PO tax should be 0. Got: {tax3}"
    assert total3 == 0, f"Empty PO total should be 0. Got: {total3}"
    
    print("\nTest Case 3: Empty PO")
    print(f"  Vendor: {vendor3}")
    print(f"  Subtotal: ${subtotal3:.2f}")
    print(f"  Tax: ${tax3:.2f}")
    print(f"  Total: ${total3:.2f}")
    print("  ✓ Passed")
    
    print("\n" + "="*50)
    print("✅ ALL TESTS PASSED!")
    print("="*50)


if __name__ == "__main__":
    run_tests()
