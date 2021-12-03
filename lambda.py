######### When we want to make anonymous functions(i.e-- Function Without name)
######### we need lambda to initialize it
from functools import reduce

f=lambda a:a*a
result=f(5)

print(result)

####### A lambda function can take any number of arguments, but can only have one expression.
print("****** Using Multiple arguments and only one expression can pass in it  ***********")
g=lambda a,b:a+b
reult1=g(10,25)
print(reult1)



#########  Use of lambda  ##########

##### We use it when we don't want to write a special pupose functions

# def is_even(n):
#     if(n%2==0):
#         print("It is even")

########## instead of writing this is_even function I used lambda

print("***** finding Even Number from list Using lambda   ***********")
n=[1,2,3,4,5,6]
evens=list(filter(lambda n: n%2==0,n))
print(evens)

########### Now I want to map this function and want plus 5 in even numbers ########
print("***** I have add 5 in list of evens ***********")
add=list(map(lambda n: n+5, evens))
print(add)

########### Now I want to reduce the values of list by adding all the list ########
print("***** I have add all the list to get sum of list***********")
red=reduce(lambda a,b:a+b, n)
print(red)