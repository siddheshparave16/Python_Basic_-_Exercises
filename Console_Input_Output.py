"""
# General form of input() function
s = input('prompt')


# receive a full_name
name = input('Enter Your Full Name :- ')


# input can use to receive one or more value
# separate a first name , middle name and Last name
f_name, m_name, l_name = input('Enter Your Full Name :- ').split()
print(f_name)
print(m_name)
print(l_name)


# if we are to received multiple integer value , we received them as a string and convert them to ints.
n1, n2, n3 = input("Enter three Integer Values : ").split()
n1, n2, n3 = int(n1), int(n2), int(n3)
print(n1+10, n2+20, n3+30)


# this thing can be comprehension also
n1, n2, n3 = [int(n) for n in input("Enter three Integer Values : ").split()]
print(n1+10, n2+20, n3+30)


# input can be used to received arbitrary number of values
number = [int(x) for x in input("Enter values followed by space :- ").split()]

# iterating list
for n in number:
    print(n+10, end=',')


# input can be used to receive different type of values at a time.

data = input('Enter Name, Age, Salary : ').split()
name = data[0]
age = int(data[1])
salary = float(data[2])

print(name, age, salary)

"""
import builtins
import math
import sys

"""
# Console Output
# Built-in function print is used to send output on screen.


# print function has this form
print(object, sep=' ', end='\n', file=sys.stdout, flush=False)
a, b, c = 1, 2, 3
print(a, b, c, sep=',', end='!')            # after each value , and ! at end

print()

x, y = 4, 5
print(x, y, sep='...', end='#')


# Formatted Printing

# 1. Using formatted string literals. ( often called fstrings )
r, l, b = 1.52, 10.5, 12.66
print(f'Length = {l} , Breadth = {b}, radius = {r}')


name = 'Sushant Ajay Raje'
for n in name.split():
    print(f'{n:10}')


# 2. Using format() method of string object :
r, l, b = 1.5678, 10.5, 12.66
name, salary, age = 'Jay', 22, 15000

# print in order by position of variables using empty{}
print('radius = {}, length = {}, breadth = {}'.format(r, l, b))
print('name = {}, salary = {}, age = {}'.format(name, salary, age))

# prin in any desire format
print('breadth = {2}, radius = {1}, length = {2}'.format(r, l, b))


# print name in 15 columns and salary in 10 columns
print('name = {0:15}, salary={0:10}'.format(name, salary))

# print radius in 10 columns , with 2 digit after decimal point
print('radius = {0:10.2f}'.format(r))


"""

"""
Que 1:- Write a program to receive radius of a circle and length and breadth of rectangular in one call to input(), 
        calculate and print circumference of circle and perimeter of rectangle

Answer starts here...


# take input for radius, length and breadth
r, l, b = input("Enter value for radius of circle, Length and breadth of Rectangle followed by space :- ").split()
r, l, b = int(r), int(l), int(b)

# circumference_of_circle
circumference = 2*3.14*r

# perimeter of rectangle
perimeter = 2*(l + b)

print(f'circumference of circle is {circumference}')
print(f'Perimeter of Rectangle is {perimeter}')

"""

"""
Que 2:- Write a program to receive 3 integer using one call to input(). The three integer specify starting value ,
        ending value and step for a range.The program should use these values to print the number , its square and
        its cube, all property right-aligned. also output the same value left-aligned


start, end, step = input('Enter start, end, step value: ').split()
# conversion of string to Integer
start, end, step = int(start), int(end), int(step)

# right-aligned printing
for i in range(start, end, step):
    print(f'{i:>5}{i**2:>7}{i**3:>8}')

print()

# left-aligned printing
for n in range(start, end, step):
    print('{0:<5}{1:<7}{2:<8}'.format(n, n*n, n*n*n))

"""

"""
Que 3:- Write a program to maintain names and cell number of 4 persons and
        then print them systematically in a tabular form.

# Note :- Passing an integer after the ':' will cause that field to be a minimum number of characters wide. 
          This is useful for making columns line up.
# Answer starts here.. 

contacts = {'Dilip': 9823077892, 'Shekhar': 6784512345,
             'Vivek': 9823011245, 'Riddhi': 97666556779}

for name, cell_no in contacts.items():
    print(f'{name:15}{cell_no:10d}')

"""

"""
Que 4:- Suppose there are 5 variables in a program-- max, min, mean, sd and var, having some suitable value
        Write a program to print these variable property aligned using multiple fstrings, but one call to print().

# Answer starts here..

min, max = 25, 75
mean = 35
sd = 0.56
var = 0.9

# one call print with multiple fstrings
print(
    f'\n{"Max Value:":<15}{max:>10}'
    f'\n{"Min Value:":<15}{min:>10}'
    f'\n{"Mean Value:":<15}{mean:>10}'
    f'\n{"SD Value:":<15}{sd:>10}'
    f'\n{"Var Value:":<15}{var:>10}'
)


"""

"""
Que 5:- Write a program to print square root, cube root of numbers from 1, 10. up to 3 decimal places, 
        Ensure that the output is displayed in separate lines, with number center-justified
        and square and cube roots, right-justified.
        
# for answer starts here 
# for center-justified use ^        
"""

for n in range(1, 11):
    s = round(math.sqrt(n), 3)
    c = round(math.pow(n, 1/3), 3)
    print(f'{n:^5}{s:10}{c:10}')


