"""
Pytest tests for Assignment 1: Inventory Normalization
"""

import pytest

from python_basics.inventory_normalization_01 import normalize_inventory


class TestNormalizeInventory:
    """Test cases for inventory normalization function."""
    
    def test_basic_normalization(self):
        """Test basic parsing of valid inventory strings."""
        inventory = [
            'SKU001,10,A1',
            'SKU002,25,B2',
            'SKU003,5,C3',
        ]
        
        clean_records, summary = normalize_inventory(inventory)
        
        assert len(clean_records) == 3
        assert ('SKU001', 10, 'A1') in clean_records
        assert ('SKU002', 25, 'B2') in clean_records
        assert ('SKU003', 5, 'C3') in clean_records
    
    def test_invalid_quantity_rejected(self):
        """Test that non-numeric quantities are rejected."""
        inventory = [
            'SKU001,10,A1',
            'SKU002,abc,B2',  # Invalid quantity
        ]
        
        clean_records, summary = normalize_inventory(inventory)
        
        assert len(clean_records) == 1
        assert ('SKU001', 10, 'A1') in clean_records
    
    def test_wrong_number_of_parts_rejected(self):
        """Test that rows with wrong number of parts are rejected."""
        inventory = [
            'SKU001,10,A1',
            'SKU002,25,B2,extra',  # Too many parts
            'SKU003,5',            # Too few parts
        ]
        
        clean_records, summary = normalize_inventory(inventory)
        
        assert len(clean_records) == 1
        assert ('SKU001', 10, 'A1') in clean_records
    
    def test_negative_quantity_accepted(self):
        """Test that negative quantities are accepted (valid integers)."""
        inventory = [
            'SKU001,-5,A1',
        ]
        
        clean_records, summary = normalize_inventory(inventory)
        
        assert len(clean_records) == 1
        assert ('SKU001', -5, 'A1') in clean_records
    
    def test_zero_quantity_accepted(self):
        """Test that zero quantity is accepted."""
        inventory = [
            'SKU001,0,A1',
        ]
        
        clean_records, summary = normalize_inventory(inventory)
        
        assert len(clean_records) == 1
        assert ('SKU001', 0, 'A1') in clean_records
    
    def test_summary_total_skus(self):
        """Test summary contains correct total SKU count."""
        inventory = [
            'SKU001,10,A1',
            'SKU002,25,B2',
            'SKU003,5,C3',
        ]
        
        clean_records, summary = normalize_inventory(inventory)
        
        assert summary['total_skus'] == 3
    
    def test_summary_total_quantity(self):
        """Test summary contains correct total quantity."""
        inventory = [
            'SKU001,10,A1',
            'SKU002,25,B2',
            'SKU003,5,C3',
        ]
        
        clean_records, summary = normalize_inventory(inventory)
        
        assert summary['total_quantity'] == 40
    
    def test_summary_min_max_quantity(self):
        """Test summary contains correct min and max quantities."""
        inventory = [
            'SKU001,10,A1',
            'SKU002,25,B2',
            'SKU003,5,C3',
        ]
        
        clean_records, summary = normalize_inventory(inventory)
        
        assert summary['min_quantity'] == 5
        assert summary['max_quantity'] == 25
    
    def test_full_sample_inventory(self):
        """Test with the full sample inventory from assignment."""
        sample_inventory = [
            'SKU001,10,A1',
            'SKU002,25,B2',
            'SKU003,5,C3',
            'SKU004,abc,D4',      # Invalid quantity
            'SKU005,15,E5,extra', # Invalid number of parts
            'SKU006,20,F6',
            'SKU007,0,G7',
            'SKU008,-5,H8'        # Negative quantity
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
        
        clean_records, summary = normalize_inventory(sample_inventory)
        
        assert clean_records == expected_clean_records
        assert summary == expected_summary
    
    def test_empty_inventory(self):
        """Test with empty inventory list."""
        inventory = []
        
        clean_records, summary = normalize_inventory(inventory)
        
        assert clean_records == []
        assert summary['total_skus'] == 0
        assert summary['total_quantity'] == 0
