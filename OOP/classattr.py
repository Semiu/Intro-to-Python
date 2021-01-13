#Initializing class attributes
class Students:
    def __init__(self, name, age, level):
        #each of the parameters is passed as attributes for objects of the class
        self.name = name
        self.age = age
        self.level = level

#Creating an object as an instance of the class with values assigned
student1 = Students("Semiu Akanmu", 37, 700)

print (student1.name) #Semiu Akanmu
print (student1.age) #37
print (student1.level) #700

try:
    print (student1.hobby)
except:
    print ("Error because hobby was not initialized as an attribute for Students class")
    #Error because hobby was not initialized as an attribute for Students class
    #The try and except bloc is to handle the error that would be generated
    #in the try bloc. 

#Checking if an object of a class has an attribute
student2 = Students("Habeeb Akanmu", 12, 50)
print(hasattr(student2, "age")) #True
print(hasattr(student2, "hobby")) #False

#Setting an attributes
setattr(student2, 'hobby', "Reading")
print(hasattr(student2, "hobby")) #True
print(hasattr(student1, "hobby")) #False. Because the setattr is specifically for the student2.
                            #This is useful with objects of the same class differ in the list of their attributes.

#Getting attribute - getter
print(getattr(student2, "hobby")) #Reading
