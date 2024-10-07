
# Map and Lambda

### Lambda
Python's lambda function allows you to create small, anonymous functions at runtime.
Anonymous function is a function without a name is defined using lambda.


```python
list_numbers=[1,2,3,4,5,6,7]

def square_me(x):
    return x*x

square_list = list(map(square_me,list_numbers))
#print (square_list)
for y in square_list:
  print (y)
```

```python
print ("Method 2!!")
list_numbers=[1,2,3,4,5,6,7]
squareList = map(lambda x: x*x, list_numbers)

for y in squareList:
    print (y)
```
