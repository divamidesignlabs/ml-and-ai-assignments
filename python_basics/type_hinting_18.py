"""
Assignment 18: Type Hinting and Static Type Checking

Implement functions with comprehensive type hints, including generic types,
Union types, Optional types, and custom type aliases. Demonstrate how type
hints improve code clarity and enable static analysis.

Instructions:
- Use type hints for all function parameters and return types
- Use typing module types: List, Dict, Tuple, Union, Optional, Callable, Any
- Create type aliases for complex types
- Validate types at runtime where necessary
- Demonstrate how type hints document expected behavior
"""

from typing import (
    List, Dict, Tuple, Union, Optional, Callable, Any, TypeVar, Generic
)


# Type aliases for improved readability
OrderID = str
SKU = str
Quantity = int
Price = float
CustomerName = str
Email = str
ShipmentStatus = str

# Generic type variable
T = TypeVar('T')


def process_product_inventory(
    inventory: List[Dict[str, Union[str, int, float]]],
    min_stock: int = 10
) -> Tuple[List[Dict[str, Any]], Dict[str, int]]:
    """
    Process product inventory and filter items with low stock.
    
    Args:
        inventory: List of product dictionaries with keys: 'sku', 'name', 'price', 'stock'
        min_stock: Minimum stock level threshold
    
    Returns:
        Tuple of:
        - List of products with stock >= min_stock
        - Summary dict with keys: 'total_products', 'low_stock_count', 'avg_price'
    
    Type Hints:
        - Demonstrates Union types (str, int, float)
        - Demonstrates Tuple return type with specific element types
        - Uses type aliases (SKU, Quantity, Price)
    """
    # TODO: Implement this function
    pass


def find_customer_orders(
    customer_id: str,
    all_orders: Dict[str, List[Tuple[OrderID, Price]]]
) -> Optional[List[Tuple[OrderID, Price]]]:
    """
    Find all orders for a specific customer.
    
    Args:
        customer_id: The customer identifier
        all_orders: Mapping of customer IDs to their orders
    
    Returns:
        List of (order_id, total_price) tuples for the customer, or None if not found
    
    Type Hints:
        - Demonstrates Optional return type (List or None)
        - Demonstrates Dict with complex value type (List of Tuples)
        - Uses OrderID type alias
    """
    # TODO: Implement this function
    pass


def apply_bulk_discount(
    orders: List[Tuple[SKU, Quantity, Price]],
    discount_calculator: Callable[[Price], Price]
) -> List[Tuple[SKU, Quantity, Price]]:
    """
    Apply a discount function to a list of order items.
    
    Args:
        orders: List of (sku, quantity, price) tuples
        discount_calculator: Callable that takes Price and returns discounted Price
    
    Returns:
        List of orders with discounted prices
    
    Type Hints:
        - Demonstrates Callable type parameter
        - Uses custom type aliases (SKU, Quantity, Price)
        - Shows how type hints document expected transformations
    """
    # TODO: Implement this function
    pass


def merge_inventory_sources(
    primary: Dict[SKU, Quantity],
    secondary: Dict[SKU, Quantity],
    merge_strategy: Union[str, Callable[[int, int], int]] = 'add'
) -> Dict[SKU, Quantity]:
    """
    Merge inventory from multiple sources.
    
    Args:
        primary: Primary inventory source (SKU -> Quantity)
        secondary: Secondary inventory source (SKU -> Quantity)
        merge_strategy: Either 'add', 'max', 'min', or a callable that takes two quantities
    
    Returns:
        Merged inventory dictionary
    
    Type Hints:
        - Demonstrates Union of str and Callable
        - Shows how Union types offer flexibility while maintaining type safety
        - Uses custom type aliases
    """
    # TODO: Implement this function
    pass


def validate_shipment_data(
    shipment: Dict[str, Any]
) -> Tuple[bool, List[str]]:
    """
    Validate shipment data structure and content.
    
    Args:
        shipment: Dictionary with shipment information
    
    Returns:
        Tuple of (is_valid, list_of_errors)
        - is_valid: Boolean indicating if shipment is valid
        - list_of_errors: List of error messages for invalid fields
    
    Expected shipment structure:
        {
            'shipment_id': str,
            'customer_name': str,
            'items': List[Dict with 'sku', 'quantity'],
            'total_price': float,
            'status': str (one of 'pending', 'shipped', 'delivered'),
            'metadata': Optional[Dict[str, Any]]
        }
    
    Type Hints:
        - Uses Dict[str, Any] for flexible data structures
        - Returns Tuple with bool and List[str]
    """
    # TODO: Implement this function
    pass


class DataStore(Generic[T]):
    """
    Generic class for storing and retrieving typed data.
    
    Type Hints:
        - Demonstrates Generic type parameter
        - Shows how Generic types ensure type consistency in collections
    
    Usage:
        string_store = DataStore[str]()
        string_store.add("key1", "value1")
        value: str = string_store.get("key1")
    """
    
    def __init__(self):
        """Initialize the data store."""
        # TODO: Implement __init__
        pass
    
    def add(self, key: str, value: T) -> None:
        """
        Add a value to the store.
        
        Args:
            key: Unique key for the value
            value: Value to store (must match generic type T)
        """
        # TODO: Implement add
        pass
    
    def get(self, key: str) -> Optional[T]:
        """
        Retrieve a value from the store.
        
        Args:
            key: Key of the value to retrieve
        
        Returns:
            The stored value or None if not found
        """
        # TODO: Implement get
        pass
    
    def get_all(self) -> Dict[str, T]:
        """
        Get all stored values.
        
        Returns:
            Dictionary of all key-value pairs
        """
        # TODO: Implement get_all
        pass
    
    def remove(self, key: str) -> bool:
        """
        Remove a value from the store.
        
        Args:
            key: Key of the value to remove
        
        Returns:
            True if removed, False if not found
        """
        # TODO: Implement remove
        pass


def batch_process_items(
    items: List[T],
    processor: Callable[[T], T],
    condition: Optional[Callable[[T], bool]] = None
) -> List[T]:
    """
    Process a batch of items with an optional filter condition.
    
    Args:
        items: List of items to process (any type T)
        processor: Function to apply to each item
        condition: Optional predicate to filter which items to process
    
    Returns:
        List of processed items
    
    Type Hints:
        - Demonstrates generic type variable T
        - Shows how type variables work across parameters and return type
        - Demonstrates Optional Callable parameter
    """
    # TODO: Implement this function
    pass


def create_shipment_summary(
    shipments: List[Dict[str, Union[str, int, float, List]]],
    filter_status: Optional[ShipmentStatus] = None
) -> Dict[str, Union[int, float, List[OrderID]]]:
    """
    Create a summary of shipments with optional status filtering.
    
    Args:
        shipments: List of shipment dictionaries
        filter_status: Optional status to filter by (e.g., 'pending', 'delivered')
    
    Returns:
        Summary dict with keys:
        - 'total_shipments': int
        - 'filtered_shipments': int
        - 'total_value': float
        - 'shipment_ids': List[str]
        - 'avg_value': float
    
    Type Hints:
        - Demonstrates complex Union return type
        - Shows Optional parameter usage
        - Demonstrates composition of type hints
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def run_tests():
    """Run test cases for type hinting."""
    
    print("Test 1: Process product inventory")
    inventory = [
        {'sku': 'SKU001', 'name': 'Widget A', 'price': 29.99, 'stock': 50},
        {'sku': 'SKU002', 'name': 'Widget B', 'price': 39.99, 'stock': 5},
        {'sku': 'SKU003', 'name': 'Gadget X', 'price': 99.99, 'stock': 2},
        {'sku': 'SKU004', 'name': 'Gadget Y', 'price': 149.99, 'stock': 15},
    ]
    
    products, summary = process_product_inventory(inventory, min_stock=10)
    print(f"  In-stock products: {len(products)}")
    print(f"  Summary: {summary}\n")
    
    print("Test 2: Find customer orders")
    all_orders = {
        'CUST001': [('ORD001', 100.00), ('ORD002', 250.50)],
        'CUST002': [('ORD003', 75.25)],
    }
    
    orders = find_customer_orders('CUST001', all_orders)
    print(f"  Customer orders: {orders}")
    print(f"  Non-existent customer: {find_customer_orders('CUST999', all_orders)}\n")
    
    print("Test 3: Apply bulk discount")
    orders = [('SKU001', 5, 50.00), ('SKU002', 3, 75.00)]
    discounted = apply_bulk_discount(orders, lambda price: price * 0.9)
    print(f"  Original: {orders}")
    print(f"  After 10% discount: {discounted}\n")
    
    print("Test 4: Merge inventory sources")
    primary = {'SKU001': 100, 'SKU002': 50}
    secondary = {'SKU001': 20, 'SKU003': 80}
    
    merged_add = merge_inventory_sources(primary, secondary, 'add')
    merged_max = merge_inventory_sources(primary, secondary, 'max')
    print(f"  Merged (add): {merged_add}")
    print(f"  Merged (max): {merged_max}\n")
    
    print("Test 5: Validate shipment data")
    valid_shipment = {
        'shipment_id': 'SHIP001',
        'customer_name': 'John Doe',
        'items': [{'sku': 'SKU001', 'quantity': 5}],
        'total_price': 150.00,
        'status': 'pending',
        'metadata': {'notes': 'Fragile'}
    }
    
    is_valid, errors = validate_shipment_data(valid_shipment)
    print(f"  Valid shipment: {is_valid}")
    print(f"  Errors: {errors}\n")
    
    print("Test 6: Invalid shipment")
    invalid_shipment = {
        'shipment_id': 'SHIP002',
        # Missing 'customer_name'
        'items': 'not a list',  # Wrong type
        'total_price': 'invalid',  # Should be float
        'status': 'unknown'  # Invalid status
    }
    
    is_valid, errors = validate_shipment_data(invalid_shipment)
    print(f"  Invalid shipment: {is_valid}")
    print(f"  Errors: {errors}\n")
    
    print("Test 7: Generic DataStore[str]")
    string_store: DataStore[str] = DataStore()
    string_store.add('greeting', 'Hello World')
    string_store.add('farewell', 'Goodbye')
    print(f"  Retrieved greeting: {string_store.get('greeting')}")
    print(f"  All items: {string_store.get_all()}\n")
    
    print("Test 8: Generic DataStore[int]")
    int_store: DataStore[int] = DataStore()
    int_store.add('count', 42)
    int_store.add('answer', 42)
    print(f"  Retrieved count: {int_store.get('count')}")
    print(f"  All items: {int_store.get_all()}\n")
    
    print("Test 9: Batch process items")
    numbers: List[int] = [1, 2, 3, 4, 5]
    doubled = batch_process_items(numbers, lambda x: x * 2)
    print(f"  Original: {numbers}")
    print(f"  Doubled: {doubled}")
    
    # With condition
    doubled_evens = batch_process_items(numbers, lambda x: x * 2, lambda x: x % 2 == 0)
    print(f"  Doubled (evens only): {doubled_evens}\n")
    
    print("Test 10: Create shipment summary")
    shipments = [
        {'id': 'SHIP001', 'status': 'delivered', 'price': 100.00},
        {'id': 'SHIP002', 'status': 'pending', 'price': 75.00},
        {'id': 'SHIP003', 'status': 'delivered', 'price': 200.00},
    ]
    
    summary = create_shipment_summary(shipments)
    print(f"  Summary: {summary}")
    
    summary_filtered = create_shipment_summary(shipments, filter_status='delivered')
    print(f"  Filtered (delivered): {summary_filtered}\n")


if __name__ == '__main__':
    run_tests()
