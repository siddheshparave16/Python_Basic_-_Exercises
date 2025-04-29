
"""
# How to use try-except ?

try:
    a = int(input('Enter an Integer: '))
    b = int(input('Enter an Integer: '))
    c = a/b
    print('c=', c)

except ZeroDivisionError as zde:
    print('Denominator is 0.')
    print(zde.args)
    print(zde)

except ValueError:
    print('Unable to convert string to int.')
except:
    print('Some unknown error.')

"""
import random

from sqlalchemy import except_

"""

# User defined exceptions
class InsufficientBalanceError(Exception):
    def __init__(self, accno, cb):
        self.__accno = accno
        self.__curbal = cb

    def get_details(self):
        return {'Acc no': self.__accno, 'Current Balance': self.__curbal}



class Customers:
    def __init__(self):
        # creating an empty diction to store Customers Details.
        self.__dct = {}

    def append(self, accno, customer_name, bal):
        self.__dct[accno] = {'Name': customer_name, 'Balance': bal}

    def deposite(self, accno, amont):
        d = self.__dct[accno]
        d['Balance'] = d['Balance'] + amont
        self.__dct[accno] = d

    def display(self):
        for k, v in self.__dct.items():
            print(k, v)
        print()

    def withdraw(self, accno, amt):
        d = self.__dct[accno]
        curbal = d['Balance']

        if curbal < 5000:
            raise InsufficientBalanceError(accno, curbal)
        else:
            d['Balance'] = d['Balance'] - amt
            self.__dct[accno] = d


c = Customers()

c.append(103, 'Jay', 2510)
c.append(120, 'Jay', 24030)
c.append(102, 'Jay', 50420)
c.append(142, 'Jay', 1423)
c.append(174, 'Jay', 5001)

c.display()

c.deposite(103, 2000)
c.deposite(174, 15200)
c.display()

try:
    c.withdraw(103, 4000)
    print('Amount Withdraw Successfully')
    c.display()

except InsufficientBalanceError as ibe:
    print('Withdrawal Denied')
    print('Insufficient Balance')
    print(ibe.get_details())


"""

"""
# else block

try:
    lst = [10, 20, 30, 'abc', 50]
    for num in lst:
        i = int(num)
        j = i*i
        print(i, j)
except NameError:
    print(NameError.args)
except ValueError:
    print('Cannot convert string to int')
else:
    print('Total Number processed', len(lst))
    del(lst)


"""


"""
Que 1:- Write a program that infinitely receives positive integer as input and prints its square.
        If a negative number is entered then raise an exceptions. display a relevant error message 
        and make a graceful exit.

# Answer starts here..


try:
    while True:
        num = int(input('Enter a num positive Integer number: '))

        if num > 0:
            sqr = num * num
            print(f'"Number: "{num}, "Numbers Square: "{sqr}')

        else:
            raise ValueError('Negative Number')

except ValueError as ve:
    print(ve.args)


"""


"""
Que 2: Write a program that implements a stack data structure of specified size. 
       If the stack becomes full and we still try to push an elements to it, then an IndexError exception should
       be raised. Similarly, if the stack is empty and try to pop an element from it then an IndexError 
       exception should be raised. 



class Stack:
    def __init__(self, arr_size):
        self.size = arr_size
        self.arr = []
        self.top = -1

    def push(self, num):
        if len(self.arr) == self.size:
            raise IndexError('Stack is Full')
        else:
            self.arr.append(num)
            self.top += 1

    def pop(self):
        if self.top == -1:
            raise IndexError("Stack is Empty")
        else:
            self.top -= 1
            return self.arr.pop()

    def printall(self):
        print(self.arr)


s = Stack(5)
try:
    s.push(10)
    s.push(12)
    s.push(15)
    a = s.pop()
    print(a)
    s.printall()

except IndexError as ie:
    print(ie)

s = Stack(5)
try:
    s.push(10)
    s.push(15)
    s.push(12)
    s.push(11)
    s.push(7)
    s.push(9)
    s.push(9)
    s.push(9)
    s.push(9)
except IndexError as ie:
    print(ie)

s.printall()


"""


"""
Que 4:- Write a program that receives an integer as input. If a string is entered Instead of an integer.
        then report an error and give another chance to user to enter an Integer. Continue this process till 
        correct input is supplied.


total_chance = 3
while True:
    if total_chance >0:
        try:
            num = int(input('Enter a Integer Number: '))
            break
        except ValueError:
            print('Incorrect input.')
            total_chance -= 1
            print('Your total chances for input left', total_chance)
    else:
        print('Your input chances over..')
        break

"""


"""
Que 4:- finally block mechanism -

file = None
try:
    file = open("example.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found!")
finally:

    if file:
        file.close()  # Ensures the file is closed no matter what
    print("This will always execute")


"""


"""
Que 5- how does nested exception handling works in python.



try:
    print("Outer try block")
    try:
        print("Inner try block")
        result = 10 / 0  # This raises ZeroDivisionError
    except ZeroDivisionError:
        print("Handled ZeroDivisionError in the inner block")
    finally:
        print("Inner finally block")
    result = int("abc")  # This raises ValueError
except ValueError:
    print("Handled ValueError in the outer block")
finally:
    print("Outer finally block")


"""


"""
Que 6:- Write a program that receives 10 integers and stores them and their cubes in dictionary. 
        if the number entered is less than 3, raise a user-defined exception NumberTooSmall, and
        if the number entered is more than 30, then raise a user-defined exception NumberTooBig. 
        Whether an exception occurs or not, at the end print the contents of the dictionary.

"""


class NumberTooSmall(Exception):
    def __init__(self, num):
        self.__number = num

    def get_message(self):
        return self.__number


class NumberTooBig(Exception):
    def __init__(self, num):
        self.__number = num

    def get_message(self):
        return f" Number {self.__number} is to small."


# user input to
user_input = int(input('Enter a Integer number: '))

try:
    if user_input > 3:
        # Initializing empty dictionary.
        numbers_dct = {}

        # storing number and their cube in dictionary.
        numbers_dct[user_input] = user_input**3
        print(numbers_dct)
except:
    raise NumberTooSmall




































