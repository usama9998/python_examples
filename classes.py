######### All About classes   ##########

class employee:
    def __init__(self,name,address):   #### Just like constructor and it will call for every object automatically
        self.name=name                 ### I can Intialize all varriables here and I will bind it with all functions
        self.address=address
    def info(self):    ##### All methods in classes will have self as instance varriables
        print("This class will hold all information about employee", self.name, self.address)

emp1=employee("Ali","Sahiwal")
emp2=employee("Qasim","Peshawar")
print(type(emp2))
emp1.info()        ###### this emp1 will pass at the place of self as argument
emp2.info()

