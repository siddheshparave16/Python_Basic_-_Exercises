# Following Questions based on Decision control Instruction

"""
Que 1 = While purchasing certain items , a discount of 10% is offered if the quantity purchased is more than 1000.
if quantity and price per item are input through the keyboard, write a program to calculate the total expenses.


qty = int(input("Enter quantity of items :\n"))
price = int(input("Enter price of an Item :\n"))

if qty > 1000:
    dis = 10
else:
    dis = 0

total_price = qty*price
total_discount = total_price*dis/100
total_expenses = total_price - total_discount

print('total_price : Rs.', total_price)
print(f' total_discount {dis} % : Rs. '
      f'', total_discount)
print('total_expenses : Rs.', total_expenses)

"""
# ---------------------------------------------------------------------------------
"""
Que 2 :- In a company an employee is paid as under :
if basic salary < 1500 
then HRA = 10% OF BS , DA = 90% OF BS

if basic salary >= 1500
then HRA = RS. 500 & DA = 98% OF BA

- If Basic salary is input through keyboard find the gross salary


basic_salary = int(input("Enter value of Basic Salary : \n"))

if basic_salary >= 1500:
    hra = 500
    da = basic_salary * 98/100
else:
    hra = basic_salary * 10/100
    da = basic_salary * 90/100


gross_salary = basic_salary + hra + da

# print(f'If basic_salary is {basic_salary} then HRA is {hra},DA will be {da} And Gross Salary=Rs. '+ str(gross_salary))

# Display the results
print(f"If the basic salary is Rs. {basic_salary:.2f}, then:")
print(f"HRA = Rs. {hra:.2f}")
print(f"DA = Rs. {da:.2f}")
print(f"Gross Salary = Rs. {gross_salary:.2f}")

"""

# ---------------------------------------------------------------------------------

"""
Que 3 :- Students percentage marks as a input and get grade 

# answer starts here ...

percentage = int(input("Enter value of Percentage : \n"))

if percentage >= 60:
    print('First Division')
elif percentage >= 50:
    print('Second Division')
elif percentage >= 40:
    print('Third Division')
else:
    print('Fail')

"""

# ---------------------------------------------------------------------------------

"""
Que 4 : - the company insures its drivers in following cases
- if driver is married
- if the driver is unmarried, male & above 30 years of age
- if the driver is unmarried, female & above 25 years

In all other cases, the driver is not insured. If the marital status, sex and age of driver are the inputs,
write a program to determine whether the driver should be insured or not.

# Answer starts here...

ms = input('Enter marital status as \'m\' or \'um\' : ')
sex = input('Enter Gender as \'ma\' or \'fe\' : ')
age = int(input("Enter age : "))

if (ms == 'm') or (ms == 'um' and sex == 'ma' and age > 30) or (ms == 'um' and sex == 'fe' and age > 25):
    print("Insured.")
    
else:
    print("Not Insured.")


"""

# ---------------------------------------------------------------------------------

"""
Que 5 :- Suppose there are flour flag variable w,x,y,z. 
        write a program to check in multiple ways whether one of them is true.


#  Different ways to check multiple flag
# lets declare variable

w, x, y, z = 0, 1, 0, 1

if (w == 1) or (x == 1) or (y == 1) or (z == 1):
    print('True')

if w or x or y or z:
    print('True')

if any((w, x, y, z)):
    print('True')

if 1 in (w, x, y, z):
    print('True')

if w | x | y | z:
    print('True')
"""

# ---------------------------------------------------------------------------------

"""
Que 6 :- Given a number we wish to do following things 
        if n is positive - print n*n , set a flag to True
        if n is negative - print n*n*n , set a flag to True
        if n is 0 - do nothing
        
#  Answer starts here


num = int(input("Enter a number : \n"))

if num > 0:
    flag = True
    print(num*num)

elif num < 0:
    flag = True
    print(num*num*num)

else:
    pass        # does nothing on his execution


"""

# ---------------------------------------------------------------------------------

"""
Que A :- Write conditional expression for 

# if a <10 , b = 20 else b = 30
a = int(input("enter value for a : "))
b = 20 if a < 10 else 30
print("value for b : ", b)



# print 'Morning' if time < 12 else 'Afternoon'
current_time = float(input("Enter Time :"))
c = 'Morning' if current_time < 12 else 'Afternoon'
print(c)



# if marks >= 70, set remarks to True, otherwise False

marks = int(input("Enter your marks : \n"))
remarks = True if marks >= 70 else False
print('Remarks : ', remarks)


"""

# ---------------------------------------------------------------------------------

"""
Que b :- Rewrite the following code snippet in one line
x = 3
y= 3.0
if x == y:
    print("Equal")
else:
    print("Not Equal")

# Answer starts here 

x = 3
y = 3.0

check_equality = 'Equal' if x == y else 'Not Equal'
print(f'{x} and {y} are', check_equality)

"""
# ---------------------------------------------------------------------------------

"""
Que B:- What will be output of following programs ? 


# a]

i, j, k = 4, -1, 0
w = i or j or k
print(w)       # 4

x = i and j and k
print(x)       # 0

y = i or j and k
print(y)      # 4

z = i and j or k
print(z)      # -1



# b]
a = 10
a = not not a
print(a)            # True



# c]
x, y, z = 20, 40, 45

# let check which number is Biggest

if x > y and x > z:
    print('Biggest number is ' + str(x))
elif y > x and y > z:
    print('Biggest number is ' + str(y))
else:
    print('Biggest number is ' + str(z))


# d]
num = 30
k = 100 if num <= 10 else 500
print(k)

# e]
a = 10
b = 60
if a and b > 20:
    print("Hello")
else:
    print("Hii")



# f]

a = 10
b = 60
if a > 20 and b > 20:
    print("Hello")
else:
    print("Hii")

# g]

a = 10
if a == 30 or 40 or 60:
    print("Hello")
else:
    print("Hi")




# h]

a = 10
if a == 30 or a == 40 or a == 60:
    print("Hello")
else:
    print("Hi")
    

# i]
a = 10

if a in (30, 40, 50):
    print("Hello")
else:
    print("Hii")
    
    
"""

# Que D] :- If a=10, b=12, c=0 , find the value of following expression

a = 10; b = 12; c = 0

exp = a != 6 and b > 5
print(exp)

exp2 = a == 9 or b < 3
print(exp2)

exp3 = not(a < 10)
print(exp3)

exp4 = not(a > 5 and c)
print(exp4)

exp5 = 5 and c != 8 or c
print(exp5)

