# Pandas Data Frame

## What is Data Frame
The pandas DataFrame is a structure that contains two-dimensional data and its corresponding labels. 
DataFrames are widely used in data science, machine learning, scientific computing, and many other data-intensive fields.

In many cases, DataFrames are faster, easier to use, and more powerful than tables or spreadsheets because 
they’re an integral part of the Python and NumPy ecosystems

```python
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

W	X	Y	Z
A	0.302665	1.693723	-1.706086	-1.159119
B	-0.134841	0.390528	0.166905	0.184502
C	0.807706	0.072960	0.638787	0.329646
D	-0.497104	-0.754070	-0.943406	0.484752
E	-0.116773	1.901755	0.238127	1.996652

## To delete permently
df.drop('new',axis=1,inplace=True)

W	X	Y	Z
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
