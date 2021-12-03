import array 
from array import *

vals=array('i',[25,45,19,7,56,100])
temp=0
for i in range(0,len(vals)):
    for j in range(i+1,len(vals)):
        if(vals[i]>vals[j]):
            temp=vals[i]
            vals[i]=vals[j]
            vals[j]=temp

print(vals)