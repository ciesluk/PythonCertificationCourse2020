

#Write a python program that takes in a floating point temperature from the user in
#celsius and converts it to fahrenheit (Reminder: to convert from celsius to fahren- heit,
#multiply by 95, and add 32)

user_input = input("Please enter a temperature in celsius.")
x = float(user_input)

print("Converting to fahrenheit...")

#Converting from celsius to fahrenheit
f = x * 1.8 + 32

#Print the temperature in fahrenheit to the user
print("The temperature in fahrenheit is: %f" % f)
print("%fC = %fF" % (x,f))
