from math import *
class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        c=self.a+self.b
        print(c)
    def subtract(self):
        c=self.a-self.b
        print(c)
    def mul(self):
        c=self.a*self.b
        print(c)
    def div(self):
        c=self.a/self.b
        print(c) 
class import_math_operations:
    def __init__(self,a):
        self.a=a
    def logarithm(self):
        print(log(self.a))
    def square_root(self):
        print(sqrt(self.a))
    def sin_m(self):
        print(sin(self.a))
    def cos_m(self):
        print(cos(self.a))
    def tan_m(self):
        print(tan(self.a))
    

while True:
    
    def menu():
        global x
        print('1. Scientific calculator \n2. Simple calculator')
        x=int(input("Enter your choice from above= "))
        
    menu()
    if x==2:
        num1=float(input("Enter first number ="))
        num2=float(input("Enter second number ="))
        operator=str(input("Enter operator +  -  /  * log ="))
        c1=calculator(num1,num2)
        if operator=='+':
            sum=c1.sum()
            
        elif operator=='*':
            c1.mul()
            
        elif operator=='/':
            c1.div()
            
        elif operator=='-':
            c1.subtract()
            
        else:
            print("Invalid Option")
    elif x==1:
        num=float(input("Enter number to apply scientific operations "))
        c2=import_math_operations(num)
        operator=str(input("Enter operator log  sqrt  sin  cos tan ="))
        if operator=='log':
            c2.logarithm()
        elif operator=='sqrt':
            c2.square_root()
        elif operator=='sin':
            c2.sin_m()
        elif operator=='cos':
            c2.cos_m()
        elif operator=='tan':
            c2.tan_m()
        else:
            print("Invalid operator")
            
    else:
        print("Invalid Input ")
        break

    

