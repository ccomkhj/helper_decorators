# Function computation time logger 

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
```#   t i m e _ l o g g e r  
 