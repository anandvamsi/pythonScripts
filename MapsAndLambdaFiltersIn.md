# Maps,Lambda,Filters,in

```python
seq = [2,3,4,5,6]
list(map(lambda num: num**3,seq))
```

## Checking even numbers using lambda
```python
numbers = [1,2,3,4,5]
list(filter(lambda x: x % 2 == 0, numbers))
```

## Using Filters : Example1
```python
seq = [2,3,4,5,6]
list(filter(lambda num: num%2 == 0,seq))
```

## Filter check the vowles
```
def filter_vowels(letters):
    vowels = ['a','e','i','u']
    return True if letters in vowels else False

letter = ['a','b','c','d']
list(filter(filter_vowels,letter))
```


## Using in
```python
'x' in ['a','b','c']
False
'x' in ['a','x','c']
True
```
