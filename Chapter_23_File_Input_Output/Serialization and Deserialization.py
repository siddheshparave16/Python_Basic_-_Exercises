import json

"""
# conversion while reading and writing numbers in file

f = open('numbers', 'w+')

# writing numbers into file
f.write(str(233) + '\n')
f.write(str(13.45) + '\n')

f.seek(0)

a = int(f.readline())
b = float(f.readline())

print(a + b)
print(b + b)

"""

"""
# Serialize and deserialize a list

# Open file for writing and reading
f = open('Sampledata.txt', 'w+')

# writing a list data into a file
lst = [10, 20, 30, 40, 50, 60, 70, 80]

# Serialize and save the list as JSON in the file
json.dump(lst, f)

f.seek(0)

# reading data from the file
data_in_lst = json.load(f)
print(data_in_lst)

f.close()

"""


"""
# Serialize and deserialize a tuple

f = open('Sampledata.txt', 'a+')

tpl = ('Ajay', 28, 15200)

# Serialize and save the tpl as JSON in the file
json.dump(tpl, f)

f.seek(0)

data_in_tpl = json.load(f)
print(tuple(data_in_tpl))

f.close()

"""


"""
# Write JSON object line by line
with open('Sampledata.txt', 'a+') as f:
    tpl = ('Ajay', 28, 15200)
    f.write(json.dumps(tpl) + '\n')  # Write each object on a new line

# Read all JSON objects
with open('Sampledata.txt', 'r') as f:
    data = [json.loads(line) for line in f]
    print("Read data:", data)

"""


"""
# serialize and deserialize a dictionary

f = open('Sampledata.txt', 'w+')

dct = {'Anil': 25, 'Ajay': 28, 'Amit': 22}

# serialize and write a data into file
json.dump(dct, f)

f.seek(0)

read_data = json.load(f)
print(read_data)
print(type(read_data))

"""


"""
# Instead of writing json data to a file, we can write to a string. and read it back from a string

lst = [10, 20, 30, 40, 50]
tpl = ('Ajay', 28, 15200)
dct = {'Anil': 25, 'Ajay': 28, 'Amit': 22}

str1 = json.dumps(lst)
str2 = json.dumps(tpl)
str3 = json.dumps(dct)

l = json.loads(str1)
t = tuple(json.loads(str2))
d = json.loads(str3)

print(l)
print(type(l))
print(t)
print(type(t))
print(d)
print(type(d))


"""


"""
# It's possible  to serialize nested lists and dictionaries ... 
"""


lofl = [10, [20, 30, 40], 50, 60, 70, 80, 90]

f = open('Sampledata.txt', 'w+')

json.dump(lofl, f)

f.seek(0)

data = json.load(f)
print(data)

f.close()


f = open('RawData', 'w+')

contacts = {'Anil': {'DOB': '17/11/98', 'Favorite': 'Igloo'},
            'Amol': {'DOB': '07/01/95', 'Favorite': 'Tundra'},
            'Ravi': {'DOB': '19/11/97', 'Favorite': 'Artic'}}


json.dump(contacts, f)

# Moving the cursor back to the start
f.seek(0)

data = json.load(f)
print(data)

f.close()

































