class A:
    def __init__(self):
        print("I am in the init of A")
    
    def feature1():
        print("I am in feature of 1")

class B():                  ##### If I don't make constructor in B than it will find of A
    def __init__(self):
        # super().__init__()    #### but if I don't write this It will only call the class of base class only
        print("This is also init of B")
    def feature1():
        print("Feature 1")

class C(A,B):
    def __init__(self):
        super().__init__()     ### In this case it will inherit the constructor of class on the left side(A,B), This is known as MRO
        print("I am in th init of z")
    
c1=C()



########## In this file We Learn three things  #######
########## 1) How constructor behave in inheritance ####
########## 2) What is the use of super() ininheritance  ###
#########  3) What is MRO