########### Array ###########
##########  Similar to list but only one difference that we have all the values of 
##########  only one type....


import array
from array import *      ### for importing all functions in array


############ Intialize array    ##############

vals=array('i',[1,3,5,7,9,11,13,15])   ##### i is code for integer type
print (vals)
print(vals.buffer_info())           ### this function prints address of array and size
vals.append(25)                      ### printing after appending
print(vals)   
                    
vals.reverse()
print(vals)                         #### printing after reversing


########### Printing through for loop   ##########

print("********* Printing through for loop     ***********")
for i in vals:
    print(i)
print("Usinfg length function")
length=len(vals)
for i in range(length):
    print(i)


########## Deletion ###############
print("Using Pop fuction to delete index based values")
vals.pop(4)
print(vals)
print("Using remove fuction to delete value of my own choice")
vals.remove(25)
print(vals)
