"""
Que A:

# a]


i = 0.1

while i < 1.0:
    print(f"{i:.1f}")
    i += 0.1


# f]

print("using while loop")
count = 1
while count <= 10:
    print(count, end=" ")
    count += 1

print("\nusing while loop")
for count in range(1, 11):
    print(count, end=" ")

"""

"""
# g] outut for following code snippet


for index in range(20, 10, -3):
    print(index, end=" ")

"""

"""
Que B

# a] 

j = 1
while j <= 10:
    print(j)
    j += 1


# b]

while True:
    print("infinite loop")


# c]

lst = [10, 20, 30, 40, 50]
for count in range(5):
    print(lst[count])


# d]
i = 15

# not(i<10) is same work as i>=10
while not(i < 10):
    print(i)
    i -= 1

# f]

for i in range(0.1,1.0,0.25):
    print(i)

# solution
i = 0.1

while i <= 1:
    print(i)
    i += 0.25




# g]

i = 1
while i <= 10:
    j = 1
    while j <= 5:
        print(i, j)
        j += 1
    print(i, j)
    i += 1


"""

"""
# Attempt the following Questions :

Que 1 :- Write a program to print first 25 odd numbers using range(). 



# first 25 odd numbers using for loop
print("First 25 odd numbers : -")
for i in range(1,50,2):
    print(i)

# first 25 odd numbers using while loop
i = 1
count = 0

while count <= 25:
    if i % 2 != 0:
        print(i)
        count += 1
    i += 1

"""

"""
Que 2:- Rewrite following program using for loop 


lst = ['desert', 'dessert', 'to', 'too', 'lose', 'loose']
s = 'Mumbai'
i = 0
while i < len(lst):
    if i > 3:
        break
    else:
        print(i, lst[i], s[i])
        i += 1

# answer starts here


lst = ['desert', 'dessert', 'to', 'too', 'lose', 'loose']
s = 'Mumbai'

for i in range(len(lst)):
    if i > 3:
        break
    print(i, lst[i], s[i])

"""

"""
Que 3:- write the program to count number of alphabets and number of digits in string 'Nagpur-440010'.

# answer starts here...
# using for loop

place = 'Nagpur-440010'

# declare count variable for Alphabets and Digits
alpha_count = 0
digit_count = 0

for i in range(len(place)):
    # checking element is alphabet
    if place[i].isalpha():
        alpha_count += 1
    # checking element is digit
    if place[i].isdigit():
        digit_count += 1

print(f'Alphabets Count in {place} is {alpha_count}')
print(f'Alphabets Count in {place} is {digit_count}')



# using while loop

# given string
place = 'Nagpur-440010'

# declare count variable for Alphabets and Digits
alpha_count = 0
digit_count = 0
i = 0
while i < len(place):
    # checking element is alphabet
    if place[i].isalpha():
        alpha_count += 1
    # checking element is digit
    elif place[i].isdigit():
        digit_count += 1

    i += 1

print(f'Alphabets Count in {place} is {alpha_count}')
print(f'Alphabets Count in {place} is {digit_count}')


"""

"""
Que 4:- If five digit number is enter through a keyboard. write a program to obtain the reversed number
        and determine whether the original and reversed number are equal or not 
        
# answer starts Here...
 

number = input("Enter a 5 Digit Number :- ")

if len(number) == 5 and number.isdigit():
    num = int(number)

    original_number = num
    reverse_number = 0

    while num > 0:
        digit = num % 10       # to get last digit of number
        reverse_number = reverse_number*10 + digit
        num = num // 10     
    print(f"Reverse number is {reverse_number}")

    if original_number == reverse_number:
        print("The original number and reversed number are equal (Palindrome).")
    else:
        print("The original number and reversed number are not equal.")

else:
    print("Invalid input! Please enter a five-digit number.")


"""

"""
Que 5:- Write a program to find the factorial value of any number entered through the keyboard

# Answer starts here

# using for loop

number = int(input("Enter an Integer :-"))

# factorial of number ( n = n*n-1)
fact = 1

if number <= 1:
    print("Factorial is", fact)
else:
    for i in range(1, number+1):
        fact = fact * i
    print(fact)


# using While loop

num = int(input("Enter an Integer :-"))
fact = 1
if num <= 1:
    print("Factorial is", fact)
else:
    i = 1
    # using infinite loop
    while True:
        fact = fact * i
        i += 1
        if i > num:
            break

    print(print("Factorial is", fact))


"""

"""
Que 6:- Write a program to print all Armstrong numbers between 1 and 500. 
        if sum of cube of each digit of the number is equal to the number itself, then the number is called
        an Armstrong number. for example 153 .

# Answer starts here...        

# Armstrong numbers between '1' to '500'


sum_of_digit = 0

for number in range(1, 501):
    # print(num)
    sum_of_digit = 0

    # find the sum of cube of each digit
    temp = number
    while temp > 0:
        digit = temp % 10
        sum_of_digit = sum_of_digit + digit ** 3
        temp = temp // 10

    if sum_of_digit == number:
        print(f"Sum of Cubes of {number} is {sum_of_digit}, The number {number} is Armstrong. \n")

        
"""

"""
Que 7:- write a program to print all primary numbers from 1 to 300.

# Answer starts here...


print("Prime numbers between '1' To '100' are : ")
# primary number from 1 to 300
for num in range(1, 301):
    # prime number for 1 & 2
    if num <= 2:
        print(num, end=",")
    else:
        # check count of number divisible by other numbers
        count = 0
        i = 1
        while i <= num:
            if num % i == 0:
                count += 1
            i += 1
        if count == 2:
            print(num, end=",")

"""

"""
Que 8 :- Write a program to print the multiplication table of the number entered by user. 
         the table should get displayed in the following form :
         29 * 1 = 29  
         29 * 2 = 58  
         
# Answer starts here...
         
# using for loop
# user input for an Integer number
num = int(input("Enter an Integer : "))

for i in range(1, 11):
    print(f"{num} * {i} =", num * i)


# Using while loop
# user input for an Integer number
num = int(input("Enter an Integer : "))

i = 1
while i <= 10:
    print(f"{num} * {i} =", num * i)
    i += 1

"""

"""
Que 9:- When interest compound q times per year at an annual rate of r% for n years, 
        the principle p compound to an amount a as per formula :
        a = p(1+r/q)**nq
        
        write a program to read 10 sets of p, r, n & q and calculate the corresponding as.
            Principal (p): Initial amount of money.
            Rate (r): Annual interest rate in percentage, converted to a decimal.
            Time (n): Duration of investment in years.
            Frequency (q): Number of times interest is compounded per year.

# Answer starts here


# take 10 sets of values for p, r, n, q
for i in range(1, 11):
    p = float(input("Enter Principle amount : "))
    r = float(input("Enter Rate % : "))/ 100
    n = float(input("Enter Time period in years : "))
    q = float(input("Enter compound Interest : "))

    total_amount = 0

    # formula a = p(1+r/q)**nq

    total_amount = p*(1+r/q)**(n*q)

    print(f"Total amount (A) after {n} years: {total_amount:.2f}")
    print("-" * 30)


"""

"""
Que 10:- Write a program to generate all Pythagorean Triplets with side length less than or equal to 30.

# Answer starts here ... 


print("Pythagorean Triplets till length 30 are : - \n")
count = 0

# to generate 3 numbers set
for i in range(31):
    for j in range(i+1, 31):
        for k in range(j+1, 31):

            # for Pythagorean Triplets
            if i < j < k:
                if i**2 + j**2 == k**2:
                    count += 1
                    print(f'{i},{j},{k}')
                    print(f'{i ** 2} + {j ** 2} = {k ** 2} \n')


print(f'There are {count} Pythagorean Triplets combination till length 30.')

"""

"""
Que 11 :- Population of a town today is 1000000. The population has increased steadily
         at the rate of 10% per year for last 10 years. Write a program to determine the population
         at the end of each year in the last circle



# Initial population
new_population = 1000000

# Growth rate per year in percentage
grows_rate = 10

# Number of years
years = 10
old_population = new_population
for year in range(1, years):
    old_population = old_population / (1 + grows_rate/100)
    print(f"Year {years - year}: Population = {old_population:.0f}")


"""

"""
Que 12:- Ramanujan number is the smallest number that can be expressed as 
         sum of two cubes in two different ways. Write a program to print all such 
         numbers up to a reasonable limit.

# Ramanujan number = sum of cubes of two numbers ( in two different ways)
# numbers that can be expressed as the sum of two cubes in two distinct ways


limit = int(input("Enter a number till that limit we will print Ramanujan number :- "))

# Iterate over all combinations of (i, j, k, l)
# this loop for sum of cubes of first pair
for i in range(1, limit+1):
    for j in range(i, limit+1):
        sum1 = i**3 + j**3

        # this loop for sum of pairs of second pair
        for k in range(1, limit+1):
            for l in range(k, limit+1):
                sum2 = k**3 + l**3

                # check if sum match and pairs are distinct
                if sum1 == sum2 and (i != k or j != l) and (i != l or j != k):
                    # Only print if (i, j) < (k, l) to avoid duplicate representation
                    if (i, j) < (k, l):
                        print(f'{sum1} = {i}^3 + {j}^3 = {k}^3 + {l}^')


"""

"""
Que 13:- Write a program to print 24 hours of day within suitable time suffixes like AM, PM, Noon, Midnight
"""

for hour in range(24):
    if hour == 0:
        print("00.00 Midnight")
    elif hour == 12:
        print("12.00 Noon")
    elif hour < 12:
        print(f'{hour:02d} AM')
    else:
        print(f'{hour:02d} PM')


