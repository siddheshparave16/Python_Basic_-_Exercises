import random
import time
import threading


"""
Que 1:- Write a program through which you can prove that in this programming situation synchronization
        is really required. Then write a program to demonstrate how synchronization can solve thee problem.
        
# Answer starts here...


def fun1():
    print('Entering fun1...')

    # accessing global variable
    global g
    lck.acquire()
    g += 1
    time.sleep(10)
    g -= 1
    lck.release()
    print('In fun1 g=', g)
    print('Exiting fun1.')


def fun2():
    print('Entering fun2...')

    # accessing global variable
    global g
    lck.acquire()
    g += 2
    g -= 2
    lck.release()
    print('In fun2 g=', g)
    print('Exiting fun2.')


# global variable
g = 10

# create lock object
lck = threading.Lock()

th1 = threading.Thread(target=fun1)
th2 = threading.Thread(target=fun2)

th1.start()
th2.start()

th1.join()
th2.join()


"""


"""
Que 2:- write a program that calculate the squares and cubes of first 6 odd numbers through function 
        that are executed in two independent threads. Incorporate a delay of 0.5 seconds after calculation of each 
        square / cube value. Report the time required for execution of the program. Make sure that 
        the output of squares() and cubes() doesn't get mixed up.  

# Answer starts here...


def squares(nos, lck):
    lck.acquire()
    print('calculating the squares...')

    for n in nos:
        print(f'n = {n}  square = {n * n}')
        time.sleep(0.5)
    lck.release()


def cubes(nos, lck):
    lck.acquire()
    print('Calculating the cubes...')

    for n in nos:
        print(f'n = {n}  cube = {n * n * n}')
        time.sleep(0.5)
    lck.release()


arr = [1, 3, 5, 7, 9, 11]

start_time = time.time()

# crete a lock object
global_lck = threading.Lock()

th1 = threading.Thread(target=squares, args=(arr, global_lck))
th2 = threading.Thread(target=cubes, args=(arr, global_lck))

th1.start()
th2.start()

th1.join()
th2.join()

end_time = time.time()
total_time = end_time - start_time
print(f'Program executed in {total_time:.2f} s')


"""


"""
Que 3:- Write a program that prints the following 3 messages through 3 different threads:
        [What s this life...]
        [We have no time...]
        [To stand and stare!]
        
        Each thread should be passed the relevant message and should print '[' message and ']' through
        three different print() calls.
        

# Answer starts here...


def print_it(msg, lck):
    lck.acquire()
    print('[', end='')
    print(msg, end='')
    time.sleep(0.5)
    print(']')
    lck.release()


lck = threading.Lock()

th1 = threading.Thread(target=print_it, args=('What s this life...', lck))
th1.start()

th2 = threading.Thread(target=print_it, args=('We have no time...', lck))
th2.start()

th3 = threading.Thread(target=print_it, args=('To stand and stare!', lck))
th3.start()


th1.join()
th2.join()
th3.join()


"""


"""
Que 4:- Write a program that run a recursive print_num() function in two threads.
        This function should received an integer and print all numbers from that number up to 1.

# Answer starts here...


def print_num(num):
    rlock.acquire()
    if num != 0:
        t = threading.current_thread()
        print(t.name, ':', 'n =',num)

        # decrement of number
        num -= 1
        print_num(num)
    rlock.release()


rlock = threading.RLock()
th1 = threading.Thread(target=print_num, args=(8,))
th2 = threading.Thread(target=print_num, args=(5,))

th1.start()
th2.start()

th1.join()
th2.join()


"""


"""
Que 5:- Write a program that run recursive factorial function in 2 threads.
        This function should receive an integer and print all the intermediate products and final product.

# Answer starts here..


def factorial_num_of(n):
    rlock.acquire()
    fact = 0

    if n != 0:
        t = threading.current_thread()
        fact = n * factorial_num_of(n-1)
        print(t.name, n, '!=', fact)
    else:
        fact = 1
    rlock.release()
    return fact


# Define a reentrant lock (RLock)
rlock = threading.RLock()

# Create threads
th1 = threading.Thread(target=factorial_num_of, args=(10,))
th2 = threading.Thread(target=factorial_num_of, args=(6,))

# starts threads
th1.start()
th2.start()

# wait for threads to finish
th1.join()
th2.join()


"""


"""
Que 6:- Write a program that define a function fun() that prints a message that it receives infinite times.
        Limit the number of threads that can invoke fun() to 3. If 4th thread tries to invoke the fun().
        it should not get invoked.
        

# Answer starts here...


def fun(msg):
    s.acquire()
    th = threading.current_thread()

    for _ in range(5):
        rlock.acquire()
        print(th.name, ':', msg)
        rlock.release()
    # s.release()


rlock = threading.RLock()

s = threading.BoundedSemaphore(3)

th1 = threading.Thread(target=fun, args=('Hello', ))
th2 = threading.Thread(target=fun, args=('Welcome', ))
th3 = threading.Thread(target=fun, args=('ByeBye', ))
th4 = threading.Thread(target=fun, args=('Good Bye', ))


th1.start()
th2.start()
th3.start()
th4.start()


th1.join()
th2.join()
th3.join()
th4.join()


"""


"""
Que 7:- Write a program that run fun1() and fun2() in two different threads. Using an event object,
        function fun1() should wait for fun2() to signal it at random intervals that its wait is over.
        On receiving the signal, fun1() should report the time and clear th event flag.
        
# Answer starts here...


def fun1(ev, n):
    for i in range(1,n):
        print(i, 'Waiting for the flag to be set..')
        ev.wait()
        print('Wait complete at:', time.ctime())
        ev.clear()
        print()


def fun2(ev, n):
    for i in range(n):
        time.sleep(random.randrange(2,5))
        ev.set()


ev = threading.Event()

th = []
num = random.randrange(4, 8)

th.append(threading.Thread(target=fun1, args=(ev, num)))
th[-1].start()

th.append(threading.Thread(target=fun2, args=(ev, num)))
th[-1].start()
for t in th:
    t.join()

print('All done!!')


"""


"""
Que 8:- Write a program that implements a Producer-Consumer algorithm. The producer thread should generate 
        random numbers in range 10 to 20. The consumer thread should print the square of the random number 
        produced by the producer thread.
        
"""


def producer():
    for i in range(5):
        time.sleep(random.randrange(2, 5))
        cond.acquire()
        # Wait until the consumer has consumed the last item
        while len(q) > 0:
            cond.wait()  # Wait for consumer to finish consuming
        num = random.randint(10, 20)
        print('Generated number=', num)
        q.append(num)
        # Notify consumer that there is a new number
        cond.notify()
        cond.release()


def consumer():
    for i in range(5):
        cond.acquire()
        # Wait if the queue is empty
        while True:
            if len(q):
                # Consume the last number from the queue
                num = q.pop()
                break
            cond.wait()

        print('Its square=', num*num)
        # Notify producer that the consumer is done and it can generate a new number
        cond.notify()
        cond.release()


cond = threading.Condition()
q = []

th1 = threading.Thread(target=producer)
th2 = threading.Thread(target=consumer)

th1.start()
th2.start()

th1.join()
th2.join()

print('All done!!')






