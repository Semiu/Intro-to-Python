#####
# A computer game that think of 3 digit number  of no repeating digits
#The user guesses the number and the computer gives clue.
#The user guesses again based on this clue till the code is broken with a match.
####
import random

while(True):

    user_guess = int(input("Guess a three digit number: "))
    computer_digit = random.randint(100,999)

    if user_guess == computer_digit:
        print ("You got it!")
        break
    elif user_guess > computer_digit:
        print("Your guess is more than the digits")
        continue
    elif user_guess < computer_digit:
        print("Your guess is less than the digits")
        continue
