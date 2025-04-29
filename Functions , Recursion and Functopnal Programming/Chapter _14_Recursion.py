"""
# Recursive Function
def fun():
    # some statements
    print('Hello')
    fun()       # recursive call


fun()



# factorial of number using Recursive function


def refact(num):
    if num == 0:
        return 1
    else:
        factorial = num * refact(num - 1)
        return factorial


n = int(input('Enter an Integer : '))

# function call
fact_of_n = refact(n)
print(f'Factorial of {n} is {fact_of_n}')




# Problems with unknown loop


def generate(n):
    lol = [[] for i in range(n**n)]
    pos = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                t = [i, j, k]
                lol[pos] = t
                pos += 1

    return lol


x = generate(4)
print(x)



def generate(n):
    lol = []
    helper(n, [], lol)
    return lol


def helper(n, t, lol):
    global j
    if len(t) == n:
        lol.append(t[:])
        j += 1
        return

    for i in range(1, n+1):
        t.append(i)
        helper(n, t, lol)
        t.pop()


j = 0
l = generate(2)
print(l)
print(j)



# Types of Recursion
def headprint(n):
    if n == 0:
        return
    else:
        headprint(n-1)
        print(n)


headprint(10)


def tailprint(n):
    if n == 11:
        return
    else:
        print(n)
        tailprint(n + 1)


print('Tailprint recursion')
tailprint(1)


"""
import sys

"""
Que 1:- If a positive Integer is entered through the keyboard, 
        write a recursive function to obtain the prime factors of the number.

# Answer starts here..


def prime_factor(num, i):
    if i > num:
        return
    if num % i == 0:
        print(i, end=',')
        prime_factor(num//i, i)
    else:
        prime_factor(num, i + 1)


user_input = int(input('Enter positive Integer : '))


# Handle 1 or numbers less than 1
if user_input <= 1:  
    print("No prime factors.")
else:
    print('Prime factors are : ')
    # function call
    prime_factor(user_input, 2)

"""

"""
Que 2:- A positive Integer entered through the keyboard, write a recursive function 
        to calculate sum of digits of digits of the 5-digit number.



def digit_sum(num):
    if num == 0:
        return 0
    else:
        digit = num % 10
        num = num // 10
        total_sum = digit + digit_sum(num)

    return total_sum


n = int(input('Enter a five Digit number : '))

if len(str(n)) != 5:
    print('kindly Enter valid five Digit number :  ')
else:
    print(digit_sum(n))


"""


"""
Que 3:- Paper of size A0 has dimensions 1189mm X 841mm. 
        Each subsequent size A(n) is defined as A(n-1) cut in half, parallel to its shorter sides. 
        Write a program to calculate and print paper sizes A0,A1,A2, ...,A8 using recursion



def paper_size(i, n, length, breadth):
    if i <= 8:
        print(f'A{i}: L= {length}, B = {breadth}')

        new_breadth = length/2
        new_length = breadth
        n -= 1
        i += 1
        return paper_size(i, n, new_length, new_breadth)


paper_size(0, 9, 1189, 841)


"""

"""
Que 4:- Write a recursive function to obtain first 15 numbers of fibonacci sequence. In fibonacci sequence
        sum of two successive terms gives the third term. 


def fibo(old, current, term):
    if term >= 0:
        new_current = old + current
        old = current
        print(f'{new_current}', end='\t')
        term -= 1
        return fibo(old, new_current, term)


first_term = 0
second_term = 1
print(f'{first_term}', end='\t')
print(f'{second_term}', end='\t')
fibo(first_term, second_term, 13)


"""

"""
Que 5:- A positive Integer enter through the keyboard; write a function to find the binary equivalent 
        of this number using recursion.



def dec_to_binary(num):
    reminder = num % 2
    new_n = num//2       # Quotient
    if new_n != 0:
        dec_to_binary(new_n)
    print(reminder, end='')


sys.setrecursionlimit(10 ** 6)
n = int(input('Enter the number: '))
print('The binary equivalent is : ')
dec_to_binary(n)


"""

"""
Que 6:- Write a recursive function to obtain the running sum of first 25 natural numbers.



def running_sum(n):
    if n == 0:
        return 0
    else:
        total_sum = n + running_sum(n-1)
        return total_sum


sys.setrecursionlimit(10 ** 6)
num = int(input('Enter a positive largest number for running sum : '))

if num < 0:
    print('Entered number is negative.')
else:
    run_sum = running_sum(num)
    print(f'Running Sum is {run_sum}')

"""


def fun(x, y):
    if x == 0:
        return y
    else:
        return fun(x-1, x*y)


print(fun(4,2))


def fun2(num):
    if num > 100:
        return num - 10
    return fun2(fun2(num + 11))


print(fun2(75))


def fun3(n):
    if n == 0:
        print('False')
    if n == 1:
        print('True')
    if n % 2 == 0:
        fun3(n/2)


fun3(256)



