######### All About classes   ##########

class employee:
    company="East West SOft"
    def __init__(self,name,address):   #### Just like constructor and it will call for every object automatically
        self.name=name                 ### I can Intialize all varriables here and I will bind it with all functions
        self.address=address
    def info(self):    ##### All methods in classes will have self as instance varriables
        print("This class will hold all information about employee", self.name, self.address)
    
    ###### Accessing class varriables  #####
    
    @classmethod    
    def class_method(cls):
       return cls.company



    @staticmethod
    def info():
        print("**** Hi, This is statoc method    **************")
emp1=employee("Ali","Sahiwal")
emp2=employee("Qasim","Peshawar")
print(type(emp2))
emp1.info()        ###### this emp1 will pass at the place of self as argument
emp2.info()


############# Above all I have discussed about instance methods  $$$$$$

##### Accesing class methods $$$$$
print("********** Accessing class method in class ********")
r=employee.class_method()
print(r)

##########   Accessing Static method in class   $$$$$$
print("********** Accessing Static method in class ********")
employee.info()