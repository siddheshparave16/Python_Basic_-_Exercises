from abc import ABC, abstractmethod

"""
# Containership

# Program for Department object is contained in an Employee object.

class Department:
    def __init__(self):
        self.__id = input('Enter a Department Id:- ')
        self.__name = input('Enter department name:- ')

    def display_department(self):
        print(f'Department Id: {self.__id}')
        print(f'Department Id: {self.__name}')


class Employee:
    def __init__(self):
        self.__eid = input('Enter Employee Id:- ')
        self.__ename = input('Enter Employee Name:- ')
        self.__dobj = Department()

    def display_employee(self):
        print(f'Employee Id: {self.__eid}')
        print(f'Employee name: {self.__ename}')
        self.__dobj.display_department()


e1 = Employee()
e1.display_employee()

"""


"""
# Inheritance 
   - Inherit feature to new class from existing class 
   - base class - derived class
   - Construction of an object is always proceed from base towards derived.
   - syntax for calling base class constructor inside child class is
     super().__init__():
   - Derived class object can contain all base class objects.  


# base class
class Index:
    def __init__(self):
        self._count = 0

    def display(self):
        print(f'Count = {self._count}')

    def incr(self):
        self._count += 1


# derived class
class NewIndex(Index):
    def __init__(self):
        super().__init__()

    def decr(self):
        self._count -= 1


# creating a child class object
i = NewIndex()

# accessing method of parent class using object of child class.
i.incr()
i.incr()
i.incr()
i.incr()
i.incr()

i.display()
i.decr()
i.display()
i.decr()
i.display()
i.decr()
i.display()


"""


"""
What is Accessible where ?


class Base:
    def __init__(self):
        self.i = 10
        self._f = 3.14
        self.__s = 'Hello'

    def display(self):
        print(self.i, self._f, self.__s)


class Derived(Base):
    def __init__(self):
        super().__init__()
        self.i = 100
        self._f = 31.4
        self.__s = 'Good Morning'
        self.j = 20
        self._b = 6.4
        self.__ss = 'Hi'

    def display(self):
        super().display()
        print(self.i, self._f, self.__s)
        print(self.j, self._b, self.__ss)


base_obj = Base()
base_obj.display()
print(base_obj.i)
print(base_obj._f)

# the private attribute of base class cannot accessible outside the class - it will through AttributeError.
# print(base_obj.__s)

drv_obj = Derived()
drv_obj.display()
print(drv_obj.i)
print(drv_obj._f)

# the private attribute of derived class cannot accessible outside the derived class - it will through AttributeError.
# print(drv_obj.__ss)


# However,private attributes can still be accessed using name mangling, but it will break principle of encapsulation :

# print(base_obj._Base__s)
# print(drv_obj._Derived__s)
# print(drv_obj._Derived__ss)

print(isinstance(base_obj, Base))
print(issubclass(Derived, Base))


print(issubclass(Base, object))

# The object class
# All methods in object class are available in all classes.

print(dir(object))
print(dir(Base))
print(dir(Derived))



print(Base.mro())
print(Derived.mro())

"""


"""
Features of Inheritance

Inheriting an Existing Feature: Derived classes inherit all methods and attributes from the base class by default.

Suppressing (Overriding) an Existing Feature: A derived class can override a method from the base class
                                              to change its behavior. The base class method is suppressed and
                                               replaced by the new version in the derived class.
      
      
Extending an Existing Feature: A derived class can extend the behavior of a base class method by calling 
                               the base class's method using super() and then adding additional functionality. 

"""


"""
Types of Inheritance:- 

# Multiple Inheritance -



class Product:
    def __init__(self):
        self.__product_name = input('Enter Product Name:- ')
        self.__price = float(input('Enter Product Price:- '))

    def display_data(self):
        print(f'Product Name: {self.__product_name}, Product Price: {self.__price}')


class Sales:
    def __init__(self):
        self.__sales_figures = [int(x) for x in input('Enter Totals sales separated by space').split()]

    def display_data(self):
        print(f'Total Sales: {self.__sales_figures}')


class HardwareItems(Product, Sales):
    def __init__(self):
        Product.__init__(self)
        Sales.__init__(self)
        self.__category = input('Enter Items Category:- ')
        self.__oem = input('Enter Original Equipment Manufacturer:- ')

    def display_data(self):
        Product.display_data(self)
        Sales.display_data(self)
        print(f'Hardware Item Category: {self.__category}, Original Equipment Manufacturer: {self.__oem}')


hw1 = HardwareItems()
hw1.display_data()

hw2 = HardwareItems()
hw2.display_data()


"""


"""
Diamond Problem
# to remove ambiguity - pyton linearized the search order in left to right order
# left to write ---> (base1 ,base2)


class Base:
    def display(self):
        print('In Base')


class Derived1(Base):
    def display(self):
        print('In Derived1.')


class Derived2(Base):
    def display(self):
        print('In Derived2')


class Der(Derived1, Derived2):
    def display(self):
        super().display()
        Derived1.display(self)
        Derived2.display(self)


d1 = Der()
d1.display()
print(Der.__mro__)


"""


"""
Abstract Classes


class Shape(ABC):
    @ abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print('In Rectangle.draw')


class Circle(Shape):
    def draw(self):
        print('In Circle.draw')


# s = Shape()           # will result in error, as Shape is abstract class
c = Circle()
c.draw()

r = Rectangle()
r.draw()


"""


"""
Que 2:- Write a program that uses simple Inheritance between classes Base and Derived.
        If there is a method in Base class, how do you prevent it from being overridden in the Derived class ?



class Base:
    def __method(self):
        print('In Base.__Method')

    def func(self):
        self.__method()


class Derived(Base):
    def __method(self):
        print('In Derived.__method')


b = Base()
b.func()

d = Derived()
d.func()

"""


"""
Que 3:- Write a program that defines an abstract class called Printer containing an abstract method print().
        Derive from it two classes - LaserPrinter and InkjetPrinter. Create a Object of derived classes and
        call the print() method using these objects, passing to it the name of the file to be printed.
        In the print method simply print the filename and the class name to which print() belongs. 



class Printer(ABC):
    def __init__(self, printer_name):
        self.__name = printer_name

    @abstractmethod
    def print_it(self):
        pass


class LaserPrinter(Printer):
    def __init__(self, printer_name):
        super().__init__(printer_name)

    def print_it(self, doc_name):
        print('>> LaserPrinter.printing...')
        print('Trying to print :', doc_name)


class InkjetPrinter(Printer):
    def __init__(self, printer_name):
        super().__init__(printer_name)

    def print_it(self, doc_name):
        print('>> InkjetPrinter.printing...')
        print('Trying to print :', doc_name)


laser_obj = LaserPrinter('Laser s1452')
laser_obj.print_it('Hello.pdf')

ink_obj = InkjetPrinter('Cannon AB145')
ink_obj.print_it('Python.py')


"""


"""
Que 4:- Define an abstract class called Character containing an abstract method patriotism(). Define a class Actor 
        containing a method style(). Define a class Person derived from derived from character and actor. Implement 
        the method patriotism() in it, and override the method style() in it. Also define new method do_acting() in it.
        create an object of Person class and call three methods in it.
"""


class Character(ABC):
    @abstractmethod
    def patriotism(self):
        pass


class Actor:
    def style(self):
        print('>>Actor Style...')


class Person(Character, Actor):
    def do_acting(self):
        print('>> Person Do Acting...')

    def patriotism(self):
        print('>>person patriotism...')

    def style(self):
        print('>>Person style...')


new_person = Person()
new_person.do_acting()
new_person.patriotism()
new_person.style()






