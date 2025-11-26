"""
Pytest tests for Assignment 9: Warehouse Allocation Simulator
"""

import pytest

from python_basics.warehouse_allocation_09 import allocate_to_bins


class TestAllocateToBins:
    """Test cases for warehouse allocation simulator."""
    
    def test_basic_allocation(self):
        """Test basic allocation to single bin."""
        bin_capacities = {'BIN-A': 100}
        items = [('SKU001', 30)]
        
        allocations, unplaced = allocate_to_bins(bin_capacities, items)
        
        assert ('SKU001', 30) in allocations['BIN-A']
        assert len(unplaced) == 0
    
    def test_multiple_items_single_bin(self):
        """Test multiple items fitting in single bin."""
        bin_capacities = {'BIN-A': 100}
        items = [('SKU001', 30), ('SKU002', 40), ('SKU003', 25)]
        
        allocations, unplaced = allocate_to_bins(bin_capacities, items)
        
        assert len(allocations['BIN-A']) == 3
        assert len(unplaced) == 0
    
    def test_item_too_large(self):
        """Test item that doesn't fit anywhere."""
        bin_capacities = {'BIN-A': 50}
        items = [('SKU001', 100)]
        
        allocations, unplaced = allocate_to_bins(bin_capacities, items)
        
        assert ('SKU001', 100) in unplaced
    
    def test_first_fit_allocation(self):
        """Test that items go to first available bin."""
        bin_capacities = {
            'BIN-A': 100,
            'BIN-B': 100,
        }
        items = [('SKU001', 50), ('SKU002', 50)]
        
        allocations, unplaced = allocate_to_bins(bin_capacities, items)
        
        # Both should fit in BIN-A (first bin)
        assert len(allocations['BIN-A']) == 2
    
    def test_overflow_to_next_bin(self):
        """Test overflow to next bin when first is full."""
        bin_capacities = {
            'BIN-A': 50,
            'BIN-B': 100,
        }
        items = [('SKU001', 50), ('SKU002', 50)]
        
        allocations, unplaced = allocate_to_bins(bin_capacities, items)
        
        # First goes to BIN-A, second to BIN-B
        assert ('SKU001', 50) in allocations['BIN-A']
        assert ('SKU002', 50) in allocations['BIN-B']
    
    def test_remaining_capacity_tracking(self):
        """Test that remaining capacity is tracked correctly."""
        bin_capacities = {'BIN-A': 100}
        items = [
            ('SKU001', 60),  # 40 remaining
            ('SKU002', 50),  # Won't fit
        ]
        
        allocations, unplaced = allocate_to_bins(bin_capacities, items)
        
        assert ('SKU001', 60) in allocations['BIN-A']
        assert ('SKU002', 50) in unplaced
    
    def test_empty_bins(self):
        """Test with empty bins dict."""
        allocations, unplaced = allocate_to_bins({}, [('SKU001', 10)])
        
        assert len(unplaced) == 1
        assert ('SKU001', 10) in unplaced
    
    def test_empty_items(self):
        """Test with empty items list."""
        bin_capacities = {'BIN-A': 100}
        
        allocations, unplaced = allocate_to_bins(bin_capacities, [])
        
        assert len(unplaced) == 0
    
    def test_full_sample_from_assignment(self):
        """Test with full sample from assignment."""
        bin_capacities = {
            'BIN-A': 100,
            'BIN-B': 50,
            'BIN-C': 75,
        }
        
        items = [
            ('SKU001', 30),
            ('SKU002', 40),
            ('SKU003', 50),
            ('SKU004', 35),
            ('SKU005', 25),
            ('SKU006', 60),
            ('SKU007', 40),
        ]
        
        allocations, unplaced = allocate_to_bins(bin_capacities, items)
        
        # Verify unplaced
        unplaced_skus = [sku for sku, _ in unplaced]
        assert 'SKU006' in unplaced_skus
        
        # Verify BIN-A allocations
        bin_a_skus = [sku for sku, _ in allocations.get('BIN-A', [])]
        assert 'SKU001' in bin_a_skus
        assert 'SKU002' in bin_a_skus
        assert 'SKU005' in bin_a_skus
        
        # Verify BIN-B allocations
        bin_b_skus = [sku for sku, _ in allocations.get('BIN-B', [])]
        assert 'SKU003' in bin_b_skus
        
        # Verify BIN-C allocations
        bin_c_skus = [sku for sku, _ in allocations.get('BIN-C', [])]
        assert 'SKU004' in bin_c_skus
        assert 'SKU007' in bin_c_skus
    
    def test_exact_fit(self):
        """Test item that exactly fits remaining capacity."""
        bin_capacities = {'BIN-A': 100}
        items = [('SKU001', 50), ('SKU002', 50)]  # Exactly fills bin
        
        allocations, unplaced = allocate_to_bins(bin_capacities, items)
        
        assert len(allocations['BIN-A']) == 2
        assert len(unplaced) == 0
    
    def test_result_structure(self):
        """Test return value structure."""
        bin_capacities = {'BIN-A': 100}
        items = [('SKU001', 50)]
        
        result = allocate_to_bins(bin_capacities, items)
        
        assert isinstance(result, tuple)
        assert len(result) == 2
        
        allocations, unplaced = result
        assert isinstance(allocations, dict)
        assert isinstance(unplaced, list)
