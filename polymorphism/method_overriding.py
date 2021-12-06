############ First I will talk about opearator overloading  ######

class A:
    s=0
    def sum(self,a=None,b=None,c=None):
        if (a!=None and b!=None and c!=None):
            s=a+b+c
        elif (a!=None and b!=None):
            s=a+b
        else:
            s=a
        return s  

a1=A()
print(a1.sum(10,25,15))


############ FUnction Overriding  ###########

class B:
    def show(self):
        print("I am in class B")
class C(B):
    def show(self):
        print("I am i  class C")

c1=C()
c1.show()
    