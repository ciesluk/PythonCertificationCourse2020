
#Write a python program that gets numbers from the user until they enter zero, then tells the user the average 
#of all the numbers, the largest number entered, and the smallest number entered.
sum = 0
counter = 0
max = 0
min = 0

while True:
    condition = input("Please enter numbers to find average, max and min: ")
    if condition == '0':
        break
    x = int(condition)
    sum = sum + x
    counter = counter + 1
    total = float(sum / counter)
    
    if max == 0 or min == 0:
        max = x
        min = x
    elif max <= x:
        max = x
    elif min >= x:
        min = x
    
print("Average = %f" % total)
print("Max = %d" % max)
print("Min = %d" % min)
