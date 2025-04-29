"""
Que A]

# a:- make code compact

# taking ages of three person
age1, age2, age3 = input("Enter age of 3 persons : ").split()
age1, age2, age3 = int(age1), int(age2), int(age3)
print(f'{age1}, {age2}, {age3}')


# b] how will you print "Rendezvous" in a line and retain
#    the cursor in the same line in which the output has been printed?

# using end=''
print('Rendezvous', end=" ")
print('a')


# c] what will be the output of following code snippet

l, b = 1.5678, 10.5
print('length = {l} breadth = {b}')
# need to change output formating
print(f'length = {l} breadth = {b}')

n = 2
print(f'{n:>5}{n**2:>7}{n*n*n:>8}')

# program for arbitrary number of input using list 'comprehension
float_list = [num for num in input('Enter a Five float numbers : ').split()]
for n in float_list:
    print(float(n))


# i] How will you receive Boolean value as an input ?
# j] How will you receive Complex value as an input ?


bool_value = bool(input("Enter a Boolean value as an Input : "))
print(bool_value)

complex_value = complex(input("Enter a Complex value as an Input : "))
print(complex_value)



# k:- How will you display price in 10 columns with 4 places beyond decimal points ?
#    Assume value of price to be 1.5567894

num = 1.5567894
print(f'{num:10.4f}')

"""

"""
Que l :- Write a program to receive arbitrary number of float using one input() statement.
         Calculate the average of float received.


# input for arbitrary number of float in single input
float_list = [num for num in input('Enter a float number :-').split()]

# Answer starts here...

sum_of_floats = 0
count = 0
# convert a string into float
for n in float_list:
    n = float(n)
    count += 1
    sum_of_floats = sum_of_floats + n
    print(n, end=" ")

print()
# Calculate the average
avg = sum_of_floats/count

print(f'The Count of {count} Numbers entered through input ,'
      f'Sum of all numbers is {sum_of_floats:.2f} and Average is {avg:.2f}')

"""

"""
Que m:- Write a program to receive the following using one input() statement.
        name of person | years of service | Diwali bonus received
        - Calculate and print the agreement deduction as per the following formula:
        deduction = 2*years of service + bonus * 5.5/100
        
# Answer starts here...

# input in single line for name, service_year and Diwali_Bonus for a person
name, year, bonus = input('Enter Person Name, Year of Service and Diwali_Bonus :- ').split()

# convert data as per data_type
name, year, bonus = name, int(year), int(bonus)

# Calculate and print the agreement deduction
deduction = 2*year + bonus * 5.5/100
print(f'Agreement Deduction for {name} is {deduction}')

"""

a = 12.34; b = 234.39; c = 444.34; d = 1.23; e = 34.67
print(f'\na = {a}'
      f'\nb = {b}'
      f'\nc = {c}'
      f'\nd = {d}'
      f'\ne = {e}')









