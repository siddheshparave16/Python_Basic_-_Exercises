import math
"""
Que 1 :- Any integer is input through the keyboard .
        write a program to find out whether it is an odd number or even number .

# Answer starts here ...


number = int(input("Enter a number : \n"))
if number == 0:
    print(f"Given Number {number} is neither Odd Number nor Even number")
elif number % 2 == 0:
    print(f"Given Number {number} is Even Number")
else:
    print(f"Given Number {number} is odd Number")


"""


"""
Que 2 :- Any year is input through keyboard. write a program to determine whether the year is a leap year or not.


year = int(input("Enter a year : \n"))

# year divisible by 400 and 100 a leap year

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f" Year {year} a Leap Year.")
        else:
            print(f" Year {year} is not Leap Year.")
    else:
        print(f" Year {year} Leap Year.")
else:
    print(f" Year {year} not a Leap Year.")

"""

"""
Que c) if ages of ram , shyam and Ajay are input through the keyboard , write a program to determine youngest of three.

# answer starts here ...

ram_age = int(input("Enter Ram's age : \n"))
shyam_age = int(input("Enter Shyam's age : \n"))
ajay_age = int(input("Enter Ajay's age : \n"))


if ram_age < shyam_age and ram_age < ajay_age:
    print("Ram is Youngest.")
elif shyam_age < ram_age and shyam_age < ajay_age:
    print("Shyam is Youngest")
elif ajay_age < ram_age and ajay_age < shyam_age:
    print("Ajay is Youngest")
elif ram_age == shyam_age and ram_age < ajay_age:
    print("Ram and Shyam are the youngest.")
elif ram_age == ajay_age and ram_age < shyam_age:
    print("Ram and Ajay are the youngest.")
elif shyam_age == ajay_age and shyam_age < ram_age:
    print("Shyam and Ajay are the youngest.")
else:
    print("They are Equal ages")


"""

"""
Que d) write a program to check whether a triangle is valid or not, 
   when the three angles of triangle enter through keyboard. 
   A triangle is valid if the sum of all the three angles is equal angles is equal to 180 degrees.

Answer starts here

f_angle = int(input("Enter First angle of triangle :- \n"))
s_angle = int(input("Enter Second angle of triangle :- \n"))
t_angle = int(input("Enter Third angle of triangle :- \n"))

# let sum of three angles of triangle
sum_of_angles = f_angle + s_angle + t_angle

# check triangle is valid or not
if sum_of_angles == 180 and f_angle > 0 and s_angle > 0 and t_angle > 0:
    print("Triangle is Valid. ")
else:
    print("Triangle is not valid.")


"""

"""
Que e) write a program to find the absolute value of a number entered through the keyboard.

# Answer starts here...


try:
    # Input the number
    number = float(input("Enter a number :- \n"))

    # Calculate the absolute value
    # first way
    # absolute_value = abs(number)

    # Second way (Calculate the absolute value using if-else )
    if number < 0:
        absolute_value = -number
    else:
        absolute_value = number

    print(f"Absolute value of {number} is ", absolute_value)

except ValueError:
    print("Invalid input! Please enter a valid number.")


"""


"""
Que f:- Given the length and breadth of a rectangle, write a program to find 
    whether the area of the rectangle is greater than its perimeter. For example, 
    the area of the rectangle with length=5 and breadth=4 is greater than its perimeter.

try:
    # take input of length and breadth of rectangle
    length = float(input("Enter a Length of Rectangle :- \n"))
    breadth = float(input("Enter a breadth of Rectangle :- \n"))

    # let check if length and breadth must be positive
    if length > 0 and breadth > 0:

        area_of_rectangle = length*breadth
        perimeter_of_rectangle = 2 * (length + breadth)

        # let check area of Rectangle is greater then perimeter

        print(f"Area of Rectangle is {area_of_rectangle}")
        print(f"Perimeter of Rectangle is {perimeter_of_rectangle}")

        #  # Compare area and perimeter
        if area_of_rectangle > perimeter_of_rectangle:
            print("Area of Rectangle is greater then Perimeter of Rectangle")
        else:
            print("Perimeter of Rectangle is greater then Area of Rectangle")

    else:
        print("Length and Breadth must be positive numbers.")

except ValueError:
    print("Invalid input! Please enter a valid number.")

"""

"""
Que g:- Given three points (x1,y1), (x2,y2)and(x3,y3), 
        write a program to check if all the three points fall on one straight line.
        
# Answer starts here..

# let take input of points
x1 = float(input("Enter x1 : "))
y1 = float(input("Enter y1 : "))
x2 = float(input("Enter x2 : "))
y2 = float(input("Enter y2 : "))
x3 = float(input("Enter x3 : "))
y3 = float(input("Enter y3 : "))

# Calculate the determinant
determinant = x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)

# Check if the determinant is zero
if determinant == 0:
    print(f"The Given points {x1,y1} , {x2,y2}, {x3,y3} are Collinear and they fall on one straight line.")
else:
    print(f"The Given points {x1,y1} , {x2,y2}, {x3,y3} are Not Collinear and they not fall on one straight line.")

"""

"""
Que H :- Given the coordinates (x,y) of center of a circle and its radius, 
        write a program that will determine whether a point lies inside the circle, 
        on the circle or outside the circle. (Hint: Use sqrt () function)

# Given co-ordinate of center of circle and radius

x_c = 0
y_c = 0
radius = 6

# take input of point with co-ordinate (x,y)
x_p = float(input("Enter X co-ordinate of Point : "))
y_p = float(input("Enter Y co-ordinate of Point : "))

# let check distance of point from center of circle
distance = math.sqrt((x_p - x_c)**2 + (y_p-y_c)**2)
print(f"Distance from center: {distance}")

# Determine the location of the point
if distance < radius:
    print(f"The point {x_p, y_p} lies inside the circle")
elif distance == radius:
    print(f"The point {x_p, y_p} lies on the circle")
else:
    print(f"The point {x_p, y_p} lies out the circle")

"""

"""
Que i) Given a point (x,y) , write a program to find out
       if it lies on the X- axis Y-axis, on the origin or in one of the four quadrants.


try:
    # user input for x co-ordinate and y co-ordinate of circle
    x = float(input("Enter X co-ordinate of point : "))
    y = float(input("Enter Y co-ordinate of point : "))

    print(f"The point is {x,y}")

    # check point lies on which Quadrants

    if (x > 0 and y > 0):
        print(f"Point {x,y} lies in First Quadrants")
    elif x > 0 and y < 0:
        print(f"Point {x,y} lies in Fourth  Quadrants")
    elif x < 0 and y < 0:
        print(f"Point {x, y} lies in Third Quadrants")
    elif x < 0 and y > 0:
        print(f"Point {x, y} lies in Second Quadrants")
    elif x == 0:
        print(f"Point ({x}, {y}) lies on the Y-axis.")
    elif y == 0:
        print(f"Point ({x}, {y}) lies on the X-axis.")
    else:
        print(f"Point {x, y} lies in Center")

except ValueError:
    print("Inter valid Input as a Integer")


"""

"""
Que j) A year is entered through the keyboard, write a program 
       to determine whether the year is leap or not. Use the logical operators and or. 

# answer starts here..

year = int(input("Enter a year "))
leap_year = (year % 4 == 0) or (year % 100 == 0 and year % 400 == 0) or "Not"
print(f"Year is {leap_year} Leap Year")

"""

"""
k) If the three side of a triangle are entered through the keyboard, 
   write a program to check whether the triangle is valid or not. 
   The triangle is valid if the sum of two sides is greater than the largest of the three sides.

# Answer starts here...



# take input of 3 sides of triangle in cm
a = float(input("Enter First side of Triangle :- "))
b = float(input("Enter Second side of Triangle :- "))
c = float(input("Enter Third side of Triangle :- "))

# check valid triangle

if a + b > c and a + c > b and b + c > a:
    print(f" The given side of Triangle a :{a}, b :{b} and c :{c} is Valid Triangle ")
else:
    print(f" The given side of Triangle a :{a}, b :{b} and c :{c} is Not Valid Triangle ")

"""

"""
Que l) If the three side of a triangle are entered through the keyboard,
       write a program to check whether the triangle is isosceles, equilateral ,scalene or right-angled triangle.

# Answer starts here...
       
"""


# take input of 3 sides of triangle in cm
a = float(input("Enter First side of Triangle :- "))
b = float(input("Enter Second side of Triangle :- "))
c = float(input("Enter Third side of Triangle :- "))

# let check Triangle is valid or not
if a + b > c and a + c > b and b + c > a:
    print(f" The given side of Triangle a :{a}, b :{b} and c :{c} is Valid Triangle ")

    # check for equilateral (all its sides equal in length.)
    if a == b == c:
        print("Triangle is Equilateral.")

    # check for isosceles ( two side of equal length )
    elif a == b or b == c or c == a:
        print("Triangle is Isosceles")

    # Independent check for right-angled
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print("Triangle is right-angled triangle")

    # check for scalene
    if a != b and b != c and c != a:
        print("Triangle is Scalene.")
else:
    print(f" The given side of Triangle a :{a}, b :{b} and c :{c} is Not Valid Triangle ")

