"""
Que 1:- Following program to calculate sum of first 5 natural numbers using tail recursion and head recursion.



# Tail Recursion


def sum_of(n, total_sum=0):

    if n == 0:
        return total_sum
    else:
        return sum_of(n-1, total_sum+n)


num = int(input('Enter a positive Integer : '))

if num < 0:
    print('Kindly enter positive Integer')
else:
    print(sum_of(num))


# head recursion


def sum_of2(n):

    if n == 0:
        return 0
    else:
        return n + sum_of2(n-1)


num1 = int(input('Enter a positive Integer : '))

if num1 <= 0:
    print('Kindly enter positive Integer')
else:
    print(sum_of2(num1))


"""

"""
Que 3:- A string is entered through keyboard. Write recursive function that count number of vowels in string.


def count_vowel(s):
    vowels = 'aeiouAEIOU'
    if not s:
        return 0

    if s[0] in vowels:
        return 1 + count_vowel(s[1:])
    else:
        return count_vowel(s[1:])


input_string = input('Enter a string : ')
result = count_vowel(input_string)
print(result)


"""


"""
Que 4:- A string is entered through keyboard. Write recursive function that remove any tabs present in string.




def remove_tabs(s):
    if not s:
        return ""

    if s[0] == "\t":
        return " " + remove_tabs(s[1:])
    else:
        return s[0] + remove_tabs(s[1:])


sentence = 'hello\t world\tof coding\t'
result = remove_tabs(sentence)
print(result)

"""

"""
Que 5:- A string is enter through a keyboard. Write a recursive function 
        that checks whether the string is a palindrome or not.



def is_palindrome(s):
    # Debug: Show the current string being checked
    print(f"Checking substring: {s}")

    # base case, if string has one character.
    if len(s) <= 1:
        return True
    # check the first and last character
    if s[0] != s[-1]:
        print(f"Mismatch found: {s[0]} != {s[-1]}")
        return False
    # Recursive case: Check the substring excluding the first and last characters
    return is_palindrome(s[1:-1])


input_string = input('Enter a string to check weather it is palindrome or not :  ').strip().lower()

if len(input_string) == 0:
    print('The string is empty. ')
else:
    result = is_palindrome(input_string)
    # call the function and output the result
    if result:
        print('The string is Palindrome.')
    else:
        print('The string is Not Palindrome.')


"""

"""
Que 6 :- Two numbers are received through keyboard into a variable a and b .
         write a recursive function that calculate the value of a**b



def power(a, b):
    # Base case: if b == 0, return 1
    if b == 0:
        return 1
    else:
        # Recursive case: multiply a by the result of power(a, b-1)
        return a * power(a, b-1)


# Input: two numbers separated by a comma
x, y = input('Enter Two Positive Numbers Separated By "Comma" : ').split(',')
x, y = int(x), int(y)

if x <= 0 or y < 0:
    print('Please enter positive numbers for the base and a non-negative integer for the exponent.')
else:
    print(power(x, y))


"""


"""
Que 7: Write a recursive function that reverses the list of numbers, that it receives.



def rev_list(lst, rev_ls=None):
    # Initialize rev_ls as an empty list if None is passed
    if rev_ls is None:
        rev_ls = []

    # base case - list is empty
    if len(lst) == 0:
        return rev_ls
    else:
        # Add last element to rev_ls
        rev_ls.append(lst[-1])
        # Recurse with the rest of the list (excluding the last element)
        return rev_list(lst[:-1], rev_ls)


# given list
num_lst = [1, 2, 3, 4, 5, 6]
a = rev_list(num_lst)
print(a)


"""


"""
Que 8: A list contains some negative and some positive numbers. 
       Write a recursive function that sanitizes the list by replacing all negative numbers with 0.



def replace_neg_num(lst):

    if len(lst) == 0:
        return lst
    else:
        if lst[0] < 0:
            lst[0] = 0
        return [lst[0]] + replace_neg_num(lst[1:])


num_lst = [1, -4, -6, 2, 3, 4, -5, 6, 0]
a = replace_neg_num(num_lst)
print(a)


"""

"""
Que 9:- Write a recursive function to obtain average of all numbers present in a given list.



def total_sum(lst, sum=0):
    if len(lst) == 0:
        return sum
    else:
        sum = sum + int(lst[0])
        return total_sum(lst[1:], sum)


# given list
num_lst = [1, 2, 3, 4, 5, 6]
result = total_sum(num_lst)
print(result)


"""

"""
Que 10:- Write a recursive function to obtain length of given string.



def str_length(s, length=0):
    if len(s) == 0:
        return length
    else:
        length += 1
        return str_length(s[1:], length)


input_string = 'Recursion'
result = str_length(input_string)
print('Length of string :', result)


"""

"""
Que 11:- Write a recursive function that receives a number as input  and return the square of the number. 
         Use the mathematical Identity (n-1)**2 = n**2 - 2n + 1. 


def square(n):
    if n == 0:
        return 0
    else:
        num_square = square(n-1)
        return num_square + 2*n-1


# Get user input
num = int(input("Enter a number to find its square: "))
result = square(num)
print(f"The square of {num} is: {result}")


"""


"""
Que 2:- There are three pegs labeled A, B and C. Four Disks are placed on peg A. The Bottom-most disk is largest,
        and disks go on decreasing in size with the topmost disk being smallest. The objective of 
        the game is to move the disks from peg A to peg C, Using peg B as an auxiliary peg.
        The rules of  the game are as follows:
        
        - Only one disk may be moved at a time, and it must be the top disk on one of the pegs.
        - A larger disk should never be placed on the top of a smaller disk.
        
        Write a program to print out sequence in which the disks should be moved such that all disks on peg A
        are finally transferred to peg C.

"""


# Recursive Python function to solve the tower of hanoi

def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    tower_of_hanoi(n - 1, auxiliary, destination, source)


# Driver code
n = 4
tower_of_hanoi(n, 'A', 'B', 'C')
# A, C, B are the name of rods














