

#Write a python program that takes in a 3 digit number from the user and adds all the digits.

user_input = input("Please enter three digits and I will add them up> ")
x = int(user_input)

y = x % 10 #add
a = int(x / 10)
z = a % 10 #add
b = int(x / 100)
sum = y + z + b
print("The sum is: %d " % sum)
