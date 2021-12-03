def greet():                                       #### func without argumnets
    print("Hello")
    print("Have a good day")

def add(a,b):                              #### func with arguments but not returning 
    c=a+b
    print(c)

def add1(a,b):          ##### func with arguments but returning a value
    c=a+b
    return c

def add_sub(a,b):        ##### func with arguments but returning more than one value
    c=a+b
    d=a-b
    return c,d


######## Calling ALL Functions    ###########

greet()
add(5,4)
sum=add1(8,7)    ##### store result of return in varriable to stor in db or memory
print(sum)
sum,sub=add_sub(10,9)
print(sum, end="\t")
print(sub)
