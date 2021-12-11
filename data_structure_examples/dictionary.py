salary={'Qasim':15000, 'Hamza': 20000, 'waleed': 30000, 'zaman': 40000}
salary['Hamid']=130000          ##### add new item in dictionary
salary.update({'Raza':27000})   ##### add new item in dictionary
print(salary['Hamid'])
print(salary)


#######################    Looping through Dictionaries    ######################
print("Looping through Dictionaries ")
for i in salary:
    print(i)         ######### pritning only keys

print("Printing only values")         
for i in salary:
    print(salary[i])          ######### pritning only values


print("Printing only values")         
for i in salary.values():
    print(i)  


print("Printing only keys")         
for i in salary.keys():
    print(i)      ####### Printing only keys

print("pritnting both keys and values")
for i,j in salary.items():
    print(i,j)            #######   printing bith keys and values



####### duplication In dictionaries   #########
employe={
    'info': {
        'name': 'Qasim',
        'address': 'SahiwaL'
    },
    'salary':
    {
        'qasim':100000,
        'ali':  50000
    }
}
print("Nested Dictionaries")
print(employe)


############ List in dictionaries #################
print(" List in dictionaries")

emp={'ali':[100000, 'Sahiwal'], 'qasim':[150000,'Islamabad']}
print(emp['qasim'])

print("After Deletion")
salary.pop('Qasim')     ### deleting item
print(salary)
print("After Deletion")
salary.popitem()         ### deleting item like stack
print(salary)
print("After Deletion")
del salary['zaman']       ### deleting item 
print(salary)

salary.clear()    ###### clear whole dictionary
print(salary)

del salary                ### deleting entire dictionary

print(salary)



