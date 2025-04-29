import sys
import getopt
import os

# Que
"""
Que 1:- IS it Necessary to mention the docstring for a function immediately below the def statment ?

Ans :-
    Placing the docstring immediately below the function definition is necessary for proper documentation,
    clarity, and compatibility with Python tools like help(), Sphinx, and other automatic documentation systems.
    It ensures that the function's behavior is clearly described and available for inspection,
    both for you and for other developers who might use the function later.

"""


"""
Que 2:- Write a program using command-line arguments to search for a word in a file and replace it with
        the specified word. the usage of the program is shown below.
        
        c:/ change -o old_word -n new_word -f filename

# Answer starts here...

try:

    # Parse the command-line arguments
    options, arguments = getopt.getopt(sys.argv[1:], 'o:n:f:')
    print(options)
    print(arguments)

    # Initialization of variable for old_word, new_word, file_name
    old_word = None
    new_word = None
    file_name = None

    # Process the options
    for opt, arg in options:
        if opt == '-o':
            old_word = arg
        elif opt == '-n':
            new_word = arg
        elif opt == '-f':
            file_name = arg

    # Ensure all required arguments are provided.
    if not (old_word and new_word and file_name):
        print('Improper arguments')
        print('mydir.py -o old_word -n new_word -f filename')
        sys.exit(1)

    # Read the file, replace the word, and save the changes
    try:
        with open('samplefile.txt', 'r') as f:
            content = f.read().lower()

        # Replace occurrences of the old word with the new word
        updated_content = content.replace((old_word).lower(), new_word)

        with open('samplefile2.txt', 'w') as f:
            f.write(updated_content)

    except FileNotFoundError:
        print(f'The File {file_name} does Not Exist ')
        sys.exit(1)

except getopt.GetoptError:
    print('mydir.py -o old_word -n new_word -f filename')
    sys.exit(1)

"""


"""
Que 3:- Write a program that can be use command prompt as a calculating utility. The Usage of program show below

        c:\\> calc <switch> <n> <m>
        
        where, n and m are two integer operands. switch can be any arithmatic operator.
        the output should be result of operation

# Answer starts here...


def main():

    try:
        # Parse the command-line arguments
        options, arguments = getopt.getopt(sys.argv[1:], 's:n:m:')

        print(options)
        print(arguments)

        # Initialize operand, first integer, second integer
        # operand
        switch = None
        first_integer = None
        second_integer = None

        # Process the options
        for opt, args in options:
            if opt == '-s':
                switch = args
            elif opt == '-n':
                first_integer = int(args)
            elif opt == '-m':
                second_integer = int(args)

        # Check all the values are provided
        if not (switch and first_integer is not None and second_integer is not None):
            print('Arguments missing.')
            print(r'Error: text.py <switch> <n> <m>')
            sys.exit(1)

        # Perform operation based on the switch
        if switch == '+':
            result = first_integer + second_integer
        elif switch == '-':
            result = first_integer - second_integer
        elif switch == '*':
            result = first_integer * second_integer
        elif switch == '/':
            if second_integer != 0:
                result = first_integer / second_integer
            else:
                print("Error: Division by zero!")
                sys.exit(1)
        else:
            print('Error: Invalid switch')
            sys.exit(1)

        # output of operation
        print(f'{first_integer} {switch} {second_integer} = {result}')

    except getopt.GetoptError:
        print(r'Error: text.py <switch> <n> <m>')
        sys.exit(1)


if __name__ == '__main__':
    main()


"""


"""
Que 4:- Rewrite the following expressions using bitwise in-place operators.

# Answer starts here...


# task1
a = 30
# a = a | 3    # output: 31
a |= 3
print(a)


# task2
a1 = 30
# a1 = a1 & 0x48        # output = 8
a1 &= 0x48
print(a1)


# task3
b = 30
# b = b ^ 0x22    # output = 60
b ^= 0x22
print(b)


# task4
c = 30
# c = c << 2    # output: 120
c <<= 2
print(c)


# task5
d = 30
# d = d >> 4      # output: 1
d >>= 4
print(d)

"""


"""
Que 5:- Consider an unsigned integer in which rightmost bit is numbered as 0. 
        Write a function checkbits(x,p,n) which return True if all 'n' bits starting from position 'p' are on,
        False otherwise. For example checkbits(x,4,3) will return True if bits 4,3 and 2 are 1 inn number x. 



def checkbits(x, p, n):
    '''
       Check if 'n' consecutive bits starting from position 'p' are all 1 in number 'x'.

       Parameters:
       x (int): The unsigned integer to check.
       p (int): The starting position of the bits (0-indexed from the right).
       n (int): The number of consecutive bits to check.

       Returns:
       bool: True if all specified bits are 1, False otherwise.
       '''

    # Initial validation
    if p < 0 and n <= 0:
        raise ValueError('p must be non-negative and n must be positive. ')

    if p - n + 1 == 0:
        raise ValueError('Not enough bits to check from the given position.')

    # Step 2: Generate the mask for 'n' bits.
    mask = (1 << n) - 1

    # Step 3: Align the mask to the position 'p'.
    aligned_mask = mask << (p - n + 1)

    # Step 4: Perform bitwise AND operation and compare.
    result = x & aligned_mask

    return result == aligned_mask


# Example usage

# Example number in binary
x = 0b111110
p = 4
n = 3

print(checkbits(x, p, n))


"""


"""
Que 6:- Write a program to receive a number as input and check whether its 3rd, 6th, 7th bit is on.

# Answer starts here...

def check_bits_on(x):

    # Create a bitmask for checking 3rd, 6th, and 7th bits (count starts from 0)
    mask = 0b1001000

    if (x & mask) == mask:
        return True
    else:
        return False


num = int(input("Enter a number: "))

# Check if 3rd, 6th, and 7th bits are on
if check_bits_on(num):
    print("3rd, 6th, and 7th bits are ON.")
else:
    print("3rd, 6th, and 7th bits are NOT ON.")


"""


"""
Que 7:- Write a program to receive an 8 bit number into a variable and
        then exchange its higher 4 bits with lower 4 bits. 

# Answer starts here...

def swap_bits(x):
    # Mask to isolate the lower 4 bits
    lower_bits = x & 0b00001111
    print(bin(lower_bits))

    # Mask to isolate the upper 4 bits
    upper_bits = x & 0b11110000
    print(bin(upper_bits))

    # Mask to isolate the lower 4 bits (0b00001111)
    lower_bits_shifted = lower_bits << 4

    # Mask to isolate the higher 4 bits (0b11110000)
    upper_bits_shifted = upper_bits >> 4

    combine_bits = lower_bits_shifted | upper_bits_shifted

    return combine_bits


num = int(input('Enter a 8-bit number: '), 2)

result = swap_bits(num)

print(f'Original Number: {bin(num)}')
print(f'Swapped Number: {bin(result)}')


"""


"""
Que 8:- Write program to receive an 8-bit number into a variable and then set its odd bits to 1.
"""


def set_odd_bit(x):
    # Define the mask with odd bits set to 1 (0b10101010)
    mask = 0b10101010
    # Apply the mask using the bitwise OR operation
    result = x | mask

    return result


num = int(input('Enter a valid 8-bits number (0-255)'),10)

if num < 0 or num > 255:
    print('Please enter a valid 8 bit number.')
else:
    odd_bit = set_odd_bit(num)

    # Output the result in binary
    print(f'Original number {bin(num)}')
    print(f'After setting odd bits to 1 {bin(odd_bit)}')




























