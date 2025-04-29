"""
Que 1:- Write a program that define a function count_lower_upper() that accepts a string
        and calculate the number of uppercase and lowercase alphabets in it.
        It should return these values as a dictionary. Call this function for some sample strings.

# Answer starts here...


def count_lower_upper(string):
    alphabets_dict = {'Uppercase': 0, 'Lowercase': 0}
    for ch in string:
        if ch.isupper():
            alphabets_dict['Uppercase'] += 1
        elif ch.islower():
            alphabets_dict['Lowercase'] += 1
        else:
            pass

    return alphabets_dict


sentence = 'The Quick Brown Fox Jumps Over The Lazy Dog'
a = count_lower_upper(sentence)
print(a)


"""
import random

"""
Que 2:- Write a program that defines a function compute() that calculates the value of n + nn + nnn + nnnn,
        where n is digit received by the function. Test the function for digit 4 and 7.
        
# Answer starts here...


def compute(num):
    total_sum = 0
    term = ""
    for i in range(1, 5):
        term += str(num)        # append digit n as a string so term+str
        total_sum += int(term)      # convert string to int and add in sum
        # for logic explain purpose
        # print(f'{term} = {term} + {total_sum}')

    return total_sum


# Function call
a = compute(4)
print(a)

b = compute(7)
print(b)

"""

"""
Que 3:- Write a program that define a function create_array() to create and return a 3D array 
        whose dimensions are passed to a function. also initialize each element of 
        this array to a value passed to the function.
        
# Answer starts here...


def create_array(x, y, z, value):
    # Create a 3D array with dimensions x, y, z, initializing each element to `value`
    three_d_array = [[[value for _ in range(x)] for _ in range(y)] for _ in range(z)]
    return three_d_array


# Function call
dimensions = (3, 3, 3)          # Dimensions of the 3D array
value_to_fill = 7                           # Value to initialize each element

# Create and print the 3D array
a = create_array(*dimensions, value_to_fill)
print(a)

"""

"""
Que 4:- Write a program that defines a function create_list() to create and return a list
        which is an intersection of two list passed to it. 


# First way to find solution


def create_list(lst1, lst2):
    s1 = set(lst1)
    s2 = set(lst2)

    intersection_lst = list(s1 & s2)
    return intersection_lst


#  Another way
def create_ins_list(lst1, lst2):
    return [item for item in lst1 if item in lst2]


l1 = [1, 2, 3, 4, 5, 6, 10]
l2 = [4, 5, 8, 9]


# Function call
result = create_list(l1, l2)
print(result)


result2 = create_ins_list(l1, l2)
print(result2)

"""

"""
Que 5:- Write a program that defines a function sanitize_list() to remove all duplicate entries
        from the list that it receives.

# Answer starts here...


def sanitize_list(lst):
    
    sanitize_lst = []
    for item in lst:
        if item not in sanitize_lst:
            sanitize_lst.append(item)
    return sanitize_lst


# Another way to solution
def sanitize_list2(lst):
    return list(set(lst))


l = [1, 2, 3, 4, 5, 2, 3, 6, 7, 1, 8, 9, 5, 4, 6, 7, 3, 9, 8, 5]
result = sanitize_list(l)
print(result)

result2 = sanitize_list2(l)
print(result2)

"""

"""
Que 6:- Which of the calls to print_it() in the following program will report errors ?



def print_it(i, a, s, *args):
    print()
    print(i, a, s, end=' ')
    for var in args:
        print(var)


print_it(10, s='Hi', a=6.28)

print_it(a=6.28, s='Hello', i=30)
print_it(40, 2.35, 'Nag', 'Mum', 10)

# print_it(10, 3.144)           # error

"""

"""
Que 7 :- Which of the calls to fun() in the following program will report errors?


def fun(a, *args, s='!'):
    print(a, s)
    for i in args:
        print(i, s)


fun(10)
fun(10, 20)
fun(10, 20, 30)
fun(10,20,30,40,s='+')

"""

"""
# Que A

def fun(x, *args):
    print(x, end=' ')
    for var in args:
        print(var, end=' ')


a = 20
lst = [10, 20, 30, 40, 50]

# Function call
fun(a, *lst)


"""


def fun():
    print('First avatar')


fun()


def fun():
    print('New avatar')


fun()


# function which returns three different values
def three_ret(n):
    return str(n), n*1.34, n**2


x = three_ret(5)
print(x)


def print_it(a, b, c, d, e):
    return a, b, c, d, e


tpl = ('A', 'B', 'C', 'D', 'E')

y = print_it(*tpl)
print(y)

