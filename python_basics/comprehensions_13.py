"""
Assignment 13: Comprehensions and Functional Programming

Implement advanced data transformation functions using list, dictionary, and set
comprehensions, along with lambda functions and higher-order functions like
map, filter, and reduce.

Instructions:
- Use comprehensions instead of loops for data transformation
- Leverage lambda functions for concise operations
- Use functional programming tools: map(), filter(), functools.reduce()
- Implement all functions with type hints
- Keep code concise and Pythonic
"""

from typing import List, Dict, Set, Callable, Any
from functools import reduce


def filter_and_transform_products(products: List[Dict]) -> List[Dict]:
    """
    Filter products by price range and transform the data structure.
    
    Args:
        products: List of dicts with 'name', 'price', 'stock'
    
    Returns:
        List of dicts with only products priced between 10 and 100 (inclusive),
        with keys transformed to 'product_name', 'price_usd', and 'in_stock'
        (boolean indicating stock > 0)
    
    Constraint:
        Use list comprehension with conditional logic
    """
    # TODO: Implement this function
    pass


def create_price_category_map(products: List[Dict]) -> Dict[str, List[str]]:
    """
    Group product names by price category.
    
    Args:
        products: List of dicts with 'name' and 'price'
    
    Returns:
        Dict mapping price categories to product name lists:
        - 'budget': price < 25
        - 'standard': 25 <= price < 75
        - 'premium': price >= 75
    
    Constraint:
        Use dictionary comprehension
    """
    # TODO: Implement this function
    pass


def find_unique_tags(products: List[Dict]) -> Set[str]:
    """
    Extract all unique tags from a list of products.
    
    Args:
        products: List of dicts with optional 'tags' key (list of strings)
    
    Returns:
        Set of all unique tags across all products
    
    Constraint:
        Use set comprehension; handle products without 'tags' key gracefully
    """
    # TODO: Implement this function
    pass


def apply_discount_to_prices(prices: List[float], discount_percent: float) -> List[float]:
    """
    Apply a discount to a list of prices.
    
    Args:
        prices: List of original prices
        discount_percent: Discount percentage (e.g., 10 for 10% off)
    
    Returns:
        List of discounted prices
    
    Constraint:
        Use map() with lambda function
    """
    # TODO: Implement this function
    pass


def filter_high_value_items(items: List[Dict], min_price: float) -> List[str]:
    """
    Filter items above a minimum price and return their names.
    
    Args:
        items: List of dicts with 'name' and 'price'
        min_price: Minimum price threshold
    
    Returns:
        List of item names with price >= min_price
    
    Constraint:
        Use filter() with lambda function
    """
    # TODO: Implement this function
    pass


def calculate_total_inventory_value(products: List[Dict]) -> float:
    """
    Calculate total inventory value (price * stock) for all products.
    
    Args:
        products: List of dicts with 'price' and 'stock' (quantity)
    
    Returns:
        Total value of all products in inventory
    
    Constraint:
        Use functools.reduce() with lambda function
    """
    # TODO: Implement this function
    pass


def nested_comprehension_matrix_transform(matrix: List[List[int]]) -> List[int]:
    """
    Flatten a 2D matrix and filter for even numbers.
    
    Args:
        matrix: 2D list of integers
    
    Returns:
        Flattened list of only even numbers, sorted in ascending order
    
    Constraint:
        Use nested list comprehension with conditional logic
    """
    # TODO: Implement this function
    pass


def create_product_summary(products: List[Dict]) -> Dict[str, Any]:
    """
    Create a summary of products with various statistics.
    
    Args:
        products: List of dicts with 'name', 'price', 'stock'
    
    Returns:
        Dict with:
        - 'names': List of product names (list comprehension)
        - 'prices': Dict mapping name to price (dict comprehension)
        - 'price_range': Tuple of (min_price, max_price)
        - 'total_stock': Total quantity across all products (reduce)
    
    Constraint:
        Use comprehensions and reduce() where applicable
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def run_tests():
    """Run test cases for comprehensions and functional programming."""
    
    print("Test 1: Filter and transform products")
    products = [
        {'name': 'Keyboard', 'price': 45.99, 'stock': 10},
        {'name': 'Mouse', 'price': 15.50, 'stock': 25},
        {'name': 'Monitor', 'price': 250.00, 'stock': 5},  # Out of range
        {'name': 'USB Cable', 'price': 5.99, 'stock': 0},  # Out of range
        {'name': 'Headphones', 'price': 75.00, 'stock': 8},
    ]
    
    filtered = filter_and_transform_products(products)
    print(f"  Filtered products: {len(filtered)}")
    for p in filtered:
        print(f"    {p}\n")
    
    print("Test 2: Create price category map")
    categories = create_price_category_map(products)
    print(f"  Budget: {categories.get('budget', [])}")
    print(f"  Standard: {categories.get('standard', [])}")
    print(f"  Premium: {categories.get('premium', [])}\n")
    
    print("Test 3: Find unique tags")
    products_with_tags = [
        {'name': 'Keyboard', 'price': 45.99, 'tags': ['electronics', 'input']},
        {'name': 'Mouse', 'price': 15.50, 'tags': ['electronics', 'input', 'wireless']},
        {'name': 'Monitor', 'price': 250.00, 'tags': ['electronics', 'display']},
        {'name': 'USB Cable', 'price': 5.99},  # No tags
    ]
    
    tags = find_unique_tags(products_with_tags)
    print(f"  Unique tags: {tags}\n")
    
    print("Test 4: Apply discount to prices")
    prices = [10.00, 20.00, 50.00, 100.00]
    discounted = apply_discount_to_prices(prices, 10)
    print(f"  Original prices: {prices}")
    print(f"  Discounted (10%): {discounted}\n")
    
    print("Test 5: Filter high value items")
    items = [
        {'name': 'Item A', 'price': 45.00},
        {'name': 'Item B', 'price': 15.00},
        {'name': 'Item C', 'price': 75.00},
        {'name': 'Item D', 'price': 5.00},
    ]
    
    high_value = filter_high_value_items(items, 50.00)
    print(f"  High value items (>= 50): {high_value}\n")
    
    print("Test 6: Calculate total inventory value")
    inventory = [
        {'name': 'Item 1', 'price': 10.00, 'stock': 5},
        {'name': 'Item 2', 'price': 20.00, 'stock': 3},
        {'name': 'Item 3', 'price': 15.00, 'stock': 8},
    ]
    
    total_value = calculate_total_inventory_value(inventory)
    print(f"  Total inventory value: ${total_value}\n")
    
    print("Test 7: Nested comprehension matrix transform")
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    evens = nested_comprehension_matrix_transform(matrix)
    print(f"  Original matrix: {matrix}")
    print(f"  Even numbers sorted: {evens}\n")
    
    print("Test 8: Create product summary")
    summary = create_product_summary(products)
    print(f"  Product names: {summary['names']}")
    print(f"  Price range: {summary['price_range']}")
    print(f"  Total stock: {summary['total_stock']}\n")


if __name__ == '__main__':
    run_tests()
