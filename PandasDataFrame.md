# Pandas Data Frame

## What is Data Frame
The pandas DataFrame is a structure that contains two-dimensional data and its corresponding labels. 
DataFrames are widely used in data science, machine learning, scientific computing, and many other data-intensive fields.

In many cases, DataFrames are faster, easier to use, and more powerful than tables or spreadsheets because 
they’re an integral part of the Python and NumPy ecosystems

```python
import pandas as pd
from numpy.random import randn
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
df

      W	      X	        Y	        Z
A	0.302665	1.693723	-1.706086	-1.159119
B	-0.134841	0.390528	0.166905	0.184502
C	0.807706	0.072960	0.638787	0.329646
D	-0.497104	-0.754070	-0.943406	0.484752
E	-0.116773	1.901755	0.238127	1.996652
```

# How to extract a column
If you want to extract column 'Y'
```python
df['Y']
A   -1.706086
B    0.166905
C    0.638787
D   -0.943406
E    0.238127
Name: Y, dtype: float64

# Method 2

df.Y
A   -1.706086
B    0.166905
C    0.638787
D   -0.943406
E    0.238127
Name: Y, dtype: float64

# Extracting multiple Columns
df[['W','X']]

	W	          X
A	0.302665	1.693723
B	-0.134841	0.390528
C	0.807706	0.072960
D	-0.497104	-0.754070
E	-0.116773	1.901755
```

## Adding/removing  a new column
```python
df['new'] = df['W'] + df ['Y']

  	  W	        X	        Y	          Z	      new
A	0.302665	1.693723	-1.706086	-1.159119	-1.403420
B	-0.134841	0.390528	0.166905	0.184502	0.032064
C	0.807706	0.072960	0.638787	0.329646	1.446493
D	-0.497104	-0.754070	-0.943406	0.484752	-1.440510
E	-0.116773	1.901755	0.238127	1.996652	0.121354

df['new']
      W	      X	          Y	        Z	      new
A	0.302665	1.693723	-1.706086	-1.159119	-1.403420
B	-0.134841	0.390528	0.166905	0.184502	0.032064
C	0.807706	0.072960	0.638787	0.329646	1.446493
D	-0.497104	-0.754070	-0.943406	0.484752	-1.440510
E	-0.116773	1.901755	0.238127	1.996652	0.121354
```

## To drop a new column
```python
This will be a temperory delete
df.drop('new',axis=1)

		W		X		Y	Z
A	0.302665	1.693723	-1.706086	-1.159119
B	-0.134841	0.390528	0.166905	0.184502
C	0.807706	0.072960	0.638787	0.329646
D	-0.497104	-0.754070	-0.943406	0.484752
E	-0.116773	1.901755	0.238127	1.996652

## To delete permently
df.drop('new',axis=1,inplace=True)

		W		X		Y	Z
A	0.302665	1.693723	-1.706086	-1.159119
B	-0.134841	0.390528	0.166905	0.184502
C	0.807706	0.072960	0.638787	0.329646
D	-0.497104	-0.754070	-0.943406	0.484752
E	-0.116773	1.901755	0.238127	1.996652

df.shape
(5,4)
```

# TO get the element based on the index
```python
df.loc['A']
W    0.302665
X    1.693723
Y   -1.706086
Z   -1.159119
Name: A, dtype: float64

df.iloc[0]
W    0.302665
X    1.693723
Y   -1.706086
Z   -1.159119
Name: A, dtype: float64
```

## To get the subset
```python
df.loc['B','Y']
0.16690463609281317

df.loc[['A','B'],['W','Y']]
W	            Y
A	0.302665	-1.706086
B	-0.134841	0.166905
```

## Condition Operator
```python
df > 0
	W	X	Y	Z
A	True	False	True	True
B	True	False	False	False
C	True	True	True	False
D	True	True	False	True
E	True	False	False	True

df[df > 0]
		W	X	Y	Z
A	0.185415	NaN	0.489342	0.431623
B	0.918789	NaN	NaN	NaN
C	1.189799	0.235070	1.049795	NaN
D	0.394640	0.143831	NaN	0.875118
E	0.705783	NaN	NaN	0.099050

df['W']> 0
A    True
B    True
C    True
D    True
E    True
Name: W, dtype: bool

df[df['W'] > 0]

	W	X	Y	Z
A	0.185415	-1.959586	0.489342	0.431623
B	0.918789	-1.703497	-0.461836	-1.096932
C	1.189799	0.235070	1.049795	-0.343215
D	0.394640	0.143831	-0.449142	0.875118
E	0.705783	-0.774156	-0.124828	0.099050

result = df[df['W'] > 0]
result['X'] ::- prints the X column
A   -1.959586
B   -1.703497
C    0.235070
D    0.143831
E   -0.774156

## Another method
df[df['W'] > 0]['X']
A   -1.959586
B   -1.703497
C    0.235070
D    0.143831
E   -0.774156

# TO list two columns
df[df['W'] > 0][['X','Y']]

X	Y
A	-1.959586	0.489342
B	-1.703497	-0.461836
C	0.235070	1.049795
D	0.143831	-0.449142
E	-0.774156	-0.124828

```

## Mutiple conditions AND OR condition
```python
df[(df['X'] >0) & (df['Y'] < 0)]
	W	X	Y	Z
D	0.39464	0.143831 -0.449142	0.875118


df[(df['X'] >0) | (df['Y'] < 0)]
	X	Y	Z
B	0.918789	-1.703497	-0.461836	-1.096932
C	1.189799	0.235070	1.049795	-0.343215
D	0.394640	0.143831	-0.449142	0.875118
E	0.705783	-0.774156	-0.124828	0.099050
```

## Adding a new column
```python
l1 = ['A','B','C','D','E']
df['alpha'] = l1
df
		W		X		Y		Z	alpha
A	0.185415	-1.959586	0.489342	0.431623	A
B	0.918789	-1.703497	-0.461836	-1.096932	B
C	1.189799	0.235070	1.049795	-0.343215	C
D	0.394640	0.143831	-0.449142	0.875118	D
E	0.705783	-0.774156	-0.124828	0.099050	E

## Resetting the index
df.set_index('alpha')
		W	X	Y	Z
alpha				
A	0.185415	-1.959586	0.489342	0.431623
B	0.918789	-1.703497	-0.461836	-1.096932
C	1.189799	0.235070	1.049795	-0.343215
D	0.394640	0.143831	-0.449142	0.875118
E	0.705783	-0.774156	-0.124828	0.099050
```

## Missing Values
```python
d = {'A':[1,2,np.nan], 'B': [3,5,np.nan], 'c': [6,7,8]}
df = pd.DataFrame(d)
df
	A	B	c
0	1.0	3.0	6
1	2.0	5.0	7
2	NaN	NaN	8

# will drop all the NA files
df.dropna()
	A	B	c
0	1.0	3.0	6
1	2.0	5.0	7


# will all the row th having minimum 3 values
df.dropna(thresh=3)
	A	B	c
0	1.0	3.0	6
1	2.0	5.0	7

# Fill the missing the values with  'test'
df.fillna('test')

A	B	c
0	1.0	3.0	6
1	2.0	5.0	7
2	test	test	8

# Filling the the average to the non values

df['A'].fillna(value=df['A'].mean())
0    1.0
1    2.0
2    1.5
