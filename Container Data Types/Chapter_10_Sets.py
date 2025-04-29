"""
# set are like list, with the exception that they do not contain duplicate Entries.

# empty set, use () instead of {}
a = set()
print(type(a))

# set with one item
b = {20}

# set with multiple items
c = {'Sanjay', 25, 343.30}

# duplicate items can store as one item only
d = {10, 10, 10, 10}
print(d)

# hashing technique is used to store elements in set
# hash value of element always be same, no matter in which order you store elements
s = {12, 23, 45, 16, 52}
t = {23, 16, 12, 52, 45}
u = {45, 52, 12, 23, 16}
print(s)
print(t)
print(u)


# it is possible to store set of strings and tuples , but not a set of lists.
# string and tuple are immutable so their hash value remain same at all times.

s1 = {'Morning', 'Evening'}
s2 = {(2, 3), (5, 7), (10, 12)}

# set of lists is not permitted
# s3 = {[1, 2], [5, 6]}          # TypeError: unhashable type: 'list'


# set are commonly use in eliminate duplicate entries, membership testing


# set is unordered collection
s = {15, 25, 45, 35, 55}
print(s)

# being an Unordered collection , item in a set cannot be accessed using indices
# set cannot sliced using [].


# Looping in Sets

s = {12, 15, 13, 23, 22, 16, 17}

for i in s:
    print(i, end=" ")

# while loop cannot be used to access set of elements. because we cannot access set element using index.
print()

# enumerate() function can be used with a set
# The Enumeration is done on access order , not on Insertion order.

for index, ele in enumerate(s):
    print(index, ele, end=" | ")


# Basic Set Operations

# set are mutable
s = {'gate', 'fate', 'late'}
print(s)
s.add('rate')
print(s)


# If we want an immutable set, we should use a frozenset
s1 = frozenset({'goo', 'loo', 'foo'})
# s1.add('yoo')       # error - 'frozenset' object has no attribute 'add'


# concatenation - Doesn't work on set  - unsupported operand
a = {1, 2, 3}
# a = a + {4, 5}
print(a)

# Merging - Doesn't work - unsupported operand

b = {4, 5, 6}
# c = a + b

# Conversion - while converting a set using set(), repetitions are eliminated.
tpl = (1, 2, 3, 4, 5, 2, 3)
s = set(tpl)
print(s)


# Aliasing - both refer same set.
x = {1, 2, 3, 4}
y = x
print(id(x))
print(id(y))
print(x)
print(y)
x.add(5)
print(x)
print(y)

print()

# Cloning - coping one set to another
d = {1, 2, 3, 4}
e = d.copy()
print(d)
print(e)
print(id(d))
print(id(e))

print()

# searching
res = 2 in d
print(res)

# Identity
print(e is d)
print(e is not d)


# comparison
a1 = {1, 2, 3, 5}
a2 = {1, 2, 3}

print(a1 == a2)


# Emptiness

g = set()

if not g:
    print('Empty Set')



# Using Built-in Function on string
s = {30, 20, 10, 40, 50}

print(len(s))
print(max(s))
print(min(s))
# sorted function returns sorted list , not sorted set
print(sorted(s))
print(sum(s))
print(any(s))
print(all(s))


# Set Methods :- syntax-- s.method()

s = {12, 15, 22, 13, 23, 16, 17}
t = {'A', 'B', 'C'}

print('Original set :', s)
# empty set
u = set()

# add element in set
s.add('Hello')
print(s)

# add element of set t to s.
s.update(t)
print(s)

# perform a deep copy (cloning)
u = s.copy()
print('Set u after deep copy :- ', u)

# remove element from s
s.remove(15)    # delete 15 from s
print(s)

# s.remove(102)     # raise error - KeyError - if element not present in set


# discard
s.discard(12)      # delete 12 from s
print(s)

# will not raise error if element not present in list
s.discard(120)

# removes all elements
s.clear()
print(s)


# relationship between to sets
s = {12, 15, 22, 13, 23, 16, 17}
t = {13, 16, 22}

# issuperset() - Checks if one set contains all elements of another	>=
print((s.issuperset(t)))

# issubset() - Checks if all elements of one set are in another	<=
print(t.issubset(s))

# isdisjoint() - Checks if two sets have no elements in common	None
print(s.isdisjoint(t))


# Mathematical Set Operations

# union, intersection and difference


# Sets
engineers = {'Vijay', 'Ajay', 'Sujay', 'Sanjay', 'Dinesh'}
managers = {'Aditya', 'Sanjay'}


# union - all people in both categories
print(engineers | managers)


# intersection - who are engineers and managers
print(engineers & managers)

# difference

# engineers who are not managers
print(engineers - managers)

# manager who are not engineers
print(managers - engineers)

# symmetric difference - managers who are not engineers and engineers who are not managers.
print(engineers ^ managers)

a = {1, 2, 3, 4, 5}
b = {2, 3, 4}

# prints True as a is superset of b
print(a >= b)

# print False as a is not subset of b
print(a <= b)

# # print True as b is not subset of a
print(b <= a)


# Updating Set Operations
# a |= b
# print(a)

# a &= b
# print(a)

# a -= b
# print(a)

a ^= b
print(a)


# Set varieties

# set cannot contain set embedded in it
# s = {'gate', 'fate', {10,20,30}, 'late'}          # TypeError

# it is possible to unpack set using the * operator
s = {'gate', 'fate', *{10, 20, 30}, 'late'}
print(s)

x = {1, 2, 3, 4}
print(*x)


"""

"""
Que 1:- What will be the output of following programs.

# Answer starts here..


a = {10, 20, 30, 40, 50, 60, 70}
b = {33, 44, 51, 10, 20, 50, 30, 33}

# union
print("Union of sets :-", a | b)

# intersection
print('Intersection of sets :-', a & b)

# difference
print('Elements of a which are not elements of b :- ', a - b)

print('Elements of b which are not elements of a :- ', b - a)

# symmetric difference - Elements of a which are not elements of b and Elements of b which are not elements of a
print(a ^ b)

# superset
print('a is superset of b :-', a >= b)

# subset
print('a is subset of b :-', a <= b)

"""

"""
Que 2:- What will be the output of following program

# Answers starts here...


a = {1, 2, 3, 4, 5, 6, 7}
b = {1, 2, 3, 4, 5, 6, 7}
c = {1, 2, 3, 4, 5, 6, 7}
d = {1, 2, 3, 4, 5, 6, 7}

e = {3, 4, 1, 0, 2, 5, 8, 9}

# union
a |= e
print(a)


# intersection
b &= e
print(b)


# difference
c -= e
print(c)


# symmetric difference
d ^= e
print(d)

"""

"""
Que 3:- write a program to carry out the following operations on the given set


s = {10, 2, -3, 4, 5, 88}

# number of items in set s
print(len(s))

# maximum element in set s
print(max(s))

# minimum element in set s
print(min(s))

# sum of all elements in set s
print(sum(s))

# obtain a new sorted set from s, set s remaining unchanged
t = print(sorted(s))

# report whether 100 is an element of set s
print(100 in s)

# report whether -3 is an element of set s
print(-3 in s)


"""

"""
Que 4:- What will be the output of the following program?

"""

lst = [10, 20, 30, 40, 50]
tpl = ('Sandeep', 25, 79.58)
s = 'set theory'

s1 = set(lst)
s2 = set(tpl)
s3 = set(s)

print(s1)
print(s2)
print(s3)
