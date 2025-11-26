"""
Pytest tests for Assignment 3: Stock Reconciliation
"""

import pytest

from python_basics.stock_reconciliation_03 import reconcile_stock


class TestReconcileStock:
    """Test cases for stock reconciliation function."""
    
    def test_matched_inventory(self):
        """Test that matching quantities are classified as matched."""
        system = {'SKU001': 100}
        physical = {'SKU001': 100}
        
        result = reconcile_stock(system, physical)
        
        assert ('SKU001', 0) in result['matched']
        assert len(result['surplus']) == 0
        assert len(result['deficit']) == 0
    
    def test_surplus_inventory(self):
        """Test that excess physical inventory is classified as surplus."""
        system = {'SKU001': 50}
        physical = {'SKU001': 75}
        
        result = reconcile_stock(system, physical)
        
        assert ('SKU001', 25) in result['surplus']
    
    def test_deficit_inventory(self):
        """Test that missing inventory is classified as deficit."""
        system = {'SKU001': 100}
        physical = {'SKU001': 80}
        
        result = reconcile_stock(system, physical)
        
        assert ('SKU001', -20) in result['deficit']
    
    def test_sku_only_in_system(self):
        """Test SKU present only in system (deficit)."""
        system = {'SKU001': 50}
        physical = {}
        
        result = reconcile_stock(system, physical)
        
        assert ('SKU001', -50) in result['deficit']
    
    def test_sku_only_in_physical(self):
        """Test SKU present only in physical (surplus)."""
        system = {}
        physical = {'SKU001': 30}
        
        result = reconcile_stock(system, physical)
        
        assert ('SKU001', 30) in result['surplus']
    
    def test_mixed_reconciliation(self):
        """Test reconciliation with mixed results."""
        system = {
            'SKU001': 100,
            'SKU002': 50,
            'SKU003': 75,
        }
        physical = {
            'SKU001': 100,  # matched
            'SKU002': 45,   # deficit
            'SKU003': 80,   # surplus
        }
        
        result = reconcile_stock(system, physical)
        
        assert ('SKU001', 0) in result['matched']
        assert ('SKU002', -5) in result['deficit']
        assert ('SKU003', 5) in result['surplus']
    
    def test_full_sample_reconciliation(self):
        """Test with full sample from assignment."""
        system_inventory = {
            'SKU001': 100,
            'SKU002': 50,
            'SKU003': 75,
            'SKU004': 30,
            'SKU005': 200,
        }
        
        physical_inventory = {
            'SKU001': 100,
            'SKU002': 45,
            'SKU003': 80,
            'SKU004': 25,
            'SKU006': 15,
        }
        
        result = reconcile_stock(system_inventory, physical_inventory)
        
        # Sort for comparison
        surplus = sorted(result['surplus'], key=lambda x: x[0])
        deficit = sorted(result['deficit'], key=lambda x: x[0])
        matched = sorted(result['matched'], key=lambda x: x[0])
        
        assert surplus == [('SKU003', 5), ('SKU006', 15)]
        assert deficit == [('SKU002', -5), ('SKU004', -5), ('SKU005', -200)]
        assert matched == [('SKU001', 0)]
    
    def test_empty_inventories(self):
        """Test with empty inventories."""
        result = reconcile_stock({}, {})
        
        assert result['surplus'] == []
        assert result['deficit'] == []
        assert result['matched'] == []
    
    def test_result_structure(self):
        """Test that result has correct structure."""
        result = reconcile_stock({'A': 10}, {'A': 10})
        
        assert 'surplus' in result
        assert 'deficit' in result
        assert 'matched' in result
        assert isinstance(result['surplus'], list)
        assert isinstance(result['deficit'], list)
        assert isinstance(result['matched'], list)
