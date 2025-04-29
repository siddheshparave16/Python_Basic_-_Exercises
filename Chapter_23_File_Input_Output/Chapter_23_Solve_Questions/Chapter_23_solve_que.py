import os
import time

"""
Que 1:- Write a program that read contents of file 'messages' one character at a time.
        Print each character that is read.



# using while loop
with open('messages.txt', 'r') as f:
    while True:
        # at a time read one character
        data = f.read(1)
        if data == '':
            break
        print(data, end='')


# using for loop
print('\nusing for loop')
with open('messages.txt', 'r') as f:
    for data in f.read():
        print(data, end='')


"""


"""
Que 2:- Write a program that writes four integers to a file called 'numbers'. Go to following positions in file
        and report these positions.

# f.seek() for moving to cursor of the file
# f.tell() will give current position of cursor in the file 



with open('numbers', 'bw') as f:
    f.write(b'231')
    f.write(b'431')
    f.write(b'2632')
    f.write(b'833')


with open('numbers', 'br') as f:
    # 10 position from beginning
    f.seek(10, 0)
    print(f.tell())

    # 2 positions to the right of current position
    f.seek(2, 1)
    print(f.tell())

    # 5 position to the left of current position
    f.seek(-5, 1)
    print(f.tell())

    # 10 position to the left from the end
    f.seek(-10, 2)
    print(f.tell())


"""


"""
Que 3:- Write a python program to searches for a file, obtains its size and
        reports the size in bytes/KB/MB/GB/TB as appropriates. 



def get_file_size(filepath):
    # get file size in bytes
    size_in_bytes = os.path.getsize(filepath)

    for units in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.2f} {units}"
        size_in_bytes /= 1024.0


# Example usage
file_name = r"D:\\Programing Videos\\Build a Social Media App with Django – Python Web Framework Tutorial.mp4"

if os.path.isfile(file_name):
    print(f'File size:', get_file_size(file_name))
    print(os.stat(file_name))
else:
    print("File Doesn't exist.")

if os.path.isdir(file_name):
    print(f'File size:', get_file_size(file_name))
else:
    print("Directory Doesn't exist.")


"""


"""
Que 4:- Write a program that reports the time of creation, time of last access and timee of last modification
        for a given file.
        
"""

file = r"D:\Siddhesh_files\Let_Us_python\Chapter_21_Iterator_&_Generator.py"
print(file)


created = os.path.getctime(file)
modified = os.path.getmtime(file)
access = os.path.getatime(file)

print('Date created', time.ctime(created))
print('Date Modified', time.ctime(modified))
print('Date Access', time.ctime(access))





























