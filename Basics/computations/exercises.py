
#################################################################
## Home Assignment - 4 ##
## Name: type your name here
## Due Date: April 29 (Wednesday), 11.59 in Blackboard
## Type your answers in this python file and submit in blackboard.
#################################################################

###############
## Problem 1 ##
###############

# Given the string:
s = 'django'
print(s)

# Use indexing to print out the following:
# 'd'
print (s[0])

# 'o'
print (s[-1])

# 'djan'
print (s[0:4])

# 'jan'
print (s[1:4])

# 'go'
print (s[4:5])

# Bonus: Use indexing to reverse the string
print (s[-1:0])

#print(s.reverse())

###############
## Problem 2 ##
###############

# Given this nested list:
l = [3, 7, [1, 4, 'hello']]
# Reassign "hello" to be "goodbye"
l[2][2] = "goodbye"
print("l reassigned")
print(l)

###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key': 'hello'}
print(d1['simple_key'])

d2 = {'k1': {'k2': 'hello'}}
print(d2['k1']['k2'])

d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]

list_set = set()

for i in mylist:
    list_set.add(i)
print (list_set)

"""
#OR

new_set = set(mylist)
print(new_set)

"""

###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"

string = "Hello my dog's name is {name} and he is {age} years old".format(name=name, age=age)

string = "Hello my dog's name is {name} and he is {age} years old".format(name="Sammy", age=4)

print(string)

# Complete the tasks below by writing functions!

#####################
## -- PROBLEM 6 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.
"""
def arrayCheck(nums):
    # CODE GOES HERE
    check = [1,2,3]

    if for num in nums == for num in check:
        return True
    else:
        return False
"""
"""
def arrayCheck(nums):
    # CODE GOES HERE
    checks = [1,2,3]
    for num in nums:
    for check in checks:
    if num == check:
        return True
    else:
        return False
"""
"""
def arrayCheck(nums):
    # CODE GOES HERE
    check = [1,2,3]
    for num in nums:
        for i in check:
            if num == i:
                return True
            else:
                return False
"""

# arrayCheck([1, 1, 2, 3, 1]) #True
# arrayCheck([1, 1, 2, 4, 1]) #False
# arrayCheck([1, 1, 2, 1, 2, 3]) #True
    #####################
    ## -- PROBLEM 7 -- ##
    #####################

    # Given a string, return a new string made of every other character starting
    # with the first, so "Hello" yields "Hlo".

def stringBits(str):
  # CODE GOES HERE
  print(str[0::2])

# stringBits('Hello') #'Hlo'
# stringBits('Hi') #'H'
# stringBits('Heeololeo') #'Hello'

    #####################
    ## -- PROBLEM 8 -- ##
    #####################

    # Given two strings, return True if either of the strings appears at the very end
    # of the other string, ignoring upper/lower case differences (in other words, the
    # computation should not be "case sensitive").
    #
    # Note: s.lower() returns the lowercase version of a string.
def end_other(a, b):
  # CODE GOES HERE
  lower_a = a.lower()
  lower_b = b.lower()
  if lower_a[-3:] == lower_b[-3:]:
      return True
  else:
      return False

# end_other('Hiabc', 'abc') #True
# end_other('AbC', 'HiaBc') #True
# end_other('abc', 'abXabc') #True

    #####################
    ## -- PROBLEM 9 -- ##
    #####################

    # Given a string, return a string where for every char in the original,
    # there are two chars.

def doubleChar(str):
  # CODE GOES HERE
  new_str = " "
  for c in str:
      new_str = new_str + c + c
  print (new_str)


# doubleChar('The') #'TThhee'
# doubleChar('AAbb') #'AAAAbbbb'
# doubleChar('Hi-There') #'HHii--TThheerree'

    #####################
    ## -- PROBLEM 10 -- ##
    #####################

    # Read this problem statement carefully!

    # Given 3 int values, a b c, return their sum. However, if any of the values is a
    # teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
    # and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
    # takes in an int value and returns that value fixed for the teen rule.
    #
    # In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
    # Define the helper below and at the same indent level as the main no_teen_sum().
    # Again, you will have two functions for this problem!


def no_teen_sum(a, b, c):
  # CODE GOES HERE


def fix_teen(n):
  # CODE GOES HERE


# no_teen_sum(1, 2, 3) #6
# no_teen_sum(2, 13, 1) #3
# no_teen_sum(2, 1, 14) #3

    #####################
    ## -- PROBLEM 11 -- ##
    #####################

    # Return the number of even integers in the given array.

def count_evens(nums):
  # CODE GOES HERE
  number_of_even = 0
  for num in nums:
      if num % 2 == 0:
          number_of_even = number_of_even + 1
  #return number_of_even
  #using print to see the result in the console
  print (number_of_even)

#count_evens([2, 1, 2, 3, 4]) # 3
#count_evens([2, 2, 0]) # 3
#count_evens([1, 3, 5]) #0
