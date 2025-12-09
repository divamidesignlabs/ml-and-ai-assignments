"""
Pytest tests for Assignment 14: Decorators and Function Wrapping
"""

import pytest
import time
from python_basics.decorators_14 import (
    timing_decorator,
    logging_decorator,
    memoize_decorator,
    validate_types_decorator,
    retry_decorator,
    count_calls_decorator,
)


class TestTimingDecorator:
    """Test cases for timing decorator."""
    
    def test_timing_decorator_preserves_function_name(self):
        """Test that decorator preserves function metadata."""
        @timing_decorator
        def sample_function():
            return "result"
        
        assert sample_function.__name__ == "sample_function"
    
    def test_timing_decorator_returns_correct_result(self):
        """Test that decorated function returns correct value."""
        @timing_decorator
        def add(a, b):
            return a + b
        
        result = add(5, 3)
        assert result == 8
    
    def test_timing_decorator_handles_args_kwargs(self):
        """Test that decorator handles various function signatures."""
        @timing_decorator
        def function_with_kwargs(a, b=10):
            return a + b
        
        result = function_with_kwargs(5, b=20)
        assert result == 25


class TestLoggingDecorator:
    """Test cases for logging decorator."""
    
    def test_logging_decorator_preserves_function_name(self):
        """Test that decorator preserves function metadata."""
        @logging_decorator
        def sample_function():
            return "result"
        
        assert sample_function.__name__ == "sample_function"
    
    def test_logging_decorator_returns_correct_result(self):
        """Test that decorated function returns correct value."""
        @logging_decorator
        def multiply(a, b):
            return a * b
        
        result = multiply(3, 4)
        assert result == 12
    
    def test_logging_decorator_handles_exceptions(self):
        """Test that decorator handles exceptions properly."""
        @logging_decorator
        def failing_function():
            raise ValueError("Test error")
        
        with pytest.raises(ValueError):
            failing_function()


class TestMemoizeDecorator:
    """Test cases for memoization decorator."""
    
    def test_memoize_returns_correct_value(self):
        """Test that memoized function returns correct value."""
        call_count = 0
        
        @memoize_decorator
        def expensive_function(n):
            nonlocal call_count
            call_count += 1
            return n * 2
        
        result = expensive_function(5)
        assert result == 10
    
    def test_memoize_caches_results(self):
        """Test that decorator caches function results."""
        call_count = 0
        
        @memoize_decorator
        def slow_function(n):
            nonlocal call_count
            call_count += 1
            return n ** 2
        
        # First call
        result1 = slow_function(5)
        count_after_first = call_count
        
        # Second call with same argument (should use cache)
        result2 = slow_function(5)
        count_after_second = call_count
        
        assert result1 == result2 == 25
        assert count_after_second == count_after_first  # No additional call
    
    def test_memoize_distinguishes_arguments(self):
        """Test that cache distinguishes between different arguments."""
        call_count = 0
        
        @memoize_decorator
        def square(n):
            nonlocal call_count
            call_count += 1
            return n ** 2
        
        square(3)
        square(5)
        square(3)  # Should use cache
        
        # Only 2 calls made (not 3)
        assert call_count == 2
    
    def test_memoize_has_cache_attribute(self):
        """Test that cache is accessible."""
        @memoize_decorator
        def simple_function(x):
            return x + 1
        
        simple_function(5)
        assert hasattr(simple_function, 'cache')
        assert isinstance(simple_function.cache, dict)


class TestValidateTypesDecorator:
    """Test cases for type validation decorator."""
    
    def test_validate_types_accepts_correct_types(self):
        """Test that decorator accepts correct types."""
        @validate_types_decorator(name=str, age=int)
        def create_person(name, age):
            return f"{name} is {age} years old"
        
        result = create_person("Alice", 30)
        assert result == "Alice is 30 years old"
    
    def test_validate_types_rejects_incorrect_types(self):
        """Test that decorator rejects incorrect types."""
        @validate_types_decorator(name=str, age=int)
        def create_person(name, age):
            return f"{name} is {age}"
        
        with pytest.raises(TypeError):
            create_person("Bob", "thirty")
    
    def test_validate_types_partial_validation(self):
        """Test that only specified types are validated."""
        @validate_types_decorator(name=str)
        def greet(name, message):
            return f"{name}: {message}"
        
        # message can be any type
        result = greet("Alice", 123)  # int for message is OK
        assert isinstance(result, str)
    
    def test_validate_types_rejects_wrong_name_type(self):
        """Test validation of different parameter types."""
        @validate_types_decorator(salary=float)
        def process_salary(name, salary):
            return salary * 1.1
        
        with pytest.raises(TypeError):
            process_salary("Alice", "50000")


class TestRetryDecorator:
    """Test cases for retry decorator."""
    
    def test_retry_succeeds_on_first_attempt(self):
        """Test function that succeeds immediately."""
        @retry_decorator(max_retries=3, delay=0.01)
        def reliable_function():
            return "success"
        
        result = reliable_function()
        assert result == "success"
    
    def test_retry_succeeds_after_failures(self):
        """Test function that succeeds after retries."""
        attempt_count = 0
        
        @retry_decorator(max_retries=3, delay=0.01)
        def eventually_succeeds():
            nonlocal attempt_count
            attempt_count += 1
            if attempt_count < 3:
                raise ValueError("Not yet")
            return "success"
        
        result = eventually_succeeds()
        assert result == "success"
        assert attempt_count == 3
    
    def test_retry_exhausts_retries(self):
        """Test function that fails all retries."""
        @retry_decorator(max_retries=2, delay=0.01)
        def always_fails():
            raise ValueError("Always fails")
        
        with pytest.raises(ValueError):
            always_fails()
    
    def test_retry_respects_max_retries(self):
        """Test that max_retries is respected."""
        call_count = 0
        
        @retry_decorator(max_retries=3, delay=0.01)
        def count_calls():
            nonlocal call_count
            call_count += 1
            if call_count <= 3:
                raise ValueError("Fail")
            return "success"
        
        with pytest.raises(ValueError):
            count_calls()
        
        # Should try max_retries times
        assert call_count == 3


class TestCountCallsDecorator:
    """Test cases for call counting decorator."""
    
    def test_count_calls_tracks_invocations(self):
        """Test that decorator counts function calls."""
        @count_calls_decorator
        def function():
            return "called"
        
        function()
        function()
        function()
        
        assert function.call_count == 3
    
    def test_count_calls_starts_at_zero(self):
        """Test that call count starts at 0."""
        @count_calls_decorator
        def new_function():
            pass
        
        assert new_function.call_count == 0
    
    def test_count_calls_reset_method(self):
        """Test resetting the call counter."""
        @count_calls_decorator
        def function():
            return "called"
        
        function()
        function()
        assert function.call_count == 2
        
        function.reset_count()
        assert function.call_count == 0
    
    def test_count_calls_with_arguments(self):
        """Test that call count works with various arguments."""
        @count_calls_decorator
        def add(a, b):
            return a + b
        
        add(1, 2)
        add(5, 10)
        add(a=3, b=4)
        
        assert add.call_count == 3
    
    def test_count_calls_returns_result(self):
        """Test that decorated function returns correct result."""
        @count_calls_decorator
        def double(x):
            return x * 2
        
        result = double(5)
        
        assert result == 10
        assert double.call_count == 1


class TestDecoratorComposition:
    """Test cases for composing multiple decorators."""
    
    def test_multiple_decorators_applied(self):
        """Test applying multiple decorators to one function."""
        @count_calls_decorator
        @memoize_decorator
        def compute(n):
            return n ** 2
        
        result = compute(5)
        assert result == 25
        assert compute.call_count == 1
    
    def test_decorator_order_matters(self):
        """Test that decorator order affects behavior."""
        attempt_count = 0
        
        @retry_decorator(max_retries=2, delay=0.01)
        @count_calls_decorator
        def retry_then_count():
            nonlocal attempt_count
            attempt_count += 1
            return "result"
        
        result = retry_then_count()
        assert result == "result"
