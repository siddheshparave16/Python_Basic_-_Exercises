import os, sys, getopt

"""
Que 1:- Write a program that display all files in current directory. It can receive options 
        -h or -l or -w from command line. If -h is received display help about the program. 
        If -l received, display files one line at a timee.
        If -w received, display files separated by tab character. 


# Answer starts here..


if len(sys.argv) == 1:
    print(os.listdir('.'))
    sys.exit(1)

try:
    options, arguments = getopt.getopt(sys.argv[1:],'hlw')
    print(options)
    print(arguments)

    for opt, arg in options:
        if opt == '-h':
            print(r'\\Chapter_24_Solve_Que.py -h -l -w')
            sys.exit(2)
        elif opt == '-l':
            lst = os.listdir('.')
            print(*lst, sep='\n')
        elif opt == '-w':
            lst = os.listdir('.')
            print(*lst, sep='\t')

except getopt.GetoptError:
    print('mydir.py -h -l -w')


"""


"""
Que 2:- Define a function show_bits() which display the binary equivalent of the integer passes to it.
        Call it to display binary equivalent of 45.
        
# Answer starts here...


def show_bits(num):
    \"\"\"
    This Python function show_bits is designed to display the binary representation
    of a 32-bit integer in a readable format. 
    \"\"\"
    
    for i in range(31,-1, -1):
        andmask = 1 << i
        k = num & andmask
        print('0', end='') if k == 0 else print('1', end='')


show_bits(45)
print()
print(bin(45))


"""


"""
Que 3:- Windows stores date of creation of a file as a 2-byte number with the following bit distribution:
        
        left-most 7 bits: year 1980
        middle 4 bits - month
        right-most 5 bits - day
        
        Write a program that converts 9766 into a date 6/1/1999. 
          
          
        the binary mask 0b111100000 is used to represent 4 bits for the month
        0b11111: A binary mask with 5 bits set to 1 (value 31 in decimal) is used to extract the 5 right-most bits.


# Answer starts from here.....

dt = 9766


# the left shift is for middle 4 bits - month and right-most 5 bits - day
y = (dt >> 9) + 1980

# the left shift is for month and right-most 5 bits - day
m = (dt & 0b111100000) >> 5
d = (dt & 0b11111)

print(str(d)+'/'+str(m)+'/'+str(y))


"""


"""
Que 4:- Windows stores time of creation of file as a 2-byte number, Distribution of different bits 
        which account for hours, minutes and seconds is as follows:
        
        felt-most 5 bits: hours 
        middle 6 bits - minutes
        right-most 5 bits - seconds/2
        
        write aa program to convert time represented by a number 26031 into 12:45:30

# Answer starts here

tm = 26031

# the left shift is for middle 6 bits - minutes and right-most 5 bits - seconds/2
hours = tm >> 11

# the left shift is for right-most 5 bits - seconds/2
minutes = (tm & 0b11111100000) >> 5

seconds = (tm & 0b11111)*2

print(str(hours)+':'+str(minutes)+':'+str(seconds))


"""


"""
Que 5:- Write assert statements for the following with suitable messages:
 
# Answer starts here....


# task 1 :- Salary multiplier must be non-zero
sm = 45
assert sm != 0, 'Oops, Salary multiplier is 0.'


# task 2:- Both p and q are same type


class Sample():
    pass


class NewSample():
    pass


p = Sample()
# q = NewSample()
q = Sample()

assert type(p) == type(q), print('Type Mismatch')
# print(f' object p {p.__class__} and q {q.__class__} are of same type')


# task 3:- Value present in number is part of the list.

lst = [10, 20, 30, 40, 50]
num = 40

assert num in lst, 'num is missing from lst'


# task 4:- Length of combined string is 45 characters

s1 = 'The quick brown fox '
s2 = 'jumps over the lazy dog'

s = s1 + s2
assert len(s) <= 45, 'String is too long.'
print(s)
print(len(s))


# task 4:- Gross salary in the range 30,000 to 45,000
gs = 30000 + 20000 * 15/100 + 20000 * 12/100
print(gs)

assert 30000 <= gs <= 45000, 'Gross salary out of range'


"""


"""
Que 6:- Define a decorators that will decorate any function such that it prepends a call with a message
        indicating that the function is being called and follows the call with a message indicating that
        the function has been called. Also, report the name of the function being called, its arguments 
        and its return value.  
"""


def call_decorator(func):
    def _decorator(*args, **kwargs):
        print(f'Calling {func.__name__}, ({args} , {kwargs})')
        value = func(*args, **kwargs)
        print(f'Called {func.__name__}, ({args}, {kwargs}) got return value: {value}')

    return _decorator


@ call_decorator
def sum_of_num(n1, n2):
    return n1 + n2


@ call_decorator
def prod_of_num(n1, n2):
    return n1 + n2


@ call_decorator
def message(msg):
    pass


sum_of_num(10, 20)
print()
prod_of_num(10, 20)

print()

sum_of_num(n1=10, n2=20)
print()
prod_of_num(n1=10, n2=20)


message('Error should never pass silently.')






