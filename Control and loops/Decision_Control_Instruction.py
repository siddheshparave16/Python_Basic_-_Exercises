"""
# Nuances of Conditions

a = 40
b = 30
x = 75 and a >= 20 and b < 60 and 35
print(x)

y = -30 and a >= 20 and b < 15 and 35
print(y)

x = 10 or a >= 20 or 60
print(x)

y = 75 or a >= 20 or 60
print(y)

y = a >= 20 or 75 or 60
print(y)

y = a >= 20 and 75 and 60
print(y)

y = a >= 20 and 75 or 60
print(y)

a1 = 10
b1 = 20
res = not(a <= b)
print(res)

res2 = not(a >= b)
print(res2)


# not need only one operand so its Urinary operator

a = int(input('Enter 0 or 1 :- \n'))

a = int(not a)              # set s to 0 if it is 1 , and set it to 1 if it is 0 .
print(a)


# Conditional Expressions

age = 15
status = 'minor' if age < 18 else 'adult'
print(status)


sunny = False
print('Let\'s go to the', 'beach' if sunny else 'room')

humidity = 76.8
setting = 25 if humidity > 75 else 28
print(setting)


# conditional expression can be nested
# <expr1> if < conditional expression > else <expr2>

weight = 55
msg = 'Obess' if weight > 85 else 'Hefty' if weight > 60 else'Prim'
print(msg)

"""

#  all()  &  any()
# instead of use and & or logical operator we can use logical operator

# all () - function returns true if all elements of parameter are true
# any () - function return true if any of elements of parameter is true

a, b, c = 10, 20, 30
res = all((a > 5, b > 20, c > 15))
print(res)

res2 = any((a > 5, b > 20, c > 15))
print(res2)


# Receiving input

name = input("Enter your name :\n")
age = int(input("Enter your age :\n"))
salary = float(input("Enter your salary :\n"))
print(name, age, salary)



