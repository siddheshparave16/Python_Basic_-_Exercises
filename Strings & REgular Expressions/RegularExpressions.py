import re

"""

The re.search() method takes a regular expression pattern and 
 a string and searches for that pattern within the string.

# re.search() return a match object otherwise return None
# match = re.search(pat, str)

s = 'Bombaywala'
print(re.search('bay', s))
print(re.search('bac', s))



# Regex Metacharacter 
# List of Metacharacter
# [] - , ^ * + ? {} | () $



# [] is used to specific set of character match

print(re.search('[hb]owl', 'howler'))
print(re.search('[hb]owl', 'bowler'))
print(re.search('[hb]owl', 'cowler'))


# '-' Metacharacter is used to indicate range of character

# example of Re for 6-digit Postal index Number (PIN)
print(" Re for 6-digit Postal index Number (PIN)")
print(re.search('[0-9][0-9][0-9][0-9][0-9][0-9]', '441019'))
print(re.search('[0-9]{6}', '401203'))

# '^' Metacharacter is complement a character set
# Re for a string which begins with anything other than[^ digit or character ]
# The ^ inside brackets negates the character class, meaning it matches anything not in the specified set.

print(re.search('[^0-9]', '0001Zebra'))
print(re.search('[^a-z]', 'ashisH'))
print(re.search('[\w]{5}', 'Hello'))

# RE for string which start with Alphabet or Digit
print(re.search('[a-z|A-Z|0-9]', '123Siddhesh'))
print(re.search('[a-z|$]', '123$'))

# '.'  match any character except new line
print(re.search('[A.Z]', 'BCA'))
print(re.search('[..Z]', '2Z123'))

# RE for words connected with 1 or more Dashes
print(re.search('\d-\d', '444-555'))

# RE for '@' any number of alphanumeric character before @
print(re.search(r'\w*@gmail.com', 'AmanLad12@gmail.com'))

print(chr(128522))
print(ord("😊"))

text = "Hello"
encoded = text.encode("utf-8")
print(encoded)

decoded = encoded.decode("utf-8")
print(decoded)


# '$' is used to match at End of the Line
print(re.search('sat$', 'The cat sat quietly, and then it sat'))



# Que :- Find all Occurrences of "T" in given string , and Replace all Occurrences of "T" with "t"

given_string = 'The Terrible Tiger Tore The Towel'
# let find position of T

start = 0
count = 0
positions = []

while True:
    # find the next occurrence of 'T' form starting from current position
    position_of_T = given_string.find('T', start)

    if position_of_T == -1:
        break

    count += 1
    positions.append(position_of_T)
    start = position_of_T + 1

print("Count of 'T' : ", count)
print("Positions of 'T':", positions)


Updated_given_string = given_string.replace('T', 't')
print(Updated_given_string)

"""

# email example of running example to demonstrate more regular expression features

email_string = 'ashashdbeh153@gmail.com'
match = re.search(r'\w+@\w+', email_string)

if match:
    print(match.group())

# The search does not get the whole email address in this case
# because the \w does not match the '-' or '.' in the address.

# let fix this using Feature of Re

email_string2 = 'ashashdbeh153@gmail.com'
match2 = re.search(r'[\w.-]+@[\w.-]+', email_string2)

if match2:
    print(match2.group())


email_string3 = 'purple alice-b@google.com monkey dishwasher'
match3 = re.search(r'([\w.-]+)@([\w.-]+)', email_string3)

if match3:
    print(match3.group())
    print(match3.group(1))
    print(match3.group(2))


# findall
"""
findall() is probably the single most powerful function in the re module. 
Above we used re.search() to find the first match for a pattern. 
findall() finds *all* the matches and returns them as a list of strings, with each string representing one match.
"""

# Suppose we have a text with many email addresses
multiple_email = ' john.doe@example.com  jane_smith123@mywork.org admin@university.edu  contact.support@company.co.in '

emails = re.findall(r'[\w.-]+@[\w.-]+', multiple_email)

# returns them as a list of strings
for email in emails:
    print(email)

