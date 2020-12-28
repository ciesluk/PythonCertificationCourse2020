

#Write a python program that will ask the user to guess a number from 1-9. Then
#generate a random number and tell the user if they guessed correct.

import random

user_input = input("Please enter a number")
x = int(user_input)

#Generate random number called variable "rand" 
rand = random.randint(1,9)

if x == rand:
    print("Correct, your guess is right!")
else:
    print("Incorrect. The correct number is %d" % rand)
