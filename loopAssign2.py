
#Write a python program that will ask the user for a number n, and output the sum of the 
#first n terms of the following infinite series: 1 + 1/2 + 1/3 + ... + 1/n 

#Get string from user
user_input = input("Enter a number: ")
x = int(user_input)
sum = 0

for i in range(1,x+1):

    num1 = float(1 / i)
    sum = sum + num1

print(sum)
