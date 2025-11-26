"""
Assignment 1: Inventory Normalization

Parse a list of "sku,qty,loc" strings. Convert qty to int, reject invalid rows,
and return (clean_records, summary) where summary includes total SKUs, total qty,
min qty, and max qty.

Instructions:
- Implement the normalize_inventory function below
- Each input string should be split by comma
- Valid records have exactly 3 parts: sku, qty, loc
- qty must be convertible to an integer
- Return a tuple of (clean_records, summary)
  - clean_records: list of tuples (sku, qty_as_int, loc)
  - summary: dict with keys 'total_skus', 'total_quantity', 'min_quantity', 'max_quantity'
"""


def normalize_inventory(inventory_list):
    """
    Parse and normalize inventory records.
    
    Args:
        inventory_list: List of strings in format "sku,qty,loc"
    
    Returns:
        Tuple of (clean_records, summary)
        - clean_records: List of tuples (sku, qty, loc) with qty as int
        - summary: Dict with total_skus, total_quantity, min_quantity, max_quantity
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def run_tests():
    """Run test cases for inventory normalization."""
    
    sample_inventory = [
        'SKU001,10,A1',
        'SKU002,25,B2',
        'SKU003,5,C3',
        'SKU004,abc,D4',      # Invalid quantity
        'SKU005,15,E5,extra', # Invalid number of parts
        'SKU006,20,F6',
        'SKU007,0,G7',
        'SKU008,-5,H8'        # Negative quantity, but still an integer
    ]
    
    expected_clean_records = [
        ('SKU001', 10, 'A1'),
        ('SKU002', 25, 'B2'),
        ('SKU003', 5, 'C3'),
        ('SKU006', 20, 'F6'),
        ('SKU007', 0, 'G7'),
        ('SKU008', -5, 'H8')
    ]
    
    expected_summary = {
        'total_skus': 6,
        'total_quantity': 55,
        'min_quantity': -5,
        'max_quantity': 25
    }
    
    result = normalize_inventory(sample_inventory)
    
    # Check if function is implemented
    assert result is not None, "Function not implemented - returns None"
    
    clean_records, inventory_summary = result
    
    # Test clean records
    assert clean_records == expected_clean_records, \
        f"Clean records mismatch.\nExpected: {expected_clean_records}\nGot: {clean_records}"
    
    # Test summary
    assert inventory_summary == expected_summary, \
        f"Summary mismatch.\nExpected: {expected_summary}\nGot: {inventory_summary}"
    
    print("Clean Records:")
    for record in clean_records:
        print(record)
    
    print("\nInventory Summary:")
    print(inventory_summary)
    
    print("\n" + "="*50)
    print("✅ ALL TESTS PASSED!")
    print("="*50)


if __name__ == "__main__":
    run_tests()
