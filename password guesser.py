import numbers
import random


numbers = int(input("enter your 4 digit pin"))
guess = 0
while( guess != numbers):
    guess = random.randint(0,9999)
    print(guess)


print(" Your pin is " + str(guess))    
