import array
from array import *

vals=array('i',[])
length=int(input("Enter the lenght of array you want to create"))
for i in range(length):
    value=int(input("Enter Next value"))
    vals.append(value)
x=int(input("Enter a number to check whether it is in array or not   "))
k=0
for i in vals:
    if(i==x):
        print("your number is present i.e-",i )
        print("Index of ", i, "is ", k)
        break
    k+=1
else:
    print("Sorry we could not find your given value in array")