from functools import wraps, lru_cache
import time
from memory_profiler import memory_usage
import tracemalloc


def measure_memo(func):
    """
    Decorator to measure the memory usage of a function.

    This decorator calculates the peak memory used by a function during its execution and prints the value in MiB.

    Args:
        func (callable): The function to be decorated. This function should accept any number of positional and keyword arguments.

    Returns:
        callable: The decorated function. The decorated function will have the same signature as the original function.
        When the decorated function is called, it will execute the original function, measure the memory usage before and after
        the execution, and print the difference in memory usage in MiB. The return value of the decorated function will be the
        same as the return value of the original function.

    Example:
        @measure_memory
        def my_function(a, b):
            # Function implementation
            pass
    """
    def wrapper(*args, **kwargs):
        mem_before = memory_usage()[0]  # Get the current memory usage in MiB
        result = func(*args, **kwargs)  # Execute the original function
        mem_after = memory_usage()[0]  # Get the memory usage after the function execution in MiB
        print(f"Memory used: {mem_after - mem_before} MiB")  # Print the memory usage difference
        return result  # Return the result of the original function

    return wrapper  # Return the decorated function


def timer(func):
    """
    Decorator to measure the execution time of a function.

    This decorator calculates the time taken by a function to execute and prints the duration in seconds.

    Args:
        func (callable): The function to be decorated. This function should accept any number of positional and keyword arguments.

    Returns:
        callable: The decorated function. The decorated function will have the same signature as the original function.
        When the decorated function is called, it will execute the original function, measure the time taken before and after
        the execution, and print the difference in time in seconds. The return value of the decorated function will be the
        same as the return value of the original function.

    Example:
        @timer
        def my_function(a, b):
            # Function implementation
            pass
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the original function
        end = time.time()  # Record the end time
        print(f"Execution time of {func.__name__}: {end - start} seconds")  # Print the execution time
        return result  # Return the result of the original function

    return wrapper  # Return the decorated function



def debug(enabled=True):
    """
    Decorator to print function call details for debugging purposes.

    This decorator prints the function name, arguments, and return value for debugging purposes.
    It can be enabled or disabled by setting the 'enabled' parameter to True or False respectively.

    Args:
        enabled (bool): Flag to enable or disable debugging. Default is True.

    Returns:
        callable: The decorated function.

    Example:
        @debug(enabled=True)
        def my_function(a, b):
            # Function implementation
            pass
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if enabled:
                print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
            result = func(*args, **kwargs)
            if enabled:
                print(f"{func.__name__} returned: {result}")
            return result
        return wrapper
    return decorator





def memoize(func):
    """
    Decorator to memoize function results.

    This decorator caches the results of a function call based on its arguments, so that if the same arguments are
    provided again, the cached result is returned instead of re-executing the function.

    Args:
        func (callable): The function to be decorated. This function should accept any number of positional arguments.

    Returns:
        callable: The decorated function. The decorated function will have the same signature as the original function.
        When the decorated function is called, it will check if the result for the given arguments is already in the cache.
        If it is, the cached result will be returned. Otherwise, the original function will be executed, the result will be
        cached, and then returned.

    Example:
        @memoize
        def expensive_function(a, b):
            # Function implementation
            pass
    """
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper



def measure_memory(func):
    """
    Decorator to measure the peak memory usage of a function using tracemalloc.

    This decorator calculates the peak memory used by a function during its execution and prints the value in KiB.

    Args:
        func (callable): The function to be decorated. This function should accept any number of positional and keyword arguments.

    Returns:
        callable: The decorated function. The decorated function will have the same signature as the original function.
        When the decorated function is called, it will execute the original function, measure the peak memory usage before and after
        the execution, and print the difference in memory usage in KiB. The return value of the decorated function will be the
        same as the return value of the original function.

    Example:
        @measure_memory
        def my_function(a, b):
            # Function implementation
            pass
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()  # Start tracing memory allocations
        result = func(*args, **kwargs)  # Execute the original function
        current, peak = tracemalloc.get_traced_memory()  # Get the current and peak memory usage
        tracemalloc.stop()  # Stop tracing memory allocations
        print(f"Peak memory usage: {peak / 1024:.2f} KiB")  # Print the peak memory usage in KiB
        return result  # Return the result of the original function

    return wrapper  # Return the decorated function


