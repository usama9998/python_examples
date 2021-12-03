###### different methods/functions of creating numpy arrays #######
####### Array Method   #######


import numpy as np          #### it is imported because it helps us to work with multidimensional arrays 
from numpy import *         #### for accessing all functions in numpy
print("creating numpy array Using Array Mrthod")                             
vals=np.array([1,2,3,4,5,6,6],int)  
vals1=np.array([1,2,3,4,5,6,6],int) 
print (vals)
##### Adding 10 to each elements in array   ######
print("After Adding 10")
vals=vals+10
print(vals) 

########### concatenate two arrays  ######
print(vals)
print(vals1)
print("Concatenate two arrays")
print(concatenate([vals,vals1]))



###### sin of every element in vals   #######
print("Applying sin(All mathemetical functions")
print(sin(vals))

###### Adding 2 arrays   ######
print("after adding vals and vals1")
vals3=vals1+vals
print(vals3)

####### shallow copy Vs Deep copy   #####

print("***** copying arrays by assigning ******")
vals=vals1
print(id(vals))
print(id(vals1))
vals[1]=98
print("****** After updating value by assigning ********")
print(vals)
print(vals1)

# ###### Shallow Copy   ******** Uncomment to see its effect *********####
# print("********* shallow Copy  ********")
# vals1=vals.view()
# print(id(vals))
# print(id(vals1))
# vals[1]=78
# print("****** After updating value ********")
# print(vals)
# print(vals1)

###### Deep Copy   ####
print("****** Deep Copy ******")
vals1=vals.copy()
print(id(vals))
print(id(vals1))
vals[1]=78
print("****** After updating value in Deep Copy ********")
print(vals)
print(vals1)




######## creating 2D Array    ######
print("2D Arrays")
vals_2d=np.array([[1,2,3,4,5,6,7,8] ,  [9,10,11,12,13,14,15,16]])
print(vals_2d[1,3])
print(vals_2d.shape)

######## creating 3D Array    ######
print("3D Arrays")
vals_3d=np.array([[[1,2,3,4,5,6,7,8] ,[9,10,11,12,13,14,15,16]],[[1,2,3,4,5,6,7,8],[11,12,13,14,15,16,17,18]]])
print(vals_3d[0,1,2])

print(vals_3d.shape)


######## linspace Method #######
print("Using linspace method")
arr=np.linspace(0,15,16)   #### it will divide 0-15 into 16 equal parts
print(arr)

######## Arrange Method #######
print("Using Arrange method")
arr1=np.arange(0,15,3)   #### it will skip number by 3
print(arr1)

########Zeros #######
print("Using Zeros method")
arr2=np.zeros(5)   #### it will add 5 zeros and create array of 5 size
print(arr2)


########Ones #######
print("Using Zeros method")
arr2=np.ones(5)   #### it will add 5 ones and create array of 5 size
print(arr2)

########logspace #######
print("Using Zeros method")
arr3=np.logspace(1,40,5)   #### it will add (1,40 ) 5 values of log
print(arr3)


