import operator

"""
# Tuple Introduction

a = ()
print(type(a))

# tuple with one item . ',' comma after item is necessary . if not use comma it treated as Integer
b = (10,)
print(type(b))

# tuple with dissimilar items
c = ('Sanjay', 25, 34.50)

# tuple with similar items
d = (10, 20, 30, 40, 50)

# while initialize tuple we may drop ()
e = 'Jay', 32, 15.20
print(type(e))


# tuple element can be repeated
tpl1 = (10,)*5
print(tpl1)

tpl2 = (10)*5
print(tpl2)
print(type(tpl2))


# Accessing Tuple Element

tpl = ('Sanjay', 25, 34.50)

print(tpl)

# access elements in tuple
msg = ('Handle', 'Exceptions', 'Like', 'a', 'boss')
print(msg[1], msg[3])


# slicing of tuple
print(msg[:])
print(msg[1:3])
print(msg[:3])
print(msg[3:])


# Looping in Tuples

tpl = (10, 20, 30, 40, 50)

# Using while loop

i = 0
while i < len(tpl):
    print(tpl[i], end=" ")
    i += 1

print()

# Using for loop
for i in tpl:
    print(i, end=" ")

print()

# enumerate() if you need to keep track index of element.
for index, ele in enumerate(tpl):
    print(index, ele, end=",")



# Basic Tuple Operations
tpl = (10, 20, 30, 40, 50)

# Tuple is immutable you cant not modified it, operation like append, remove and insert do not work with a tuple.

# both time Error - TypeError: 'tuple' object does not support item assignment
# tpl[2] = 32             # error
# tpl[2:4] = [25, 36]     # error


# though a Tuple is immutable, it can contain mutable object like lists.

# mutable list, immutable string - all can belong to tuple
s = ([1, 2, 3, 4], [4, 5], 'Ocelot')

# change first item of list which is tuple
s[1][1] = 7
print(s)

# one more way to change first item of first list
p = s[1]
p[1] = 100
print(s)



# Basic Tuple operations

# concatenate
tpl = (1, 2, 3, 4, 5)
tpl = tpl + (6, 7, 8)
print(tpl)


# Merging
tpl1 = (1, 2, 3, 4, 5)
tpl2 = (6, 7, 8)
tpl3 = tpl1 + tpl2
print(tpl3)


# convertion to Tuple
a = [1, 2, 3]
print(tuple(a))

b = 'Aman'
print(tuple(b))


# Aliasing in Tuple
tpl1 = (1, 2, 3, 4, 5)
tpl2 = tpl1
print(tpl1)
print(tpl2)

print(tpl1 is tpl2)
print(id(tpl1))
print(id(tpl2))


# cloning

tpl1 = (1, 2, 3, 4, 5)
tpl2 = ()
tpl2 = tpl1[:]
print(tpl1)
print(tpl2)

print(tpl1 is tpl2)
print(id(tpl1))
print(id(tpl2))

# searching
res = 2 in tpl1
print(res)

# Identity
print(tpl1 is tpl2)


# comparison
t1 = (1, 2, 3, 4, 5)
t2 = (1, 2, 5)
print(t1 < t2)


# Emptiness
tpl = ()
if not tpl:
    print('Empty tuple')


# built-in functions on Tuple

t = (12, 15, 13, 23, 22, 16, 17)
print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(any(t))
print(all(t))

sorted_tuple = sorted(t)
print(sorted_tuple)

reversed_tuple = tuple(reversed(t))
print(reversed_tuple)


# Tuple Methods

tpl = (12, 15, 13, 23, 22)
print(tpl.count(23))
print(tpl.index(23))


# Tuple Varieties

# tuple of tuple
a = (1, 3, 5, 7, 9)
b = (2, 4, 6, 8, 10)
c = (a, b)
print(c)

print(c[0][0], c[1][2])


records = (('Priyanka', 24, 3455.50), ('Shailesh', 25, 4555.50),
           ('Subhash', 25, 4505.50), ('Sugandh', 27, 4455.55))


for n, a, s in records:
    print(n, a, s)


# embedded another tuple
x = (1, 2, 3, 4)
y = (10, 20, x, 30)

print(y)

# Unpacking tuple within tuple using * operator
z = (10, 20, *x, 30)
print(z)



# it is possible to create a list of tuples, or tuple of lists
lst = [('Priyanka', 24, 3455.50), ('Shailesh', 25, 4555.50)]
tpl = (['Subhash', 25, 4505.50], ['Sugandh', 27, 4455.55])

print(sorted(lst))
sort_tuple = tuple(sorted(tpl))
print(sort_tuple)


# if we wish to sort by salary , we need itemgetter() function

print(sorted(lst, key=operator.itemgetter(2)))
print(sorted(tpl, key=operator.itemgetter(2)))


"""

"""
Que 1:- Pass a tuple to the divmod() function and obtain the Quotient and the remainder.

# Answer starts here...

# quotient and reminder
result = divmod(26, 4)
print(result)

# other way
t = (17, 3)
print(divmod(*t))

"""

"""
Que 2:- Write a program to perform the following operations.

# Answer starts here...


# pack the first 10 multiples of 10 into a tuple
tpl = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# Unpack the tuple into 10 variables, each holding 1 value
a, b, c, d, e, f, g, h, i, j = tpl
print(a, b, c, d, e, f, g, h, i, j)

# unpack such a way 1 st value stored in x,second value stored in y , And all values between into disposable variable.
x, _, _, _, _, _, _, _, _, y = tpl
print(x, y, _)

# unpack such a way 1 st value stored in s,second value stored in t , And all values between into disposable variable.
s, *_, t = tpl
print(s, t, _)

"""

"""
Que 3:- A list contains names of boys and girls as its elements. Boy's names are stored as tuples. 
        Write a python program to find out number of boys and girls in the list.
        
# Answer starts here... 


lst = ['Subha', 'Nisha', 'Sudha', ('Suresh',), ('Rajesh',), 'Radha', ('Aman',)]

# count for boys and girls
boys = 0
girls = 0

for ele in lst:
    if isinstance(ele, tuple):
        boys += 1
    else:
        girls += 1

print('Boys :-', boys, 'Girls :-', girls)

"""

"""
Que 4:- A list contain tuples contain roll number, names and age of student.
        Write a python program to gather all the names from this list into another list.

# Answer starts here...

lst = [('A101', 'Shraddha', 23), ('A102', 'Yash', 20), ('A103', 'Aman', 22), ('A104', 'Jay', 24)]

name_lst = []

for ele in lst:
    name_lst = name_lst + [ele[1]]

print(name_lst)


"""

"""
Que 5:- Write a program to carried out the following operations :

# Answer starts here...
"""

tpl = ('F', 'l', 'a', 'b', 'b', 'e', 'r', 'g', 'a', 's', 't', 'e', 'd')

# Add an ! at the end of the tuple
tpl = tpl + ('!',)
print(tpl)

# convert a tuple to string
s = ''.join(tpl)
print(s)


# extract ('b','b') from tuple
t = tpl[3:5]
print(t)

# find out number of occurrences of 'e' .
print(tpl.count('e'))


# check whether 'r' exist in the tuple
print('r' in tpl)

# convert the tuple to a list
lst = list(tpl)
print(lst)


# Delete character 'b', 'b', 'e', 'r' from the tuple
# cannot remove elements from tuple , so we will split tuple and then merge

tpl = tpl[0:3] + tpl[8:]
print(tpl)

