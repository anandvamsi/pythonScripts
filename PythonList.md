
```bash
data = [1,1,'A','B','C']
for x in data:
    print (x)
```


## Appending data to list
```bash
data.append(34)
print ("After Appending the data")
for x in data:
    print (x)
```

## Inserting data to  list
```bash
data.insert(0,"Anand")
print ("After inserting element")
for x in data:
    print (x)
```

## Deleting the element from list
```bash
print ("After removing  element")
del data[0]
for x  in data:
    print (x)
```

## slicing the list print the entri list
print ("slicing the list")
print (data[:])



#slicing the list print the starting from 0 and end till 2nd index where second index is not printed
print ("slicing the list")
print (data[0:2:])


## Printing the list another method with newline seperation
```bash
print (*port_list,sep = "\n")
```
#slicing the list print the starting from 0 and end till 2nd index where second index is not printed
print ("Alternating index")
print (data[0::2])
