class A:
    def feature(self):
        print("Hello this is feature 1")
    def feature2(self):
        print("Hello to the feature 2")

# class B(A):                            ##### SIngle level Inheritance only one base class and one super class
#     def feature3(self):
#         print("Hello to the feature 3")

#     def feature4(self):
#         print("Hello to the feature 4")

class B():                            ##### this code is only for multiple inheritance
   def feature3(self):
       print("Hello to the feature 3")

   def feature4(self):
        print("Hello to the feature 4")

# class c(B):                 #### This is basically multilevel inheritance that next class is inherited from previous one
#     def feature5(self):
#         print("Hello to the feature 5")

#     def feature6(self):
#         print("Hello to the feature 6")

class c(A,B):
    def multi_inheritance(self):
        print("Multilevel inheritance is here")

c1=c()
c1.feature()