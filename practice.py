# print("Hello world")
# a=input("Enter a number")
# print(a[-1])
# print(a[2:4])
# print(a[:4])
# print(a[2:])

# print("I "+a[5:])


# print('Telusko \n rocks')



# a=10
# print(id(a))
# b=10
# print(id(b))
# a=9
# print(id(a))
# print(type(a))


# num=complex(a)
# print(num)
# print(type(num))

# range(0,10)
# print(list(range(10)))
# print(list(range(2,10,2)))

# num=int(input("Enter a number to check whether it is even or odd "))
# if(num%2==0):
#     print("It is Even Number")
# else:
#     print("It is odd Number")





#########      If Else Assignment   #####################
##### Write a code to check whether a number is +ve or -ve

# num=int(input("Enter a  number to check whther it is positive or negative"))
# if(num>0):
#     print("Number is positive")
# else:
#     print("Number is negative")



#### if Else 2 #####
#### take three values from the user and find the greater of them ####

# num1=int(input("Enter first Number"))
# num2=int(input("Enter Second Number"))
# num3=int(input("Enter third Number"))
# if(num1>num2 and num1>num3):
#     print("Number1 is greater",num1)
# elif(num2>num1 and num2>num3):
#     print("Number2 is greater",num2)
# elif(num3>num1 and num3>num2):
#     print("Number3 is greater",num3)
# else:
#     print("you Entered Wrong value")





####### While loop practice ######

# num=1
# while(num<=100):
#     if(num%3!=0 and num%5!=0):
#         print("Number is ", num)
#     num+=1



### While loop 2 ##### 
#### Write a code to built below pattern   ######
# i=1

# while(i<=5):
#     j=1
#     print("#",end="")
#     while(j<=5):
#         print("#", end="")
#         j=j+1
#     i=i+1
    
#     print(end="\n")
    




###### For loop problem ####

##### Find perfect square numbers between 1 to 50 #########
# import math
# for i in range(1,50):
#     square=math.sqrt(i)
#     if( (square)**2==i):
#         print("Perfect Square numbers are", i)




###### Break ######

# available=10
# i=1
# x=int(input("Enter the number of candies you want to print"))
# while i<x:
    
#     print("Take your candy",i)
#     i=i+1


   ##### fibonacci series ###### 

# f1=0
# f2=1
# print(f1, end="")
# for i in range(1,50):
#     print(f2,end="")
#     next=f1+f2
#     f1=f2
#     f2=next




################ for else ############

nums=["Ali","Khalid","Raza"]
for i in nums:
   if(i=="Hamza"):
      print(i)
      break
else:
   print("Not found")


    



