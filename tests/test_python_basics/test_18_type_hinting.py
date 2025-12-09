"""
Pytest tests for Assignment 18: Type Hinting and Static Type Checking
"""

import pytest
from typing import List, Dict, Tuple, Optional, Union
from python_basics.type_hinting_18 import (
    process_product_inventory,
    find_customer_orders,
    apply_bulk_discount,
    merge_inventory_sources,
    validate_shipment_data,
    DataStore,
    batch_process_items,
    create_shipment_summary
)


class TestInventoryProcessing:
    """Test cases for product inventory processing."""
    
    def test_process_product_inventory_filters_low_stock(self):
        """Test filtering products with low stock."""
        inventory = [
            {'sku': 'SKU001', 'name': 'Item A', 'price': 29.99, 'stock': 50},
            {'sku': 'SKU002', 'name': 'Item B', 'price': 39.99, 'stock': 5},
            {'sku': 'SKU003', 'name': 'Item C', 'price': 99.99, 'stock': 2},
        ]
        
        products, summary = process_product_inventory(inventory, min_stock=10)
        
        assert len(products) == 1
        assert products[0]['sku'] == 'SKU001'
    
    def test_process_product_inventory_summary(self):
        """Test summary statistics generation."""
        inventory = [
            {'sku': 'SKU001', 'name': 'Item A', 'price': 50.00, 'stock': 20},
            {'sku': 'SKU002', 'name': 'Item B', 'price': 100.00, 'stock': 10},
            {'sku': 'SKU003', 'name': 'Item C', 'price': 75.00, 'stock': 15},
        ]
        
        products, summary = process_product_inventory(inventory, min_stock=5)
        
        assert summary['total_products'] == 3
        assert 'avg_price' in summary
        assert 'low_stock_count' in summary
    
    def test_process_product_inventory_empty(self):
        """Test processing empty inventory."""
        products, summary = process_product_inventory([])
        
        assert len(products) == 0
        assert summary['total_products'] == 0


class TestFindCustomerOrders:
    """Test cases for customer order lookup."""
    
    def test_find_customer_orders_existing(self):
        """Test finding orders for existing customer."""
        all_orders = {
            'CUST001': [('ORD001', 100.00), ('ORD002', 250.50)],
            'CUST002': [('ORD003', 75.25)],
        }
        
        orders = find_customer_orders('CUST001', all_orders)
        
        assert orders is not None
        assert len(orders) == 2
        assert ('ORD001', 100.00) in orders
    
    def test_find_customer_orders_not_found(self):
        """Test finding orders for non-existent customer."""
        all_orders = {
            'CUST001': [('ORD001', 100.00)],
        }
        
        orders = find_customer_orders('CUST999', all_orders)
        
        assert orders is None
    
    def test_find_customer_orders_empty_list(self):
        """Test finding orders for customer with no orders."""
        all_orders = {
            'CUST001': [],
        }
        
        orders = find_customer_orders('CUST001', all_orders)
        
        assert orders == []


class TestApplyBulkDiscount:
    """Test cases for applying bulk discount."""
    
    def test_apply_bulk_discount_percentage(self):
        """Test applying percentage discount."""
        orders = [
            ('SKU001', 5, 50.00),
            ('SKU002', 3, 75.00)
        ]
        
        discounted = apply_bulk_discount(orders, lambda price: price * 0.9)
        
        assert discounted[0][2] == 45.00  # 50 * 0.9
        assert discounted[1][2] == 67.50  # 75 * 0.9
    
    def test_apply_bulk_discount_flat_discount(self):
        """Test applying flat discount."""
        orders = [('SKU001', 1, 100.00)]
        
        discounted = apply_bulk_discount(orders, lambda price: price - 10)
        
        assert discounted[0][2] == 90.00
    
    def test_apply_bulk_discount_preserves_sku_quantity(self):
        """Test that SKU and quantity are preserved."""
        orders = [('SKU001', 5, 50.00)]
        
        discounted = apply_bulk_discount(orders, lambda price: price * 0.5)
        
        assert discounted[0][0] == 'SKU001'
        assert discounted[0][1] == 5


class TestMergeInventorySources:
    """Test cases for merging inventory sources."""
    
    def test_merge_inventory_add_strategy(self):
        """Test merging with add strategy."""
        primary = {'SKU001': 100, 'SKU002': 50}
        secondary = {'SKU001': 20, 'SKU003': 80}
        
        merged = merge_inventory_sources(primary, secondary, 'add')
        
        assert merged['SKU001'] == 120
        assert merged['SKU002'] == 50
        assert merged['SKU003'] == 80
    
    def test_merge_inventory_max_strategy(self):
        """Test merging with max strategy."""
        primary = {'SKU001': 100, 'SKU002': 50}
        secondary = {'SKU001': 150, 'SKU003': 80}
        
        merged = merge_inventory_sources(primary, secondary, 'max')
        
        assert merged['SKU001'] == 150
        assert merged['SKU002'] == 50
        assert merged['SKU003'] == 80
    
    def test_merge_inventory_min_strategy(self):
        """Test merging with min strategy."""
        primary = {'SKU001': 100, 'SKU002': 50}
        secondary = {'SKU001': 20, 'SKU003': 80}
        
        merged = merge_inventory_sources(primary, secondary, 'min')
        
        assert merged['SKU001'] == 20
        assert merged['SKU002'] == 50
        assert merged['SKU003'] == 80
    
    def test_merge_inventory_callable_strategy(self):
        """Test merging with custom callable strategy."""
        primary = {'SKU001': 100}
        secondary = {'SKU001': 50}
        
        # Custom strategy: average
        merged = merge_inventory_sources(primary, secondary, lambda x, y: (x + y) // 2)
        
        assert merged['SKU001'] == 75


class TestValidateShipmentData:
    """Test cases for shipment validation."""
    
    def test_validate_valid_shipment(self):
        """Test validation of valid shipment."""
        shipment = {
            'shipment_id': 'SHIP001',
            'customer_name': 'John Doe',
            'items': [{'sku': 'SKU001', 'quantity': 5}],
            'total_price': 150.00,
            'status': 'pending',
            'metadata': {'notes': 'Fragile'}
        }
        
        is_valid, errors = validate_shipment_data(shipment)
        
        assert is_valid is True
        assert len(errors) == 0
    
    def test_validate_missing_required_fields(self):
        """Test validation with missing required fields."""
        shipment = {
            'shipment_id': 'SHIP001',
            # Missing 'customer_name', 'items', 'total_price', 'status'
        }
        
        is_valid, errors = validate_shipment_data(shipment)
        
        assert is_valid is False
        assert len(errors) > 0
    
    def test_validate_invalid_status(self):
        """Test validation with invalid status."""
        shipment = {
            'shipment_id': 'SHIP001',
            'customer_name': 'John Doe',
            'items': [],
            'total_price': 100.00,
            'status': 'unknown',  # Invalid status
            'metadata': None
        }
        
        is_valid, errors = validate_shipment_data(shipment)
        
        assert is_valid is False
        assert any('status' in error.lower() for error in errors)
    
    def test_validate_invalid_types(self):
        """Test validation with invalid types."""
        shipment = {
            'shipment_id': 'SHIP001',
            'customer_name': 'John Doe',
            'items': 'not a list',  # Should be list
            'total_price': 'not a number',  # Should be float
            'status': 'pending',
            'metadata': None
        }
        
        is_valid, errors = validate_shipment_data(shipment)
        
        assert is_valid is False


class TestDataStore:
    """Test cases for generic DataStore class."""
    
    def test_datastore_add_and_get(self):
        """Test adding and retrieving values."""
        store = DataStore()
        store.add('key1', 'value1')
        
        value = store.get('key1')
        assert value == 'value1'
    
    def test_datastore_get_nonexistent(self):
        """Test getting non-existent key."""
        store = DataStore()
        
        value = store.get('nonexistent')
        assert value is None
    
    def test_datastore_get_all(self):
        """Test retrieving all values."""
        store = DataStore()
        store.add('key1', 'value1')
        store.add('key2', 'value2')
        
        all_values = store.get_all()
        
        assert len(all_values) == 2
        assert all_values['key1'] == 'value1'
        assert all_values['key2'] == 'value2'
    
    def test_datastore_remove(self):
        """Test removing a value."""
        store = DataStore()
        store.add('key1', 'value1')
        
        removed = store.remove('key1')
        
        assert removed is True
        assert store.get('key1') is None
    
    def test_datastore_remove_nonexistent(self):
        """Test removing non-existent key."""
        store = DataStore()
        
        removed = store.remove('nonexistent')
        
        assert removed is False
    
    def test_datastore_with_integers(self):
        """Test DataStore with integer values."""
        store = DataStore()
        store.add('count', 42)
        
        value = store.get('count')
        assert value == 42
        assert isinstance(value, int)


class TestBatchProcessItems:
    """Test cases for batch item processing."""
    
    def test_batch_process_all_items(self):
        """Test processing all items."""
        items = [1, 2, 3, 4, 5]
        
        result = batch_process_items(items, lambda x: x * 2)
        
        assert result == [2, 4, 6, 8, 10]
    
    def test_batch_process_with_condition(self):
        """Test processing with condition filter."""
        items = [1, 2, 3, 4, 5]
        
        result = batch_process_items(items, lambda x: x * 2, lambda x: x % 2 == 0)
        
        # Only even numbers are doubled
        assert result == [4, 8]
    
    def test_batch_process_condition_none(self):
        """Test processing with no condition."""
        items = ['a', 'b', 'c']
        
        result = batch_process_items(items, lambda x: x.upper(), condition=None)
        
        assert result == ['A', 'B', 'C']
    
    def test_batch_process_empty_list(self):
        """Test processing empty list."""
        result = batch_process_items([], lambda x: x * 2)
        
        assert result == []


class TestCreateShipmentSummary:
    """Test cases for shipment summary creation."""
    
    def test_create_summary_basic(self):
        """Test creating basic summary."""
        shipments = [
            {'id': 'SHIP001', 'status': 'delivered', 'price': 100.00},
            {'id': 'SHIP002', 'status': 'pending', 'price': 75.00},
            {'id': 'SHIP003', 'status': 'delivered', 'price': 200.00},
        ]
        
        summary = create_shipment_summary(shipments)
        
        assert summary['total_shipments'] == 3
        assert summary['total_value'] == 375.00
        assert 'avg_value' in summary
    
    def test_create_summary_with_filter(self):
        """Test creating summary with status filter."""
        shipments = [
            {'id': 'SHIP001', 'status': 'delivered', 'price': 100.00},
            {'id': 'SHIP002', 'status': 'pending', 'price': 75.00},
            {'id': 'SHIP003', 'status': 'delivered', 'price': 200.00},
        ]
        
        summary = create_shipment_summary(shipments, filter_status='delivered')
        
        assert summary['filtered_shipments'] == 2
        assert summary['total_value'] == 300.00
    
    def test_create_summary_shipment_ids(self):
        """Test that shipment IDs are included."""
        shipments = [
            {'id': 'SHIP001', 'status': 'pending', 'price': 100.00},
            {'id': 'SHIP002', 'status': 'pending', 'price': 75.00},
        ]
        
        summary = create_shipment_summary(shipments)
        
        assert 'shipment_ids' in summary
        assert 'SHIP001' in summary['shipment_ids']
        assert 'SHIP002' in summary['shipment_ids']
