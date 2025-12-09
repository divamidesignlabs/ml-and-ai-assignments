"""
Assignment 16: Context Managers and Resource Management

Implement context managers to safely manage resources like files, database
connections, locks, and temporary data. Use both class-based and decorator-based
approaches.

Instructions:
- Implement context managers with __enter__ and __exit__ methods
- Use @contextlib.contextmanager decorator for simpler implementations
- Ensure proper resource cleanup even when exceptions occur
- Implement transaction-like behavior for safe operations
- Support nested context managers
"""

import contextlib
from typing import Any, Callable, Optional
from contextlib import contextmanager


class DatabaseConnection:
    """
    Context manager for managing database connections.
    
    Usage:
        with DatabaseConnection('database.db') as conn:
            conn.execute("SELECT * FROM users")
        # Connection is automatically closed
    
    Implementation:
        - __enter__: Open connection and return self
        - __exit__: Close connection (handle exceptions gracefully)
        - Implement execute() and commit() methods for testing
    """
    
    def __init__(self, db_path: str):
        """
        Initialize database connection context manager.
        
        Args:
            db_path: Path to the database file
        """
        # TODO: Implement __init__
        pass
    
    def __enter__(self) -> 'DatabaseConnection':
        """Open the database connection."""
        # TODO: Implement __enter__
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """
        Close the database connection and handle exceptions.
        
        Args:
            exc_type: Exception type if an exception occurred, else None
            exc_val: Exception value if an exception occurred, else None
            exc_tb: Traceback if an exception occurred, else None
        
        Returns:
            True if the exception should be suppressed, False otherwise
        """
        # TODO: Implement __exit__
        pass
    
    def execute(self, query: str) -> str:
        """Execute a query and return a result."""
        # TODO: Implement execute (can return a mock result)
        pass
    
    def commit(self) -> None:
        """Commit changes to the database."""
        # TODO: Implement commit
        pass


class TemporaryFile:
    """
    Context manager for managing temporary files.
    
    Usage:
        with TemporaryFile() as f:
            f.write("temporary data")
        # File is automatically deleted when exiting the context
    
    Implementation:
        - __enter__: Create a temporary file and return file object
        - __exit__: Close and delete the temporary file
        - Support read() and write() operations
    """
    
    def __init__(self, mode: str = 'w+'):
        """
        Initialize temporary file context manager.
        
        Args:
            mode: File mode (e.g., 'w+', 'r+')
        """
        # TODO: Implement __init__
        pass
    
    def __enter__(self):
        """Create and open the temporary file."""
        # TODO: Implement __enter__
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Close and delete the temporary file."""
        # TODO: Implement __exit__
        pass
    
    def write(self, data: str) -> None:
        """Write data to the temporary file."""
        # TODO: Implement write
        pass
    
    def read(self) -> str:
        """Read data from the temporary file."""
        # TODO: Implement read
        pass


class TransactionManager:
    """
    Context manager for handling transactions with rollback capability.
    
    Usage:
        with TransactionManager() as txn:
            txn.add_operation(operation1)
            txn.add_operation(operation2)
        # Operations are committed; if exception, all are rolled back
    
    Implementation:
        - __enter__: Initialize transaction state
        - __exit__: Commit if successful, rollback if exception
        - Implement add_operation() to queue operations
        - Implement commit() and rollback() methods
    """
    
    def __init__(self):
        """Initialize transaction manager."""
        # TODO: Implement __init__
        pass
    
    def __enter__(self) -> 'TransactionManager':
        """Start a transaction."""
        # TODO: Implement __enter__
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """
        Commit or rollback the transaction based on exceptions.
        
        Returns:
            False to allow exceptions to propagate
        """
        # TODO: Implement __exit__
        pass
    
    def add_operation(self, operation: Callable) -> None:
        """Add an operation to the transaction."""
        # TODO: Implement add_operation
        pass
    
    def commit(self) -> None:
        """Execute all operations in the transaction."""
        # TODO: Implement commit
        pass
    
    def rollback(self) -> None:
        """Rollback all operations in the transaction."""
        # TODO: Implement rollback
        pass


@contextmanager
def timer_context(name: str = "Operation"):
    """
    Context manager using @contextmanager decorator for timing code blocks.
    
    Usage:
        with timer_context("Data processing"):
            process_large_dataset()
        # Prints: "Data processing took X.XX seconds"
    
    Args:
        name: Name of the operation being timed
    
    Implementation:
        - Yield to allow the with block to execute
        - Measure time before and after yield
        - Print elapsed time on exit
    """
    # TODO: Implement this context manager
    pass


@contextmanager
def error_handler(error_message: str = "An error occurred"):
    """
    Context manager for graceful error handling.
    
    Usage:
        with error_handler("Processing failed"):
            risky_operation()
        # Catches exceptions and logs the error message
    
    Args:
        error_message: Message to display on error
    
    Implementation:
        - Catch any exceptions in the with block
        - Print the error message and exception details
        - Do not re-raise the exception (suppress it)
    """
    # TODO: Implement this context manager
    pass


@contextmanager
def resource_pool(resources: list):
    """
    Context manager for managing a pool of resources.
    
    Usage:
        connections = [conn1, conn2, conn3]
        with resource_pool(connections) as pool:
            resource = pool.acquire()
            use(resource)
            pool.release(resource)
        # All resources are cleaned up on exit
    
    Args:
        resources: List of resources to manage
    
    Implementation:
        - Yield a resource manager object
        - Track acquired and released resources
        - Ensure all resources are released on exit
    """
    # TODO: Implement this context manager
    pass


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

class ResourceManager:
    """Helper class for managing a pool of resources."""
    
    def __init__(self, resources):
        self.resources = resources.copy()
        self.available = resources.copy()
        self.acquired = []
    
    def acquire(self):
        if self.available:
            resource = self.available.pop(0)
            self.acquired.append(resource)
            return resource
        return None
    
    def release(self, resource):
        if resource in self.acquired:
            self.acquired.remove(resource)
            self.available.append(resource)


def run_tests():
    """Run test cases for context managers."""
    
    print("Test 1: DatabaseConnection context manager")
    try:
        with DatabaseConnection(':memory:') as conn:
            conn.execute("SELECT * FROM users")
            conn.commit()
            print("  Database connection opened and closed successfully\n")
    except Exception as e:
        print(f"  Error: {e}\n")
    
    print("Test 2: TemporaryFile context manager")
    try:
        with TemporaryFile('w+') as tf:
            tf.write("This is temporary data")
            content = tf.read()
            print(f"  Wrote and read: {content}")
            print("  Temporary file deleted on exit\n")
    except Exception as e:
        print(f"  Error: {e}\n")
    
    print("Test 3: TransactionManager - successful commit")
    try:
        results = []
        
        def operation1():
            results.append("Operation 1 executed")
        
        def operation2():
            results.append("Operation 2 executed")
        
        with TransactionManager() as txn:
            txn.add_operation(operation1)
            txn.add_operation(operation2)
        
        print(f"  Transaction committed: {results}\n")
    except Exception as e:
        print(f"  Error: {e}\n")
    
    print("Test 4: TransactionManager - rollback on exception")
    try:
        results = []
        
        def op1():
            results.append("Operation 1")
        
        def op_error():
            raise ValueError("Operation failed")
        
        try:
            with TransactionManager() as txn:
                txn.add_operation(op1)
                txn.add_operation(op_error)
        except ValueError as e:
            print(f"  Exception caught: {e}")
            print(f"  Results (should be empty due to rollback): {results}\n")
    except Exception as e:
        print(f"  Error: {e}\n")
    
    print("Test 5: timer_context decorator")
    try:
        import time
        with timer_context("Sleep operation"):
            time.sleep(0.2)
        print()
    except Exception as e:
        print(f"  Error: {e}\n")
    
    print("Test 6: error_handler decorator")
    try:
        with error_handler("Processing failed"):
            x = 1 / 0  # This will raise ZeroDivisionError
            print("  This line should not execute")
        print("  Error was handled gracefully\n")
    except Exception as e:
        print(f"  Error: {e}\n")
    
    print("Test 7: resource_pool context manager")
    try:
        resources = ["Resource1", "Resource2", "Resource3"]
        with resource_pool(resources) as pool:
            r1 = pool.acquire()
            r2 = pool.acquire()
            print(f"  Acquired resources: {r1}, {r2}")
            pool.release(r1)
            print(f"  Released {r1}")
        print("  All resources cleaned up on exit\n")
    except Exception as e:
        print(f"  Error: {e}\n")


if __name__ == '__main__':
    run_tests()
