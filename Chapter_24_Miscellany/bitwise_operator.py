
# Bitwise operator usage:

ch = 32

"""
- NOT (~)
    Inverts each bit (flips 0 to 1 and 1 to 0).
    Works on a single number and gives the two's complement.
"""

# In two's complement, applying ~ to a number gives the negative of the number minus 1.
dh = ~ch
print(dh)


"""
- Left Shift (<<)
    Shifts bits to the left by a specified number of positions.
    Each left shift is equivalent to multiplying by 2. --- 2**n
"""

eh = ch << 3
print(eh)


"""
- Right Shift (>>)
    Shifts bits to the right by a specified number of positions.
    Each right shift is equivalent to integer division by 2.
"""

eh = ch >> 3
print(eh)

print()

