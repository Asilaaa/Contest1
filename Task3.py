import time


def decorator_1(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        print(f"{func.__name__} call executed in {elapsed:.4f} sec")
    return wrapper
