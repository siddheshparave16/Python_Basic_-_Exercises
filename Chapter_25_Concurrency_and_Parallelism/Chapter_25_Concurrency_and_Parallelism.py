import threading
import time
from time import sleep

# returns current thread object
"""

t = threading.current_thread()
print('Current thread:', t)

print('Thread name:-', t.name)
print('Thread Identifier:- ', t.ident)
print('Thread status:- Is Thread alive:-', t.is_alive())


t.name = 'MyThread'
print('After name change:-', t.name)
"""


# Method1 - Thread creation

def func1():
    print('Function func1 is processing...')
    time.sleep(2)
    print('Function func1 is executed...')


def func2():
    print('Function func2 is under process...')
    time.sleep(1)
    print('Function func2 is executed successfully...')


th1 = threading.Thread(name='My first Thread', target=func1)

# user default name of thread
th2 = threading.Thread(target=func2)


"""
# start() method will raise an exception - RuntimeError("threads can only be started once")
# if called more than once on the same thread object.
# th2.start()
"""


def square(n):
    number_square = n * n
    time.sleep(2.5)
    print(f"Square of number {n} is {number_square}")


def cube(n):
    number_cube = n * n * n
    time.sleep(2.6)
    print(f"cube of number {n} is {number_cube}")


th3 = threading.Thread(target=square, args=(5,))
th4 = threading.Thread(target=cube, args=(5,))

th1.start()
th2.start()
th3.start()
th4.start()

# Print active thread count while threads are running
time.sleep(0.5)  # Short delay to ensure threads are active
print(f"Active threads count: {threading.active_count()}")

th1.join()
th2.join()
th3.join()
th4.join()
print(f"Active threads count after completion: {threading.active_count()}")


t = threading.current_thread()
print(t.name)
print(t.ident)
print(threading.get_native_id())


print('Return a list of all Thread objects currently active')
print(threading.enumerate())
print(threading.main_thread())
