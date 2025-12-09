"""
Assignment 19: Asynchronous Programming with async/await

Implement asynchronous functions for concurrent I/O operations such as
fetching data from multiple sources, processing data streams, and managing
concurrent tasks.

Instructions:
- Use async def to define coroutines
- Use await to wait for async operations
- Use asyncio.gather() for concurrent operations
- Implement timeout handling and error handling in async contexts
- Demonstrate difference between async execution and sequential execution
"""

import asyncio
from typing import List, Dict, Any, Coroutine, Optional, Tuple
import time


async def fetch_data_source(
    source_id: str,
    delay: float = 1.0
) -> Dict[str, Any]:
    """
    Simulate fetching data from an external source with a delay.
    
    Args:
        source_id: Identifier for the data source
        delay: Simulated network delay in seconds
    
    Returns:
        Dictionary with source data
    
    Implementation:
        - Simulate network delay with await asyncio.sleep(delay)
        - Return a dictionary with source_id and data
    """
    # TODO: Implement this coroutine
    pass


async def process_data(
    data: Dict[str, Any],
    delay: float = 0.5
) -> Dict[str, Any]:
    """
    Simulate processing data asynchronously.
    
    Args:
        data: Data to process
        delay: Simulated processing time in seconds
    
    Returns:
        Dictionary with processed data and processing time
    
    Implementation:
        - Await asyncio.sleep(delay) to simulate processing
        - Return processed result with timestamp
    """
    # TODO: Implement this coroutine
    pass


async def fetch_and_process_concurrent(
    sources: List[str]
) -> List[Dict[str, Any]]:
    """
    Fetch data from multiple sources concurrently and process them.
    
    Args:
        sources: List of source identifiers
    
    Returns:
        List of processed results from all sources
    
    Implementation:
        - Create fetch tasks for all sources
        - Use asyncio.gather() to execute concurrently
        - Process each result
        - Return all processed results
    
    Benefits:
        - All sources are fetched concurrently, not sequentially
        - Total time = max(individual times), not sum
    """
    # TODO: Implement this coroutine
    pass


async def fetch_with_timeout(
    source_id: str,
    timeout_seconds: float = 2.0
) -> Optional[Dict[str, Any]]:
    """
    Fetch data with a timeout constraint.
    
    Args:
        source_id: Source identifier
        timeout_seconds: Maximum time to wait
    
    Returns:
        Data if fetch completes within timeout, None otherwise
    
    Implementation:
        - Use asyncio.wait_for() to enforce timeout
        - Catch asyncio.TimeoutError and return None
        - The fetch operation should take longer than typical sources (3 seconds)
    """
    # TODO: Implement this coroutine
    pass


async def parallel_fetch_multiple_timeouts(
    sources: List[Tuple[str, float]]
) -> Dict[str, Optional[Dict[str, Any]]]:
    """
    Fetch from multiple sources with individual timeout constraints.
    
    Args:
        sources: List of (source_id, timeout) tuples
    
    Returns:
        Dictionary mapping source_id to result (or None if timed out)
    
    Implementation:
        - Create fetch_with_timeout tasks for each source
        - Use asyncio.gather() with return_exceptions=True
        - Aggregate results by source_id
    """
    # TODO: Implement this coroutine
    pass


async def retry_async_operation(
    operation: Coroutine,
    max_retries: int = 3,
    delay_between_retries: float = 1.0
) -> Optional[Any]:
    """
    Retry an async operation with exponential backoff.
    
    Args:
        operation: Coroutine to retry
        max_retries: Maximum number of attempts
        delay_between_retries: Delay between retries (increases exponentially)
    
    Returns:
        Result of the operation, or None if all retries fail
    
    Implementation:
        - Attempt the operation up to max_retries times
        - On failure, wait before retrying (exponential backoff)
        - Return the result on success
        - Return None if all attempts fail
    """
    # TODO: Implement this coroutine
    pass


async def stream_data_processor(
    data_stream: List[int],
    process_delay: float = 0.1
) -> List[int]:
    """
    Process items from a data stream asynchronously.
    
    Args:
        data_stream: List of items to process
        process_delay: Time to process each item
    
    Returns:
        List of processed items (doubled)
    
    Implementation:
        - Create async tasks for processing each item
        - Use asyncio.gather() to process concurrently
        - Process items by doubling them
    """
    # TODO: Implement this coroutine
    pass


async def batch_async_operations(
    items: List[str],
    batch_size: int = 3,
    operation_delay: float = 0.5
) -> List[Dict[str, Any]]:
    """
    Execute async operations on items in batches.
    
    Args:
        items: Items to process
        batch_size: Number of concurrent operations per batch
        operation_delay: Time for each operation
    
    Returns:
        List of operation results
    
    Implementation:
        - Split items into batches
        - Process each batch concurrently
        - Wait for batch to complete before starting next batch
        - Return all results in order
    """
    # TODO: Implement this coroutine
    pass


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def run_tests():
    """Run test cases for async programming."""
    
    print("Test 1: Basic async function")
    async def test_basic():
        result = await fetch_data_source('source1', delay=0.5)
        print(f"  Fetched: {result}\n")
    
    asyncio.run(test_basic())
    
    print("Test 2: Concurrent fetching (gather)")
    async def test_concurrent():
        print("  Starting concurrent fetch from 3 sources...")
        start_time = time.time()
        
        results = await fetch_and_process_concurrent(['source1', 'source2', 'source3'])
        
        elapsed = time.time() - start_time
        print(f"  Completed in {elapsed:.2f} seconds")
        print(f"  Number of results: {len(results)}")
        print(f"  Sequential would take ~3+ seconds, concurrent took ~1-2 seconds\n")
    
    asyncio.run(test_concurrent())
    
    print("Test 3: Fetch with timeout (success)")
    async def test_timeout_success():
        result = await fetch_with_timeout('source_fast', timeout_seconds=2.0)
        print(f"  Result: {result}")
        print(f"  Status: {'Success' if result else 'Timeout'}\n")
    
    asyncio.run(test_timeout_success())
    
    print("Test 4: Fetch with timeout (failure)")
    async def test_timeout_failure():
        result = await fetch_with_timeout('source_slow', timeout_seconds=0.5)
        print(f"  Result: {result}")
        print(f"  Status: {'Success' if result else 'Timeout'}\n")
    
    asyncio.run(test_timeout_failure())
    
    print("Test 5: Parallel fetches with mixed timeouts")
    async def test_parallel_timeouts():
        sources = [
            ('source1', 2.0),  # Should succeed
            ('source2', 0.5),  # Should timeout
            ('source3', 2.0),  # Should succeed
        ]
        results = await parallel_fetch_multiple_timeouts(sources)
        print(f"  Results:")
        for source, result in results.items():
            status = 'Success' if result else 'Timeout'
            print(f"    {source}: {status}")
        print()
    
    asyncio.run(test_parallel_timeouts())
    
    print("Test 6: Stream data processor")
    async def test_stream():
        data = [1, 2, 3, 4, 5]
        print(f"  Input: {data}")
        
        start_time = time.time()
        results = await stream_data_processor(data, process_delay=0.1)
        elapsed = time.time() - start_time
        
        print(f"  Output: {results}")
        print(f"  Processed in {elapsed:.2f} seconds (parallel, not {0.5} sequential)\n")
    
    asyncio.run(test_stream())
    
    print("Test 7: Batch async operations")
    async def test_batch():
        items = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6']
        print(f"  Processing {len(items)} items in batches of 3...")
        
        start_time = time.time()
        results = await batch_async_operations(items, batch_size=3, operation_delay=0.3)
        elapsed = time.time() - start_time
        
        print(f"  Results: {len(results)} items processed")
        print(f"  Time: {elapsed:.2f} seconds (batched concurrency)\n")
    
    asyncio.run(test_batch())
    
    print("Test 8: Retry async operation (simulation)")
    async def test_retry():
        print("  Retrying a simulated unreliable operation...")
        
        attempt_count = 0
        async def unreliable_op():
            nonlocal attempt_count
            attempt_count += 1
            if attempt_count < 3:
                raise ValueError("Temporary failure")
            return "Success on attempt 3"
        
        result = await retry_async_operation(unreliable_op(), max_retries=3, delay_between_retries=0.2)
        print(f"  Result: {result}")
        print(f"  Required {attempt_count} attempts\n")
    
    asyncio.run(test_retry())
    
    print("Test 9: Multiple concurrent tasks")
    async def test_multiple():
        print("  Running 5 concurrent fetch operations...")
        
        tasks = [fetch_data_source(f'source{i}', 0.5) for i in range(5)]
        results = await asyncio.gather(*tasks)
        
        print(f"  Completed {len(results)} operations")
        print(f"  All results: {all(r for r in results)}\n")
    
    asyncio.run(test_multiple())


if __name__ == '__main__':
    run_tests()
