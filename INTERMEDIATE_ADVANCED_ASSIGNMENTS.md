# New Intermediate and Advanced Python Assignments

This document describes the new assignments (11-19) added to cover intermediate and advanced Python topics beyond the basic assignments.

## Assignment Overview

### Intermediate Topics (Assignments 11-14)

#### **Assignment 11: Error Handling and Exception Management**
- **File**: `python_basics/error_handling_11.py`
- **Test File**: `tests/test_python_basics/test_11_error_handling.py`
- **Topics Covered**:
  - Custom exception classes
  - `try`, `except`, `else`, `finally` blocks
  - Exception handling strategies
  - Retry logic with error recovery
  - Type validation and error messages
  
**Key Concepts**:
- Define custom exceptions (`InvalidOrderError`, `InvalidItemError`)
- Handle multiple exception types
- Implement graceful error recovery
- Validate complex data structures with comprehensive error reporting

**Example Use Cases**:
- Order processing with validation
- Robust API error handling
- Fallback mechanisms in failing operations

---

#### **Assignment 12: File I/O and Data Persistence**
- **File**: `python_basics/file_io_12.py`
- **Test File**: `tests/test_python_basics/test_12_file_io.py`
- **Topics Covered**:
  - File reading and writing operations
  - Context managers (`with` statement)
  - Error handling for file operations
  - Data parsing and transformation
  - Log file analysis
  
**Key Concepts**:
- Use `with` statement for safe file handling
- Parse structured text data
- Handle file not found and encoding errors
- Implement append vs. write modes
- Transform raw data into structured analysis

**Example Use Cases**:
- Log file parsing and analysis
- Data import/export operations
- Configuration file handling
- Report generation

---

#### **Assignment 13: Comprehensions and Functional Programming**
- **File**: `python_basics/comprehensions_13.py`
- **Test File**: `tests/test_python_basics/test_13_comprehensions.py`
- **Topics Covered**:
  - List, dictionary, and set comprehensions
  - Generator expressions
  - Lambda functions
  - Higher-order functions: `map()`, `filter()`, `reduce()`
  - Functional programming patterns
  
**Key Concepts**:
- Replace loops with concise comprehensions
- Use lambda for quick, anonymous functions
- Leverage functional tools for data transformation
- Apply conditional filtering in comprehensions
- Nested comprehensions for complex transformations

**Example Use Cases**:
- Data filtering and transformation
- Price calculations and discounts
- Inventory categorization
- Data aggregation

---

#### **Assignment 14: Decorators and Function Wrapping**
- **File**: `python_basics/decorators_14.py`
- **Topics Covered**:
  - Function decorators with `@decorator` syntax
  - Decorators with and without parameters
  - `functools.wraps` for preserving function metadata
  - Common decorator patterns (timing, logging, caching, validation, retry)
  - Composing multiple decorators
  
**Key Concepts**:
- Understand decorator mechanics and closure
- Apply cross-cutting concerns (logging, timing)
- Implement caching to improve performance
- Validate function arguments
- Build retry mechanisms with exponential backoff
- Compose decorators for combined functionality

**Example Use Cases**:
- Performance monitoring
- Function call logging
- Input validation
- Memoization for expensive operations
- Automatic retry logic for unreliable functions

---

### Advanced Topics (Assignments 15-19)

#### **Assignment 15: Iterators and Generators**
- **File**: `python_basics/iterators_generators_15.py`
- **Topics Covered**:
  - Custom iterator classes (`__iter__`, `__next__`)
  - Generator functions with `yield`
  - Generator expressions
  - Lazy evaluation and memory efficiency
  - Infinite sequences
  - Streaming data processing
  
**Key Concepts**:
- Implement `__iter__()` and `__next__()` for custom iterators
- Use `yield` for simple, memory-efficient generators
- Compare iterators vs. generators
- Generator expressions as lazy alternatives to list comprehensions
- Implement sliding windows and data streams
- Handle `StopIteration` exception

**Example Use Cases**:
- Processing large files line-by-line
- Fibonacci and other mathematical sequences
- Infinite data streams
- Memory-efficient data transformations

---

#### **Assignment 16: Context Managers and Resource Management**
- **File**: `python_basics/context_managers_16.py`
- **Topics Covered**:
  - Context managers with `__enter__` and `__exit__`
  - `contextlib.contextmanager` decorator
  - Resource acquisition and cleanup
  - Exception handling in context managers
  - Transaction management with rollback
  
**Key Concepts**:
- Implement class-based context managers
- Use decorator-based context managers for simpler cases
- Ensure cleanup even when exceptions occur
- Suppress or propagate exceptions in `__exit__`
- Manage nested contexts
- Implement transaction-like semantics

**Example Use Cases**:
- Database connection management
- Temporary file handling
- Lock/semaphore management
- Transaction rollback on errors
- Resource pooling

---

#### **Assignment 17: Object-Oriented Programming - Inheritance and Polymorphism**
- **File**: `python_basics/oop_inheritance_17.py`
- **Test File**: `tests/test_python_basics/test_17_oop_inheritance.py`
- **Topics Covered**:
  - Single and multi-level inheritance
  - Method overriding
  - `super()` function
  - Polymorphic method dispatch
  - Abstract base patterns
  - Type-specific behavior
  
**Key Concepts**:
- Design inheritance hierarchies
- Use `super()` to call parent class methods
- Override methods for specialized behavior
- Polymorphic operations across types
- Implement common interfaces
- DRY principle through inheritance

**Example Use Cases**:
- Vehicle/transportation systems (logistics example)
- Payment processing with multiple methods
- Shape drawing with different rendering
- Animal behavior hierarchies

---

#### **Assignment 18: Type Hinting and Static Type Checking**
- **File**: `python_basics/type_hinting_18.py`
- **Topics Covered**:
  - Function parameter and return type hints
  - Type aliases for readability
  - Generic types: `List`, `Dict`, `Tuple`, `Union`, `Optional`
  - `Callable` for function types
  - Generic classes with `TypeVar`
  - Type validation at runtime
  
**Key Concepts**:
- Annotate function signatures comprehensively
- Use `typing` module for complex types
- Create type aliases for domain-specific types
- Implement generic classes for type safety
- Use `Union` and `Optional` for flexible typing
- Enable IDE autocompletion and static analysis

**Example Use Cases**:
- Improving code documentation
- Enable static type checking with `mypy`
- Better IDE support and refactoring
- Creating reusable generic data structures

---

#### **Assignment 19: Asynchronous Programming with async/await**
- **File**: `python_basics/async_programming_19.py`
- **Topics Covered**:
  - Async functions with `async def`
  - Awaiting coroutines with `await`
  - Concurrent execution with `asyncio.gather()`
  - Timeout handling with `asyncio.wait_for()`
  - Error handling in async contexts
  - Batched async operations
  
**Key Concepts**:
- Understand async vs. threading vs. multiprocessing
- Create coroutines with `async def`
- Execute multiple coroutines concurrently
- Implement timeout constraints
- Retry logic in async functions
- Process data streams asynchronously
- Batch operations for controlled concurrency

**Example Use Cases**:
- Concurrent API requests
- Web scraping with multiple sources
- Streaming data processing
- Responsive user interfaces
- Load balancing with batch processing

---

## How to Use These Assignments

### For Students
1. **Read the docstring**: Each assignment file has comprehensive documentation
2. **Implement the functions**: Replace `pass` statements with your implementation
3. **Test your code**: Run the provided test suite with `pytest`
4. **Understand the concepts**: Review the notebook material and examples

### For Instructors
1. **Check progress**: Use test files to verify student implementations
2. **Adjust difficulty**: Some assignments can be simplified or extended
3. **Provide feedback**: Tests show exactly which requirements aren't met
4. **Connect to real-world**: Each assignment has practical applications

### Running Tests

```bash
# Run all tests
pytest tests/test_python_basics/

# Run specific assignment tests
pytest tests/test_python_basics/test_11_error_handling.py
pytest tests/test_python_basics/test_13_comprehensions.py

# Run with verbose output
pytest -v tests/test_python_basics/test_17_oop_inheritance.py

# Run specific test function
pytest tests/test_python_basics/test_11_error_handling.py::TestOrderValidation::test_valid_order
```

### Running Assignment Code

```bash
# Each assignment has built-in test code
python python_basics/error_handling_11.py
python python_basics/comprehensions_13.py
python python_basics/decorators_14.py
python python_basics/iterators_generators_15.py
```

---

## Progression Path

### For Beginners (Starting Point)
- Assignments 1-10: Basic Python fundamentals
- Start with Assignments 11-12: Error handling and file I/O

### For Intermediate Learners
- Assignments 11-14: Solid intermediate skills
- Focus on comprehensions (13) and decorators (14) for practical coding

### For Advanced Learners
- Assignments 15-19: Deep dives into advanced topics
- Recommended order: Iterators (15) → Context Managers (16) → OOP (17) → Type Hints (18) → Async (19)

---

## Common Patterns Across Assignments

### Error Handling Pattern
```python
try:
    # Attempt operation
    result = operation()
except SpecificError as e:
    # Handle specific error
    handle_error(e)
except Exception as e:
    # Handle generic error
    log_error(e)
finally:
    # Cleanup
    cleanup()
```

### Resource Management Pattern
```python
with resource_manager() as resource:
    use(resource)
    # Automatic cleanup
```

### Functional Transformation Pattern
```python
result = (list(data)
    .filter(condition)
    .map(transform)
    .reduce(aggregate))
```

### Async Concurrency Pattern
```python
async def concurrent_operations():
    tasks = [async_operation(item) for item in items]
    results = await asyncio.gather(*tasks)
    return results
```

---

## Learning Outcomes

After completing all assignments, students will understand:

1. **Error Handling**: Writing robust, production-ready code
2. **File I/O**: Parsing, processing, and persisting data
3. **Functional Programming**: Writing concise, declarative code
4. **Decorators**: Advanced function composition and metaprogramming
5. **Iterators/Generators**: Memory-efficient data processing
6. **Context Managers**: Safe resource management
7. **OOP**: Building scalable, maintainable class hierarchies
8. **Type Hints**: Self-documenting code and static analysis
9. **Async Programming**: High-performance concurrent operations

---

## References

- **Error Handling**: Python Docs on Exceptions
- **File I/O**: Python Docs on `io` module
- **Comprehensions**: PEP 202, 274, 289
- **Decorators**: PEP 318
- **Generators**: PEP 255
- **Context Managers**: PEP 343
- **Type Hints**: PEP 484, 526
- **Async/Await**: PEP 492

---

## Notes

- All assignments follow PEP 8 style guidelines
- Type hints are comprehensive but not enforced at runtime (unless validated)
- Test files use `pytest` framework
- Assignments build on each other but can be completed independently
- Real-world examples are used throughout
