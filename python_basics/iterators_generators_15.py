"""
Assignment 15: Iterators and Generators

Implement iterator classes and generator functions for processing large datasets
efficiently, with support for lazy evaluation and streaming data.

Instructions:
- Implement custom iterator classes with __iter__ and __next__
- Implement generator functions with yield statements
- Use generators for memory-efficient data processing
- Support infinite sequences and lazy computation
- Implement generator expressions for concise iteration
"""

from typing import Iterator, Generator, List, Any


class RangeIterator:
    """
    Custom iterator class that generates numbers in a range.
    Similar to Python's range() but implemented as an iterator class.
    
    Usage:
        for num in RangeIterator(1, 5):
            print(num)  # Outputs: 1, 2, 3, 4
    
    Implementation:
        - Implement __init__, __iter__, and __next__ methods
        - Raise StopIteration when the range is exhausted
    """
    
    def __init__(self, start: int, end: int, step: int = 1):
        """
        Initialize the iterator.
        
        Args:
            start: Starting number (inclusive)
            end: Ending number (exclusive)
            step: Step size between numbers (default: 1)
        """
        # TODO: Implement __init__
        pass
    
    def __iter__(self) -> 'RangeIterator':
        """Return the iterator object itself."""
        # TODO: Implement __iter__
        pass
    
    def __next__(self) -> int:
        """Return the next number in the range."""
        # TODO: Implement __next__
        pass


class FileLineIterator:
    """
    Iterator that reads a file line by line without loading the entire file into memory.
    
    Usage:
        for line in FileLineIterator('data.txt'):
            process(line)
    
    Implementation:
        - Store file handle as instance variable
        - Implement lazy reading: only read one line at a time
        - Properly close the file when iteration ends or object is destroyed
        - Strip newline characters from lines
    """
    
    def __init__(self, file_path: str):
        """
        Initialize the file iterator.
        
        Args:
            file_path: Path to the file to iterate over
        """
        # TODO: Implement __init__
        pass
    
    def __iter__(self) -> 'FileLineIterator':
        """Return the iterator object itself."""
        # TODO: Implement __iter__
        pass
    
    def __next__(self) -> str:
        """Return the next line from the file."""
        # TODO: Implement __next__
        pass
    
    def __del__(self):
        """Ensure file is closed when iterator is destroyed."""
        # TODO: Implement __del__
        pass


def fibonacci_generator(max_count: int) -> Generator[int, None, None]:
    """
    Generator function that yields Fibonacci numbers up to max_count numbers.
    
    Usage:
        for fib in fibonacci_generator(5):
            print(fib)  # Outputs: 0, 1, 1, 2, 3
    
    Args:
        max_count: Maximum number of Fibonacci numbers to generate
    
    Implementation:
        - Use yield to produce values lazily
        - Generate Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ...
        - Stop after generating max_count numbers
    """
    # TODO: Implement this generator
    pass


def infinite_counter(start: int = 0) -> Generator[int, None, None]:
    """
    Generator function that yields an infinite sequence of numbers.
    
    Usage:
        counter = infinite_counter(10)
        for _ in range(5):
            print(next(counter))  # Outputs: 10, 11, 12, 13, 14
    
    Args:
        start: Starting number (default: 0)
    
    Implementation:
        - Yield numbers indefinitely
        - Caller is responsible for limiting iteration
    """
    # TODO: Implement this generator
    pass


def data_processor(data: List[int]) -> Generator[int, None, None]:
    """
    Generator function that processes data with multiple transformations.
    
    Processing pipeline:
        1. Filter: Only keep numbers > 0
        2. Transform: Multiply by 2
        3. Yield: Produce the result
    
    Args:
        data: List of integers to process
    
    Implementation:
        - Use yield for each processed item
        - Apply all transformations before yielding
    """
    # TODO: Implement this generator
    pass


def chain_generators(*iterables) -> Generator[Any, None, None]:
    """
    Generator function that chains multiple iterables together.
    
    Usage:
        result = list(chain_generators([1, 2], [3, 4], [5, 6]))
        # Result: [1, 2, 3, 4, 5, 6]
    
    Args:
        *iterables: Variable number of iterables to chain
    
    Implementation:
        - Yield items from each iterable in sequence
        - Support any iterable type (list, tuple, generator, etc.)
    """
    # TODO: Implement this generator
    pass


def sliding_window_generator(data: List[Any], window_size: int) -> Generator[List[Any], None, None]:
    """
    Generator function that yields sliding windows of data.
    
    Usage:
        data = [1, 2, 3, 4, 5]
        windows = list(sliding_window_generator(data, 3))
        # Result: [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    
    Args:
        data: List of items to create windows from
        window_size: Size of each window
    
    Implementation:
        - Yield windows of size window_size
        - Each window slides by 1 position
        - Stop when there aren't enough items for a complete window
    """
    # TODO: Implement this generator
    pass


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def run_tests():
    """Run test cases for iterators and generators."""
    
    print("Test 1: Custom RangeIterator")
    numbers = list(RangeIterator(1, 6))
    print(f"  RangeIterator(1, 6): {numbers}")
    print(f"  Expected: [1, 2, 3, 4, 5]\n")
    
    print("Test 2: RangeIterator with step")
    numbers = list(RangeIterator(0, 10, 2))
    print(f"  RangeIterator(0, 10, 2): {numbers}")
    print(f"  Expected: [0, 2, 4, 6, 8]\n")
    
    print("Test 3: FileLineIterator")
    # Create a test file
    test_file = '/tmp/test_lines.txt'
    with open(test_file, 'w') as f:
        f.write("Line 1\nLine 2\nLine 3\nLine 4\n")
    
    lines = list(FileLineIterator(test_file))
    print(f"  FileLineIterator read {len(lines)} lines")
    for i, line in enumerate(lines, 1):
        print(f"    Line {i}: {line}")
    print()
    
    print("Test 4: Fibonacci generator")
    fibs = list(fibonacci_generator(8))
    print(f"  First 8 Fibonacci numbers: {fibs}")
    print(f"  Expected: [0, 1, 1, 2, 3, 5, 8, 13]\n")
    
    print("Test 5: Infinite counter (limited to 5 items)")
    counter = infinite_counter(100)
    first_five = [next(counter) for _ in range(5)]
    print(f"  First 5 numbers from infinite_counter(100): {first_five}")
    print(f"  Expected: [100, 101, 102, 103, 104]\n")
    
    print("Test 6: Data processor")
    raw_data = [-5, 3, -1, 0, 7, -2, 4]
    processed = list(data_processor(raw_data))
    print(f"  Input: {raw_data}")
    print(f"  Processed (filter > 0, multiply by 2): {processed}")
    print(f"  Expected: [6, 14, 8]\n")
    
    print("Test 7: Chain generators")
    chained = list(chain_generators([1, 2], [3, 4], [5, 6]))
    print(f"  chain_generators([1,2], [3,4], [5,6]): {chained}")
    print(f"  Expected: [1, 2, 3, 4, 5, 6]\n")
    
    print("Test 8: Sliding window")
    data = [1, 2, 3, 4, 5]
    windows = list(sliding_window_generator(data, 3))
    print(f"  sliding_window_generator({data}, 3): {windows}")
    print(f"  Expected: [[1, 2, 3], [2, 3, 4], [3, 4, 5]]\n")
    
    print("Test 9: Memory efficiency with generator expression")
    # Generator expression (not list comprehension)
    gen = (x ** 2 for x in range(1000000))
    print(f"  Generator object created: {gen}")
    print(f"  First 5 values: {[next(gen) for _ in range(5)]}")
    print(f"  Generator is memory efficient: doesn't create all 1M values upfront\n")


if __name__ == '__main__':
    run_tests()
