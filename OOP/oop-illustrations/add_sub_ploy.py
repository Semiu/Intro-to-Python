"""
Created on Jun 22, 2017

@author: SummitWorks
"""


# operator overloading

class Vector:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return repr(self.data)

    def __add__(self, other): # __mul__, __div__
        data = []
        for j in range(len(self.data)):
            data.append(self.data[j] + other.data[j])
        return Vector(data)

    def __sub__(self, other):
        data = []
        for j in range(len(self.data)):
            data.append(self.data[j] - other.data[j])
        return Vector(data)


x = Vector([1, 2, 3])
y = Vector([3, 0, 2])

print(x + y)  # operator overloading
print(x-y)
# print(2 + 4)

#
# print(x.__str__())
# print(x.__repr__())