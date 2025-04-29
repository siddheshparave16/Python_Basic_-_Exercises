"""
Que A:- What will be the output of following program


# a
msg = list('www.kicit.com')
ch = msg[-1]
print(ch)

msg2 = list('kanlabs.techable.com')
s = msg2[4:6]
print(s)

s2 = msg2[:3]
print(s2)

s3 = msg2[-5:-2]
print(s3)

t = msg2[::-1]
print(t)



# f :-

num1 = [10, 20, 30, 40, 50]
num2 = num1

# both refers same object (Aliasing)
print(id(num1))
print(id(num2))

print(type(num2))
print(isinstance(num1, list))
print(num1 is num2)

num1[2:4] = []
print(num1)


n1 = [10, 20, 30, 40, 50]
n2 = [60, 70, 80]
n1.append(n2)
print(n1)


l = [10, 25, 4, 12, 3, 8]
print(sorted(l))
print(l)

a = [1,2,3,4]
b = [1,2,5]
print(a<b)

ls = [10, 25, 4, 12, 3, 8]
ls.sort(reverse=True)
print(ls)
a = 30 in ls
print(a)

ls.insert(2, 30)
print(ls)

s = 'Hello'
lst = [*s]
print(lst)

"""
import random

"""
Que 1:- Write a program to create a list of 5 odd integers. Replace the third element with
        a list of 4 even integers. Flatten, sort, and print the list

# Answer starts here...

# creating empty list
num = []

count = 0
i = 1
while count < 5:
    # check for odd integer and add into list
    if i % 2 != 0:
        num.append(i)
        count += 1
    i += 1

print("List with 5 odd integers:- ", num)

num[3] = [2, 4, 6, 8]

print("List after replacing the third element:", num)

# so now  [1, 3, 5, [2, 4, 6, 8], 9, 11] will your multi dimentional list

# creating flatten list
# flattened_list = [1, 3, 5, *[2, 4, 6, 8], 11]
flattened_list = [item for a in num for item in (a if isinstance(a, list) else [a])]
print("Flattened List:-", flattened_list)
flattened_list.sort()
print(" Sorted List :-", flattened_list)

"""

"""
Que 2:- Suppose a list contain 20 integers generated randomly. Receive the number from a keyboard and
       report position of all occurrences of this number in the list.
       
# Answer starts here...       


# creating empty list
num = []


i = 0
while i < 20:
    n = random.randint(1, 100)
    num.append(n)
    i += 1

# Generating random Integers
user_num = int(input("Enter a number between 1, 100 :- "))


# Check if the number is in the list
if user_num in num:
    # Find all positions of the number in the list
    positions = [index for index, value in enumerate(num) if value == user_num]
    # Count the occurrences of the number
    count = len(positions)
    print(f"The number {user_num} occurs {count} time(s) at positions: {positions}")
else:
    print(f"{user_num} not present in List.")


# Optionally print the list
print("List of numbers:", num)


"""

"""
Que 3:- Suppose a list has 20 Numbers. Write a program that removes all duplicates from this list.

# Answer starts here...

# Initial list with duplicates
num = [6, 72, 94, 34, 72, 80, 45, 65, 35, 93, 6, 94, 2, 34, 54, 81, 71, 59, 6, 98]
print('Original list :- ', num)

# # Temporary list to store unique elements
unique_num = []

for n in num:
    if n not in unique_num:
        unique_num.append(n)


# print('unique_num', unique_num)

# Update the original list with unique elements
num[:] = unique_num
print('Original List after removing Duplicates :- ', num)

"""

"""
Que 4:- Suppose a list contains positive and negative numbers.
        Write a program to create two lists- one contain positive numbers and another contain negative.

# Answer starts here...        


# list of negative and positive numbers.
num = [10, 47, 77, -85, -54, 98, -100, 40, 90, 1, -34, 50]

# creating an Empty strings
positive_nums = []
negative_nums = []
zeros_nums = []

# iterating through each element in list
i = 0
while i < len(num):
    if num[i] < 0:
        negative_nums.append(num[i])
    elif num[i] > 0:
        positive_nums.append(num[i])
    else:
        zeros_nums.append(num[i])
    i += 1

print("Positive Number List :- ", positive_nums)
print('Negative Number List :- ', negative_nums)
print('Zeros Number List :- ', zeros_nums)

"""

"""
Que 5:- Suppose the list contain 5 strings. write a program to convert all these strings to uppercase.

# Answers starts here ....


animals = ['Lion', 'Cat', 'Dog', 'Elephant', 'Tiger']
print(f'List before :- {animals}')


for i in range(len(animals)):
    animals[i] = animals[i].upper()

print(f'List after :- {animals}')

"""

"""
Que 6:- Write a program that convert list of temperature in Fahrenheit degree 
        to equivalent Celsius degrees.
        
# Answer starts here..
°C = °F-32 * 9/5


# Temperature list in Fahrenheit
fahrenheit_lst = [75.2, 78.85, 96.8, 93.2, 66.2, 86.0]

# convert list of temperature to Fahrenheit in celsius
celsius_lst = []

for fahrenheit in fahrenheit_lst:
    celsius = (fahrenheit-32) * (5/9)
    celsius_lst.append(round(celsius, 2))

print("Temperatures in Fahrenheit:", fahrenheit_lst)
print('Equivalent temperatures in Celsius :- ', celsius_lst)


"""

"""
Que 7:- Write aa program to obtain a median value of a list of numbers, 
        without Disturbing the order of the numbers in the list. 
        
# Answer starts here...        


# Given list
numbers = [63, 47, 77, 85, 54, 98, 72, 68, 90, 45, 57, 70]

# Create a sorted copy of the list
sorted_number = sorted(numbers)

# Calculate the median
n = len(sorted_number)

if n % 2 == 0:      # Even number of elements
    median = (sorted_number[n//2 - 1] + sorted_number[n//2])/2
else:       # Even number of elements
    median = sorted_number[n//2]


# Print the median without disturbing the original list
print("Original List:", numbers)
print("Sorted List:", sorted_number)
print("List Length :", len(sorted_number))
print("Median:", median)


"""

"""
Que 8:- A list contain only positive and negative Integers. 
        Write a program to obtain the number of negative numbers present in the list.
        
# Answer starts here...

# Given list
numbers = [10, 47, 77, -85, -54, 98, -68, 40, 90, -18, -34, 50]

# Initialize counter for negative numbers
negative_num = []
negative_count = 0

# Iterate through the list to count negatives
for index, num in enumerate(numbers):
    # check number is negative
    if num < 0:
        negative_num.append(num)
        negative_count += 1

print(f"the number of negative numbers present in the list is {negative_num} and count is {negative_count}.")

"""

"""
Que 9:- Suppose a list contain several words. Write a program to create another list 
        that contain first character of each word present in the first list.

# Answer starts here...

# given list
words = ['Lion', 'Leaf', 'Cat', 'Each', 'Elephant', 'Life', 'Tiger']

# Initialize an empty list to store the first letters
first_letter = []

# Extract the first character of each word
for word in words:
    first_letter.append(word[0])

print("list that contain first character of each word :- ", first_letter)


"""

"""
Que 10:- A list contains 10 numbers. Write a program to eliminate all duplicate from the list.

# Answer starts here...


numbers = [26, 32, 96, 25, 46, 16, 72, 41, 96, 16]
print("Original list :- ",  numbers)

# Loop through the list and remove duplicates
i = 0
while i < len(numbers):
    if numbers.count(numbers[i]) > 1:
        numbers.remove(numbers[i])       # Remove duplicate
    else:
        i += 1      # Move to the next element only if no duplicate is found

print("list after removing duplicates :- ", numbers)

"""


"""
Que 11:- Write a program to find the mean, median and mode of a list of 10 numbers.

# Answer starts here...
mean - (Sum of data values) / (Number of data values)
Median - (n th term (n//2 - 1 ) + n th term (n//2)) / 2
Mode = 3 Median – 2 Mean

"""

# Original List
numbers = [26, 32, 25, 46, 72, 41, 96, 46, 64, 84]
print('Original list :- ', numbers)

# sort the given list
sorted_numbers = sorted(numbers)
print('Sorted number list :- ', sorted_numbers)
num_len = len(sorted_numbers)

# Mean
mean = sum(sorted_numbers) // num_len

# Median
median = (sorted_numbers[num_len//2 - 1] + sorted_numbers[num_len//2])/2

# Mode
mode = max(sorted_numbers, key=sorted_numbers.count)

print("Mean for given list is ", mean)
print("Median for given list is", median)
print("Mode for given list is", mode)


