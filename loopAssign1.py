

#Write a python program that will grab a string from the user and output the string in reverse.

#Get string from the user
str = input("Please enter a string: ")

for index in range(len(str)-1, -1, -1):
    print(str[index], end='')
print("\n")
