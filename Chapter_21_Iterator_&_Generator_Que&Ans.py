import itertools
import random

"""
Que 1:-  Write a program to create a list of 5 odd numbers. Replace the third element with list of 4 even integers.
         Flatten , sort and print the list


# list of odd numbers
lst = [1, 3, 5, 7, 9]
print(lst)

# Replace third element
x = [2, 4, 6, 8]
lst[2] = x
print(lst)

# Flatten
flatten_lst = [item for sublist in lst for item in (sublist if isinstance(sublist, list) else [sublist])]
print(flatten_lst)

# sort and print the list
print(sorted(flatten_lst))


"""


"""
Que 2 :- Write a program to flatten the following list:


mat1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

flatten_mat1 = [item for sublist in mat1 for item in sublist]
print(flatten_mat1)

"""


"""
Que 3:- Write a program to Generate a list of numbers in the range 2 to 50 that are divisible by 2 and 4. 


# Creating generator using generator expressions
gen = (num for num in range(2, 51) if num % 2 == 0 and num % 4 == 0)
print(gen)

lst = list(gen)

print(lst)

"""


"""
Que 4:- Suppose there are two lists, each holding 5 strings. Write a program to generate a list
        that consists of strings that are concatenated by picking corresponding elements from two lists.
        


fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]
colors = ["Red", "Blue", "Green", "Yellow", "Purple"]

# concatenated by picking corresponding elements from two lists
lst = [fruit + ' ' + color for fruit, color in zip(fruits, colors)]
print(lst)

"""


"""
Que 5:- Suppose a list contains 20 integers generated randomly. Received the number from the keyboard
        and report position of all occurrences of this number in the list. 

# Answer starts from here...

numbers = [random.randint(1, 15) for _ in range(21)]
print(numbers)

user_num = int(input('Enter a number Between 1 to 15 :- '))

# position of number in list
position = [index for index, n in enumerate(numbers) if n == user_num]


if position:
    print(f"Positions of all occurrences of {user_num} in the list: {','.join(map(str, position))}")
else:
    print(f"The number {user_num} does not exit inside list")


"""


"""
Que 6:- Suppose there are two list one contain Questions and another contain 4 possible answer for each question.
        Write a program to generate a list that contain list of question and its four possible answers.

# Answer starts here...

# list of questions
questions = [
    "What is your name?",
    "How old are you?",
    "Where are you from?",
    "What is your favorite color?",
    "Do you like pets?"
]


# list of possible answers
options = [
    ["a) John", "b) Alice", "c) Bob", "d) Sam"],  # Options for "What is your name?"
    ["a) 20", "b) 25", "c) 30", "d) 35"],        # Options for "How old are you?"
    ["a) New York", "b) Paris", "c) Tokyo", "d) London"],  # Options for "Where are you from?"
    ["a) Blue", "b) Green", "c) Red", "d) Yellow"],  # Options for "What is your favorite color?"
    ["a) Yes", "b) No", "c) Sometimes", "d) Maybe"]  # Options for "Do you like pets?"
]


combine_lst = [[que, opt] for que, opt in zip(questions, options)]
lst = list(combine_lst)
print(lst)


"""


"""
Que 7:- Suppose a list has 20 numbers. Write a program that removes all duplicates from this list.
 
# Answer starts here...


# first way to solve problem
numbers = [5, 12, 7, 9, 12, 7, 15, 18, 5, 11, 19, 20, 15, 18, 9, 11, 19, 20, 3, 21]

lst = list(set(numbers))
print(lst)


# Second way to solve the problem
sorted_numbers = sorted(numbers)
print(sorted_numbers)

unique_numbers = [key for key, group in itertools.groupby(sorted_numbers)]

ls = list(unique_numbers)
print(ls)

"""


"""
Que 8:- Write a program to obtain a median value of a list of numbers, 
        without disturbing the order of the numbers in the list.

# Answer starts here...

# first way 

def median_of_list(data):
    # create a copy of list
    data_copy = data.copy()

    # sort the copied list
    data_copy.sort()

    # calculating median based on sorted copy
    n = len(data)

    if n % 2 == 1:
        # Odd number of elements: middle value
        median = data_copy[n//2]
        return median
    else:
        # Even number of elements: average of the two middle values
        mid1 = data_copy[n//2 - 1]
        mid2 = data_copy[n//2]
        median = mid1 + mid2 / 2
        return median


original_list = [40, 10, 30, 50, 20, 25, 45, 15]
median_value = median_of_list(original_list)

print("Original list:", original_list)
print("Median value:", median_value)


# Second way - using generator expression

numbers = [15, -7, 22, -3, 10, -12, 8, -5, 30, -20, 5, -2]
print(numbers)

# Step 1: Sort the numbers
sorted_numbers = sorted(numbers)

# Step 2: Calculate median using generator expressions
n = len(sorted_numbers)
if n % 2 == 1:
    # Odd case: median is the middle value
    median = (x for i, x in enumerate(sorted_numbers) if i == n // 2).__next__()
else:
    # Even case: median is the average of the two middle values
    gen = (x for i, x in enumerate(sorted_numbers) if i in {n // 2 - 1, n // 2})
    median = sum(gen) / 2

print(f"The median is {median}")


"""


"""
Que 9:- A list contains only positive and Negative integers. Write a program 
        to obtain the number of negative numbers present in the list.


numbers = [15, -7, 22, -3, 10, -12, 8, -5, 30, -20, 5, -2]
print(numbers)

count = 0
for n in numbers:
    if n < 0:
        count += 1

print(f'Count of negative numbers present in list is {count}')


# Count negative numbers using a generator expression

count_neg = sum(1 for n in numbers if n < 0)
print(f'Count of negative numbers present in list is {count_neg}')

"""

"""
Que 10:- Write a program to convert list of tuple to another list of tuple.


data = [(10, 20, 30), (150.55, 145.80, 157.65), ('A1', 'B1', 'C1')]

n, f, s = zip(*data)
print(n, f, s)

lst = list((n, f, s))
print(lst)

"""


"""
Que 11:- What will be the output of program ?

# Answer starts here

x = [[1, 2, 3, 4], [5, 6, 7, 8]]
y = [[1, 2], [3, 4], [5, 6], [7, 8]]

l1 = [xrow for xrow in x]
print(l1)

l2 = [ycol for ycol in zip(*y)]
print(l2)

lst = [(xrow, ycol) for ycol in zip(*y) for xrow in x]
print(lst)


"""


"""
Que 12:-  Write a program that use a Generator to create a set of unique words from a line
          input through the keyboard.

# Answer starts here...

user_input = input('Enter a sentence ...:- ')

gen = (word for word in (user_input.lower()).split(' '))
print(gen)

s = set(gen)
print(s)


"""


"""
Que 13:- Write a program that uses a generator to find out maximum marks obtain by a students 
         and his name from tuple of multiple students.

# Answer starts here...


students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 88), ("Eve", 92), ("Frank", 81)]

# find max marks in list of students
max_marks = max(mark for _, mark in students)
print(max_marks)

# generate a student name and marks who have max marks
top_students_gen = ((student, marks) for student, marks in students if marks == max_marks)
print(top_students_gen)

top_student = list(top_students_gen)
print(top_student)


"""


"""
Que 14:- Write a program that uses a generator that generates characters from a string in reverse order.  

# Answer starts here..

s = 'generator'

rev_string_gen = (alpha for alpha in s[::-1])
print(rev_string_gen)
for a in rev_string_gen:
    print(a, end='')


"""


"""
Que 15:- what are the difference between the following statements.


lst = [x**2 for x in range(20)]
print(lst)

gen = (x**2 for x in range(20))
print(gen)
for a in gen:
    print(a, end=',')
    

s1 = sum([x**2 for x in range(20)])
s2 = sum(x**2 for x in range(20))
print(s1)
print(s2)


"""


"""
Que 16:- Suppose there are two list, each holding 5 strings write a program to generate a list that consist 
         of strings that are concatenated by picking corresponding element from the two list.

# Answer starts here..

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
colors = ["red", "yellow", "red", "brown", "purple"]


concat_string = ((f + '_' + c) for f, c in zip(fruits, colors))
print(concat_string)

# list of concatenated of two lists
lst = list(concat_string)
print(lst)

"""


"""
Que 17:- 36 Unique combinations can result from use of two dice. create a dictionary which 
         stores these combination as tuples.
"""

# dice have 6 possible values
d1 = [1, 2, 3, 4, 5, 6]
d2 = [1, 2, 3, 4, 5, 6]


# creating generator that have 36 unique combinations
dic_gen = ((ele1, ele2) for ele1 in d1 for ele2 in d2)
print(dic_gen)

# adding combination as index and the combination as tuple inside dictionary.
dic = {index: combination for index, combination in enumerate(dic_gen)}
print(dic)






