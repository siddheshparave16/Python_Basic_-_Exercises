

"""
def print_it():  # Global Function
    print('Opener')


class Message:
    # Instance Method
    def display(self, msg):
        print_it()
        print(msg)

    # class method
    def show():
        print_it()
        print('Hello')
        # display()         # this call will result as an error.


# call global function
print_it()
m = Message()        # creating Instance of class

# call Instance method
m.display('Good Morning')

# call class method
Message.show()

"""

"""

class Complex:
    def __init__(self, r=0.0, i=0.0):
        self.__real = r
        self.__imag = i

    def __add__(self, other):
        z = Complex()
        z.__real = self.__real + other.__real
        z.__imag = self.__imag + other.__imag

        return z

    def __sub__(self, other):
        z = Complex()
        z.__real = self.__real - other.__real
        z.__imag = self.__imag - other.__imag

        return z

    def __mul__(self, other):
        z = Complex()
        z.__real = self.__real * other.__real
        z.__imag = self.__imag * other.__imag

        return z

    def magnitude(self):
        return (self.__real ** 2 + self.__imag ** 2) * 0.5

    def __lt__(self, other):
        if not isinstance(other, Complex):
            return NotImplemented
        return self.magnitude() < other.magnitude()

    def __isub__(self, other):
        if not isinstance(other, Complex):
            raise TypeError("Operand must be complex object")
        self.__real -= other.__real
        self.__imag -= other.__imag
        return self

    def display(self):
        print(self.__real, self.__imag)


c1 = Complex(1.1, 2.5)
c2 = Complex(2.1, 1.7)

c3 = c1 + c2
c3.display()

c4 = c1 - c2
c4.display()

c5 = c1 * c2
c5.display()

print(c1 > c2)

a = Complex(2, 5)
b = Complex(4, 3)
a -= b
a.display()


"""

"""

i = 20
j = i
k = j
k = 30
print(k)
print(i, j)


x = 20
y = 20

print(id(x))
print(id(y))
x = 30
print(x, y)
print(id(x))
print(id(y))

print(type(Complex), id(Complex))

"""

"""

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


person = Person('Alice', 30, 'New York')
print(person.name)
print(person.age)


class Bird:
    pass


bird = Bird()
bird.name = 'Parrot'
bird.colour = 'Green'
bird.weight = 300
bird.animal_type = 'Vertebrate'

print(bird.name)

# Modifying attributes Dynamically
bird.weight = 250
bird.colour = 'light-green'

print(bird.name, bird.colour, bird.weight, bird.animal_type)

# deleting attribute dynamically
del bird.animal_type


a1 = 123
a2 = str(a1)
print(type(a2))


"""


"""
Que 1:- Write a program that display the attributes of integer, float and function objects. 
        Also show How this attributes can be used.
        
# Answer starts here..


def fun():
    print('Everything is a Object')


print(dir(55))
print(dir(-2.36))
print(dir(fun()))


print((5).__add__(6))
print((-2.36).__abs__())

d = globals()
d['fun'].__call__()

fun.__call__()


"""


"""
Que 2:- Create a class Date that has a list containing day, month and year attributes. 
        Define an overloaded == operator to compare two date object.


class Date:
    def __init__(self, date, month, year):
        self.__date = date
        self.__month = month
        self.__year = year

    def __eq__(self, other):
        if self.__date == other.__date and self.__month == other.__month and self.__year == other.__year:
            return True
        else:
            return False


d1 = Date(12, 10, 2024)
d2 = Date(24, 12, 2024)
d3 = Date(12, 10, 2024)
print(id(d1))
print(id(d2))
print(id(d3))
print(d1 == d3)
print(d1 == d2)


"""


"""
Que 3:- Create a class Weather that has a list containing Weather parameters. Define an overloaded 'in' operator
        that checks whether an item is present in the list.  
"""


class Weather:

    def __init__(self):
        self.params = ['Temp', 'Rel Hum', 'Cloud Cover', 'Wind Vel']

    def __contains__(self, item):
        return True if item in self.params else False


w = Weather()

if 'Rel Hum' in w:
    print('Valid Weather parameter')
else:
    print('InValid Weather parameter')


if 'Degree' in w:
    print('Valid Weather parameter')
else:
    print('InValid Weather parameter')

















