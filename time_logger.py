from loguru import logger

# Timer decorator
def timer(fn):
    from time import perf_counter
    
    def inner(*args, **kwargs):
        start_time = perf_counter()
        to_execute = fn(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        logger.info('{0} took {1:.8f}s to execute'.format(fn.__name__, execution_time))
        return to_execute
    
    return inner

@timer
def function_1():
    for i in range(10000):
        pass
@timer
def function_2():
    for i in range(10000000):
        pass

if __name__ == "__main__":
    function_1()
    function_2()
    