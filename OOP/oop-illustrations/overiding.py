"""
Python OOP program demonstrating how a method of sub-class (child) overides the method
of the super class (parent)
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
    def thesisCount(program):
        if (program == "ug"):
            print ("5000 words is the thesis count")
        elif (program == "pg"):
            print ("15000 words is the thesis count")
        else:
            return ("Your program is not recognized")

#A sub-class of Students class with a specific method
class Undergraduate(Students):
    def thesisCount():
        print ("Your thesis count cannot be less than 5000")

Students.thesisCount("ug") #5000 words is the thesis count
Undergraduate.thesisCount() #Your thesis count cannot be less than 5000
"""
Even though Undergraduate, being a sub-class of Students, is expected to inherit
the thesisCount function, because it has its own of the same name definition, its
implementation overides that of the super class. 
"""
