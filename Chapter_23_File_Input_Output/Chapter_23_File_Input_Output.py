import os

# File I/O
# Program that implements this sequence of file I/O operations.

# write and read text data

msg1 = 'Pay taxes with a smile..\n'
msg2 = 'I tried, but they wanted money!\n'
msg3 = 'Don\'t feel bad...\n'
msg4 = 'It is alright to have no talent!\n'

# Open file for writing....
f = open('messages', 'w')

f.write(msg1)
f.write(msg2)
f.write(msg3)
f.write(msg4)
f.close()


# opens file for reading...
f = open('messages', 'r')
data = f.read()
print(data)
f.close()

# The "a" mode will append the new data to the existing content in the file.
# So, previous contents will remain intact when you write new data.

f = open('messages', 'a+')
msg = 'Success is not final, failure is not fatal: It is the courage to continue that counts.\n'
msgs = ['Humpty\n', 'Dumpty\n', 'Sat\n', 'On\n', 'a\n', 'wall\n']
f.write(msg)
f.writelines(msgs)


# Writing other types of data (tuple, list, dictionary)
tpl = ('Ajay', 23, 15000)
lst = [24, 45, 67, 78, 23]
d = {'Name': 'Ajit', 'Age': 23}

f.write(str(tpl) + '\n')        # Convert tuple to string
f.write(str(lst) + '\n')        # Convert lst to string
f.write(str(d) + '\n')          # Convert dict to string

# To read the file after writing to it, you need to move the cursor back to the beginning
f.seek(0)

# method file_name.read() will read entire file contents and return as a string.
print("To read entire file content\n")
new_data = f.read()
print(new_data)

print('\n')


# read 'n' character and return as string
print("To read file till n th content\n")
f.seek(0)
# read data till 100th characters
datas = f.read(100)
print(datas)

print('\n')

# read a line and return as string
# Moves the file cursor to beginning of list
print("To read entire file content line by line \n")
f.seek(0)
n_data = f.readline()
print(n_data)
n_data = f.readline()
print(n_data)
n_data = f.readline()
print(n_data)

f.close()


# writing a file in binary mode
f = open('a.dat', 'wb+')

# series of bytes, \x indicates hexadecimal
d = b'\xee\x86\xaa'
f.write(d)

f.close()


# print("Current working directory:", os.getcwd())






