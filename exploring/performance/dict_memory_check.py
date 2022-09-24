import tracemalloc
import time

from memory_profiler import profile


def trace_profile(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        out = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        print(
            f"{func.__name__}() Current: {current} bytes; Peak: {peak} bytes"
        )
        tracemalloc.stop()
        return out

    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        out = func(*args, **kwargs)
        print(
            f"{func.__name__}() {type(*args)} {time.perf_counter() - start} second(s)"
        )
        return out

    return wrapper


@profile
def main():
    y = list_of_tups()
    x = create_dict()

    iterate(y)
    iterate(x)


@trace_profile
def create_dict():
    # 42.1 MiB
    new_dict = {}
    for i in range(100):
        new_dict[str(i) + "rock"] = 10
        new_dict[str(i) + "metal"] = 90
        new_dict[str(i) + "pop"] = 0
        new_dict[str(i) + "dubstep"] = 9001
    return new_dict


@trace_profile
def list_of_tups():
    # 41.9 MiB
    new_tups = []
    for i in range(100):
        new_tups.append(("rock", 10))
        new_tups.append(("metal", 90))
        new_tups.append(("pop", 0))
        new_tups.append(("dubstep", 9001))

    return new_tups


@timer
def iterate(n):
    for i in n:
        return i


if __name__ == "__main__":
    main()
