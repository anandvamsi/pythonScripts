# Maps in Python

## Syntax of map

The map() function takes two arguments:

- function - a function
- iterable - an iterable like sets, lists, tuples, etc

Map() function returns an object of map class,The returned values can be passed to functions like list and set

```python
map(function, iterable, ...)
```


- Example1:
```python
def times2(var): return var**2

seq = [2,3,4,5,6]
list(map(times2,seq))
```

