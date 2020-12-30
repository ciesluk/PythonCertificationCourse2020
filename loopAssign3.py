
#Write a python program that will get a string from the user. 
#The program should output the string and remove extra spaces between each word.

import re

str = input("Please enter a string with spaces: ")
new_str = re.sub(' +', ' ', str)

print(new_str)


