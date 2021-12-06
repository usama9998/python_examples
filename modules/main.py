###########  I will take all functions from that file and used it in this file  ####
from func import *

a10=a8+a9        ####### to imprt it here I need to get these varriable out
                #######  from if conditon of _name_="main" than I can Acees it here
                #####    because _name_ will become in this file is equal to
                ####      func.
print(a10)
a=7
b=9

sum=add(a,b)
print("Sum of numbers")
print(sum)

subt=sub(a,b)
print("Subtraction of numbers")
print(subt)

mult=mul(a,b)
print("Multiplication of numbers")
print(mult)

divi=div(a,b)
print("Divisions of varriables")
print(divi)


