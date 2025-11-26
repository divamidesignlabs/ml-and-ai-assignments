"""
Pytest tests for Assignment 4: Purchase Order Costing
"""

import pytest

from python_basics.purchase_order_costing_04 import compute_po_cost


class TestComputePOCost:
    """Test cases for purchase order costing function."""
    
    def test_basic_po_calculation(self):
        """Test basic PO calculation with multiple line items."""
        result = compute_po_cost(
            (10, 25.00),
            (5, 50.00),
            tax_rate=0.05,
            vendor='Test Vendor'
        )
        
        vendor, subtotal, tax, total = result
        
        assert vendor == 'Test Vendor'
        assert abs(subtotal - 500.00) < 0.01
        assert abs(tax - 25.00) < 0.01
        assert abs(total - 525.00) < 0.01
    
    def test_custom_tax_rate(self):
        """Test with custom tax rate."""
        result = compute_po_cost(
            (10, 100.00),
            tax_rate=0.10,
            vendor='Vendor'
        )
        
        vendor, subtotal, tax, total = result
        
        assert abs(tax - 100.00) < 0.01  # 10% of 1000
        assert abs(total - 1100.00) < 0.01
    
    def test_default_tax_rate(self):
        """Test default tax rate of 5%."""
        result = compute_po_cost(
            (100, 10.00),
            vendor='Vendor'
        )
        
        vendor, subtotal, tax, total = result
        
        assert abs(subtotal - 1000.00) < 0.01
        assert abs(tax - 50.00) < 0.01  # 5% default
        assert abs(total - 1050.00) < 0.01
    
    def test_default_vendor(self):
        """Test default vendor when not provided."""
        result = compute_po_cost(
            (10, 10.00),
        )
        
        vendor, subtotal, tax, total = result
        
        assert vendor == 'Unknown'
    
    def test_empty_po(self):
        """Test PO with no line items."""
        result = compute_po_cost(vendor='Empty Vendor')
        
        vendor, subtotal, tax, total = result
        
        assert vendor == 'Empty Vendor'
        assert subtotal == 0
        assert tax == 0
        assert total == 0
    
    def test_single_line_item(self):
        """Test PO with single line item."""
        result = compute_po_cost(
            (5, 20.00),
            tax_rate=0.08,
            vendor='Single Item Vendor'
        )
        
        vendor, subtotal, tax, total = result
        
        assert vendor == 'Single Item Vendor'
        assert abs(subtotal - 100.00) < 0.01
        assert abs(tax - 8.00) < 0.01
        assert abs(total - 108.00) < 0.01
    
    def test_full_sample_po(self):
        """Test with full sample from assignment."""
        result = compute_po_cost(
            (10, 25.00),
            (5, 50.00),
            (20, 10.00),
            tax_rate=0.08,
            vendor='Acme Supplies',
            po_number='PO-2024-001'
        )
        
        vendor, subtotal, tax, total = result
        
        assert vendor == 'Acme Supplies'
        assert abs(subtotal - 700.00) < 0.01
        assert abs(tax - 56.00) < 0.01
        assert abs(total - 756.00) < 0.01
    
    def test_zero_tax_rate(self):
        """Test with zero tax rate."""
        result = compute_po_cost(
            (10, 10.00),
            tax_rate=0.0,
            vendor='No Tax Vendor'
        )
        
        vendor, subtotal, tax, total = result
        
        assert abs(tax) < 0.01
        assert abs(subtotal - total) < 0.01
    
    def test_metadata_ignored_except_vendor(self):
        """Test that extra metadata doesn't affect calculation."""
        result = compute_po_cost(
            (10, 10.00),
            vendor='Meta Vendor',
            po_number='PO-001',
            department='Warehouse',
            priority='High'
        )
        
        vendor, subtotal, tax, total = result
        
        assert vendor == 'Meta Vendor'
        assert abs(subtotal - 100.00) < 0.01
