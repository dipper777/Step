import time
import unittest

def timer_decor(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"Func {func.__name__} executed in {time.time()}")
        return result
    return wrapper()

class Test_time_decor(unittest.TestCase)
    def Test_time_func(self):
        start_time = time.time()

