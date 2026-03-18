import time
from typing import Union


def print_timings(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        start_time = time.process_time()
        result = func(*args, **kwargs)
        end_time = time.process_time()
        print(f'Function {func.__name__!r} executed in {(end_time-start_time):.4f}s')
        return result
    return wrap_func


def parse_boolean(input: Union[str, bool]) -> bool:
    if isinstance(input, bool):
        return input

    if str(input).lower() in ["true", "vrai"]:
        return True
    return False
