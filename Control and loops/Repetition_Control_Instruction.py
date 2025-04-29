# while loop - Repeat a set of statement till a condition remains True.

"""
num = int(input("Enter a number : "))

# loop will terminate when input as a 5
while num != 5:
    print(f"Number {num} Square {num * num}")
    num = int(input("Enter a number : "))


# while loop can be used to repeat a set of statements a finite number of times.

count = 0
print("Number\t""Square\t" "Cube")
while count < 10:
    print(count, count*count, count*count*count)
    count += 1



# iterating over string
s = 'Mumbai'
lst = ['desert', 'dessert', 'to', 'too', 'lose', 'loose']
tpl = (10, 20, 30, 40, 50, 60)

i = 0
while i < len(lst):
    print(i, s[i], lst[i], tpl[i])
    i += 1


"""
"""

# for loop - Repeat a set of statements a finite number of times
# To repeat a statement through finite number of times - range()
# for(start, stop, steps)

for i in range(10):
    print(i)


for i in range(10, 20):
    print(i)

for i in range(10, 20, 2):
    print(i)

for i in range(20, 10, -3):
    print(i)


for i in range(1, 10, 2):
    print(i, i*i, i*i*i)


# iterate through string
print('iterate through string')
for char in 'Leopard':
    print(char)

print("\n")

# iterate through List
print('iterate through List')
for animal in ['cat', 'dog', 'lion', 'tiger', 'fox']:
    print(animal)

print("\n")

# iterate through Tuple
print('iterate through Tuple')
for flower in ('Rose', 'Lily', 'Jasmine', 'Lotus'):
    print(flower)

print("\n")

# iterate through Set
print('iterate through Set')
for num in {1, 2, 3, 4, 5, 6}:
    print(num)

# iterate through Dictionary
for key in {'A101': 'Aman', 'A102': 'Jay', 'A103': 'Raj'}:
    print(key)


# Get Index of an Item through Iterate
lst = ['cat', 'dog', 'lion', 'tiger', 'fox']

for index, item in enumerate(lst):
    print(index, item)


"""

"""
# Determine whether a number is prime or not

num = int(input("Enter a Integer : "))

i = 2
while i <= num-1:
    if num % i == 0:
        print(f'{num}, is not Prime Number')
        break
    i += 1

else:
    print(f'{num}, is Prime Number')


# using for loop Prime number ..
count = 0
for i in range(1, num+1):
    if num % i == 0:
        count += 1
if count > 2:
    print(f'{num}, is Not Prime Number')
else:
    print(f'{num}, is Prime Number')



# Que
number = [10, 20, 30, 50, 57, 60, 70]
for ele in number:
    if ele % 10 != 0:
        print(ele, 'is not a multiple of 10')
        break

else:
    print("All numbers are multiple of 10.")


"""

"""
Que 1 :- Write a program to receives 3 set of values of p, n and r ( Principle , month, interest rate)
        and calculate simple interest for each
        

i = 1
while i <= 3:
    p = float(input("Enter a value of Principle Amount : "))
    n = int(input("Enter a value of year: "))
    r = float(input("Enter a value of Rate Interest : "))

    # calculate simple interest
    simple_interest = p*n/12*r / 100
    print(f'Simple Interest = Rs. {simple_interest}.')

    i = i+1


"""

"""
Que 2 :- Write a program to print 1 to 10 numbers using infinite loop.
        All numbers should get print in same line

# answer starts here
        

# while 1 is crete Infinite loop, as 1 is non-zero.
i = 0
while 1:
    print(i, end=" ")
    i += 1

    if i > 10:
        break


"""

"""
Que 4 : - Write a program to print all unique combination of 1, 2 and 3.

# Answer starts here...


i = 1
while i <= 3:
    j = 1
    while j <= 3:
        k = 1
        while k <= 3:
            if i == j or j == k or k == i:
                k += 1
                continue
            else:
                print(i, j, k)
            k += 1
        j += 1
    i += 1


"""

"""
Que 4 :- Write a program that obtain value of a binary value of a binary numeric string.
         for example, decimal value of '1111' is 15.

# Answer starts here ....

b = '1111'
# 'i'    will store the decimal equivalent of the binary string
i = 0
original_b = b  # Keep the original value for printing

# The loop runs as long as b is not empty.
while b:
    i = i * 2 + (ord(b[0]) - ord('0'))

    # Removes the first character of b, shortening it by one character.
    b = b[1:]

print(f'Decimal value of {b} is ' + str(i))


print(ord('1'))
print(ord('0'))

"""

"""
Que :- Write a program that generate a following output using a program.
      'A to Z' and 'z to a'

"""

for index, i in enumerate(range(0, 128+1)):
    print(index, chr(i))

print(" Alphabets from 'A' to 'Z'")
for alpha in range(65, 91):
    print(chr(alpha), end=" ")

print('\n')

print(" Alphabets from 'z' to 'a'")
for alpha in range(122, 96, -1):
    print(chr(alpha), end=" ")

print('\n')
print('\n')




place = 'Nagpur-440010'

# declare count variable for Alphabets and Digits
alpha_count = 0
digit_count = 0

for i in range(len(place)):
    # checking element is alpha
    if place[i].isalpha():
        alpha_count += 1
    # checking element is digit
    elif place[i].isdigit():
        digit_count += 1

print(f'Alphabets Count in {place} is {alpha_count}')
print(f'Alphabets Count in {place} is {digit_count}')
