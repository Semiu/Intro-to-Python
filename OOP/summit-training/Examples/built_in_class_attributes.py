"""
Created on Aug 1, 2017

@author: SummitWorks
"""


#
# class MyClass:
#     count = 0 #special meaning
#     def __init__(self):
#         self.p1 = 0
#         self.p2 = 'string data'
#
#     def myaction(self):
#         self.p3= 23
#
# obj = MyClass() #
# obj.p1=100 # instance
# obj.myaction() #
#
# obj2 = MyClass()
# obj2.p1 = 10
# obj.p3 = 200


class Employee:
    """Common base class for all employees"""
    empCount = 0 # class variable

    def __init__(self, name, salary):  # initializer __str__,__repr__, magic method, init.py
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def __del__(self): #
        pass

    def displayCount(self):
        print("in displayCount method")
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)
    # def __str__(self):
    #     return self.name
    #
    # def __del__(self):
    #     del self

print(Employee.empCount)
emp1 = Employee('Kanchan',1000) #
print(Employee.empCount)
emp2 = Employee("Manni", 5000)
print(Employee.empCount)
emp1.displayEmployee() #
emp2.displayEmployee()
print(type(emp2))
del(emp1)
emp1.__del__()
emp1.displayEmployee()



# create a obj. Employee # class object
# init invoke class object
# Employee.__init__(emp1, 'Kanchan',1000)
# Employee.displayEmployee(emp2)

# emp1.displayCount()
# emp2.displayCount()
# emp1.displayEmployee()
# Employee.displayEmployee(emp1)

# # print(Employee.empCount)
# del (emp1)
