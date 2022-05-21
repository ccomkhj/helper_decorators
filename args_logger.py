import inspect
from collections.abc import Iterable

# Parameter decorator
def tracer(fn):
    f = open(f"args_log_{fn.__name__}.txt", mode = "a") # select logging location if you need.
    
    def inner(*args, **kwargs):
        to_execute = fn(*args, **kwargs)
        f.write(f'""" {fn.__name__}: \n')
        f.write("== Args \n")

        params = inspect.getfullargspec(fn).args
        for param, arg in zip(params, args):
            f.write(f"{param}: {type(arg)}\n")

        f.write(f"== Returns\n")

        if isinstance(to_execute, Iterable):
            for out in to_execute:
                f.write(f"{type(out)}\n")

        else:
            f.write(f"{type(to_execute)}\n")
        f.write(f'"""\n')
        f.close()
        return to_execute
    

    return inner



@tracer
def function_1(a,b,c):
    import numpy as np
    return "hi", b, np.array([10,10])


if __name__ == "__main__":
    function_1(1,2,'a')
    