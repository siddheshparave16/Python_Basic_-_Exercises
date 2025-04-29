import threading
import time
import sys

"""
Que 1:- Write a program that launches three threads, assigns new name to two threads of them.
        Suspend each thread for 1 seconds after it has been launched.

# Answer starts here..




def func1():
    t = threading.current_thread()
    print('Starting a current thread in func1...', t.name)
    time.sleep(1)
    print('Exiting a current thread in func1...', t.name)


def func2():
    t = threading.current_thread()
    print('Starting a current thread in func2...', t.name)
    time.sleep(1)
    print('Exiting a current thread in func2...', t.name)


def func3():
    t = threading.current_thread()
    print('Starting a current thread in func3...', t.name)
    time.sleep(1)
    print('Exiting a current thread in func3...', t.name)


# use default name
th1 = threading.Thread(target=func1)

# Assigning new name to thread.
th2 = threading.Thread(name='MyThread2', target=func2)
th3 = threading.Thread(name='MyThread3', target=func3)


th1.start()
th2.start()
th3.start()

"""


"""
Que2:- Write a programs that calculates the squares and cubes of the first 6 odd numbers through function
       that executed sequentially. Incorporate a delay of 0.5 seconds after calculation of each square/cube value.
       Report the time required for execution of program.

# Answer starts here...


def squares(num_list):
    print('Calculating cubes..')

    for num in num_list:
        square_of_num = num * num
        time.sleep(0.5)
        print(f'num = {num}   square = {square_of_num}')


def cubes(num_list):
    print('Calculating cubes...')

    for num in num_list:
        cube_of_number = num*num*num
        time.sleep(0.5)
        print(f'num = {num}   cube = {cube_of_number}')


arr = [1, 3, 5, 7, 9, 11]
start_time = time.time()

squares(arr)
cubes(arr)

end_time = time.time()

total_time = end_time - start_time
print(f'Time required to execute program is {total_time}')


"""


"""
Que 3:- Write a programs that calculates the squares and cubes of the first 6 odd numbers through function
       that executed in two independent threads. Incorporate a delay of 0.5 seconds after calculation of 
       each square/cube value. Report the time required for execution of program.

# Answer starts here...


def squares(num_list):
    print('Calculating cubes..')

    for num in num_list:
        square_of_num = num * num
        time.sleep(0.5)
        print(f'num = {num}   square = {square_of_num}')


def cubes(num_list):
    print('Calculating cubes...')

    for num in num_list:
        cube_of_number = num*num*num
        time.sleep(0.5)
        print(f'num = {num}   cube = {cube_of_number}')


arr = [1, 3, 5, 7, 9, 11]
start_time = time.time()

th1 = threading.Thread(target=squares, args=(arr,))
th2 = threading.Thread(target=cubes, args=(arr,))

th1.start()
th2.start()


th1.join()
th2.join()

end_time = time.time()

total_time = end_time - start_time
print(f'Time required to execute program is {total_time} sec')


"""


"""
Que 4:- Write a program that reads the contents of 3 file a.text, b.txt and c.txt sequentially and
        reports the number of lines present in it as well as the total reading time. These files should be
        added to the project and filled with some text. The should receive the file names as command-line
        arguments. Suspend the program for 0.5 seconds after reading a line from any file.
        
# Answer starts here...


start_time = time.time()

lst = sys.argv
lst = lst[1:]
print(lst)

for file in lst:
    count = 0
    with open(file, 'r') as f:
        while True:
            data = f.readline()

            if data == '':
                break
            count += 1

    print('File:', file, 'Count_of_Line in file is', count)

    time.sleep(0.5)

end_time = time.time()

total_time = end_time - start_time
print(f'Time required to execute program is {total_time} sec')


"""

"""
Que 4:- Write a program that reads the contents of 3 file a.text, b.txt and c.txt in different thread and
        reports the number of lines present in it as well as the total reading time. These files should be
        added to the project and filled with some text. The should receive the file names as command-line
        arguments. Suspend the program for 0.5 seconds after reading a line from any file.

"""


def readFile(input_file):
    count = 0
    with open(input_file, 'r') as f:
        while True:
            data = f.readline()
            time.sleep(0.5)

            if data == '':
                break
            count += 1

    print('File:', input_file, 'Count_of_Line in file is', count)


start_time = time.time()

lst = sys.argv
lst = lst[1:]
print(lst)

th_lst = []
for file in lst:
    th = threading.Thread(target=readFile, args=(file,))
    th.start()

    th_lst.append(th)

for th in th_lst:
    th.join()

end_time = time.time()

total_time = end_time - start_time
print(f'Time required to execute program is {total_time} sec')

































