# 5.	Decorator:
# o	Write a decorator that logs the execution time of a function.

import time

def log_execution_time(fun):
    def wrapper(a, b):
        start_time = time.time()
        result = fun(a, b)
        end_time = time.time()
        excution_time = end_time - start_time
        
        print(f"execution_time:{excution_time:.4f} second")
        return result
    return wrapper

@log_execution_time
def slow_function():
    time.sleep(5)
    
slow_function()