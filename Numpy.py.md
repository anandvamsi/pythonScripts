# Numpy

# What is Numpy and advantages

1. Less Meomory
2. Fast
3. convient 


# To install numpy Module
```bash
pip3 install numpy
```

# To use in the program

```python
import numpy as np
mylist = [2,3,4,5]
np.array(mylist)
```

## Random numbers
```python
np.random.rand(5)
array([0.15668726, 0.29394134, 0.18163961, 0.20100653, 0.55747179])

#To display a two mentional array
np.random.rand(5,5)
array([[0.64762291, 0.56209399, 0.82639867, 0.38642705, 0.35253886],
       [0.21183618, 0.74993563, 0.70603091, 0.38870389, 0.4605119 ],
       [0.84695945, 0.0032151 , 0.39553587, 0.04020141, 0.19984033],
       [0.78646781, 0.21147743, 0.57682311, 0.06479972, 0.19242824],
       [0.46275963, 0.6657931 , 0.4770955 , 0.52623333, 0.40606067]])
Note: Two square brakets indicate they are two dimentional

a1= np.random.rand(5,5)
# Determine the max and minimum number 
a1.max()
a1.max()
```





## To get the dimesions of the array
```python
np_2d = np.array([[2,3,4],[23,4,5],[2,3,5]])

#Provides the dimention of the array
np_2d.ndim 
2

#Size of the array
np_2d.size
9

#Shape of the array
np_2d.shape()
(3, 3)



## To provide a random integer
```python
np.random.randint(1,100)
67
```

# provide 10 randome integer max limit is 100; not inclsive of 100
```python
np.random.randint(1,100,10)
array([45, 92, 47, 61, 26, 97, 15, 51, 71, 46])
```

# Provide 5 numbers between start limit to end limit

```python
np.linspace(1,5,10)
array([1.        , 1.44444444, 1.88888889, 2.33333333, 2.77777778,
       3.22222222, 3.66666667, 4.11111111, 4.55555556, 5.        ])
​```
 
## Getting the maximum number from the array
```python
ranarray = np.random.randint(0,35,10)
ranarray.max()
ranarray.min()
ranarray.argmin()
```

## TO see the dataype of the array
```python
ranarray.dtype
```


# Indexing in numpy
```python
l1 = [1,2,3,4,5,6,7,8,9,10]
narray = np.array(l1)
narray[5:]
array([ 6,  7,  8,  9, 10])
```

## Copying the array


## Searching index in the arrya
```python
np_2d = np.array([[2,3,4],[23,4,5],[2,3,5]])
np_2d[0]
[2,3,4]

np_2d[0][1] Means column0,row1
3
np_2d[:3,1:]
array([[3, 4],
       [4, 5],
       [3, 5]])
# TO get the first line
np_2d[:3,1:][0]
```

## Mathematics operations Elements in numpy
```python
a1 = np.array([1,3,4])
a2 = np.array([2,3,4])
a1+a2
array([3, 6, 8])

a1-a2
array([-1,  0,  0])

a1*a2
array([ 2,  9, 16])

#Matrix multiplication
a1.dot(a2)
27

```

## Flatterin the array
```python
a2=np.random.rand(5,5)
for x in a2.flat:
    print(x)
```

## Rearranging the array vertical stacking and horizondal stacking 
```python
a=np.arange(9).reshape(3,3)
b=np.arange(9).reshape(3,3)
np.vstack((a,b))

array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8],
       [0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])

np.hstack((a,b))
array([[0, 1, 2, 0, 1, 2],
       [3, 4, 5, 3, 4, 5],
       [6, 7, 8, 6, 7, 8]])
```
## Splitting the array in horizondal and vertical
```python
c= np.arange(30).reshape(2,15)
result=np.hsplit(c,3)
result[0]

array([[ 0,  1,  2,  3,  4],
       [15, 16, 17, 18, 19]])

result[1]
array([[ 5,  6,  7,  8,  9],
       [20, 21, 22, 23, 24]])

result[2]
array([[10, 11, 12, 13, 14],
       [25, 26, 27, 28, 29]])

result = np.vsplit(c,2)
result[0]
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14]])

result[1]
array([[15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])
```
