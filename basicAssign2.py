
#Write a python program to get a grade from the user. The program should output
#what their respective letter grade is.

user_input = input("Please enter a grade> ")
x = int(user_input)

if x > 100:
    print("Not a grade")
elif 80 <= x <= 100:
    print("Your grade is A")
elif 70 <= x <= 79:
    print("Your grade is B")
elif 60 <= x <= 69:
    print("Your grade is C")
elif 50 <= x <= 59:
    print("Your grade is D")
elif 0 <= x <= 49:
    print("Your grade is F")
else:
    print("No grade")
