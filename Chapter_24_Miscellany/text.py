"""
 This file is only for purpose of executing programs in Chapter_24_Miscellany_Que_Ans.py
 for purpose of command line arguments copy Questions and execute solutions
"""

import sys
import getopt
import os

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

