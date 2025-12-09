"""
Pytest tests for Assignment 15: Iterators and Generators
"""

import pytest
from python_basics.iterators_generators_15 import (
    RangeIterator,
    FileLineIterator,
    fibonacci_generator,
    infinite_counter,
    data_processor,
    chain_generators,
    sliding_window_generator
)
import tempfile
import os


class TestRangeIterator:
    """Test cases for custom RangeIterator class."""
    
    def test_range_iterator_basic(self):
        """Test basic range iteration."""
        result = list(RangeIterator(1, 5))
        assert result == [1, 2, 3, 4]
    
    def test_range_iterator_with_step(self):
        """Test range with custom step."""
        result = list(RangeIterator(0, 10, 2))
        assert result == [0, 2, 4, 6, 8]
    
    def test_range_iterator_negative_step(self):
        """Test range with negative step."""
        result = list(RangeIterator(5, 0, -1))
        assert result == [5, 4, 3, 2, 1]
    
    def test_range_iterator_single_element(self):
        """Test range with single element."""
        result = list(RangeIterator(5, 6))
        assert result == [5]
    
    def test_range_iterator_empty(self):
        """Test range that produces no elements."""
        result = list(RangeIterator(5, 5))
        assert result == []
    
    def test_range_iterator_is_iterable(self):
        """Test that RangeIterator is properly iterable."""
        ri = RangeIterator(1, 3)
        assert iter(ri) is ri
    
    def test_range_iterator_stopiteration(self):
        """Test that StopIteration is raised at end."""
        ri = RangeIterator(1, 2)
        next(ri)
        
        with pytest.raises(StopIteration):
            next(ri)


class TestFileLineIterator:
    """Test cases for FileLineIterator class."""
    
    def test_file_iterator_reads_lines(self):
        """Test reading lines from file."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("Line 1\nLine 2\nLine 3\n")
            temp_file = f.name
        
        try:
            lines = list(FileLineIterator(temp_file))
            assert len(lines) == 3
            assert lines[0] == "Line 1"
            assert lines[2] == "Line 3"
        finally:
            os.unlink(temp_file)
    
    def test_file_iterator_strips_newlines(self):
        """Test that newlines are stripped from lines."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("Text\n")
            temp_file = f.name
        
        try:
            lines = list(FileLineIterator(temp_file))
            assert lines[0] == "Text"
            assert not lines[0].endswith('\n')
        finally:
            os.unlink(temp_file)
    
    def test_file_iterator_empty_file(self):
        """Test reading empty file."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            temp_file = f.name
        
        try:
            lines = list(FileLineIterator(temp_file))
            assert lines == []
        finally:
            os.unlink(temp_file)
    
    def test_file_iterator_is_iterable(self):
        """Test that FileLineIterator is properly iterable."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("Test\n")
            temp_file = f.name
        
        try:
            fli = FileLineIterator(temp_file)
            assert iter(fli) is fli
        finally:
            os.unlink(temp_file)


class TestFibonacciGenerator:
    """Test cases for fibonacci generator."""
    
    def test_fibonacci_basic(self):
        """Test generating Fibonacci numbers."""
        result = list(fibonacci_generator(5))
        assert result == [0, 1, 1, 2, 3]
    
    def test_fibonacci_single(self):
        """Test generating single Fibonacci number."""
        result = list(fibonacci_generator(1))
        assert result == [0]
    
    def test_fibonacci_eight_numbers(self):
        """Test generating 8 Fibonacci numbers."""
        result = list(fibonacci_generator(8))
        assert result == [0, 1, 1, 2, 3, 5, 8, 13]
    
    def test_fibonacci_zero(self):
        """Test generating zero Fibonacci numbers."""
        result = list(fibonacci_generator(0))
        assert result == []
    
    def test_fibonacci_is_generator(self):
        """Test that function returns a generator."""
        gen = fibonacci_generator(5)
        assert hasattr(gen, '__iter__')
        assert hasattr(gen, '__next__')


class TestInfiniteCounter:
    """Test cases for infinite counter generator."""
    
    def test_infinite_counter_basic(self):
        """Test infinite counter from 0."""
        counter = infinite_counter()
        
        values = [next(counter) for _ in range(5)]
        assert values == [0, 1, 2, 3, 4]
    
    def test_infinite_counter_with_start(self):
        """Test infinite counter from custom start."""
        counter = infinite_counter(100)
        
        values = [next(counter) for _ in range(3)]
        assert values == [100, 101, 102]
    
    def test_infinite_counter_negative_start(self):
        """Test infinite counter starting from negative."""
        counter = infinite_counter(-5)
        
        values = [next(counter) for _ in range(3)]
        assert values == [-5, -4, -3]
    
    def test_infinite_counter_large_number(self):
        """Test infinite counter from large number."""
        counter = infinite_counter(1000000)
        
        first = next(counter)
        assert first == 1000000


class TestDataProcessor:
    """Test cases for data processor generator."""
    
    def test_data_processor_basic(self):
        """Test processing data with filter and transform."""
        data = [1, 2, 3, 4, 5]
        result = list(data_processor(data))
        
        # Should filter positive and multiply by 2
        assert result == [2, 4, 6, 8, 10]
    
    def test_data_processor_with_negatives(self):
        """Test that negatives are filtered."""
        data = [-5, 3, -1, 0, 7, -2, 4]
        result = list(data_processor(data))
        
        # Only positive values doubled
        assert result == [6, 14, 8]
    
    def test_data_processor_empty(self):
        """Test processing empty data."""
        result = list(data_processor([]))
        assert result == []
    
    def test_data_processor_all_negative(self):
        """Test processing all negative data."""
        data = [-5, -3, -1]
        result = list(data_processor(data))
        assert result == []


class TestChainGenerators:
    """Test cases for chain generators function."""
    
    def test_chain_two_lists(self):
        """Test chaining two lists."""
        result = list(chain_generators([1, 2], [3, 4]))
        assert result == [1, 2, 3, 4]
    
    def test_chain_three_iterables(self):
        """Test chaining three iterables."""
        result = list(chain_generators([1], (2, 3), [4, 5]))
        assert result == [1, 2, 3, 4, 5]
    
    def test_chain_empty_iterables(self):
        """Test chaining with empty iterables."""
        result = list(chain_generators([], [1, 2], []))
        assert result == [1, 2]
    
    def test_chain_single_iterable(self):
        """Test chaining single iterable."""
        result = list(chain_generators([1, 2, 3]))
        assert result == [1, 2, 3]
    
    def test_chain_no_iterables(self):
        """Test chaining no iterables."""
        result = list(chain_generators())
        assert result == []
    
    def test_chain_with_generator(self):
        """Test chaining with a generator."""
        def gen():
            yield 1
            yield 2
        
        result = list(chain_generators(gen(), [3, 4]))
        assert result == [1, 2, 3, 4]


class TestSlidingWindow:
    """Test cases for sliding window generator."""
    
    def test_sliding_window_basic(self):
        """Test basic sliding window."""
        data = [1, 2, 3, 4, 5]
        result = list(sliding_window_generator(data, 3))
        
        assert result == [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    
    def test_sliding_window_size_2(self):
        """Test sliding window of size 2."""
        data = ['a', 'b', 'c', 'd']
        result = list(sliding_window_generator(data, 2))
        
        assert result == [['a', 'b'], ['b', 'c'], ['c', 'd']]
    
    def test_sliding_window_size_1(self):
        """Test sliding window of size 1."""
        data = [1, 2, 3]
        result = list(sliding_window_generator(data, 1))
        
        assert result == [[1], [2], [3]]
    
    def test_sliding_window_equal_size(self):
        """Test sliding window same size as data."""
        data = [1, 2, 3]
        result = list(sliding_window_generator(data, 3))
        
        assert result == [[1, 2, 3]]
    
    def test_sliding_window_larger_than_data(self):
        """Test sliding window larger than data."""
        data = [1, 2]
        result = list(sliding_window_generator(data, 3))
        
        assert result == []
    
    def test_sliding_window_empty_data(self):
        """Test sliding window on empty data."""
        result = list(sliding_window_generator([], 3))
        assert result == []


class TestGeneratorExpressions:
    """Test cases for generator expressions."""
    
    def test_generator_expression_is_lazy(self):
        """Test that generator expressions are lazy."""
        def count_calls():
            for i in range(5):
                yield i
        
        gen = (x * 2 for x in count_calls())
        
        # Generator is created but not executed
        assert hasattr(gen, '__next__')
        
        # Values computed on demand
        first = next(gen)
        assert first == 0
    
    def test_generator_expression_vs_list(self):
        """Test memory difference between generator and list."""
        gen = (x ** 2 for x in range(1000000))
        lst = [x ** 2 for x in range(1000000)]
        
        # List uses more memory
        import sys
        assert sys.getsizeof(gen) < sys.getsizeof(lst)
