from functools import wraps, lru_cache
import time
from memory_profiler import memory_usage
import tracemalloc


def measure_memory(func):
    """
    Decorator to measure the memory usage of a function.

    This decorator calculates the peak memory used by a function during its execution and prints the value in MiB.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function.
    """
    def wrapper(*args, **kwargs):
        mem_before = memory_usage()[0]
        result = func(*args, **kwargs)
        mem_after = memory_usage()[0]
        print(f"Memory used: {mem_after - mem_before} MiB")
        return result

    return wrapper


def timer(func):
    """
    Decorator to measure the execution time of a function.

    This decorator calculates the time taken by a function to execute and prints the duration in seconds.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time of {func.__name__}: {end - start} seconds")
        return result

    return wrapper



def debug(enabled=True):
    """
    Decorator to print function call details for debugging purposes.

    This decorator prints the function name, arguments, and return value for debugging purposes.

    Args:
        enabled (bool): Flag to enable or disable debugging.

    Returns:
        callable: The decorated function.
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

# Использование
# @debug(enabled=True)



def memoize(func):
    """
    Decorator to memoize function results.

    This decorator caches the results of a function call based on its arguments, so that if the same arguments are
    provided again, the cached result is returned instead of re-executing the function.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function.
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
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Peak memory usage: {peak / 1024:.2f} KiB")
        return result

    return wrapper


