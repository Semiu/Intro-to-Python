"""
Python OOP program demonstrating how object of a sub-class (child) inherits methods of
the super class (parent)
"""
#The super class with two different methods asides from the __init__ method
class Students:
    def __init__(self, name, program, course, funding):
        self.name = name
        self.program = program
        self.course = course
        self.funding = funding
    def fundingStatus(program):
        if (program == "ug"):
            print ("False")
        elif (program == "pg"):
            print ("True")
        else:
            return ("Your program is not recognized")
    def showName(name):
        print ("My name is " + name)

#A sub-class of Students class with a specific method
class Undergraduate(Students):
    def thesisCount():
        print ("5000 words is the thesis count")

#Another sub-class of the Students class with its method
class Postgraduate(Students):
    def thesisCount():
        print ("15000 words is the thesis count")

#Create an instance of the super class
student1 = Students("Sem Cole", "pg", "Software Engineering", "True")
print(student1.name) #Sem Cole
Undergraduate.showName("Kale Zenith") #My name is Kale Zenith
Undergraduate.thesisCount() #5000 words is the thesis count
Postgraduate.thesisCount() #15000 words is the thesis count
"""
In line 34, the name assigned to the object student1 of the super class is printed
In line 35, showName function which was not specifically defined for Undergraduate class was inherited
In lines 36 and 37, the thesisCount methods, even though they are of the same name, specifically implements
their respective definitions
"""
