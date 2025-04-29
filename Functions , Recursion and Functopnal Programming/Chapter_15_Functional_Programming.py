import math
import functools
import operator

"""

# Function as First-Class Values

# function assigning to a variable and calling function using variable.


def func():
    print('Hello')


def sum_of(x, y):
    print(x+y)


f = func
f()

s = sum_of
s(10, 20)


# Passing function as argument to a function:

def sum_all(x, y, a):
    print(x + y)
    a()            # Function call


def fun():
    print('World')


f1 = fun

sum_all(30, 50, f1)
# Syntax - lambda arguments : expressions



# function that are receives an arguments and return its cube.
print((lambda n: n ** 3)(3))
a = lambda n: n ** 3
print(a(4))

# function that receives three arguments and returns average of them
b = lambda x, y, z: (x + y + z) / 3
print((lambda x, y, z: (x + y + z) / 3)(10, 20, 30))
print(b(40, 45, 50))
# function that receives a string, strips any whitespace and returns the uppercase version of the string.
c = lambda s: s.strip().upper()
print((lambda s: s.strip().upper())('  ngp  '))
print(c('   Ajay        '))


# Calculate Average of numbers in list
lst1 = [1, 2, 3, 4, 5]
lst2 = [10, 20, 30, 40, 50]

print((lambda l: sum(l)/len(l))(lst1))
print((lambda num: sum(num)/len(num))(lst2))



# Higher order function

d = {'Oil': 230, 'Clip': 150, 'Stud': 175, 'Nut': 35}
# Lambda functions takes dictionary items and returns a value
d1 = sorted(d.items(), key=lambda kv: kv[1])
print(d1)


# map() function
# syntax :- map(function_to_apply, list_of_inputs)
# it returns a map object which can be converted to a list using list() function.

def fun(n):
    return n*n


lst = [5, 10, 15, 20, 25]
m1 = map(math.radians, lst)
print(list(m1))

m2 = map(math.factorial, lst)
print(list(m2))

m3 = map(fun, lst)
print(list(m3))




# filter() function
# Syntax :- filter(function_to_apply, list_of_inputs)
# Its return Sequence of those elements for which function returns True.

def fun(n):
    if n % 5 == 0:
        return True
    else:
        return False


lst1 = [5, 10, 14, 27, 25]
res = filter(fun, lst1)
print(list(res))

lst2 = ['A', 'X', 'Y', '3', 'M', '4', 'D']
res2 = filter(str.isalpha, lst2)
print(list(res2))



# reduce() function
# Syntax :- reduce(function_to_apply, list_of_inputs)
# its function operation performs a rolling computation to sequential pairs of values in a sequence. and return result


def get_sum(x, y):
    return x + y


def prod(x, y):
    return x * y


lst = [1, 2, 3, 4, 5]

s = functools.reduce(prod, lst)
print(s)



# Using Lambda with map(), filter(), reduce()


# Using lambda with map
lst = [5, 10, 15, 20, 25]

res_m = map(lambda n: n*n, lst)
print(list(res_m))


# Using lambda with filter
lst2 = [5, 10, 18, 27, 25]
res_f = filter(lambda x: x % 5 == 0, lst2)
print(list(res_f))


# Using lambda with reduce
lst3 = [1, 2, 3, 4, 5, 6]
res_sum = functools.reduce(lambda a, b: a+b, lst3)
res_prod = functools.reduce(lambda a, b: a*b, lst3)
print(res_sum)
print(res_prod)


# map() ,filter() and reduce() can be used together.

def fun(n):
    return n > 1000


lst4 = [10, 20, 30, 40, 50]
res = filter(fun, map(lambda n: n*n, lst4))
print(list(res))


"""


"""
Que 1:- Define three functions fun(), disp(), msg(), store them in a list and call them one by one in a loop.

# Answer starts here...


def fun():
    print('Inside Function fun')


def disp():
    print('Inside function disp')


def msg():
    print('Inside Function msg')


lst = [fun, disp, msg]

for f in lst:
    f()


"""


"""
Que 2:- Suppose there are two list , one containing numbers from 1 to 6, and other containing numbers from 6 to 1.
        Write a program to obtain lis that contains elements obtain by adding corresponding elements of two lists.
        
# Answer starts here..



lst1 = [1, 2, 3, 4, 5, 6]
lst2 = [6, 5, 4, 3, 2, 1]

result = map(lambda n1, n2: n1+n2, lst1, lst2)
print(list(result))

"""


"""
Que 3:- Write a program to create a new list by obtaining square of all numbers in a list.

# Answer starts here..

lst = [4, 5, 2, 7, 9, 6]
res_lst = list(map(lambda x: x*x, lst))

print(res_lst)

"""


"""
Que 4:- Though map() function is available ready-made in python, can you define yourself and test it?

# Answer starts here...


def my_map(fun, seq):
    result = []

    for ele in seq:
        # result.append(fun(ele))
        yield fun(ele)

    return result


lst1 = [4, 6, 3, 7, 9, 8]
res_lst = my_map(lambda x: x**2, lst1)
print(res_lst)
print(list(res_lst))


"""

"""
Que 5:-  Following data shows names, ages and marks of students in a class:
         Anil,21,80 , Sohail, 20, 90 , Sunil,20,91 , Shobha,18,93 , Anil,19,85
         
         Write a program to sort this data on multiple keys in the order name, age and marks.


lst = [('Anil', 21, 80), ('Sohail', 20, 90), ('Sunil', 20, 91), ('Shobha', 18, 93), ('Anil', 19, 85)]

sort_list = sorted(lst, key=operator.itemgetter(0, 1, 2))
print(sort_list)

sort_list2 =sorted(lst, key=lambda tpl: (tpl[0], tpl[1], tpl[2]))
print(sort_list2)

"""

"""
Que 6:- Suppose dictionary contain key-value pairs, where the key is an alphabets and value is number,
        Write a program that obtains the maximum and minimum values from the dictionary.
         
"""

d = {'x': 500, 'y': 5874, 'z': 560}

key_max = max(d.keys(), key=(lambda k: d[k]))
print('Maximum Value : ', d[key_max])


key_min = min(d.keys(), key=lambda k: d[k])
print('Minimum Value : ', d[key_min])
