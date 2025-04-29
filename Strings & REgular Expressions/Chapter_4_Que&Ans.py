import re
# following Question based on Strings & RegularExpressions

"""
Que1 : - write a program that generates the following output from the string ' Shenanigan'.
s h | a n | enanigan | Shenan | Shenan | Shenan | Shenan | Shenanigan | Seaia | Snin
| Saa| ShenaniganType | ShenanWabbite

#  Answer start from Here

# variable assigning
mystring = 'Shenanigan'

print(mystring[0], mystring[1])
print(mystring[4], mystring[5])
print(mystring[2:])
print(mystring[:6])
print(mystring[0:6])
print(mystring[-10:-4])
print(mystring[:-4])
print(mystring[:])
print(mystring[::2])
print(mystring[::3])
print(mystring[::4])
new_string = mystring + 'Type'
print(new_string)

new_string2 = mystring[0:6] + 'Wabbite'
print(new_string2)

"""


"""
Que2 : - write a program to convert following string 
   ' Visit ykanetkar.com for online courses in programming'
   into first letter should be capital of each word in given string 

# Answer start from here
the_string = 'Visit ykanetkar.com for online courses in programming'
print(the_string.title())

"""


"""
Que3 : - write a program to convert following string 
   ' Light travels faster than sound. This is why some people appear bright until you hear them speak'
   
# Answer start here 


n_string = ' Light travels faster than sound. This is why some people appear bright until you hear them speak'
n_string = n_string.replace('Light', 'LIGHT')
n_string = n_string.replace('sound', 'SOUND')
print(n_string)

"""


"""
Que4 :- What will be output of following program ?
s = ' HumptyDumpty'

# Answer start from here

s = 'HumptyDumpty'

print('s=', s)
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
print(s.islower())
print(s.isupper())
print(s.startswith('Hump'))
print(s.endswith('Dump'))

s1 = 'Hello , " Lets Us Python" '

"""


"""
Que5 :- What is purpose of Raw string

# Answer start from here

Raw string is useful when a string needs to contain a backslash, 
such as for a regular expression or Windows directory path, 
and you don't want it to be treated as an escape character.

# a raw string is a special type of string that allows you to include backslashes (\) without interpreting them as escape sequences.

"""


"""
Que6 : - If we wish to work with an individual word in the following string,
        how you will separate them

#  Answer starts here

the_string = 'The difference between stupidity and genius is that genius has its limits'
print(the_string.split(" "))

"""


""""
Que7 :- Mention two ways to store a string: He said, "Let Us Python".

# Answer start here

# using regular string
s_string = 'He said, "Let Us Python"'
print(s_string)
print(id(s_string))

# using raw string
s_string = r'He said, "Let Us Python"'
print(s_string)
print(id(s_string))

# using Escape character
s_string = "He said, \"Let Us Python\""
print(s_string)
print(id(s_string))

"""

"""
Que 8 :- What will be the output of following code snippet ?

# Answer start from here

print(id('Imaginary'))
print(type('Imaginary'))

"""

"""
Que 9 :- What will be the output of following code snippet ?

# Answer start from here



s3 = 'c:\\Users\\kanetkar\\Documents'

print(s3.split('\\'))
print(s3.partition('\\'))          # in this case , output will be a tuple and its makes partition after \\

print()
"""

"""
Que 10 :- How will you extract ' TraPoete' from the string 'ThreadProperties' ?

# Answer start from here

a_string = 'ThreadProperties'
print(a_string[::2])

"""

""""
Que 11 :- How can you eliminate spaces on either side of the string 
string = '  Flanked by spaces on either side  '?


n_string = '     Flanked by spaces on either side     '
print(n_string.strip())

"""

"""
Que 12 :- What will be output of the following code snippet ?

# Answer start here

s1 = s2 = s3 = 'Hello'
print(id(s1), id(s2), id(s3))

"""

"""
Que 13:- What will get stored in ch in the following code snippet :

# Answer start from here

ms = 'Aeroplane'
ch = ms[-0]
print(ch)

"""

"""
Que 14:- 
 
# Answer start from here

msg = 'Keep yourself warm'

print(msg.partition(' '))
print(msg.split())
print(msg.startswith('Keep'))
print(msg.swapcase())
print(msg.capitalize())
print(msg.count('e'))
print(len(msg))
print(msg[0])
print(msg[-1])
print(msg[1:1:1])
print(msg[-1:3])
print(msg[:-3])
print(msg[-3:])
print(msg[0:-2])

"""

"""
Que 15:- Give an Example of string whhich will return a match for the following regular expression.

\w+ | \d | \w{1,} | \w{2,4} | A*B | \d+

Answer start here 


Combined Example:
If the full regular expression is a combination of these patterns (\w+ | \d | \w{1,} | \w{2,4} | A*B | \d+), you can write a string that contains multiple parts matching different segments.

Example String:
"AB123 Hello AAB CD78B"

Matches (Explained):

AB → Matches A*B.
123 → Matches \d+.
Hello → Matches \w+ or \w{1,}.
AAB → Matches A*B.
CD78 → Matches \w{2,4} (CD matches first), and 78 matches \d.
"""

conditions = [r"\w+", r"\d", r"\w{1,}", r"\w{2,4}", r"A*B", r"\d+"]
regex = r"\w+|\d|\w{1,}|\w{2,4}|A*B|\d+"
test_string = "AB123 Hello AAB CD78B"


# Find all matches in the string

matches = re.findall(regex, test_string)
print("Matches:", matches)

for condition in conditions:
    matches2 = re.findall(condition, test_string)
    print(f"Condition '{condition}' matches: {matches2}")


