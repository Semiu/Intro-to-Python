"""
Created on Jun 22, 2017

@author: SummitWorks
"""


class Car: # __private _protected
    __maxspeed = 0 # Class
    _name = "" # class

    def __init__(self):
        self.__maxspeed = 200
        self._name = "Supercar"

    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))

    def getmaxspeed(self):
        return self.__maxspeed

    def setmaxspeed(self,i):
        self.__maxspeed = i

redcar = Car()
redcar.drive()
# print(Car.__maxspeed) #
print(Car._name) # name mangling , __init__
#
# redcar.setmaxspeed = 10  # will not change variable because its private
# redcar.drive()
# redcar._name = 'NewRedCar'
# print(redcar._name)


