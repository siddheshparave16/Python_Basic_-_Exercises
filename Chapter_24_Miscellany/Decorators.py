import time

# Decorators in python
"""
def my_decorator(func):
    def wrapper():
        print('Lets do some decoration to your function.')
        func()
        print('Thanks for using this decorative function.')

    return wrapper


# if you want to apply decorative function
@ my_decorator
def display():
    print('Inside display function...')
    print('I stand decorated.')


@ my_decorator
def show():
    print('Inside show function...')
    print('Nothing great, Me Too!')


'''
obj_display = my_decorator(display)
obj_display()

print('\n')

obj_show = my_decorator(show)
obj_show()
'''

# instead of above
display()
print('\n')
show()


"""

#  Decorating function with arguments


def timer(func):
    def calculate(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        runtime = end_time - start_time
        print(f'Finished {func.__name__!r} in {runtime:.8f} secs')

        return value
    return calculate


@timer
def product(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact


@ timer
def product_and_sum(num):
    p = 1
    for i in range(1, num+1):
        p = p * i

    s = 0
    for i in (1, num+1):
        s = s + i

    return p,s


@ timer
def time_pass(num):
    for i in range(num):
        i += 1


obj_p = product(10)
print('Product of first 10 numbers=', obj_p)

print()

obj_p1 = product(20)
print('Product of first 20 numbers=', obj_p1)

print()

fs = product_and_sum(10)
print('Product and sum of first 10 numbers=', fs)

print()

fs1 = product_and_sum(20)
print('Product and sum of first 20 numbers=', fs1)

print()

time_pass(20)






























