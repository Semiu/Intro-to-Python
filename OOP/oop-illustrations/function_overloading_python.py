"""
Created on Aug 4, 2017

@author: SummitWorks
"""

# __dir__={'add':<function ... >,'add1':<}
class Test:
    def myaddition(self, instanceOf, *args):  # really not overloaded. (){}
        if instanceOf == 'int':
            result = 0
        if instanceOf == 'str':
            result = ''
        for i in args:
            result = result + i
        return result


t1 = Test()
print(t1.myaddition('int', 3, 4, 5,6,8,9,10))  # if f name is same and diff parameters.
print(t1.myaddition('str', 'I', ' am', ' in', ' Python'))


# len([])
