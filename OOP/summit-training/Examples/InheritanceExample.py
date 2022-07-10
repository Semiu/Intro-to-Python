"""
Created on Jun 22, 2017

@author: SummitWorks
"""
# class object():
#
# class Person(object):
#     def __init__(self):
#         self.name = 'name'
#         self.cell = '123456789'
#
#     def changeCell(self, newCell):
#         self.cell = newCell
#
#
# class Employee(Person):
#     def __init__(self):
#         # self.person = Person()
#         self.name = ' Child name'
#         # self.cell = ''
#         self.changeCell()



class Animal(object): # local
    def __init__(self):
        super().__init__()
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal): # local
    def __init__(self):
        super().__init__() # base + some more
        print("Dog created")

    # overriding
    def whoAmI(self): # all different, parent has implemented + add more steps
        print("Dog")

    def bark(self): # in addition to what I inherit
        print("Woof!")


class Pet(Animal):
    def __init__(self):
        print("Pet created")

    # overriding len(),
    def whoAmI(self): # all different, parent has implemented + add more steps
        print("Pet")


class Lab(Pet,Dog): # MRO
    def __init__(self):
        print("Lab created")


l = Lab()
l.whoAmI()
print(Lab.mro())
print(Lab.__mro__)


# # a = Animal()
# # a.whoAmI()
# d = Dog() # __init__
# # d.bark()
# # d.whoAmI()
# # d.eat()
# # # #
# d = Dog()
# d.eat()
# d.whoAmI()
# # d.bark()
# print(issubclass(Dog, Animal))



# int add(int n1,int n2)  # (positional, *args, **kwagrs)
# add(str s1,str s2')
# add(1.2.3.4.5.)
#
#  add(1,2()))