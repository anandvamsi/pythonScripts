# Numpy

# What is Numpy and advantages

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
np.random.rand(5.5)
array([[0.64762291, 0.56209399, 0.82639867, 0.38642705, 0.35253886],
       [0.21183618, 0.74993563, 0.70603091, 0.38870389, 0.4605119 ],
       [0.84695945, 0.0032151 , 0.39553587, 0.04020141, 0.19984033],
       [0.78646781, 0.21147743, 0.57682311, 0.06479972, 0.19242824],
       [0.46275963, 0.6657931 , 0.4770955 , 0.52623333, 0.40606067]])
Note: Two square brakets indicate they are two dimentional
```
## To provide a random integer
```python
np.random.randint(1,100)
67

# provide 10 randome integer max limit is 100; not inclsive of 100
np.random.randint(1,100,10)
array([45, 92, 47, 61, 26, 97, 15, 51, 71, 46])
```

## Getting the maximum number from the array
```
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

np_2d[0][1]
3
```