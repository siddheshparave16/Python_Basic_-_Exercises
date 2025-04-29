import math
import random
import sys

"""
# zip() function:-
- receive multiple Iterable objects and return iterator of tuple based on them.



words = ['And', 'Coddle', 'Called', 'Molly']
numbers = [10, 20, 30, 40]

for ele in zip(words, numbers):
    print(ele[0], ele[1])

print('\n')

for ele in zip(words, numbers):
    print(*ele)

print('\n')

for w, n in zip(words, numbers):
    print(w, n)

print('\n')

words = ['And', 'Coddle', 'Called', 'Molly']
numbers = [10, 20, 30, 40, 50, 60]

for w, n in zip(words, numbers):
    print(w, n)



# list/tuple/set can be generated from the iterator of tuples return by zip().

words = ['And', 'Coddle', 'Called', 'Molly']
numbers = [10, 20, 30, 40]

ele = zip(words, numbers)
lst = list(ele)
print(lst)


# Necessary to zip again
ele = zip(words, numbers)
tpl = tuple(ele)
print(tpl)

# Necessary to zip again
ele = zip(words, numbers)
s = set(ele)
print(s)


# Values can be unzipped from the list into tuple using *.
words = ['And', 'Coddle', 'Called', 'Molly']
numbers = [10, 20, 30, 40]

ele = zip(words, numbers)
lst = list(ele)
w, n = zip(*lst)
print(w)
print(n)



# Iterator

for ch in 'Good Afternoon':
    print(ch, end=',')

print()

for num in [10, 20, 30, 40]:
    print(num, end=',')


print()

print(dir(str))

numbers = [10, 20, 30, 40]
i = numbers.__iter__()
print(i)
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
# print(i.__next__())           # through StopIteration Error


numbers = [10, 20, 30, 40]
i = iter(numbers)
print(i)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# print(next(i))                  # through StopIteration Error


# let check iterable and iterator objects attributes

s = 'Hello'
numbers = [10, 20, 30, 40]

print(hasattr(s, '__iter__'))
print(hasattr(s, '__next__'))

print(hasattr(numbers, '__iter__'))
print(hasattr(numbers, '__next__'))


i = iter(s)
print(i)

print(hasattr(i, '__iter__'))
print(hasattr(i, '__next__'))


i = iter(numbers)
print(i)

print(hasattr(i, '__iter__'))
print(hasattr(i, '__next__'))




# User defined iterator.
class AvgAdj:
    def __init__(self, data):
        self.__data = data
        self.__len = len(data)
        self.__first = 0
        self.__sec = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.__sec == self.__len:
            # raise exception (runtime error)
            raise StopIteration
        self.__avg = (self.__data[self.__first] + self.__data[self.__sec])/2

        self.__first += 1
        self.__sec += 1
        return self.__avg


lst = [10, 20, 30, 40, 50, 60, 70]
col = AvgAdj(lst)
print(col)

for ele in col:
    print(ele)




# Generator

# Example of Generator that returns average of adjacent numbers in list

def AvgAdj(data):
    for i in range(0, len(data)-1):
        yield (data[i] + data[i + 1])/2


lst = [10, 20, 30, 40, 50, 60, 70]
for ele in AvgAdj(lst):
    print(ele, end=" ")

print()


# Generator Expressions

# Generator expression creates a generator on the fly without being required to use the yield statement

# Generator Expression
gen_expr = max(random.randint(10, 100) for n in range(20))
print(gen_expr)


# sum of cubes of all numbers less than 20
gen_exp = (sum(n*n*n for n in range(20)))
print(gen_exp)


lst = [i*i for i in range(15)]
gen = (i*i for i in range(15))

print(lst)
print(gen)

print(sys.getsizeof(lst))
print(sys.getsizeof(gen))


"""


"""
Que 1:- Write a program that proves that a list is an iterable and not an iterator.

dir(list) shows __iter__ attribute but not __next__. so list is iterable.

# Answer starts here...


lst = [10, 20, 30, 40, 50]
print(lst)

i = iter(lst)

print(dir(lst))
print(dir(i))

"""


"""
Que 2:- Write a program that generates prime numbers below 3 million. Print sum of these prime numbers.



def generate_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


def is_prime(n):
    if n > 1:
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(2, int(math.sqrt(n)), 1):            # Check divisibility up to sqrt(n)
            if n % i == 0:
                return False
        else:
            return True
    else:
        return False


total = 0
for next_prime in generate_primes():
    if next_prime < 3000000:
        total += next_prime
    else:
        print(total)
        exit()


"""


"""
Que 3:- Write a program that uses dictionary comprehensions to print sin, cos and tan tables for angles ranging
        form 0 to 360 in steps 15 degrees. write a generator expressions to find the maximum value of sine and cos.
        


pi = 3.14

sine_table = {ang: round(math.sin(ang * pi / 180), 3) for ang in range(0, 360, 15)}
cos_table = {ang: round(math.cos(ang * pi / 180), 3) for ang in range(0, 360, 15)}
tan_table = {ang: round(math.tan(ang * pi / 180), 3) for ang in range(0, 360, 15)}


print(sine_table)
print(cos_table)
print(tan_table)

max_sin = max((math.sin(ang * pi / 180)) for ang in range(0, 360, 15))
max_cos = max((math.cos(ang * pi / 180)) for ang in range(0, 360, 15))
max_tan = max((math.tan(ang * pi / 180)) for ang in range(0, 360, 15))


print(max_sin)
print(max_cos)
print(max_tan)


"""


"""
Que 4:- Create 3 lists - a list of names , list of ages and list of salaries. Generate and print 
        list of tuple containing name, age and salary from the 3 list. From this list generate 3 tuples - 
        one containing all names, another containing all ages and third containing all salaries.



names = ['Ajay', 'Raj', 'Dipak', 'Rohan']
ages = [23, 25, 28, 20]
salary = [14500, 12500, 17000, 19000]

# creating Iterator of tuple
it = list(zip(names, ages, salary))

# build the list by iterating iterator object
lst = list(it)

# Unzip the list into tuples
n, a, s = zip(*lst)
print(n)
print(a)
print(s)


"""


"""
Que 5:- Write a program to obtain transpose of a 3x4 matrix.


mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print(mat)
# unzip element in mat, each tuple contain 3 elements
it = zip(*mat)

# creating the empty list
lst = [[] for _ in range(4)]
print(lst)

# appending transpose element in it
i = 0
for ele in it:
    # appending an element of iterator in list, iterator element in form of tuple
    lst[i] = list(ele)
    i += 1

print(lst)


# using list comprehension
mat2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
ls = [[row[i] for row in mat2] for i in range(len(mat2[0]))]
print(ls)


"""


"""
Que 6:- Write a program to multiply two matrices x(2 X 3) and y(3, 2) using list comprehension.


x = [[1, 2, 3], [4, 5, 6]]
y = [[11, 12], [21, 22], [31, 32]]


l1 = [xrow for xrow in x]
print(l1)

l2 = [(xrow, ycol) for ycol in zip(*y) for xrow in x]
print(l2)


l3 = [[sum(a*b for a, b in zip(xrow, ycol)) for ycol in zip(*y)] for xrow in x]
print(l3)


"""


"""
Que 7:- Suppose we have list of 5 integers and a tuple of 5 floats. 
        Can we zip them and obtain an iterator ? If yes, how?


integers = [10, 20, 30, 40, 50]

floats = (1.4, 2.5, 5.2, 3.4, 7.2)

# creating iterator object from list and tuple
it = zip(integers, floats)
print(it)

# creating list of iterator to obtain an iterator
lst =list(it)
print(lst)


"""


"""
Que 8:- Create two lists students and marks. Create a dictionary from these two lists using dictionary comprehension.
        Use names as key and marks as value.
        


# list of key
students = ['jay', 'raj', 'Yash', 'Pratik', 'Rakesh']
marks = [78, 70, 83, 90, 68]

# dictionary comprehensions
d1 = {k: v for (k, v) in zip(students, marks)}
print(d1)

"""


"""
Que 9:- Create a dictionary containing names of students and marks obtained by them in three subjects.
        Write a program  to print these names in tabular form with sorted names as column and marks in 
        three subjects listed below each student name as shown as below:
        rahul - 67,76,39 , Rakesh - 59, 70, 81 , Sameer - 58, 86, 78
         

d = {'Rahul': [67, 76, 39], 'Sameer': [58, 86, 78], 'Rakesh': [59, 70, 81]}

lst = [(k, *v) for k, v in d.items()]
print(lst)

# sorted by name
lst = [(k, *v) for k, v in sorted(d.items())]
print(lst)

for row in zip(*lst):
    print(row)


for row in zip(*lst):
    print(*row, '\t')


for row in zip(*((k, *v) for (k, v) in sorted(d.items()))):
    print(*row, '\t')

"""


"""
Que 10:- Write  a program that define a function pascal triangle() that display a pascal triangle of level
         received as parameter to the function. 



def pascal_triangle(n):
    row = [1]               # Pascal's Triangle starts with the first row as [1]
    z = [0]                 # Helper list [0] for aligning elements during addition
    for x in range(n):
        # Print the current row of Pascal's Triangle
        print(row)

        # Generate next row of pascal triangle
        # Use zip to pair adjacent elements for summation
        # row + z shifts the row to the left by appending a 0 at the end
        # z + row shifts the row to the right by prepending a 0 at the start
        row = [left + right for left, right in zip(row + z, z + row)]


pascal_triangle(8)


"""


"""
Que 11:- Write a class called progression and inherits 3 class AP, GP, FP. 
         Progression class acts as a user define iterator,by default its generate integers starting from 0 and steps of 1.
         AP, GP, FP should use iteration facilities of Progression class.
        
        A progression (which is also known as a sequence) is nothing but a pattern of numbers.
"""


class Progression:
    # integers starts from 0.
    def __init__(self, start=0):
        self._start = start
        self._current = self._start

    def __iter__(self):
        return self

    def advance(self):
        # steps of 1
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            data = self._current
            self.advance()
            return data

    def display(self, n):
        # here n is number till that range we need sequence
        print(' '.join(str(next(self)) for _ in range(n)))


# Arithmetic Progression
class AP(Progression):
    def __init__(self, start=0, step=1):
        super().__init__(start)
        self.__step = step

    def advance(self):
        # difference between two consecutive numbers are same in AP
        self._current += self.__step


# Geometric Progression
class GP(Progression):
    def __init__(self, start=1, step=2):
        super().__init__(start)
        self.__step = step

    def advance(self):
        # ratio between two consecutive number are same in GP
        self._current *= self.__step


# Fibonacci Progression
class FP(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self.__previous = second - first

    def advance(self):
        self.__previous, self._current = self._current, self.__previous + self._current


print('default progression')
obj_prog = Progression()
obj_prog.display(5)


print('\nArithmetic Progression : ')    
obj_ap = AP(5)
print('AP with step 5')
obj_ap.display(10)

print()

obj_ap = AP(2, 4)
print('AP starts with 2 and step 4')
obj_ap.display(10)

print()

print('GP with default multiple:')
g = GP()
g.display(10)

print('\nGp starts with 1 and steps 3')
g = GP(1, 3)
g.display(10)


print('\nFP with default multiple:')
f = FP()
f.display(10)


print('\nFP start value 4 and 6:')
f = FP(4, 6)
f.display(10)


