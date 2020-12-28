

#Write a program that will accept the x and y coordinates of two points on a line. Then take
#in another coordinate and test whether it’s on the line or not. Remember, the equation of a
#line is y = mx+b (or equivalently b = y−mx) and slope is m = (y2 − y1)/(x2 − x1).

user_input = input("Enter the x coordinate of the first point: ")
x1 = int(user_input)

user_input2 = input("Enter the y coordinate of the first point: ")
y1 = int(user_input2)

user_input3 = input("Enter the x coordinate of the second point: ")
x2 = int(user_input3)

user_input4 = input("Enter the y coordinate of the second point: ")
y2 = int(user_input4)

m = float((y2 - y1) / (x2 - x1))

b = float(y1 - m * x1)

new_point = input("Enter the x coordinate of the new point: ")
x3 = int(new_point)

new_point2 = input("Enter the y coordinate of the new point: ")
y3 = int(new_point2)

right_side = m * x3 + b

if right_side == y3:
    print("The point (%d,%d) is on the line y = %fx+%f" % (x3, y3, m, b))
else:
    print("The point (%d,%d) is NOT on the line y = %fx+%f" % (x3, y3, m, b))
