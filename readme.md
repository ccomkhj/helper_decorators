# Helper function

## 1. function arguments logging
After finishing prototyping, this module could help your documentation.
```
@tracer
def function_1(a,b,c):
    pass
    return "hi", b, np.array([10,10])
```
`args_log_function_1.txt`
```
""" function_1: 
== Args 
a: <class 'int'>
b: <class 'int'>
c: <class 'str'>
== Returns
<class 'str'>
<class 'int'>
<class 'numpy.ndarray'>
"""
```


## 2. function computation tracking
### Examples
```
@timer
def function_1():
    for i in range(10000):
        pass
@timer
def function_2():
    for i in range(10000000):
        pass
```
```
2022-03-12 16:04:43.873 | INFO     | __main__:inner:12 - function_1 took 0.00039920s to execute
2022-03-12 16:04:44.135 | INFO     | __main__:inner:12 - function_2 took 0.25947600s to execute
```

