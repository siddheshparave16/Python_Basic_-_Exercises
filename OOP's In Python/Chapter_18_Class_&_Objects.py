import builtins


"""
# User-defined class

class Employee:

    # creating class methods
    def set_data(self, emp_name, emp_age, emp_salary):
        self.name = emp_name
        self.age = emp_age
        self.salary = emp_salary

    def display_data(self):
        print(self.name, self.age, self.salary)


# creating class object
e1 = Employee()
e1.set_data('Ajay', 28, 15000)
e1.display_data()

e2 = Employee()
e2.set_data('Vinay', 24, 13000)
e2.display_data()

e2.age = 28

e2.display_data()

"""

"""

# Object Initialization


class Employee:

    # class Method to set data
    def set_data(self, emp_name, emp_age, emp_salary):
        self.__name = emp_name
        self.__age = emp_age
        self.__salary = emp_salary

    def display_data(self):
        print(self.__name, self.__age, self.__salary)

    def __init__(self, emp_name='', emp_age=0, emp_salary=0):
        self.__name = emp_name
        self.__age = emp_age
        self.__salary = emp_salary

    # def __del__(self):
    #     print('Deleting object' + str(self))


# creating class object using user defined methods
e1 = Employee()
e1.set_data('Suresh', 35, 12500)
e1.display_data()


# creating class object using special method
e2 = Employee('Amit', 27, 14000)
e2.display_data()


print(vars(Employee))
print(dir(Employee))


"""

"""
Que 1:- Write a class Number which maintain an Integer. It should have 
       following methods in it to perform various operation on the integer. 

# Answer starts here...

class Number:

    # set number into int
    def set_number(self, num):
        self.__number = num

    # return current value of Integer
    def get_number(self):
        return self.__number

    # print the int
    def print_number(self):
        print(self.__number)

    # check weather Integer is negative.
    def is_negative(self):
        if self.__number < 0:
            return True
        else:
            return False

    # check weather Integer is divisible by n
    def is_divisibleby(self, num):
        if num == 0:
            return False
        if self.__number % num == 0:
            return True
        else:
            return False

    # return Absolute value of Integer
    def absolute_value(self):
        if self.__number >= 0:
            return self.__number
        else:
            return abs(self.__number)


x = Number()
x.set_number(-2340)
x.get_number()
x.print_number()

# check number is negative or not
if x.is_negative():
    print(f'{x.get_number()} is Negative')
else:
    print(f'{x.get_number()} is Positive')

# check number is divisible or not.
if x.is_divisibleby(2):
    print(f'{x.get_number()} is divisible by {2}')
else:
    print(f'{x.get_number()} is Not divisible by {2}')

# absolute value
print(f'Absolute value of {x.get_number()} is {x.absolute_value()}')


"""


"""
Que 2:- Write a program to create a class called Fruit with attributes size and colour.
        Create multiple objects of this class. Report how many objects have been created from the class.
         
# Answer starts here...


class Fruit:
    # class variable for Instance Count
    count = 0

    def __init__(self, f_name, f_size, f_colour):
        self.__name = f_name
        self.__size = f_size
        self.__colour = f_colour
        Fruit.count += 1

    # class method for count Total created objects.
    @classmethod
    def display(cls):
        print(cls.count)


a = Fruit('Banana', 7, 'Yellow')
b = Fruit('Guava', 4, 'Peach')
c = Fruit('Apple', 10, 'Red')
d = Fruit('Berry', 5, 'red')

Fruit.display()

"""


"""
Que 3:- Write a program that determines whether two objects are of same type, weather their attributes
        are same and weather they are pointing to same object.
        
# Answer starts here...


class Complex:

    def __init__(self, r=0.0, i=0.0):
        self.__real = r
        self.__imag = i

    def __eq__(self, other):
        if self.__real == other.__real and self.__imag == other.__imag:
            return True
        else:
            False


c1 = Complex(1.1, 0.2)
c2 = Complex(2.1, 0.4)
c3 = c1

if type(c1) == type(c2):
    print('c1 and c2 are same type.')
else:
    print('c1 and c2 are different type')


if c1 == c2:
    print('Attributes of c1 and c2 are same')
else:
    print('Attributes of c1 and c2 are Different.')


if c1 is c3:
    print('c1 and c3 pointing same object')
else:
    print('c1 and c3 pointing different object')


"""


"""
Que 4:- Write a program to get a list of built-in functions.


print(dir(builtins))
print('\n')

print(vars(builtins))

"""


"""
Que 5:- Suppose we have defined two functions msg1 and msg2() in main module. What will be output of 
        var() and dir() on current module? How will you obtain the list of names which are present in both outputs.
        those which are unique to either list ?


def msg1():
    print('Wright brothers are responsible for 9/11 too')


def msg2():
    print('Cells divide to multiply')


d = vars()
l = dir()

print(sorted(d.keys()))
print(l)

print(d.keys() - l)
print(l - d.keys())

"""


"""
Que 6:- Is there any difference in the values returned by the functions dir() and vars(..).keys()?
        If yes, write a program to obtain that difference?
        
"""

s = set(dir(list)).difference(vars(list).keys())

print(s)


class Message:
    def display(self, msg):
        pass

    def show(msg):
        pass





















