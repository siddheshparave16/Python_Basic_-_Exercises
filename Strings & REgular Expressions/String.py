import random

"""
# String And Regular Expression

# escape them by preceding them with a "\" .
msg = 'He Said, \'Lets Us Python\''
print(msg)

# prepend the string with r indicates a row string
msg2 = r'He said, "Lets Us Python"'
print(msg2)

#  Indexing of String
mystring = "Hello"

# iterating over loop & showing positive index with position
for index, i in enumerate(mystring):
    print(index, i)

# -0 is sane as 0(zero)
a = mystring[0]
b = mystring[-0]
print(a)
print(b)


# String Slicing

print(mystring[:])   # start to end [ : ]
print(mystring[2:])  # [start:]
print(mystring[:3])  # end will be excluded
print(mystring[-4:])   # extract from negative index position to end
print(mystring[:-3])
print(mystring[::-1])  # reversing string through slicing

print(mystring[3:100])
"""


# String Properties

s = 'Hello'
print(s)

# python string is Immutable , they cannot be changed.
# s[0] = 'M'        # rejected
s = 'bye'        # s is a variable , it can change
print(s)

s1 = 'Hello'
s2 = 'My Friend'

# string can be concatenated using '+'
s3 = s1 + s2
print(s3)

# string can be replicate during printing

print('-'*50)

print('ell' in s3)

print(len(s1))
print(min(s1))
print(max(s1))


print(type(s1))
print(id(s1))


# module.function()
num = random.randint(1, 25)           # this function will give random number
print(num)


def string_doc():
    """
    This is a Docstring for below mention method.
    below are String methods by categories
    """
    pass


# help(string_Doc())
print(string_doc().__doc__)

# String Methods

new_str = 'hello'


# content test functions of string - check all character

print(new_str.isalpha())
print(new_str.isdigit())
print(new_str.isalnum())

print(new_str.isupper())
print(new_str.islower())
print(new_str.startswith('h'))
print(new_str.endswith('o'))


# search & replace


print(new_str.find('l'))
print(new_str.replace('h', 'H'))
print(new_str)


# trims whitespace   -  remove whitespace from string

message = '   Hello Friends    '
print(message.strip())
print(message.lstrip())
print(message.rstrip())


# split and partitions

my_str = "Python is a versatile programming language to learn."

print(my_str.split())

# string method which describe (max_split )
text = "apple,banana,orange,grape"
result = text.split(",", 2)  # Only split twice

print(result)


# Que  - Handling Multiple Lines of CSV:


csv_data = """John,25,Male,Engineer
Jane,28,Female,Doctor
Alice,30,Female,Artist"""

print("\n before split function... \n")

print(csv_data)

# Split by newlines to get each row
rows = csv_data.split('\n')

print("\n Get clear data line by line from csv data \n")

# Split each row by comma to get individual fields
for row in rows:
    split_data = row.split(",")
    print(split_data)


ms1 = "Hello"
ms2 = "world"
print("-".join(ms1))


print("\n")
print("\n")

print(" String Comparison")

# string comparison done in alphabetical character by character
# so capital is considered to be less than their lower case counterparts


a1 = 'Bombay'
a2 = 'bombay'
a3 = 'Nagpur'
a4 = 'Bombaywala'
a5 = 'Bombay'

print(a1 == a2)
print(a1 == a5)
print(a1 != a3)
print(a1 < a5)
print(a1 < a2)
print(a1 > a2)
print(a1 <= a4)

print(id(a1))
print(id(a5))

print(" Let see \'Swap case\' example")
s1 = "Bring It On"
print(s1.swapcase())

