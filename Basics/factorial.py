#A Python program that takes an integer and calculates its factorial.
#For example, factorial of 4 is 1*2*3*4

number = input("Enter an integer: ") #An input is taken from the user

integer = int(number) #The input function takes string type. This has to be cast to  integer to work for the factorial function

#The implementation of the factorial function
def factorial(integer):
    factorial = 1 #initialize to 1
    for i in range(1, integer + 1): #A for loop that assigns the value of all the numbers between 1 and the integer to i
        factorial = factorial * i
    print ("The factorial of " + number + " is " + str(factorial))

factorial(integer) #Calling the factorial function
