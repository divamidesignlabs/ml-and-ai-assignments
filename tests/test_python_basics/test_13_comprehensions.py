"""
Pytest tests for Assignment 13: Comprehensions and Functional Programming
"""

import pytest
from python_basics.comprehensions_13 import (
    filter_and_transform_products,
    create_price_category_map,
    find_unique_tags,
    apply_discount_to_prices,
    filter_high_value_items,
    calculate_total_inventory_value,
    nested_comprehension_matrix_transform,
    create_product_summary
)


class TestListComprehensions:
    """Test cases for list and filtering comprehensions."""
    
    def test_filter_and_transform_products(self):
        """Test filtering and transforming product data."""
        products = [
            {'name': 'Keyboard', 'price': 45.99, 'stock': 10},
            {'name': 'Mouse', 'price': 15.50, 'stock': 25},
            {'name': 'Monitor', 'price': 250.00, 'stock': 5},
            {'name': 'USB Cable', 'price': 5.99, 'stock': 0},
            {'name': 'Headphones', 'price': 75.00, 'stock': 8},
        ]
        
        result = filter_and_transform_products(products)
        
        # Should filter out Monitor (too expensive) and USB Cable (too cheap)
        assert len(result) == 3
        
        # Check transformation of keys
        for item in result:
            assert 'product_name' in item
            assert 'price_usd' in item
            assert 'in_stock' in item
        
        # Check in_stock boolean
        for item in result:
            assert isinstance(item['in_stock'], bool)
    
    def test_filter_price_boundaries(self):
        """Test that boundary prices (10 and 100) are included."""
        products = [
            {'name': 'Item A', 'price': 10.00, 'stock': 5},
            {'name': 'Item B', 'price': 100.00, 'stock': 5},
            {'name': 'Item C', 'price': 9.99, 'stock': 5},
            {'name': 'Item D', 'price': 100.01, 'stock': 5},
        ]
        
        result = filter_and_transform_products(products)
        
        # Should include items A and B, exclude C and D
        assert len(result) == 2
        names = [item['product_name'] for item in result]
        assert 'Item A' in names
        assert 'Item B' in names
    
    def test_in_stock_boolean(self):
        """Test that in_stock correctly reflects stock > 0."""
        products = [
            {'name': 'In Stock', 'price': 50.00, 'stock': 10},
            {'name': 'Out of Stock', 'price': 50.00, 'stock': 0},
        ]
        
        result = filter_and_transform_products(products)
        
        for item in result:
            if item['product_name'] == 'In Stock':
                assert item['in_stock'] is True
            elif item['product_name'] == 'Out of Stock':
                assert item['in_stock'] is False


class TestDictionaryComprehensions:
    """Test cases for dictionary comprehensions."""
    
    def test_create_price_category_map(self):
        """Test creating price category mapping."""
        products = [
            {'name': 'Item A', 'price': 20.00},
            {'name': 'Item B', 'price': 50.00},
            {'name': 'Item C', 'price': 100.00},
        ]
        
        categories = create_price_category_map(products)
        
        assert 'budget' in categories
        assert 'standard' in categories
        assert 'premium' in categories
        
        assert 'Item A' in categories['budget']
        assert 'Item B' in categories['standard']
        assert 'Item C' in categories['premium']
    
    def test_category_boundaries(self):
        """Test that boundary values are correctly categorized."""
        products = [
            {'name': 'Budget Edge', 'price': 24.99},  # budget
            {'name': 'Standard Start', 'price': 25.00},  # standard
            {'name': 'Standard End', 'price': 74.99},  # standard
            {'name': 'Premium Start', 'price': 75.00},  # premium
        ]
        
        categories = create_price_category_map(products)
        
        assert 'Budget Edge' in categories.get('budget', [])
        assert 'Standard Start' in categories.get('standard', [])
        assert 'Standard End' in categories.get('standard', [])
        assert 'Premium Start' in categories.get('premium', [])


class TestSetComprehensions:
    """Test cases for set comprehensions."""
    
    def test_find_unique_tags(self):
        """Test extracting unique tags from products."""
        products = [
            {'name': 'Item A', 'tags': ['electronics', 'input']},
            {'name': 'Item B', 'tags': ['electronics', 'wireless']},
            {'name': 'Item C', 'tags': ['home', 'electronics']},
            {'name': 'Item D'},  # No tags
        ]
        
        tags = find_unique_tags(products)
        
        assert isinstance(tags, set)
        assert 'electronics' in tags
        assert 'input' in tags
        assert 'wireless' in tags
        assert 'home' in tags
        assert len(tags) == 4
    
    def test_unique_tag_deduplication(self):
        """Test that duplicate tags are removed."""
        products = [
            {'name': 'Item A', 'tags': ['tag1', 'tag2', 'tag1']},
            {'name': 'Item B', 'tags': ['tag1', 'tag3']},
        ]
        
        tags = find_unique_tags(products)
        
        # Should only have 3 unique tags
        assert len(tags) == 3


class TestLambdaAndFunctionalProgramming:
    """Test cases for lambda functions and functional programming."""
    
    def test_apply_discount_to_prices(self):
        """Test applying discount with map and lambda."""
        prices = [100.00, 50.00, 75.00]
        discounted = apply_discount_to_prices(prices, 10)
        
        # 10% discount
        expected = [90.00, 45.00, 67.50]
        assert all(abs(a - b) < 0.01 for a, b in zip(discounted, expected))
    
    def test_filter_high_value_items(self):
        """Test filtering items by price with filter and lambda."""
        items = [
            {'name': 'Item A', 'price': 45.00},
            {'name': 'Item B', 'price': 15.00},
            {'name': 'Item C', 'price': 75.00},
            {'name': 'Item D', 'price': 5.00},
        ]
        
        high_value = filter_high_value_items(items, 50.00)
        
        assert len(high_value) == 1
        assert 'Item C' in high_value
    
    def test_calculate_total_inventory_value(self):
        """Test calculating total value with reduce and lambda."""
        products = [
            {'price': 10.00, 'stock': 5},  # 50
            {'price': 20.00, 'stock': 3},  # 60
            {'price': 15.00, 'stock': 8},  # 120
        ]
        
        total = calculate_total_inventory_value(products)
        
        assert total == 230.00


class TestNestedComprehensions:
    """Test cases for nested comprehensions."""
    
    def test_nested_comprehension_matrix_transform(self):
        """Test flattening and filtering 2D matrix."""
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        
        evens = nested_comprehension_matrix_transform(matrix)
        
        expected = [2, 4, 6, 8]
        assert evens == expected
    
    def test_nested_with_empty_rows(self):
        """Test nested comprehension with empty matrix."""
        matrix = [[], [2, 4], []]
        
        evens = nested_comprehension_matrix_transform(matrix)
        
        assert evens == [2, 4]


class TestComprehensionSummary:
    """Test cases for product summary using multiple comprehensions."""
    
    def test_create_product_summary(self):
        """Test creating comprehensive product summary."""
        products = [
            {'name': 'Item A', 'price': 25.00, 'stock': 10},
            {'name': 'Item B', 'price': 50.00, 'stock': 5},
            {'name': 'Item C', 'price': 15.00, 'stock': 20},
        ]
        
        summary = create_product_summary(products)
        
        assert 'names' in summary
        assert 'prices' in summary
        assert 'price_range' in summary
        assert 'total_stock' in summary
        
        # Check names
        assert len(summary['names']) == 3
        
        # Check price range
        assert summary['price_range'][0] == 15.00
        assert summary['price_range'][1] == 50.00
        
        # Check total stock
        assert summary['total_stock'] == 35
