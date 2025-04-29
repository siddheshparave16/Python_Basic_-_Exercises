import collections
import random

"""
# define a list in [] by comma-separated elements
num = [10, 20, 30, 40, 50]
names = ['Sanjay', 'Anil', 'Radha', 'Suparna']

# list with Dissimilar data-types
animal = ['Zebra', 'Cat', 155.53, 10]

# Items in list can be repeated, list may contain Duplicate Items
ages = [25, 26, 22, 27, 25]
numbers = [10]*5

# list can be printed using name of list
print(numbers)

# list can empty
lst = []

# Accessed list elements
print(ages[1], ages[3])

# like string List can be sliced
print(ages[1:3])
print(ages[3:])


# Looping in List
animals = ['Tiger', 'Lion', 'Cat', 'Dog', 'Kangaroo']

# Iterate through loop

# Using while loop
i = 0
while i < len(animals):
    print(animals[i], end=" ")
    i += 1

print()

# Using for loop
for animal in animals:
    print(animal, end="|")

print()

# Iterating through a list if you wish to keep track of index you can use enumerate() function
for index, animal in enumerate(animals):
    print(index, animal, end="  ")


# Basic List Operations

# List is mutable( changeable )

animals = ['Tiger', 'Lion', 'Cat', 'Dog', 'Kangaroo']
print("List before change made :- \n", animals)

# to change an element of list at particular index
animals[2] = 'Rhinoceros'         # change the element cat to Rhinoceros
print("List after change made :-\n", animals)


age = [26, 23, 25, 29, 21, 19, 26, 27]
print("Original list:-\n", age)

print("after operations on List :- ")
# index 5 change element
age[5] = 31
print(age)

age[2:5] = [20, 22, 30]             # set items 2-4 by values 20,22,30
print(age)

age[6:8] = []
print(age)


# Concatenation :- concatenate one list with another at the end of first one

lst = [12, 25, 18, 29, 16, 38, 11]
lst = lst + [33, 44, 55]
print(lst)


# Merging - Two list can be merged to create a new list
s = [10, 20, 30]
t = [100, 200, 300]
w = s + t
print(w)


# Conversion - convert string,tuple and set to list
n_list = list('Africa')
print(n_list)


# Aliasing or shallow copy - Assigning one list to another
lst1 = [10, 20, 30, 40, 50]
lst2 = lst1               # lst2 doesn't copy a list , its refers to same list
print(lst1)
print(lst2)
print(id(lst1))             # its gives same address location
print(id(lst2))

# change in one list change another
lst1[0] = 100
print(lst1[0], lst2[0])



# Coping the list - Change in one Doesn't change another
lst1 = [10, 20, 30, 40, 50]
lst2 = []
lst2 = lst2 + lst1
print(lst1)
print(lst2)

lst1[0] = 100
print(lst1[0], lst2[0])



# Searching - using 'in' Membership operator
lst = ['a', 'e', 'i', 'o', 'u']
res = 'a' in lst
res2 = 'z' in lst
print(res)
print(res2)


# identity - Using 'is' identity operator
lst1 = [10, 20, 30, 40, 50]
lst2 = [10, 20, 30, 40, 50]
lst3 = lst1
print(lst1 is lst2)
print(lst1 is lst3)
print(lst1 is not lst2)

print()
print(id(lst1))
print(id(lst2))


num1 = 10
num2 = 10
print(id(num1))
print(id(num2))


# comparison - compare of two lists , it is done by item by items till there mismatch

a = [1, 2, 3, 4]
b = [1, 2, 5]
print(a < b)


# Emptiness - can check list is empty using not operator
lst = []
if not lst:
    print('Empty list')

print(bool(lst))


# Using built-in functions on string
num_lst = [10, 20, 30, 40, 0, 60, 70, 80]
print(len(num_lst))
print(max(num_lst))
print(min(num_lst))
print(sum(num_lst))
print(any(num_lst))
print(all(num_lst))                 # if element equivalent to zero will return false

num_lst2 = [10, 20, 30, 40, 0, 60, 70, 80]
del(num_lst2[3])
print(num_lst2)
del(num_lst2[2:5])
print(num_lst2)
del(num_lst2[:])
print(num_lst2)

n1 = [10]
n2 = [10]

print(id(n1))
print(id(n2))

l1 = [10, 30, 20, 50, 40]
l3 = l2 = l1
l1 = []
print(l2)
print(l3)

l2[:] = []
print(l2)
print(l3)



#  List Methods
# Accessing the list methods by using list_object.method()

num = [12, 15, 16, 19, 18, 11, 14]

# append - adding new item at the end
num.append(21)

# remove - delete the item from the list , if item not in list it will through ValueError
num.remove(11)
print(num)

# pop - remove the last item in the list
num.pop()
print(num)


# insert - adding an item at particular index
num.insert(3, 22)
print(num)

# count - return number of times item appear in list
print(num.count(15))

# index - return a index of item
print(num.index(19))



# Sorting and reversing a list
# reverse() and sort() does not return a list , Both Manipulate the list in place.

lst = [10, 2, 28, 9, 16, 5, 21, 30, 1, 12]
print("List before...", lst)
lst.reverse()
print("List After Reversing...", lst)

lst.sort()
print("List After sorting...", lst)

lst.sort(reverse=True)
print("sorting Items in Reverse order...", lst)

print(lst)

print(sorted(lst))              # sorted function returns new sorted list
print(sorted(lst, reverse=True))

# using slicing possible to reverse a list
print(lst[::-1])
print(lst)




# List Varieties

# it is possible to create list of list (nested list)
a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]

c = [a, b]
print(c)

print(c[0][0], c[1][2])


# list may be embedded in another list
x = [1, 2, 3, 4]
y = [10, 20, x, 30]
print(y)


# unpack a string or list within a list
s = 'Hello'
l = [*s]
print(l)

n = [10, 20, 30, 40]
y = [1, 2, *n, 3]
print(y)

a = []
print(bool(a))

"""
# ---------------------------------------------------------------------------------
# Solved Que

"""
Que 1:- Perform following operations on the list of names

# answer starts here


# create a list of 5 names
names = ['Anil', 'Amol', 'Aditya', 'Avi', 'Alka']
print(names)

# Insert name Anuj before Aditya
names.insert(2, 'Anuj')
print(names)

# Append a name 'Zulu
names.append('Zulu')
print(names)

# delete Avi from list
names.remove('Avi')
print(names)

# Replace Anil with Anilkumar
names[0] = 'Anilkumar'
print(names)

# Sort all the names in the list
names.sort()
print(names)

# Print the reversed sorted list
names.reverse()
print(names)

"""

"""
Que 2:- Perform the list following operation on the list of numbers.

# Answer starts here .....


# create a list of odd numbers
a = [1, 3, 5, 7, 9]
print(a)

# create a list of Even numbers
b = [2, 4, 6, 8, 10]
print(b)

# combine two list
c = a + b
print(c)

# Add prime numbers 11,17,29 at the beginning of the combined list
c = [11, 17, 29] + c
print(c)

# Report how many elements are present in the list
num = len(c)
print(num)

# Replace last 3 numbers in the list with 100, 200, 300
c[num-3:num] = [100, 200, 300]
print(c)

# delete all the numbers in the list
c[:] = []
print(c)

# delete the list
del c

"""

"""
Que 3:- Write a program to implement a stack data structure. Stack is a Last In First Out (LIFO)
        list in which addition and deletion takes place at the same end.
        
# Answer starts here...        


# stack - LIFO list
# empty stack
s = []

# push the element on stack
s.append(10)
s.append(20)
s.append(30)
s.append(40)
s.append(50)
print(s)

# pop the element from stack
print(s.pop())
print(s.pop())
print(s.pop())
print(s)

"""

"""
Que 4:- Write a program to implement a Queue data structure. Queue is First In First Out (FIFO) list,
        in which addition takes place at the end of the queue and deletion takes place at the front end of the queue. 


q = collections.deque()

q.append('Suhana')
q.append('Shabana')
q.append('Shakila')
q.append('Shakira')
q.append('Sameera')
print(q)

# In Deque deletion takes place in both end of queue
print(q.popleft())                      # delete item from front end
print(q.pop())                          # delete item from last end
print(q.popleft())
print(q)

"""

"""
Que 5:- Write a program to generate and store in a list 20 random number in range 10 to 100.
        from this list delete all those entries which have value between 20 and 50. print the remaining list.

#  Answer starts here.... 


# creating en Empty list
a = []

# store 20 random numbers in list

i = 1
while i <= 20:
    # generating random number
    num = random.randint(10, 100)
    a.append(num)
    i += 1

print("Original List:- ", a)

# delete those  entries which have value between 20 and 50

a = [num for num in a if not (20 < num < 50)]

print('Filtered list :- ', a)

"""


"""
Que 6:- Write a program to add two 3x4 matrices.

# Answers starts here...

"""
# two matrices of 3X4
mat1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
mat2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


# addition of two matrices will resultant matrices
mat3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# iterating through row
for i in range(len(mat1)):
    # iterating through column
    for j in range(len(mat1[0])):
        mat3[i][j] = mat1[i][j] + mat2[i][j]


print(mat3)








