# Pandas
- Pandas is an open source liberary build on top of Numpy
- It allows for fast analysis and data cleaning and preparations
- It excels in performance and Productvity
- It also has build-in visualization features


## Importing Pandas
```python
import pandas as pd
l1=['a','b','c','d']
l2=[1,2,3,4]
pd.Series(l1,l2)
1    a
2    b
3    c
4    d
dtype: object
```

```python
pd.Series([1,2,3,4],['USA','JAPAN','Russia','USSR'])
USA       1
JAPAN     2
Russia    3
USSR      4
dtype: int64
```

## Adding two list
```python
s1 = pd.Series([1,2,3,4],['USA','JAPAN','Russia','USSR'])
s2 = pd.Series([1,2,3,4],['USA','CHINA','Russia','USSR'])
s1 + s2
CHINA     NaN
JAPAN     NaN
Russia    6.0
USA       2.0
USSR      8.0
dtype: float64
```



``
