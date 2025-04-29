import random

"""
Que 1:- A set contain names which begin either with A or with B. write a program ro separate out
        the names into two sets, one containing names beginning with A and another containing names beginning with B.

# Answer starts here...

# Initial set of names
names = {'Ajay', 'Bipin', 'Raj', 'Ankit', 'Brar', 'Bapat', 'Akshay', 'Yash', 'Aakash', 'Badshah', 'Ajit', 'Abhay'}
print('Original Names Set :-', names)

# Initialize two empty sets for names starts with A and B.
a_names = set()
b_names = set()

# Iterate through the names to separate them
for name in names:
    if name.startswith('A'):
        a_names.add(name)
    elif name.startswith('B'):
        b_names.add(name)


print('List of names beginning with A :-', a_names)
print('List of names beginning with B :-', b_names)

"""

"""
Que 2:- Create an Empty set. Write a program that adds five new names to this set,
        modifies one existing name and deletes two names existing in it.


# initialize an Empty Set
names = set()

# to add five names in set
for i in range(5):
    name = input(f'Enter a name {i + 1} to add in set :- ')
    names.add(name)

print('Initial Names Set', names)

# modifies one existing name in the set
old_name = input('Enter the name you want to modify: ')
if old_name in names:
    new_name = input(f'Enter the new name to replace "{old_name}": ')
    names.remove(old_name)
    names.add(new_name)
    print(f'{old_name} has been replace with {new_name}.')
else:
    print(f'{old_name} not found in set.')


print('Set after modification:', names)


# Delete two names from the set
for i in range(2):
    name_to_remove = input(f'Enter a name {i + 1} want to remove from the set :')
    if name_to_remove in names:
        names.remove(name_to_remove)
        print(f'{name_to_remove} is removed from set')
    else:
        print(f'{name_to_remove} not found in set.')

print('Final Names Set:', names)

"""

"""
Que 3:- What is difference between the two set functions - discard() and remove().

When to Use:
- Use remove() when:
    You want to ensure the element exists in the set before removing it.
    An error (e.g., a KeyError) would signal a logic issue if the element is missing.

- Use discard() when:
    You want to avoid handling errors explicitly.
    It's acceptable for the operation to have no effect if the element is not present.

"""

"""
Que 4:- Write a program to create a set containing 10 randomly generated number in the range 15 to 45.
        count how many of these numbers are less than 30. delete all numbers which are greater than 35.
        

# Initialize an set for numbers
numbers = set()

# Generating 10  unique random numbers in the range 15 to 45
while len(numbers) < 10:
    num = random.randint(15, 45)
    numbers.add(num)

print('Set of Randomly generated numbers : ', numbers)


# Using set methods to count numbers less than 30
count_less_than_30 = 0

for i in numbers:
    # Increment the count if the number is less than 30
    if i < 30:
        count_less_than_30 += 1

print(f'There are {count_less_than_30} numbers less than 30.')


# Iterate through the set and remove numbers greater than 35
for num in numbers.copy():
    if num > 35:
        numbers.remove(num)

print('Set after removing numbers greater than 35:', numbers)

"""

"""
Que 5:- what do the following set operators do ?
---- | , & , ^ , ~ ( - ). 

# Answer starts here...

A = {1, 2, 5, 6, 8, 9, 10, 3}
B = {2, 4, 5, 9, 7, 8}

print('Set A :', A)
print('Set B :', B)

print('Union of set A and Set B :', A | B)
print('Intersection of set A and Set B :', A & B)
print('Symmetric Difference of set A and Set B :', A ^ B)
print('Elements present in Set A but not in Set B', A - B)
print('Elements present in Set B but not in Set A:', B - A)

"""


"""
Que 6:- what do the following set operators do ?
  |= , &=, ^=, -=.
  
# Answer starts here...

a = {1, 2, 5, 6, 8, 9, 10, 3}
b = {1, 2, 5, 6, 8, 9, 10, 3}
c = {1, 2, 5, 6, 8, 9, 10, 3}
d = {1, 2, 5, 6, 8, 9, 10, 3}

e = {2, 4, 5, 9, 1, 8}

a |= e
print('Union of a and e, updated a:', a)

b &= e
print('Intersection of b and e, updated b:', b)

c ^= e
print('Symmetric difference of c and e, updated c:', c)

d -= e
print('Difference of d and e, updated d:', d)

"""

"""
Que 7:- How will you remove all duplicate elements present in a string, a list and a tuple ?

# Answer starts here

my_string = "programming"

my_list = [1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 3]

my_tuple = (1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 3)


# Remove duplicates from the string by converting it to a set
my_string = ''.join(set(my_string))  # Convert set back to string
print('String after removing duplicates:', my_string)


# Remove duplicates from the list by converting it to a set
my_list = list(set(my_list))  # Convert set back to list
print('List after removing duplicates:', my_list)


# Convert the set back to a tuple after removing duplicates
my_tuple = tuple(set(my_tuple))  # Convert set back to tuple
print('Tuple after removing duplicates:', my_tuple)


"""

"""
Que 8:- Which operator is user to determining whether a set is a subset of another set .

# Answer starts here


a = {1, 2, 3, 4, 5, 6}
b = {2, 5, 6}

# subset
print('set b is subset of a :', b <= a)

"""

"""
Que 9:- What will be the output of following program ?

s = {'Mango', 'Banana', 'Guava', 'Kiwi'}

s.clear()
print(s)

del (s)
print(s)

"""

"""
Que 10:- Which of the following is correct way to create an empty set ?
"""

s1 = set()   # correct way to create empty set
s2 = {}

print(type(s1))
print(type(s2))

print(isinstance(s1, set))
print(isinstance(s2, dict))
