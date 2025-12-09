"""
Assignment 11: Error Handling and Exception Management

Implement a robust order processing system that handles various types of errors
gracefully. The function should validate orders, process them with proper error
handling, and provide clear error messages and recovery mechanisms.

Instructions:
- Implement the process_orders function with comprehensive error handling
- Handle invalid order formats, missing fields, and invalid data types
- Validate that order_id is a string, items is a list, and total_price is numeric
- Each item must be a dict with 'product' (str) and 'quantity' (int > 0)
- Implement retry logic for recoverable errors (max 3 retries)
- Return a tuple of (successful_orders, failed_orders, summary)
  - successful_orders: list of processed order dicts
  - failed_orders: list of tuples (order_id, error_message)
  - summary: dict with counts of successful, failed, and retry attempts
"""


class InvalidOrderError(Exception):
    """Raised when an order is invalid."""
    pass


class InvalidItemError(Exception):
    """Raised when an order item is invalid."""
    pass


def process_orders(orders, max_retries=3):
    """
    Process a list of orders with comprehensive error handling.
    
    Args:
        orders: List of order dictionaries
        max_retries: Maximum number of retries for each order
    
    Returns:
        Tuple of (successful_orders, failed_orders, summary)
        - successful_orders: List of successfully processed orders
        - failed_orders: List of tuples (order_id, error_message)
        - summary: Dict with 'successful', 'failed', 'total_retries' counts
    
    Raises:
        No exceptions should propagate; all errors are caught and logged.
    
    Error Handling:
        - Catch TypeError for invalid data types
        - Catch ValueError for invalid values (empty items, non-positive quantity)
        - Catch InvalidOrderError and InvalidItemError
        - Implement retry logic with exponential backoff concept
    """
    # TODO: Implement this function
    pass


def validate_order(order):
    """
    Validate a single order structure and content.
    
    Args:
        order: Dictionary with 'order_id', 'items', 'total_price'
    
    Raises:
        InvalidOrderError: If order structure is invalid
        InvalidItemError: If any item in the order is invalid
        TypeError: If data types are incorrect
        ValueError: If values are out of acceptable range
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def run_tests():
    """Run test cases for error handling."""
    
    print("Test 1: Valid orders")
    valid_orders = [
        {
            'order_id': 'ORD001',
            'items': [
                {'product': 'Widget A', 'quantity': 5},
                {'product': 'Widget B', 'quantity': 3}
            ],
            'total_price': 150.00
        },
        {
            'order_id': 'ORD002',
            'items': [
                {'product': 'Gadget X', 'quantity': 2}
            ],
            'total_price': 75.50
        }
    ]
    
    successful, failed, summary = process_orders(valid_orders)
    print(f"  Successful: {len(successful)}, Failed: {len(failed)}")
    print(f"  Summary: {summary}\n")
    
    print("Test 2: Mixed valid and invalid orders")
    mixed_orders = [
        {
            'order_id': 'ORD003',
            'items': [{'product': 'Item A', 'quantity': 2}],
            'total_price': 50.00
        },
        {
            'order_id': 'ORD004',
            'items': [{'product': 'Item B', 'quantity': -1}],  # Invalid: negative quantity
            'total_price': 100.00
        },
        {
            'order_id': 'ORD005',
            'items': [],  # Invalid: empty items
            'total_price': 0.00
        },
        {
            'order_id': 'ORD006',
            'items': [{'product': 'Item C'}],  # Invalid: missing quantity
            'total_price': 75.00
        }
    ]
    
    successful, failed, summary = process_orders(mixed_orders)
    print(f"  Successful: {len(successful)}, Failed: {len(failed)}")
    print(f"  Failed orders: {failed}")
    print(f"  Summary: {summary}\n")
    
    print("Test 3: Invalid order structure")
    invalid_structure = [
        {
            'order_id': 'ORD007',
            'items': 'not a list',  # Invalid: items should be a list
            'total_price': 50.00
        },
        {
            'order_id': 'ORD008',
            # Missing 'items' key
            'total_price': 100.00
        },
        {
            'order_id': 'ORD009',
            'items': [{'product': 'Item D', 'quantity': 5}],
            'total_price': 'not a number'  # Invalid: total_price should be numeric
        }
    ]
    
    successful, failed, summary = process_orders(invalid_structure)
    print(f"  Successful: {len(successful)}, Failed: {len(failed)}")
    print(f"  Summary: {summary}\n")
    
    print("Test 4: Type errors")
    type_errors = [
        None,  # Invalid: not a dict
        {'order_id': 123, 'items': [], 'total_price': 50.00},  # order_id should be string
    ]
    
    successful, failed, summary = process_orders(type_errors)
    print(f"  Successful: {len(successful)}, Failed: {len(failed)}")
    print(f"  Summary: {summary}\n")


if __name__ == '__main__':
    run_tests()
