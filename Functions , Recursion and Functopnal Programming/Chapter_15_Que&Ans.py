import functools
import math
import operator

"""
Que1 :- Suppose a dictionary contains type of pet (cat, dog, etc.), name of pet and age of pet.
        Write a program that obtains the sum of all Dog's ages.


pets = [
        {"type": "cat", "name": "Whiskers", "age": 3}, {"type": "dog", "name": "Buddy", "age": 5},
        {"type": "cat", "name": "Mittens", "age": 2}, {"type": "dog", "name": "Max", "age": 4},
        {"type": "cat", "name": "Luna", "age": 1}, {"type": "dog", "name": "Rocky", "age": 6},
        {"type": "cat", "name": "Shadow", "age": 4}, {"type": "dog", "name": "Bella", "age": 3},
        {"type": "cat", "name": "Oliver", "age": 2}, {"type": "dog", "name": "Charlie", "age": 5}
    ]


dog_ages = list(map(lambda pet: pet['age'], filter(lambda pet: pet['type'] == 'dog', pets)))
sum_of_ages = functools.reduce(lambda a, b: a+b, dog_ages)
print(sum_of_ages)

"""

"""
Que 2:- Consider the following list:
        lst = [1.23, 3.22, 4.68, 10.95, 32.55, 12.54]
        
        The numbers in the list represent radius of circles. Write a program to obtain a list of
        areas of these circles rounded off to two decimal places.


lst = [1.23, 3.22, 4.68, 10.95, 32.55, 12.54]

areas_of_circle = list(map(lambda x: math.pi * x ** 2, lst))
print(areas_of_circle)
formatted_area = [f'{area: .2f}' for area in areas_of_circle]
print(formatted_area)

"""

"""
Que 3:- Consider the following lists:

        Write a program to obtain a list of tuples, where each tuple contains a number from one list
        and string from another , in the same order in which they appear in the original lists.


nums = [10, 20, 30, 40, 50, 60, 70, 80]
strs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Combine the two lists into a list of tuples
combine_list = list(map(lambda x, y: (x, y), nums, strs))

# Print the combined list of tuples
print(combine_list)

"""

"""
Que 4:- Suppose a dictionary contains names of students and marks obtained by them in an examination.
        Write a program to obtain list of students who obtained more than 80 marks in the examination.


students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 78},
    {"name": "Charlie", "marks": 92},
    {"name": "David", "marks": 64},
    {"name": "Eva", "marks": 88},
    {"name": "Frank", "marks": 73},
    {"name": "Grace", "marks": 95},
    {"name": "Hannah", "marks": 81},
    {"name": "Isaac", "marks": 67},
    {"name": "Jack", "marks": 90},
]

marks_more_than_80 = mfilter(lambda student: student['marks'] > 80, students)
print(list(marks_more_than_80))

"""

"""
Que 5:- Consider the following list
        write a program to print those strings which are palindrome.
        

lst = ['Malayalam', 'Drawing', 'madamlamadam', 1234321]

filtered_lst = filter(lambda x: str(x).lower()[::-1] == str(x).lower(), lst)
print(list(filtered_lst))


"""

"""
Que 6:- A list contain names of employees. Write a program to filtered out 
        those names who's length is more than 8 characters


employee_names = ['John', 'Samantha', 'Dominique', 'Alice', 'Charlotte', 'David', 'Katherine', 'Olivia']

filtered_name = filter(lambda name: len(name) > 8, employee_names)
print(list(filtered_name))

"""

"""
Que 7:- A Dictionary contain following information about 5 employees:
        first name, last name, age, grade( skilled, semi-skilled, highly skilled)
        write a program to obtain a list of employees ( first name + last name) who are highly skilled
        


employees = [
    {'first_name': 'John', 'last_name': 'Doe', 'age': 28, 'grade': 'skilled'},
    {'first_name': 'Alice', 'last_name': 'Smith', 'age': 34, 'grade': 'highly skilled'},
    {'first_name': 'Bob', 'last_name': 'Johnson', 'age': 25, 'grade': 'semi-skilled'},
    {'first_name': 'Emma', 'last_name': 'Brown', 'age': 30, 'grade': 'skilled'},
    {'first_name': 'Chris', 'last_name': 'Lee', 'age': 40, 'grade': 'highly skilled'}
]

filtered_emp = map(lambda emp: emp['first_name'] + emp['last_name'],
                   filter(lambda emp: emp['grade'] == 'highly skilled', employees))

print(list(filtered_emp))


"""


"""
Que 8:- Considered a following list:
        write a program to obtain a string 'Benevolent Dictator For Life'.

lst = ['Benevolent', 'Dictator', 'For', 'Fife']

sentence = functools.reduce(lambda x, y: x + " " + y, lst)
print(sentence)


"""


"""
Que 9:- Considered the following list of students in a class.
        
        Write a program to obtain list in which all names converted to uppercase.
"""

lst = ['Rahul', 'Priya', 'Chaaya', 'Narendra', 'Prashant']

upper_case_lst = map(lambda name: name.upper(), lst)
print(list(upper_case_lst))







