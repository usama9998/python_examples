num=[0,2,4,6,8,"Hello", True]
name=["ali", "Qasim", "Maham"]
mix=[num,name]    #### combining two lists
print(mix)

print(num)
print(num[5])        
print(num[2:])          ### Slicing list
print(num[:3])
print(num[2:5]) 

num.append(45)          #### Append at the end of the list
num.insert(4,"Khalid")  #### insert at  my prefered location

for i in num:           ##### for loop on list
   print(i)

num.pop(3)              #### for removing at prefered location
print("After Pop")
for i in num:
    print(i)


num.remove("Khalid")    #### for removing data of my own choice

for i in num:
    print(i)

print ("delete multipe")

del (num[2:5])     #### for deleting multiple values
for i in num:
    print(i)

print("After eXTENDING")

num.extend([3,4,5,6,7])
for i in num:
    print(i)

print("Maximum number", end="\t")
print(max(num))      #### Print maximum
print("Minimum number", end="\t")
print(min(num))      ##### print minimum
print("Sum of numbers", end="\t")
print(sum(num))      ##### sum of number
num.remove(True)
print(num)
print("Sorting Numbers", end="\t")
num.sort()
print(num)



##### List  ##############

num=[0,2,4,6,8,"Hello", True]
name=["ali", "Qasim", "Maham"]
mix=[num,name]
print(mix)

print(num)
print(num[5])
print(num[2:])
print(num[:3])
print(num[2:5])
for i in num:
   print(i)