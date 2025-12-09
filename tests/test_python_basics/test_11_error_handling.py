"""
Pytest tests for Assignment 11: Error Handling and Exception Management
"""

import pytest
from python_basics.error_handling_11 import process_orders, validate_order, InvalidOrderError, InvalidItemError


class TestOrderValidation:
    """Test cases for order validation."""
    
    def test_valid_order(self):
        """Test validation of a valid order."""
        order = {
            'order_id': 'ORD001',
            'items': [{'product': 'Item A', 'quantity': 5}],
            'total_price': 50.00
        }
        # Should not raise any exception
        validate_order(order)
    
    def test_invalid_order_id_type(self):
        """Test validation rejects non-string order_id."""
        order = {
            'order_id': 123,  # Should be string
            'items': [{'product': 'Item A', 'quantity': 5}],
            'total_price': 50.00
        }
        with pytest.raises(TypeError):
            validate_order(order)
    
    def test_items_not_list(self):
        """Test validation rejects non-list items."""
        order = {
            'order_id': 'ORD001',
            'items': 'not a list',
            'total_price': 50.00
        }
        with pytest.raises(InvalidOrderError):
            validate_order(order)
    
    def test_negative_quantity(self):
        """Test validation rejects negative quantities."""
        order = {
            'order_id': 'ORD001',
            'items': [{'product': 'Item A', 'quantity': -5}],
            'total_price': 50.00
        }
        with pytest.raises(ValueError):
            validate_order(order)
    
    def test_missing_quantity(self):
        """Test validation catches missing quantity field."""
        order = {
            'order_id': 'ORD001',
            'items': [{'product': 'Item A'}],  # Missing quantity
            'total_price': 50.00
        }
        with pytest.raises((KeyError, InvalidItemError)):
            validate_order(order)


class TestProcessOrders:
    """Test cases for order processing with error handling."""
    
    def test_process_valid_orders(self):
        """Test processing valid orders."""
        orders = [
            {
                'order_id': 'ORD001',
                'items': [{'product': 'Item A', 'quantity': 5}],
                'total_price': 50.00
            },
            {
                'order_id': 'ORD002',
                'items': [{'product': 'Item B', 'quantity': 3}],
                'total_price': 30.00
            }
        ]
        
        successful, failed, summary = process_orders(orders)
        
        assert len(successful) == 2
        assert len(failed) == 0
        assert summary['successful'] == 2
        assert summary['failed'] == 0
    
    def test_process_mixed_orders(self):
        """Test processing mix of valid and invalid orders."""
        orders = [
            {
                'order_id': 'ORD001',
                'items': [{'product': 'Item A', 'quantity': 5}],
                'total_price': 50.00
            },
            {
                'order_id': 'ORD002',
                'items': [{'product': 'Item B', 'quantity': -5}],  # Invalid
                'total_price': 50.00
            },
            {
                'order_id': 'ORD003',
                'items': [],  # Invalid: empty
                'total_price': 0.00
            }
        ]
        
        successful, failed, summary = process_orders(orders)
        
        assert len(successful) == 1
        assert len(failed) == 2
        assert summary['successful'] == 1
        assert summary['failed'] == 2
    
    def test_process_invalid_type(self):
        """Test handling of non-dict orders."""
        orders = [None, 'not a dict', 123]
        
        successful, failed, summary = process_orders(orders)
        
        assert len(successful) == 0
        assert len(failed) == 3
    
    def test_retry_logic(self):
        """Test that retry count is tracked."""
        orders = [
            {
                'order_id': 'ORD001',
                'items': [{'product': 'Item A', 'quantity': 5}],
                'total_price': 50.00
            }
        ]
        
        successful, failed, summary = process_orders(orders, max_retries=3)
        
        assert 'total_retries' in summary
        assert summary['total_retries'] >= 0
    
    def test_empty_orders_list(self):
        """Test processing empty orders list."""
        orders = []
        
        successful, failed, summary = process_orders(orders)
        
        assert len(successful) == 0
        assert len(failed) == 0
        assert summary['successful'] == 0
    
    def test_missing_required_fields(self):
        """Test handling of orders with missing required fields."""
        orders = [
            {
                'order_id': 'ORD001',
                # Missing 'items' and 'total_price'
            }
        ]
        
        successful, failed, summary = process_orders(orders)
        
        assert len(successful) == 0
        assert len(failed) == 1
    
    def test_invalid_total_price(self):
        """Test handling of invalid total_price."""
        orders = [
            {
                'order_id': 'ORD001',
                'items': [{'product': 'Item A', 'quantity': 5}],
                'total_price': 'not a number'
            }
        ]
        
        successful, failed, summary = process_orders(orders)
        
        assert len(successful) == 0
        assert len(failed) == 1
