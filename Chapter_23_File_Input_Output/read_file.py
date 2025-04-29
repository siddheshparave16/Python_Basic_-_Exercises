f = open('messages', 'rb+')

"""
# first way to read file data
# iterating over the file object
print('reading data in file using for loop')
for data in f:
    print(data, end='')


# second way to read file data
print('reading data in file using readline with infinite loop')

while True:
    data = f.readline()
    if data == '':
        break
    print(data, end='')


# using 'readlines' - read all the lines in a file
print('\nUsing readlines method.....\n')
f.seek(0)
data = f.readlines()
print(data)


f.seek(0)
with open('messages', 'r') as f:
    data = [line.strip() for line in f.readlines()]
    print(data)



f.seek(0)
print(f.tell())

# move to 100 th position from beginning of file.
f.seek(20, 0)
# data = f.read()
# print(data)

print('\n')

f.seek(0)

data = f.readline()
print(data)

print(f.tell())

"""
print(f.tell())
f.seek(5, 1)
data = f.readline()
print(data)



f.close()
