# Quick Reference - Intermediate & Advanced Assignments

## Assignment at a Glance

### Assignment 11: Error Handling & Exceptions
**Key Methods:** `try`, `except`, `else`, `finally`, custom exceptions
**Main Functions:** `process_orders()`, `validate_order()`
**Example Pattern:**
```python
try:
    validate_order(order)
    process_order(order)
except InvalidOrderError as e:
    handle_invalid(e)
except ValueError as e:
    handle_value_error(e)
finally:
    cleanup()
```

### Assignment 12: File I/O & Data Persistence
**Key Methods:** `open()`, `with`, file modes, parsing
**Main Functions:** `parse_log_file()`, `analyze_logs()`, `write_analysis_report()`
**Example Pattern:**
```python
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        process(line)
```

### Assignment 13: Comprehensions & Functional Programming
**Key Methods:** List/dict/set comprehensions, lambda, `map()`, `filter()`, `reduce()`
**Main Functions:** `filter_and_transform_products()`, `apply_discount_to_prices()`
**Example Pattern:**
```python
# List comprehension
result = [x*2 for x in data if x > 0]

# With map/lambda
result = list(map(lambda x: x*2, data))

# With filter/lambda
result = list(filter(lambda x: x > 0, data))
```

### Assignment 14: Decorators
**Key Syntax:** `@decorator`, `functools.wraps`
**Main Decorators:** `@timing_decorator`, `@memoize_decorator`, `@validate_types_decorator`
**Example Pattern:**
```python
@timing_decorator
@logging_decorator
def my_function(x):
    return x * 2
```

### Assignment 15: Iterators & Generators
**Key Methods:** `__iter__`, `__next__`, `yield`
**Main Classes/Functions:** `RangeIterator`, `fibonacci_generator()`, `sliding_window_generator()`
**Example Pattern:**
```python
# Custom iterator
class MyIterator:
    def __iter__(self):
        return self
    def __next__(self):
        if condition:
            return value
        raise StopIteration

# Generator
def my_generator():
    for i in range(10):
        yield i * 2
```

### Assignment 16: Context Managers
**Key Methods:** `__enter__`, `__exit__`, `@contextmanager`
**Main Classes:** `DatabaseConnection`, `TemporaryFile`, `TransactionManager`
**Example Pattern:**
```python
class MyContextManager:
    def __enter__(self):
        setup()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        cleanup()
        return False  # Don't suppress exceptions

# Or with decorator
@contextmanager
def my_context():
    setup()
    try:
        yield resource
    finally:
        cleanup()
```

### Assignment 17: OOP - Inheritance & Polymorphism
**Key Concepts:** Inheritance, `super()`, method overriding, polymorphism
**Main Classes:** `Vehicle`, `Truck`, `Van`, `Drone`, `LogisticsFleet`
**Example Pattern:**
```python
class Base:
    def method(self):
        return "base"

class Derived(Base):
    def method(self):
        base_result = super().method()
        return base_result + " + derived"
```

### Assignment 18: Type Hinting
**Key Syntax:** `-> type`, `:type`, type aliases, generics
**Main Patterns:** `List[T]`, `Dict[K, V]`, `Optional[T]`, `Union[T1, T2]`, `TypeVar`, `Generic[T]`
**Example Pattern:**
```python
from typing import List, Dict, Optional

def process(items: List[int], mapping: Dict[str, int]) -> Optional[int]:
    return mapping.get('key')

class Store(Generic[T]):
    def add(self, key: str, value: T) -> None:
        pass
    def get(self, key: str) -> Optional[T]:
        pass
```

### Assignment 19: Async Programming
**Key Syntax:** `async def`, `await`, `asyncio.gather()`, `asyncio.wait_for()`
**Main Functions:** `fetch_data_source()`, `fetch_and_process_concurrent()`
**Example Pattern:**
```python
import asyncio

async def fetch_data():
    # Simulate I/O
    await asyncio.sleep(1)
    return "data"

async def main():
    # Concurrent execution
    results = await asyncio.gather(
        fetch_data(),
        fetch_data(),
        fetch_data()
    )
    return results

# Run
asyncio.run(main())
```

---

## Common Python Patterns by Assignment

| Pattern | Assignment | Usage |
|---------|-----------|-------|
| Try/Except/Finally | 11 | Error handling |
| Context Manager | 12, 16 | Resource management |
| Comprehension | 13 | Data transformation |
| Lambda | 13 | Anonymous functions |
| Map/Filter/Reduce | 13 | Functional operations |
| Decorator | 14 | Function enhancement |
| Iterator | 15 | Custom iteration |
| Generator | 15 | Lazy evaluation |
| yield | 15 | Produce values |
| __enter__/__exit__ | 16 | Context management |
| Inheritance | 17 | Code reuse |
| super() | 17 | Parent access |
| Type Hints | 18 | Documentation |
| Generic | 18 | Type-safe containers |
| async/await | 19 | Async operations |
| asyncio.gather | 19 | Concurrent tasks |

---

## Testing Commands Cheat Sheet

```bash
# Run all tests
pytest tests/test_python_basics/

# Run specific file
pytest tests/test_python_basics/test_11_error_handling.py

# Run specific class
pytest tests/test_python_basics/test_11_error_handling.py::TestOrderValidation

# Run specific test
pytest tests/test_python_basics/test_11_error_handling.py::TestOrderValidation::test_valid_order

# Verbose output
pytest -v tests/test_python_basics/

# Show print statements
pytest -s tests/test_python_basics/

# Stop on first failure
pytest -x tests/test_python_basics/

# Run with coverage
pytest --cov=python_basics tests/test_python_basics/

# Generate HTML coverage report
pytest --cov=python_basics --cov-report=html tests/test_python_basics/
```

---

## Implementation Checklist

### For Each Assignment:

- [ ] Read the docstring and understand requirements
- [ ] Identify all functions/classes to implement
- [ ] Plan implementation approach
- [ ] Write code (replace `pass` statements)
- [ ] Run tests: `pytest tests/test_python_basics/test_XX_*.py`
- [ ] Fix failing tests
- [ ] Verify all tests pass
- [ ] Review code for style (PEP 8)
- [ ] Add comments if needed
- [ ] Test with the built-in `run_tests()` function

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Ensure `python_basics/` directory is in Python path |
| `pytest not found` | Install: `pip install pytest` |
| Tests timeout | Check for infinite loops, adjust timeouts in test file |
| Import errors | Verify `__init__.py` files exist in directories |
| Type errors in tests | Ensure return types match expectations |

---

## Performance Tips

### Assignment 15: Iterators/Generators
- Use generators for large datasets (memory efficient)
- Generator expressions are faster than list comprehensions for one-time use
- Use `itertools` for complex iteration patterns

### Assignment 19: Async Programming
- Use `asyncio.gather()` for concurrent I/O operations
- Batch operations with controlled concurrency
- Use `asyncio.wait_for()` for timeouts
- Avoid blocking operations in async functions

### Assignment 14: Decorators
- Use `functools.lru_cache` for automatic memoization
- Be aware of decorator overhead for frequently-called functions
- Stack decorators thoughtfully (order matters)

---

## Key Takeaways by Topic

### Error Handling (11)
- Use specific exception types
- Implement retry logic for transient failures
- Always cleanup in `finally` block

### File I/O (12)
- Always use `with` statement for files
- Parse structured data carefully
- Handle encoding issues gracefully

### Comprehensions (13)
- Prefer comprehensions over loops for readability
- Use `map()`, `filter()`, `reduce()` for functional style
- Avoid deeply nested comprehensions

### Decorators (14)
- Use `functools.wraps` to preserve metadata
- Keep decorators simple and focused
- Document decorator behavior clearly

### Generators (15)
- Use for memory-efficient processing
- Leverage `yield` for lazy evaluation
- Understand `StopIteration` exception

### Context Managers (16)
- Use for resource management
- Implement `__exit__` cleanup logic
- Leverage `contextlib` for simple cases

### OOP (17)
- Design class hierarchies carefully
- Use `super()` for parent method calls
- Implement polymorphic interfaces

### Type Hints (18)
- Annotate all public functions
- Use type aliases for clarity
- Leverage generic types for containers

### Async (19)
- Use `await` for I/O-bound operations
- Use `asyncio.gather()` for concurrency
- Handle timeouts and errors properly

---

## Resources & Further Reading

### Standard Library Modules
- `typing` - Type hints
- `contextlib` - Context manager helpers
- `functools` - Function decorators
- `asyncio` - Async operations
- `itertools` - Iterator tools

### PEPs (Python Enhancement Proposals)
- PEP 318 - Decorators for Functions and Methods
- PEP 342 - Coroutines via Enhanced Generators
- PEP 343 - The "with" Statement
- PEP 492 - Coroutines with async and await

### Online References
- Python Official Docs
- Real Python tutorials
- Stack Overflow for specific issues
- GitHub for code examples

---

## Difficulty Progression

| Level | Assignments | Topics |
|-------|-------------|--------|
| Beginner | 1-10 | Basics, control flow, data structures |
| Intermediate | 11-14 | Error handling, file I/O, comprehensions, decorators |
| Advanced | 15-19 | Generators, context managers, OOP, types, async |

---

## Time Estimates

| Assignment | Estimated Time | Prerequisites |
|-----------|-----------------|-----------------|
| 11 | 2-3 hours | Basic Python |
| 12 | 2-3 hours | Assignment 11 |
| 13 | 3-4 hours | Basic Python |
| 14 | 3-4 hours | Assignments 11-13 |
| 15 | 4-5 hours | Assignment 13 |
| 16 | 3-4 hours | Assignments 11-12 |
| 17 | 3-4 hours | Basic OOP |
| 18 | 2-3 hours | Assignment 14 |
| 19 | 4-5 hours | Assignment 15 |

**Total: ~25-35 hours of focused learning**

---

Last Updated: December 8, 2025
