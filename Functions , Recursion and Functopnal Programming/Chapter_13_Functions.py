"""
# User define function
def fun():
    print('My opinions may have changed')
    print('But not that fact that I am right')


# function can call any number of times
fun()       # first call
fun()       # second call

"""
import re
import string

"""
# Function can be nested
# Inner function can be access the variable of outer function.
# Outer function to be called for the inner function to execute.


def fun1():
    print('Reached fun1')

    def fun2():
        print('Inner avatar')
    print('Outer avatar')

    # to execute inner function
    fun2()


fun1()
print(type(fun1()))


"""

"""
# Communication with functions

# - done using parameter / arguments passed to it and the value(s) return from it.
# - the way to pass values to a function and return value from it


# function calculate sum of three arguments.
def cal_sum(x, y, z):
    return x+y+z 


s1 = cal_sum(10, 20, 30)
print(s1)


# function calculate sum of three parameters.
a, b, c = 5, 10, 15

s2 = cal_sum(a, b, c)
print(s2)



# Types of arguments

# 1] Positional argument


def fun(i, j, k):
    print(i + j)
    print(k.upper())


# correct positional order
# function takes int, float, string soo we have to pass arguments in same order.
# number of arguments pass must be number of argument received.
fun(10,  3.14, 'Rohan')


# 2] Keyword argument


def print_it(i, a, string):
    print(i, a, string)


# function call
print_it(i=30, a=3.14, string='Jay')

print_it(string='Aman', a=10, i=3.14)

print_it(a=10, i=5, string='Ajay')


# 3] Positional arguments as well as keyword arguments.

# the positional arguments must precede keyword arguments


def printing(i, a, string):
    print(i, a, string)


printing(10, a=1.523, string='Aman')
printing(10, string='Aman', a=1.523)
printing(10, 3.14, string='Aman')

# SyntaxError: positional argument follows keyword argument
# printing(string='Ajay', 50, a= 10)




# 4] Variable-length positional arguments
# - sometimes number of position arguments pass in function is not certain
# - In such a case variable length positional argument can be received using *args.


def print_it(*args):
    print()
    for var in args:
        print(var, end=" , ")


# function call
print_it(12, 3.14, 5.6, 12, 'Aryan', 'Vilas', 9, 17)


# args used in definition of print_it as a tuple.
# '*' Indicates that it will hold all arguments passed to print_it.
# The tuple can be iterate through using a for loop.




# 5] variable-length keyword arguments
# - Sometimes number of keyword arguments pass in function is not certain.
# - In such case, variable-length keyword arguments can be received using **kwargs


def print_it(**kwargs):
    print()
    for name, value in kwargs.items():
        print(name, value, end=" , ")


# function call
print_it(a=10, b=5, c=1.25, d='Aman', e='Rajesh')

girls = {"Emma": 28, "Sophia": 24, "Olivia": 26, "Sophia": 40}
print_it(**girls)


# kwargs used in definition of print_it() is a dictionary containing variable name as a key
#   and values as value.
# '**' indicates that it will hold all the arguments passed to print_it()
# we cannot use more that one args and more than one kwarg while defining function.




# if function  is to received required as well as positional arguments
# then they must occur in following order:

# - positional arguments--->variable length positional arguments--->
#   keyword arguments ---> variable length keyword arguments


def print_it(i, j, *args, x, y, **kwargs):
    print()
    print(i, j, end=' ')
    for var in args:
        print(var, end=' ')
    print(x, y, end=' ')
    for key, value in kwargs.items():
        print(key, value, end=' ')


# nothing goes in args, kwargs
print_it(10, 20, x=50, y=60)

# nothing goes in kwargs
print_it(10, 20, 100, 200, 400, y=40, x=50)

# 100, 200 go to args , 'a,':5, 'b':6, 'c':7 go to kwargs
d = {'a': 5, 'b': 6, 'c': 7}
print_it(10, 20, 100, 200, x=30, y=40, a=5, b=6, c=7)
print_it(10, 20, 100, 200, x=30, y=40, **d)


# function using Default value
# default value will be use if we do not pass the value for that arguments during function call.
# Note that while defining a function, default arguments must follow non-default argument

def fun(a, b=100, c=3.14):
    return a+b+c


print('\n')

# function call
w = fun(30)
print(w)

x = fun(20, 50)
print(x)

y = fun(30, 60, 6.23)
print(y)

z = fun(1, c=3, b=5)
print(z)

"""

"""
# Unpacking Arguments


def print_it(a, b, c, d, e):
    print(a, b, c, d, e)


lst = [10, 20, 30, 40, 50]
tpl = ('A', 'B', 'C', 'D', 'E')
s = {1, 2, 3, 4, 5}


# function call
print_it(*lst)
print_it(*tpl)
print_it(*s)


def print_dict(name='Sanjay', marks=75):
    print(name, marks)


d = {'name': 'Anil', 'marks': 50}
# function call
# pass key to function
print_dict(*d)

# passes values to function
print_dict(**d)

# function execute default value
print_dict()

"""

"""
Que 1:- Write a program to receive three integers from keyboard and get their sum,
        and product calculated through user-defined function cal_sum_prod()

# Answer starts here..


def cal_sum_prod(a, b, c):
    total_sum = a+b+c
    product = a*b*c

    return total_sum, product


num1, num2, num3 = (input("Enter an Integer :")).split()
num1, num2, num3 = int(num1), int(num2), int(num3)


# call function
x, y = cal_sum_prod(num1, num2, num3)

print(f'Total Sum of {num1}, {num2}, {num3} is {x} \n', f'\nProduct of {num1}, {num2}, {num3} is {y}')


"""

"""
Que 2:- Pangram is a sentence that uses every letter of the alphabet. Write a program that checks
        whether a given string is pangram or not , through the user-defined function ispangram().



def ispangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(s.lower())


a = 'Program is a sentence that uses every letter of the alphabet'
print(ispangram(a))

print(ispangram('The quick brown fox jumps over the lazy dog'))

"""

"""
Que 3:- Write a program in python that accepts a hyphen-separated sequence of words as input
        and calls a function convert() which converts it into a hyphen-separated sequence 
        after sorting them alphabetically.
        


def convert(s):
    items = [word for word in s.split('-')]
    items.sort()
    alpha_sort = '-'.join(items)
    return alpha_sort


print(convert('bala-vijay-aman-sandeep-lad'))

"""

"""
Que 4:- Write a python function to create and return a list containing tuples of 
        the form (x, x2, x3) for all x between 1 to 20(both Include).

# Answer starts here..


def num_square_cube():
    num_lst = list()
    for num in range(1, 21):
        num_lst.append((num, num**2, num**3))

    return num_lst


# creating a list of num 1 to 20
i = num_square_cube()

print(i)


# second way of solution
def num_square_cube2(num):
    lst = []
    for n in num:
        lst.append((n, n**2, n**3))
    return lst


num_lst = [n for n in range(1, 21)]

a = num_square_cube2(num_lst)
print(a)


"""

"""
Que 5:- A Palindrome is a word or phase which reads the same in both directions. 
        Write a program that define a function ispalindrome() which check whether a given string is a palindrome or not.
        Ignore space and case mismatch while checking for palindrome. 

# First method


def ispalindrome(s):
    no_space_sentence = s.replace(" ", "").lower()
    reverse_sentence = ''.join(reversed(no_space_sentence))
    if no_space_sentence == reverse_sentence:
        return True
    else:
        return False


a = 'Rats live no on evil star'

a = ispalindrome(a)
print(a)

b = ispalindrome('Malayalam')
print(b)

c = ispalindrome('Ajay  googavle ')
print(c)

# Second Method


def ispalindrome2(s):
    t = s.lower()
    left = 0
    right = len(t)-1

    while right >= left:
        if t[left] == ' ':
            left += 1
        if t[right] == ' ':
            right -= 1

        if t[left] != t[right]:
            return False
        left += 1
        right -= 1
    return True


print(ispalindrome2('Murder for a jar of red rum'))


"""

"""
Que 6:- Write a function that defines a function convert() that receives a string containing a sequence
        of whitespace separated words and returns a string after removing all duplicate words 
        and sorting them alphanumerically.



def convert(s):
    # Remove punctuation using str.translate
    s = s.translate(str.maketrans('', '', string.punctuation))
    # list of word in parameter string
    words_lst = [word for word in s.split()]
    # to remove duplicate words convert it to set and also sort them
    words_set = set(words_lst)
    # sorting set and converting into string
    sort_s = ' '.join(sorted(words_set))

    return sort_s


a = "the teacher explained the concept clearly, helping the students understand the concept better."
y = convert(a)
print(y)

"""

"""
Que 7:- Write a program that defines function count_alphabets_digit() that accepts a string and 
        calculates the number of alphabets and digit in it. It should return these values as a dictionary.
        Call this function for some sample strings.



def count_alphabets_digit(s):
    # Initialise a dict
    d = {'Alphabet': 0, 'Digit': 0}
    for ch in s:
        if ch.isalpha():
            d['Alphabet'] += 1
        elif ch.isdigit():
            d['Digit'] += 1
        else: 
            pass

    return d


a = 'Akshay1243'
print(count_alphabets_digit(a))

         
"""

"""
Que 8:- Write a program that defines a function called frequency() which computes the frequency of words
        present in string passed to it. The frequencies should be returned in sorted order by words in the strings. 

# Answer starts here...


def frequency(s):
    freq = {}
    for word in s.split():
        freq[word] = freq.get(word, 0) + 1

    return freq


sentence = "dog cat dog bird cat dog bird fish dog fish bird cat dog"
d = frequency(sentence)
# sort element of d by keys
words = sorted(d)

# return as string
for w in words:
    print(f'{w}: {d[w]}')


"""

"""
Que 9:- Write a program that defines two functions called create_sent1() and create_sent2().
        both receive following 3 list. 
        Both function should form sentences by picking elements from these lists and return them.
        Use for loop in create_sent1 and list comprehensions in create_sent2().
        
"""

# given three list
subjects = ['He', 'She']
verbs = ['loves', 'hates']
objects = ['TV serial', 'Netflix']


def create_sent1(sub, verb, obj):
    lst = []
    for s in sub:
        for v in verb:
            for o in obj:
                lst.append(f'{s} {v} {o}')

    return lst


# function call
a = create_sent1(subjects, verbs, objects)
for sentence in a:
    print(sentence)


def create_sent2(sub, verb, obj):
    lst = [(s + ' ' + v + ' ' + o)for s in sub for v in verb for o in obj]
    return lst


print('\n')

b = create_sent2(subjects, objects, verbs)
for sentence in b:
    print(sentence)
