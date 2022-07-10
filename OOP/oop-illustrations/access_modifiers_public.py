"""
Created on Aug 2, 2017

@author: SummitWorks
"""


class Cup:
    def __init__(self):
        self.color = None
        self.content = None

    def fill(self, beverage):
        self.content = beverage

    def empty(self):
        self.content = None

    def getColor(self): # getter
        return self.color

    def setColor(self,c): # setter
        self.color = c
    # @property
    # def color(self,c):
    #     self.color = c

redCup = Cup()
redCup.color = "red"
print(redCup.getColor())
# print(redCup.color)
# redCup.setColor("Blue")
# redCup.content = "tea"
# print(redCup.content)
#
# redCup.empty()
# print(redCup.content)
#
# redCup.fill("coffee")
# print(redCup.color)
# print(redCup.content)  # All of this is good and acceptable, because all the attributes and methods are public.
