

# Documentation strings

def display():
    """Display a Message"""
    print('hello')
    print(display.__doc__)


def show(mes1='', mes2=''):
    """ Display 2 Messages

        :argument
        mes1 = message to be displayed in lowercase (default:)
        mes2 = message to be displayed in uppercase (default:)
    """

    print(mes1.lower())
    print(mes2.upper())
    print(show.__doc__)


# function call
display()

# show function call
show('Cinderella', 'Mozzarella')

# Using help() method we can print function/class/method documentation systematically
help(display)
help(show)

































