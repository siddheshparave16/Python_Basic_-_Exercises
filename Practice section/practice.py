import datetime
import os.path
import pathlib
from distutils.command.build_ext import extension_name_re
from math import pi



"""
# Write a Python program to display the current date and time.
current_time = datetime.datetime.now()
print(current_time.strftime("%Y-%m-%d %H:%M:%S"))



# Que2:- Write a Python program that calculates the area of a circle based on the radius entered by the user.
radius = float(input("Enter a radius of circle : "))

area_of_circle = 2*pi*radius

print(f"Area of circle is {area_of_circle:.2f}")



# Que 3:- Write a Python program that accepts the user's first and last name and prints them
#         in reverse order with a space between them.


first_name, last_name = input("Enter Your First and Last name separated by space :- ").strip().split()
print(f"Your First name is '{first_name}'.")
print(f"Your Last name is '{last_name}'.")
f_name = last_name + " " + first_name
full_name = last_name[::-1] + " " + first_name[::-1]
print(f_name)
print(full_name)



# Que 6:- Write a Python program that accepts a sequence of comma-separated numbers from the user
#         and generates a list and a tuple of those numbers.

numbers = input("Enter a numbers separated by comma: ").split(",")
print(numbers)      # this will get list as output- ['1', ' 2', ' 3']
print(tuple(numbers))



# Que 7:- Write a Python program that accepts a filename from the user and prints the extension of the file.

file_name_input = input("Enter a file name so we can fetch extension of file :- ")

file_extension = file_name_input.split('.')
print(file_extension)
print("The Extension of file is : " + repr(file_extension[-1]))

print(os.path.splitext(file_name_input)[1])
print(pathlib.Path(file_name_input).suffix)


# Que8 :- Write a Python program to display the first and last colors from the following list.
color_list = ["Red", "Green", "White", "Black"]

print(f"first colour : {color_list[0]}")
print(f"first colour : {color_list[-1]}")

"""

# Que 9:- Write a Python program to display the examination schedule. (extract the date from exam_st_date).

exam_st_date = (11, 12, 2014)
print("The examination will start from : %i / %i / %i" % exam_st_date)






