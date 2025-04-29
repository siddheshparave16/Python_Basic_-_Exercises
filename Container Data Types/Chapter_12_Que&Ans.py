import random
from collections import Counter

"""
C] Attempt the following Questions:


# a]

s = set([int(n) for n in input('Enter values: ').split()])
print(s)


# b]
a = []
for n in range(10, 30):
    if n % 2 == 0:
        a.append(n)

print(a)

a1 = [num for num in range(10, 30) if num % 2 == 0]
print(a1)


# c]

a = {num for num in range(21, 40) if num % 2 == 0}
print(a)


# d]
s = [a+b for a in ['They ', 'We '] for b in ['are gone!', 'have come!']]

print(s)


# e]
sent = 'Pack my box with five dozen liquor jugs'

lst = [word for word in sent.split()]
print(lst)

# g]
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
d = {k: v*100 for (k, v) in d.items()}
print(d)

# h]
lst1 = [2, 7, 8, 6, 5, 5, 4, 4, 8]
s = {True if n % 2 == 0 else False for n in lst1}
counter = Counter(s)
print(counter)


# i]

d = {'amol': 20, 'anil': 12, 'sunil': 13, 'ramesh': 10}
d = {k: v**2 for (k,v) in d.items()}
print(d)

# j]
l = ['Amol', 'Anil', 'Sunil', 'Ramesh', 'Sandeep', 'Vinay']

s = {name.upper() for name in l}
print(s)


"""

"""
Que 1:- Write a program that generates a list of Integer coordinates for all points
        in quadrant from (1,1) to (5,5). Use list comprehensions

# Answer starts here..

lst = [(a, b) for a in range(1, 6) for b in range(1, 6)]
print(lst)

"""

"""
Que 2:- Using list comprehensions, write a program to create a list by multiplying each element in the list by 10.

# Answer starts here...

lst = [23, 87, 45, 12, 76, 39, 8, 65, 91, 30]
print('Original list :', lst)
lst = [num*10 for num in lst]
print('List after multiplying by 10 :', lst)

"""

"""
Que 3:- Write a program to generate first 20 fibonacci numbers using list comprehensions.


# fibonacci_lst = [num_a + num_b for num_a in range(20) for num_b in range(1, num_a) if nu]
# print(fibonacci_lst)

a = 0
b = 1
temp = 0
for i in range(20):
    temp = a + b
    a = b
    b = temp
    print(temp)

# fibonacci series where each number is sum of two number precede it
# making a loop of 18 numbers and adding next number as sum of last two number in list
# soo lst[-2] + lst[-1]

fibonacci_lst = [0, 1]
[fibonacci_lst.append(fibonacci_lst[-2] + fibonacci_lst[-1]) for _ in range(18)]
print(fibonacci_lst)


"""

"""
Que 4:- Write a program to generate two list using list comprehension. one list should contain first 20 Odd numbers.
        and another contain 20 even numbers. 


odd_lst = []
even_lst = []

even_lst = [num for num in range(1, 41) if num % 2 == 0 ]
odd_lst = [num for num in range(1, 41) if num % 2 != 0 ]

print(odd_lst)
print(even_lst)

"""

"""
Que 5:- Suppose a list contains positive and negative numbers. Write a program to create 2 list 
        - one containing positive numbers and another containing negative number. 


num_lst = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]

# List for positive numbers
positive_num = [num for num in num_lst if num > 0]

# List for negative numbers
negative_num = [num for num in num_lst if num < 0]
print(positive_num)
print(negative_num)

"""

"""
Que 6:- Suppose a list contain five strings. Write a program to convert all these string to uppercase.


fruits = ["apple", "banana", "cherry", "date", "elderberry"]

fruits = [fruit.upper() for fruit in fruits]
print(fruits)

"""

"""
Que 7:- Write a program that convert list of temperature to fahrenheit degree to equivalent celsius degrees
        using  list comprehensions.


temperatures_fahrenheit = [32, 45, 64, 72, 100, 150, 212, 98, 73, 55]
print('Temperature in Fahrenheit',temperatures_fahrenheit)

temperatures_celsius = [float(f'{((temp - 32) * (5 / 9)): .2f}') for temp in temperatures_fahrenheit]
print('Temperature in Celsius',temperatures_celsius)

"""

"""
Que 8:- Write a program to generate 2D matrix of size 4X5 containing random multiple of 4 in 
        the range 40 to 160.


mat = [[random.choice([num for num in range(40, 161) if num % 4 == 0]) for r in range(4)] for c in range(5)]

print(mat)

"""

"""
Que 9 :- Write a program that convert words present in list into uppercase and store them to set.

"""

fruits = ["apple", "banana", "cherry", "date", "elderberry", "date", "apple"]
fruits_set = {fruit.upper() for fruit in fruits}

print(fruits_set)




