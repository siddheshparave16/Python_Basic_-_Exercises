from abc import ABC, abstractmethod

"""
Que 2:- Suppose there are base class B and a derived class D from B. B has two public member functions
        b1() and b2(), whereas D has two member function d1() and d2(). Write these classes for the following
        different solutions:

        - b1() should be accessible from main module, b2() should not be.
        - Neither b1(), nor b2() should be accessible from main module.
        - Both b1() and b2() should be accessible from main module


# - b1() should be accessible from main module, b2() should not be.

class B:
    def b1(self):
        print('Inside b1() of class B')

    def __b2(self):
        print('Inside b2() of class B')


class D(B):
    def d1(self):
        super().b1()
        # super().__b2()
        print('Inside d1() of class D')

    def d2(self):
        print('Inside d2() of class D')


obj_d = D()
obj_d.d1()


# - Neither b1(), nor b2() should be accessible from main module.

class B:
    def __b1(self):
        print('Inside b1() of class B')

    def __b2(self):
        print('Inside b2() of class B')

    def _call_private_methods(self):
        self.__b1()
        self.__b2()

class D(B):
    def d1(self):
        # super().__b1()
        # super().__b2()
        self._call_private_methods()
        print('Inside d1() of class D')

    def d2(self):
        print('Inside d2() of class D')


obj_d = D()
obj_d.d1()


# - Both b1() and b2() should be accessible from main module

class B:
    def b1(self):
        print('Inside b1() of class B')

    def b2(self):
        print('Inside b2() of class B')


class D(B):
    def d1(self):
        super().b1()
        super().b2()
        print('Inside d1() of class D')

    def d2(self):
        print('Inside d2() of class D')


obj_d = D()
obj_d.d1()


"""
import gc

"""
Que 4:- If a class D derived from two base classes B1 and B2, then write these classes each containing a constructor.
        Ensure that while building an object of type D, constructor of B2 should get called.
        Also provide a destructor in each class. In what order would these destructor get called ?



class MobilePhone:
    def __init__(self):
        self.__brand = input('Enter a Name of Phone brand :- ')
        self.__screen_size = input('Enter a screen size in inches :- ')
        self.__storage = input('Enter a phone storage in GB:- ')

    def display(self):
        print(self.__brand, self.__screen_size, self.__storage)

    def make_call(self):
        print(f'MobilePhones use to contact through call.')

    def __del__(self):
        print('Deleting MobilePhone object ' + str(self))


class CameraDevice:
    def __init__(self):
        self.__camera_resolution = input('Resolution of camera :- ')
        self.__zoom_level = input('Zoom level of camera :- ')

    def display(self):
        print(self.__camera_resolution, self.__zoom_level)

    def take_photo(self):
        print('Camera used to click clear and adorable Photos.')

    def __del__(self):
        print('Deleting CameraDevice object ' + str(self))


class SmartPhones(CameraDevice, MobilePhone):
    def __init__(self):
        print("SmartPhones Constructor is being called")
        super().__init__()
        MobilePhone.__init__(self)

    def display(self):
        CameraDevice.display(self)
        MobilePhone.display(self)

    def video_call(self):
        print('SmartPhones have features of Video calling.')

    def __del__(self):
        print('Deleting SmartPhone object ' + str(self))
        super().__del__()
        MobilePhone.__del__(self)


# Create an instance of SmartPhones
obj_s = SmartPhones()
obj_s.display()
obj_s.video_call()

# Explicitly delete the object to trigger destructor calls
del obj_s

# Call garbage collection manually to ensure destructors are invoked
gc.collect()  # Forces garbage collection


"""


"""
Que 3:- Create an abstract class called Vehicle containing methods speed(), maintenance() and value() in it.
        Derive classes FourWheeler, TwoWheeler, Airborne from Vehicle class. check whether your able to prevent
        creation of Vehicle class. call the methods using objects of other class. 



class Vehicle(ABC):
    @abstractmethod
    def speed(self):
        pass

    @abstractmethod
    def maintenance(self):
        pass

    @abstractmethod
    def value(self):
        pass


class FourWheeler(Vehicle):
    def speed(self):
        print('>>>Speed of FourWheeler Vehicle....')

    def maintenance(self):
        print('>>>Maintenance for FourWheeler Vehicle....')

    def value(self):
        print('>>>Value of FourWheeler Vehicle...')


class TwoWheeler(Vehicle):
    def speed(self):
        print('>>>Speed of TwoWheeler Vehicle....')

    def maintenance(self):
        print('>>>Maintenance for TwoWheeler Vehicle....')

    def value(self):
        print('>>>Value of TwoWheeler Vehicle...')


class Airborne(Vehicle):
    def speed(self):
        print('>>>Speed of Airborne Vehicle....')

    def maintenance(self):
        print('>>>Maintenance for Airborne Vehicle....')

    def value(self):
        print('>>>Value of Airborne Vehicle...')


obj_fv = FourWheeler()
obj_fv.speed()
obj_fv.maintenance()
obj_fv.value()

print('\n')

obj_tw = FourWheeler()
obj_tw.speed()
obj_tw.maintenance()
obj_tw.value()

print('\n')

obj_fv = FourWheeler()
obj_fv.speed()
obj_fv.maintenance()
obj_fv.value()


# Uncommenting the next line will raise a TypeError, as Vehicle is abstract and can't be instantiated
# obj_ab = Vehicle()            # This will throw a TypeError


"""


"""
Que 4:- Assume class D is Derived from class B, which of the following an object of class D Access?
    - members of D
    - members of B



class B:
    def __init__(self):
        self.b_member = "'B's class Member."

    def b_method(self):
        print("This Method Contain inside Class B")


class D(B):
    def __init__(self):
        # This calls the constructor of class B
        super().__init__()
        self.d_member = "'D's class member"

    def d_method(self):
        print("This Method Contain inside Class D")


# Creating an object of class D
obj_of_b = D()

# Accessing the inherited member from class B
print(obj_of_b.b_member)

# Accessing the member from class D
print(obj_of_b.d_member)

# Calling the inherited method from class B
obj_of_b.b_method()

# Calling the method from class D
obj_of_b.d_method()

"""


"""
Que d:- What can an abstract class contain -- Instance method, class method, abstract method.



class Vehicle(ABC):
    # Abstract method
    @abstractmethod
    def speed(self):
        pass

    # Regular instance method with implementation
    def display_type(self):
        print('This is Vehicle type.')

    # Class method with implementation
    @classmethod
    def vehicle_type(cls):
        print(f"The Vehicle type is {cls.__name__} ")


class Car(Vehicle):
    # Implementing the abstract method
    def speed(self):
        print("Speed of Car is 120 km/hr")


# Create an instance of Car
obj_c = Car()
obj_c.speed()

# Call Instance method
obj_c.display_type()

# calling class method
obj_c.vehicle_type()

"""


# sample code for execute
class Sample(ABC):
    @abstractmethod
    def display(self):
        pass


s = Sample()

























