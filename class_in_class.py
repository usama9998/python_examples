class employee:
    def __init__(self,name,address,salary):
        self.name=name
        self.address=address
        self.salary=salary
        # self.edu=self.eductaion_details()
    def show(self):
        print(self.name)
        print(self.address)
        print(self.salary)
        # self.edu.show()
    
    class eductaion_details:
        def __init__(self,uni,degree,city):
            self.uni=uni
            self.degree=degree
            self.city=city
        
        def show(self):
            print(self.uni)
            print(self.degree)
            print(self.city)

emp1=employee("Ali","East West Soft","100000")
print("Employee Info")
emp1.show()

print("Employee's Education Info")
edu=employee.eductaion_details("UOS","BSCS","Sahiwal")
edu.show()