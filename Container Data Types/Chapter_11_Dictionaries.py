import operator

"""
# Dictionary - collection of key-value pairs. also known as maps or associative array.

# Empty Dictionary
d1 = {}

# keys:values
d2 = {'A101': 'Amol', 'A102': 'Anil', 'B103': 'Ravi'}

print(type(d1))
print(d2)

# Different key may have same value
d = {10: 'A', 20: 'A', 30: 'B'}
print(d)

# Keys must be Unique. If keys are same, but values are different, latest key value pair get stored.
d = {'A': 10, 'B': 20, 'A': 30}
print(d)


# If key value pair are repeated, then only one pair gets stored. ( eliminate Duplicate value. )
d3 = {'A': 20, 'B': 40, 'A': 20}
print(d3)


# Accessing Dictionary Elements

# Element of Dictionary can access using the Key, not accessing using position.
# Elements of Dictionary are not position Indexed, but key Indexed
# Dictionaries cannot be sliced using [].

d = {'A101': 'Amol', 'A102': 'Anil', 'B103': 'Ravi', 'B104': 'Dinesh'}
print(d['B103'])            # print value for key 'B103'



# Looping in Dictionaries

d = {'A101': 'Amol', 'A102': 'Anil', 'B103': 'Ravi', 'B104': 'Dinesh'}

print('Iterating Key and Value from Dictionary :- ')
# Iterate over key-value pairs

for k, v in d.items():
    print(k, v, end="   ")

print('\n')

# Iterate over keys
print('Iterating keys from Dictionary :- ')
for k in d.keys():
    print(k, end="   ")

print('\n')

# shorter way for keys iteration
for k in d:
    print(k, end="  ")


print('\n')

# Iterate over values

print('Iterating Value from Dictionary :- ')
for v in d.values():
    print(v, end="   ")

print('\n')

# enumerate - keep track index
# Note - that () around k,v are necessary

for index, (k, v) in enumerate(d.items()):
    print(index, k, v)



# Basic Dictionary Operations
# Dictionaries are mutable.  so you can perform add/modify/delete operation on a dictionary.

courses = {'CS101': 'CPP', 'CS102': 'DS', 'CS203': 'OOP',
           'CS226': 'DAA', 'CS601': 'Crypt', 'CS442': 'Web'}

# add new key value pair
courses['CS444'] = 'Web Services'
print(courses)

# modify value for a key
courses['CS203'] = 'OOP Using Java'
print(courses)


# delete a key value pair
del (courses['CS102'])
print(courses)

# delete entire list
del (courses)
print(courses)



student_1 = {
    "name": "Rohan Verma",
    "roll_number": 203,
    "math_marks": 85,
    "science_marks": 90,
    "english_marks": 78
}

student_2 = {
    "name": "Ananya Sharma",
    "roll_number": 204,
    "math_marks": 88,
    "science_marks": 92,
    "english_marks": 84
}

# concatenation - Doesn't work
# Merging - Doesn't work

# conversion
data = [("Rohan", 203), ("Ananya", 204), ("Priya", 205)]
students_data = dict(data)
print(students_data)


student_names = ["Rohan", "Ananya", "Priya", "Aman", "Sneha"]
student_ids = [203, 204, 205, 206, 207]
student_data2 = dict(zip(student_names, student_ids))
print(student_data2)


# Aliasing - two variable refers same dict
std_data = {'Rohan': 203, 'Ananya': 204, 'Priya': 205, 'Aman': 206, 'Sneha': 207}
std_data2 = std_data
print(id(std_data))
print(id(std_data2))


# cloning
original_dict = {'Rohan': 203, 'Ananya': 204, 'Priya': 205, 'Aman': 206, 'Sneha': 207}
copy_dict = original_dict.copy()
print(id(original_dict))
print(id(copy_dict))


# Searching
# search for key
print('Rohan' in original_dict)
# search for value
print(204 in original_dict.values())

# Identity
print(original_dict is copy_dict)

# Emptiness
sample = {}
if not sample:
    print('Empty Dict')


# Using Built-in Functions on Dictionaries'

students = {'Rohan': 203, 'Ananya': 204, 'Priya': 205, 'Aman': 206, 'Sneha': 207}
print(len(students))

print(max(students.values()))
print(min(students))
print(sorted(students.items()))         # sorted function returns sorted list
print(sum(students.values()))
print(any(students))
print(all(students))

for k, v in reversed(students.items()):
    print(k, v)



# Dictionary Methods

courses = {'CS101': 'CPP', 'CS102': 'DS', 'CS203': 'OOP', 'CS226': 'DAA'}
courses2 = {'CS601': 'Crypt', 'CS442': 'Web'}

# dict.get(key, default=None)
# The get() method in Python is used to access the value associated with a specified key in a dictionary.
# It provides a way to safely retrieve the value without raising a KeyError if the key does not exist.
# No error is raised when a key is not found.

# get()
print(courses.get('CS102', 'Absent'))
print(courses.get('EE102', 'Absent'))
# print(courses['EE102'])    # this will raise Key_error in absence of key in dict


# Update() - Update one dict with item in another dict
courses.update(courses2)
print(courses)


# pop()
print(courses.popitem())            # remove & return item in LIFO order
print(courses.pop('CS102'))         # remove key & returns its value

print(courses)

courses.clear()
print(courses)


# Dictionary Varieties

# keys must be Unique and Immutable , Numbers, Strings, Tuple, frozenset can be used as Keys.
# key should not contain mutable elements like list.


# Two Dictionaries can be merge to create third dictionary by unpacking the two dictionary using ** .
# If we use * only keys will be unpacked

animals = {'Tiger': 141, 'Lion': 152, 'Leopard': 110}
birds = {'Eagle': 38, 'Crow': 30, 'Parrot': 20}

print(animals)
print(birds)

# unpacking the two dictionary using **
combined = {**animals, **birds}
print(combined)

# If we use * only keys will be unpacked
combined2 = {*animals, *birds}
print(combined2)


# Dictionary contain different keys but same values can be created
# fromkeys() function

lst = [12, 13, 14, 15, 16]
d = dict.fromkeys(lst, 'A')
print(d)


"""
import operator

"""
Que 1: Create a dictionary called students containing names and ages. 
       Copy the dictionary to stud . Empty the students dictionary, as stud continues to hold the data
         

students = {'Anil': 23, 'Sanjay': 28, 'Ajay': 25}
print(students)

# shallow copy
stud = students
print(stud)

print(id(students))
print(id(stud))

# empty dictionary
students = {}       # refers to new object
print(students)
print(stud)         # still refers to the original dictionary


"""

"""
Que 2:- Create a list of cricketers. Use this list to create a dictionary in which 
        the list values become keys of the dictionary. Set the values of all keys to 50 in the dictionary created.


lst = ['Sunil', 'Sachin', 'Rahul', 'Kapil', 'Sunil', 'Rahul']
players = dict.fromkeys(lst, 50)

print(len(lst))
print(len(players))
print(players)
     
"""

"""
Que 3:- Write a program to sort a dictionary in ascending/descending order by key and 
        ascending/descending order by value.


d = {'Praveen': 52, 'Sachin': 40, 'Rahul': 36, 'Kapil': 47}
print('Original Dictionary :', d)


# ascending/descending order by key

# ascending by key
d1 = sorted(d.items())
print('Ascending in order by Key', d1)

# descending by key
d2 = sorted(d.items(), reverse=True)
print('Descending in order by Key', d2)


# ascending/descending order by value

# ascending by value
d3 = sorted(d.items(), key=operator.itemgetter(1))
print('Ascending in order by Value', d3)

# descending by value
d4 = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
print('Descending in order by value', d4)

"""

"""
Que 4:- Write a program to create three dictionary and concatenate them to create fourth dictionary.


dict1 = {"Apple": 150, "Mango": 100, "Pineapple": 120}
dict2 = {"Banana": 50, "Grapes": 80, "Watermelon": 60}
dict3 = {"Orange": 80, "Peach": 110, "Papaya": 70}

# to unpack in fourth dict
dict4 = {**dict1, **dict2, **dict3}
print(dict4)

# to unpack only keys
dict5 = {*dict1, *dict2, *dict3}
print(dict5)


# unpacking can also done using update()
dict6 = {}

for d in (dict1, dict2, dict3):
    dict6.update(d)

print(dict6)

"""

"""
Que 6:- Write a program to check whether a dictionary is empty or not.
 

d1 = {'Anil': 45, 'Ajit': 32}

if bool(d1):
    print("Dictionary is not Empty")

d2 = {}

if not bool(d2):
    print("Dictionary is Empty")

"""

"""
Que 6:- Suppose there are two dictionary boys and girls containing names as key and ages as value. 
        Write a program to merge the two dictionaries into third dictionary.


# Dictionary for boys
boys = {"John": 25, "Michael": 30, "David": 22}

# Dictionary for girls
girls = {"Emma": 28, "Sophia": 24, "Olivia": 26, "Sophia": 40}

# creating third dict
combine = {**boys, **girls}
combine2 = {**girls, **boys}

print(combine)
print(combine2)

"""

"""
Que 7:- For the following dictionary , write a program to report the maximum and minimum salary.


d = {
    'Anuj': {'salary': 10000, 'age': 20, 'height': 6},
    'Aditya': {'salary': 6000, 'age': 26, 'height': 5.6},
    'Rahul': {'salary': 7000, 'age': 24, 'height': 5.9}
}


salary_lst = []

for v in d.values():
    salary_lst.append(v['salary'])

print(salary_lst)

print(max(salary_lst))
print(min(salary_lst))

"""

"""
Que 8:- Suppose Dictionary contains roll numbers and names of students. 
        Write a program to receive the roll numbers, extract the name corresponding to the roll number
        and display a message Congratulating the student by his name. 
        If the roll number doesn't exist in the dictionary, the message should be 'Congratulations Students'.

# Answer starts here..        

"""
students = {101: 'Anil', 102: 'Sanjay', 103: 'Ajay', 104: 'Ravi', 105: 'Priya', 106: 'Neha'}

# take input of Roll number
roll_no = int(input('Enter Your Roll Number : '))
name = students.get(roll_no, ' Students')
print(f'Congratulations {name}!')

roll_no = int(input('Enter Your Roll Number : '))
name = students.get(roll_no, ' Students')
print(f'Congratulations {name}!')



