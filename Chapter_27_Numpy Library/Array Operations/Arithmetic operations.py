import numpy as np

a1 = np.array([[10, 12, 14, 16], [5, 6, 7, 8]])
a2 = np.array([[1, 2, 3, 4], [11, 13, 15, 17]])


# Add arguments element-wise.
a3 = a1 + a2
print(a3)
print(np.add(a1, a2))


print()
# subtract array

a4 = a1 - a2
print(a4)
sub_arr = np.subtract(a1, a2)
print(sub_arr)


print()
# Multiply arguments element-wise.

mul = a1 * a2
print(mul)
print(np.multiply(a1, a2))


print()
# Divide arguments element-wise.

div = a1 / a2
print(div)
print(np.divide(a1, a2))


print()
# Returns the element-wise remainder of division.
mod = a1 % a2
print(mod)
print(np.mod(a1, a2))


print()
# Return element-wise quotient and remainder simultaneously.
print(np.divmod(a1, a2))


print()
# power
a5 = a1 ** 2
print(a5)

# First array elements raised to powers from second array, element-wise.
print(np.pow(a1, a2))


# Scalar Arithmetic Operations in NumPy

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Scalar value
scalar = 2

# Addition
addition = arr + scalar
print("Addition: ", addition)

# Subtraction
subtraction = arr - scalar
print("Subtraction: ", subtraction)

# Multiplication
multiplication = arr * scalar
print("Multiplication: ", multiplication)

# Division
division = arr / scalar
print("Division: ", division)

# Floor Division
floor_division = arr // scalar
print("Floor Division: ", floor_division)

# Modulus
modulus = arr % scalar
print("Modulus: ", modulus)

# Exponentiation
exponentiation = arr ** scalar
print("Exponentiation: ", exponentiation)

