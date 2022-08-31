"""
Created on Aug 1, 2017

@author: SummitWorks
"""

import datetime
today = datetime.datetime.now()
print(str(today)) # __str__
print(repr(today)) # __repr__



class Employee:
    """Common base class for all employees"""

    def __init__(self, name, salary): #initializer __main__,  __init__ , __str__, __next__ __add__ 1+2, add(1,2) [(),{}]
        self._name = name # public
        self.salary = salary
        self.dob = 'some date'


    def _displayEmployee(self):
        # self.dob = 'some date'
        print("Name : ", self.__name, ", Salary: ", self.salary)

    def __str__(self): #overridding
        # super().__str__()
        return self._name.title()

    def getsalary(self):
        return self.salary

class child(Employee):
    pass
#
# emp1 = Employee("zara", 2000)
# emp2 = Employee("Manni", 5000)
# print(emp1)
# print(emp1.__repr__())

# emp1.name

# emp1.address = 'some address' # python dymanic nature

# print(emp1.dob)
# emp2.displayEmployee()
# Employee.displayEmployee(emp2)


# #
# # emp1.displayEmployee() #=== Employee.displayEmployee((emp1))
# emp2.displayEmployee()

# calling a method with a list of n arguments is equivalent to
# calling the corresponding function with an argument list that is
# created by inserting the method’s instance object before the first argument.
# Same as emp2.displayEmployee()
# Employee.displayEmployee(emp2)


# print("Employee.__doc__:", Employee.__doc__)
# print("Employee.__name__:", Employee.__name__)
# print("Employee.__module__:", Employee.__module__)
# print("Employee.__bases__:", Employee.__bases__)
# print("Employee.__dict__:", Employee.__dict__)
