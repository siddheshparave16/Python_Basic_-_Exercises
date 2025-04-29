import sys
import threading
import time
import shutil
import os


"""
Que 3:- Which are the two methods available for launching thread in a python program ?

# Answer starts here...


# A simple function that will run in a thread
def print_numbers(n):
    for i in range(1, n+1):
        square = i * i
        print(f'num = {i}  square = {square}')
    print()


# Create a thread object
th1 = threading.Thread(target=print_numbers, args=(10,))


# This starts the thread in a new, separate thread.
# th1.start()


# This will run the target function in the main thread, not in a separate thread.
th1.run()

"""


"""
Que 4:- If ex class is extend the thread class, then can we launch multiple thread for objects of ex class?
        If yes, how?

# Answer starts here...


class MyThread(threading.Thread):

    def __init__(self, name=None):
        if name is None:
            super().__init__()
        else:
            super().__init__(name=name)
        self.name = self.name

    def run(self):
        th = threading.current_thread()
        for i in range(1, 5):
            print(f'{th.name} ----->  Number - {i} , Square - {i*i}')
            time.sleep(1)


start_time = time.time()

# Initialize objects of MyThread

th1 = MyThread(name='New Thread1')
th2 = MyThread()
th3 = MyThread(name='New Thread3')

print('Printing Square of first 5 Natural Numbers :-')

# to launch a thread
th1.start()
th2.start()
th3.start()

# wait for thread to complete
th1.join()
th2.join()
th3.join()


end_time = time.time()
total_time = end_time - start_time
print(f'\nThe program executed in {total_time}s')
print("All threads have finished.")


"""


"""
Que 5:- Write a multithreaded program that copies contents of one folder into another folder.
        The source and target folder paths should be input through keyboard.

# Answer starts here...


def folder_copy(source, target):
    try:
        print('Directory coping under process...')
        # Check if the source exists
        if not os.path.exists(source):
            print(f'Source directory {source}  not exist')
            return

        # Copy the directory
        shutil.copytree(source, target, dirs_exist_ok=True)
        print('Directory copied successfully')

    except Exception as e:
        print(f'Error {e}')


source_folder = input('Enter a Source folder for copying content :- ')
target_folder = input('Enter a target folder to copy content of Source folder :- ')

start_time = time.time()

# Create and start a thread for copying
th1 = threading.Thread(target=folder_copy, args=(source_folder, target_folder))
th1.start()
th1.join()

end_time = time.time()
total_time = end_time - start_time

print(f"Program executed in {total_time}s")

"""


"""
Que 5:- Write a program that reads the contents of 3 file a.txt, b.txt and c.txt sequentially and 
        convert their content into uppercase and writes them into files aa.txt, bb.txt and cc.txt respectively.
        the program should report the time required in carrying out this conversion. The file a.txt, b.txt and c.txt 
        should be added to the project and filled with some text. The program should receive the fine names as 
        command-line arguments. suspend the program for 0.5 seconds after reading a line from any file.

# Answer starts here...

# Record the start time
start_time = time.time()

# list of file names received as command-line arguments
lst = sys.argv[1:]      # Exclude the script name
print("Source files:", lst)


# Destination file names corresponding to the source files
destination_lst = ['aa.txt', 'bb.txt', 'cc.txt']

# Process each source file and its corresponding destination file
for file1, file2 in zip(lst, destination_lst):
    print(f"Processing {file1} -> {file2}")

    try:
        with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'w', encoding='utf-8') as f2:

            while True:
                # Read one line from the source file
                data = f1.readline()

                # Suspend the program for 0.5 seconds after reading the line
                time.sleep(0.5)

                # Break the loop if EOF is reached
                if data == '':
                    break

                # Write the line in uppercase to the destination file
                f2.write(data.upper())

    except FileNotFoundError:
        print(f'File {file1} not found. Skipping...')
    except Exception as e:
        print(f"An error occurred while processing {file1}: {e}")

# Record the end time
end_time = time.time()

# Calculate and display the total execution time
total_time = end_time - start_time
print(f'Program executed in {total_time}s')


"""


"""
Que 6:- Write a program that accomplishes the same task mentioned in Excise Que5 above by launching
        the conversion operation in 3 different thread.
"""


def file_processing(source_file, destination_file):
    try:
        with open(source_file, 'r', encoding='utf-8') as f1, open(destination_file, 'w', encoding='utf-8') as f2:

            while True:
                # Read one line from the source file
                data = f1.readline()

                # Suspend the program for 0.5 seconds after reading the line
                time.sleep(0.5)

                # Break the loop if EOF is reached
                if data == '':
                    break

                # Write the line in uppercase to the destination file
                f2.write(data.upper())

    except FileNotFoundError:
        print(f'File {source_file} not found. Skipping...')
    except Exception as e:
        print(f"An error occurred while processing {source_file}: {e}")


# Record the start time
start_time = time.time()

# list of file names received as command-line arguments
lst_of_file = sys.argv[1:]      # Exclude the script name
print("Source files:", lst_of_file)


# Destination file names corresponding to the source files
dest_lst = ['aa.txt', 'bb.txt', 'cc.txt']

# Thread object for each source file and its corresponding destination file
threads = []
for file1, file2 in zip(lst_of_file, dest_lst):

    # creating thread object for each pair
    th = threading.Thread(target=file_processing, args=(file1, file2))
    threads.append(th)
    print(f'launching thread {th.name}...')
    # launching a thread
    th.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
    print(f'Thread {thread.name} executed..')


# Record the end time
end_time = time.time()

# Calculate and display the total execution time
total_time = end_time - start_time
print(f'Program executed in {total_time:.2f}s')






















