import random

"""
Comprehensions - Easy and compact easy to creating lists, sets and dictionary.
- comprehensions works by looping or iterating over the elements by assigning them to container
  like list, set, Dictionary.
- this container cannot be tuple, as Tuple being immutable is unable to receive assignments.

- consist of brackets contain expression followed by for clause, and zero or more for or if clauses.

- General Expression -
    [ expression for var in sequence [optional for and/or if]
    
    

# Examples of List Comprehensions

# Generate 20 random numbers in range of 10 to 100.
# assigning to a container List.
num_lst = [random.randint(1, 100) for num in range(20)]
print(num_lst)


# Generate square and cube of numbers between 0 to 10 .
numbers = [(num, num**2, num**3) for num in range(10)]
print(numbers)


# Convert the list of strings to a list of Integer.
a = [int(s) for s in ['10', '20', '30', '40']]
print(a)


# Examples of use of if in list comprehensions:

# Generate a list of even numbers in the range 10 to 30.
even_numbers = [num for num in range(10, 31) if num % 2 == 0]
print('Even number in 10 to 30 :', even_numbers)


# from a list delete all numbers having value between 20 and 50.
lst = [13, 27, 37, 78, 69, 58, 82, 88, 73, 47, 38, 16, 88, 45, 20, 76, 94, 30, 37, 10]
print('Original List', lst)
lst = [num for num in lst if num < 20 or num > 50]
print('List after deleting numbers between 20 to 50 : \n', lst)


# Example of if-else in list Comprehensions

# when if-else both are used, place them before for

# replace a vowel in a string with !.

word = ['!' if alphabet in 'aeiou' else alphabet for alphabet in 'Technical']
print(word)


# Example of use of multiple for and if in list comprehension:

# flatten a list of lists
arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
arr_lst = [n for ele in arr for n in ele]
print(arr_lst)

arr_lst2 = [*arr[0], *arr[1], *arr[2]]
print(arr_lst2)


# nested for in list comprehension use for to obtain flatten list or iterating over nested list.
n = [a + b for a in [1, 2, 3] for b in [4, 5, 6]]
print(n)


# nested comprehensions use to form nested lists
n1 = [[a+b for a in [1, 2, 3]] for b in [4, 5, 6]]
print(n1)

# Examples of use of multiple for and if in list comprehensions.

# Generate all unique combinations of 1, 2 and 3.
c = [(i, j, k) for i in [1, 2, 3] for j in [1, 2, 3] for k in [1, 2, 3] if i != j and j != k and k != i]

print('All Unique combinations of 1, 2, 3 are : \n', c)


"""

"""
Set Comprehensions:- 
- offers an easy way to creating a sets.
- It consist of braces containing expressions followed by a for clause, and zero or more for or if .
s = {expression for var in statements [optional for and if]} 


# Generate a set containing square of numbers between 0 to 10.
s = {num ** 2 for num in range(11)}
print(s)

# from above set delete all numbers between 20 to 50.
a = [num for num in s if num < 20 or num > 50]
print(a)


"""

"""
Dictionary Comprehensions
- General form
dict_var = {key:value for (key, value) in d.items()}


d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# obtain dictionary with each value cube
d1 = {k: v**3 for (k, v) in d.items()}
print(d1)


# obtain dictionary with each value cubed if value > 3
d2 = {k: v**3 for (k, v) in d.items() if v > 3}
print(d2)


# Identify odd and even entries in the dictionary
d3 = {k: ('Even' if v % 2 == 0 else 'Odd') for (k, v) in d.items()}
print(d3)


"""

"""
Que 1:- Using list comprehension, write a program to generate a list of numbers 
    in the range 2 to 50 that are divisible by 2 and 4.

numbers = [num for num in range(2, 51) if num % 2 == 0 and num % 4 == 0]

print("List of numbers between 2 to 50 that are divisible by 2 & 4 :\n", numbers)

"""

"""
Write a program to flatten the following list using list comprehension:

# given  nested list
mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

flatten_mat = [num for ele in mat for num in ele]
print(flatten_mat)

"""

"""
Que 3:- Write a program to create a set containing some randomly generated numbers in the range 15 to 45.
        Count how many of these numbers are less than 30. Delete all numbers which are less than 30
        
# Answer starts here...

# Generate 10 numbers
numbers = {random.randint(15, 45) for i in range(10)}
print('Generate 10 random numbers :', numbers)

# count of numbers less than 30
count = len({num for num in numbers if num < 30})
print('Count of numbers less than 30 :', count)

# updated set after removing numbers less than 30
numbers = {num for num in numbers if num > 30}
print('Updated set after removing numbers less than 30 :', numbers)

"""

"""
Que 4:- Write a program using list comprehension to eliminate empty tuples from a list of tuples.

lst = [(1, 2), (3, 4), (), (5, 6), (), (7, 8), (9, 10), (), (11, 12), (13, 14), ()]
print(lst)

lst = [tpl for tpl in lst if tpl]
print(lst)

"""

"""
Que 5:- Given a string, split in on whitespace, capitalize each element of the resulting list
        and join them back into a string. Your implementation should use a list comprehension.
         
# Answer starts here

s1 = 'dream may change, but friends are forever.'

# capitalize each element of the resulting list
s2 = [' '.join(word.capitalize() for word in s1.split())]

# resulting string
s3 = s2[0]
print(s3)

"""

"""
Que 6:- From a dictionary with string keys create a new dictionary with the vowels removed from the keys.
 

words_dict = {"apple": 1, "banana": 2, "cherry": 3, "date": 4}

# creating new dictionary with the vowels removed from the keys

d = {''.join(alpha for alpha in k if alpha not in 'aeiou'): v for (k, v) in words_dict.items()}
print(d)

"""

"""
Que 7:- Write a program to add two 3 X 4 matrices using
        a) list     b) list comprehensions 

# Answer starts here...

mat1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
mat2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# resultant matrix
mat3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
mat4 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# using list

# iterate through rows
for i in range(len(mat1)):
    # iterate through columns
    for j in range(len(mat1[0])):
        mat3[i][j] = mat1[i][j] + mat2[i][j]

print(mat3)

# using list comprehensions
mat4 = [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
print(mat4)


"""

"""
Que 8:- Suppose a dictionary contains following information for 5 Employees
        
        using dictionary comprehensions, write a program to create :
        
"""

emp = {
        'A101': {'name': 'Ashish', 'age': 30, 'salary': 21000},
        'B102': {'name': 'Dinesh', 'age': 25, 'salary': 12200},
        'A103': {'name': 'Ramesh', 'age': 28, 'salary': 11000},
        'D104': {'name': 'Akheel', 'age': 30, 'salary': 18000},
        'A105': {'name': 'Akash', 'age': 32, 'salary': 20000}
      }


# Dictionary of all codes and values, where codes that start with 'A'.
emp_dict = {k: v for (k, v) in emp.items() if k.startswith('A')}
print('\n Dictionary of Codes startswith "A" :\n', emp_dict)


# Dictionary of all codes and names
code_name_dict = {k: v['name'] for (k, v) in emp.items()}
print("\n Dictionary of all codes and names :\n", code_name_dict)


# Dictionary of codes and ages
code_age_dict = {k: v['age'] for (k, v) in emp.items()}
print("\n Dictionary of all codes and ages :\n", code_age_dict)

# Dictionary of all codes and ages, where age is more than 30.
age_dict = {k: v for (k, v) in emp.items() if v['age'] > 30}
print("\nDictionary of all codes and ages, where age is more than 30 :\n", age_dict)

# Dictionary of all codes and names, where names that start with 'A'.
emp_name_dict = {k: v['name'] for (k, v) in emp.items() if v['name'].startswith('A')}
print("\n Dictionary of employee who's name startswith A :\n", emp_name_dict)


# Dictionary of all codes and salaries, where salary is in the range 13000 to 20000.
emp_salary_dict = {k: v['salary'] for (k, v) in emp.items() if 13000 < v['salary'] <= 20000}
print("\n Dictionary of Employee who's salaries in range 13000 to 20000 :\n", emp_salary_dict)





