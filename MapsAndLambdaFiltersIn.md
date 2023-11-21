# Maps,Lambda,Filters,in

```python
seq = [2,3,4,5,6]
list(map(lambda num: num**3,seq))
```
## Using Filters
```python
seq = [2,3,4,5,6]
list(filter(lambda num: num%2 == 0,seq))
```

## Using in
```python
'x' in ['a','b','c']
False
'x' in ['a','x','c']
True
```
