"""
Pytest tests for Assignment 6: BinCollection Sequence Class
"""

import pytest

from python_basics.bin_collection_06 import BinCollection


class TestBinCollection:
    """Test cases for BinCollection class."""
    
    def test_init_with_list(self):
        """Test initialization with a list of bins."""
        bins = BinCollection(['A1', 'A2', 'B1'])
        assert len(bins) == 3
    
    def test_init_empty(self):
        """Test initialization without arguments."""
        bins = BinCollection()
        assert len(bins) == 0
    
    def test_len(self):
        """Test __len__ method."""
        bins = BinCollection(['A1', 'A2', 'B1', 'B2', 'C1'])
        assert len(bins) == 5
    
    def test_getitem_positive_index(self):
        """Test __getitem__ with positive index."""
        bins = BinCollection(['A1', 'A2', 'B1'])
        
        assert bins[0] == 'A1'
        assert bins[1] == 'A2'
        assert bins[2] == 'B1'
    
    def test_getitem_negative_index(self):
        """Test __getitem__ with negative index."""
        bins = BinCollection(['A1', 'A2', 'B1'])
        
        assert bins[-1] == 'B1'
        assert bins[-2] == 'A2'
        assert bins[-3] == 'A1'
    
    def test_getitem_index_error(self):
        """Test __getitem__ raises IndexError for out of bounds."""
        bins = BinCollection(['A1', 'A2'])
        
        with pytest.raises(IndexError):
            _ = bins[10]
    
    def test_setitem(self):
        """Test __setitem__ method."""
        bins = BinCollection(['A1', 'A2', 'B1'])
        
        bins[1] = 'A2-MODIFIED'
        
        assert bins[1] == 'A2-MODIFIED'
        assert len(bins) == 3
    
    def test_setitem_negative_index(self):
        """Test __setitem__ with negative index."""
        bins = BinCollection(['A1', 'A2', 'B1'])
        
        bins[-1] = 'B1-MODIFIED'
        
        assert bins[-1] == 'B1-MODIFIED'
        assert bins[2] == 'B1-MODIFIED'
    
    def test_delitem(self):
        """Test __delitem__ method."""
        bins = BinCollection(['A1', 'A2', 'B1'])
        
        del bins[1]
        
        assert len(bins) == 2
        assert bins[0] == 'A1'
        assert bins[1] == 'B1'
    
    def test_delitem_negative_index(self):
        """Test __delitem__ with negative index."""
        bins = BinCollection(['A1', 'A2', 'B1'])
        
        del bins[-1]
        
        assert len(bins) == 2
        assert bins[-1] == 'A2'
    
    def test_iter(self):
        """Test __iter__ method."""
        bins = BinCollection(['A1', 'A2', 'B1'])
        
        result = list(bins)
        
        assert result == ['A1', 'A2', 'B1']
    
    def test_iter_in_for_loop(self):
        """Test iteration in for loop."""
        bins = BinCollection(['A1', 'A2', 'B1'])
        
        collected = []
        for bin_code in bins:
            collected.append(bin_code)
        
        assert collected == ['A1', 'A2', 'B1']
    
    def test_repr(self):
        """Test __repr__ method returns something meaningful."""
        bins = BinCollection(['A1', 'A2'])
        
        repr_str = repr(bins)
        
        assert repr_str is not None
        assert isinstance(repr_str, str)
    
    def test_sequence_operations_chain(self):
        """Test chaining multiple sequence operations."""
        bins = BinCollection(['A1', 'A2', 'B1', 'B2', 'C1'])
        
        # Modify
        bins[1] = 'A2-MOD'
        assert bins[1] == 'A2-MOD'
        
        # Delete
        del bins[2]  # Remove B1
        assert len(bins) == 4
        
        # Iterate and collect
        result = list(bins)
        assert result == ['A1', 'A2-MOD', 'B2', 'C1']
    
    def test_empty_collection_operations(self):
        """Test operations on empty collection."""
        bins = BinCollection()
        
        assert len(bins) == 0
        assert list(bins) == []
        
        with pytest.raises(IndexError):
            _ = bins[0]
