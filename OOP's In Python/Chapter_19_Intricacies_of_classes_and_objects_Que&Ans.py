
"""
Que 3:- How will you define a structure Employee containing the attributes Name, Age,
        Salary, Address, Hobbies dynamically ?


class Employee:
    pass


# Creating an object of Employee class
e1 = Employee()

# Dynamically assigning attributes to e1
e1.name = 'Ajay'
e1.age = 29
e1.salary = 15000
e1.address = 'Nerul, Navi Mumbai'
e1.hobbies = 'Play Cricket'

# Printing the initial values
print(f'{e1.name}, {e1.age}, {e1.salary}, {e1.address}, {e1.hobbies}')

# Modifying some attributes
e1.salary = 18000
e1.hobbies = 'Music Listening'

# Printing the updated values
print(f'{e1.name}, {e1.age}, {e1.salary}, {e1.address}, {e1.hobbies}')


"""


"""
Que 1:- Which function should be defined to overload the +,-,/,// operators.
a = 5
b = 6

print(a.__add__(b))
print(a.__sub__(b))
print(a.__truediv__(b))
print(a.__floordiv__(b))

"""


"""
Que 3,4,5:- To overload the +, % , //= operator , which methods should be defined in the corresponding class. 



class Numbers:

    def __init__(self, num):
        self.__num = num

    def __add__(self, other):
        z = self.__num + other.__num
        return z

    def __mod__(self, other):
        z = self.__num % other.__num
        return z

    def __ifloordiv__(self, other):
        self.__num //= other.__num
        return self

    def __str__(self):
        return f'Mynumber({self.__num})'


a = Numbers(48)
b = Numbers(5)

print(a.__add__(b))
print(a.__mod__(b))
print((a.__ifloordiv__(b)).__str__())


"""


"""
Que 14:- How will you define the overloaded * operator for the following code snippet ?


class Complex:
    def __init__(self, r=0.0, i=0.0):
        self.__real = r
        self.__imag = i

    def __mul__(self, other):
        z = Complex()
        z.__real = self.__real * other.__real - self.__imag * other.__imag
        z.__imag = self.__real * other.__imag + self.__imag * other.__real
        return z

    def display(self):
        print(f'{self.__real: .2f}, {self.__imag: .2f}i')


c1 = Complex(1.1, 0.2)
c2 = Complex(1.1, 0.2)
c3 = c1 * c2
c3.display()


"""


"""
Que 15:- Implementing a string class containing the following functions.
        - Overload += operator
        - toLower()
        - toUpper()
"""


class String:
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError('Value must be string')
        self.__s = value

    def __iadd__(self, other):
        self.__s += other.__s
        return self

    def toLower(self):
        result = ''
        for char in self.__s:
            if 'A' <= char <= 'Z':
                result += chr(ord(char) + 32)
            else:
                result += char
        self.__s = result
        print(self.__s)
        return self

    def toUpper(self):
        result = ''
        for char in self.__s:
            if 'a' <= char <= 'z':
                result += chr(ord(char) - 32)
            else:
                result += char
        self.__s = result
        print(self.__s)
        return self

    def display(self):
        print(self.__s)


a = String('Jay')
b = String('Chorghe')

c = a.__iadd__(b)
c.display()

b.toUpper()

b.toLower()





