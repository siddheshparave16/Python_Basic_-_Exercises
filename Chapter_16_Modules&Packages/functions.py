
def display():
    print('Earlier reach owned cars, while poor had horses')


def show():
    print('Now everyone has car, while only rich own horses')

# same code different Interpretation


def main():
    print('If you beat your own record, you win as well as lose.')
    print('Internet connect people at long distance.')
    print('Internet disconnect people at short distance.')

    display()


"""
-  Sometimes we want to use this program as independent script, 
   and at other times as a module from which we can use display() function
"""


if __name__ == '__main__':
    main()


"""
If we run it as an independent program, it will satisfied, as a result, main() will be called.
If we import this module in another program, it will fail, so main() will not be called.

however the program can called display() and show() independently.
"""











