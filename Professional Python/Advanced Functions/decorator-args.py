import time

# A decorator factory that creates a decorator to test function speed multiple times
def dec_speed_test(count):
    def speed_test(fn):
        def inner(*args, **kwargs):
            start_time = time.perf_counter()
            print(f"The function '{fn.__name__}' is running.")
            for _ in range(count):
                result = fn(*args, **kwargs)
                end_time = time.perf_counter()
                run_time = end_time - start_time
                print(f"Elapsed time: {run_time:.6f} seconds")
            return result
        return inner
    return speed_test

# This function uses a generator to sum numbers from 0 to 9,999,999
@dec_speed_test(count=2)
def sum_gen():    
    return sum((x for x in range(10000000)))

# This function uses a list to sum numbers from 0 to 9,999,999
@dec_speed_test(count=3)
def sum_list():
    return sum([x for x in range(10000000)])

# Run and print the results of both functions
print(sum_gen())
print(sum_list())
