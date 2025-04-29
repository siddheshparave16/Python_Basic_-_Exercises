import math

"""
Que 1:- Write a program to create a class that represents Complex numbers containing real and imaginary parts
        and then use it to perform complex number addition, Subtraction, multiplication and division.



class Complex:

    def __init__(self, real, image):
        self.__real = real
        self.__image = image

    def display(self):
        print(f'Complex Number {self.__real} + {self.__image}j')

    def add_complex_numbers(self, other):
        # Add two complex numbers
        real_part = self.__real + other.__real
        image_part = self.__image + other.__image
        return Complex(real_part, image_part)

    def sub_complex_numbers(self, other):
        real_part = self.__real - other.__real
        image_part = self.__image - other.__image
        return Complex(real_part, image_part)

    def multi_complex_numbers(self, other):
        real_part = self.__real * other.__real
        image_part = self.__image * other.__image
        return Complex(real_part, image_part)

    def div_complex_numbers(self, other):
        real_part = self.__real / other.__real
        image_part = self.__image / other.__image
        return Complex(real_part, image_part)


x = Complex(7, 4)
y = Complex(5, 2)
x.display()
y.display()


# Perform operations
a = x.add_complex_numbers(y)
print("Addition: ", end="")
a.display()

b = x.sub_complex_numbers(y)
print("Subtraction: ", end="")
b.display()

c = x.multi_complex_numbers(y)
print("Multiplication: ", end="")
c.display()

d = x.div_complex_numbers(y)
print("Division: ", end="")
d.display()


"""


"""
Que 2:- Write a program that implements a Matrix class and perform addition, multiplication, 
        and transpose operations on 3X3 matrices.
        
# Answer starts here...


class Matrix:
    def __init__(self, row1, row2, row3):
        if len(row1) != 3 and len(row2) != 3 and len(row3) != 3:
            raise ValueError('Each row must contain exactly 3 elements.')

        # Initialize the matrix
        self.matrix = [row1, row2, row3]

    def display(self):
        [print(" ".join(map(str, row))) for row in self.matrix]

    def add_matrix(self, other):
        result = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[i]))] for i in range(len(self.matrix))]

        return Matrix(*result)

    def multi_matrix(self, other):
        result = [
            [self.matrix[i][j] * other.matrix[i][j] for j in range(len(self.matrix[i]))] for i in range(len(self.matrix))]

        return Matrix(*result)

    def transpose_matrix(self):
        result = [
            [self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]

        return Matrix(*result)


print("Matrix 1:")
x = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
x.display()

print()

print("Matrix 2:")
y = Matrix([9, 8, 7], [6, 5, 4], [3, 2, 1])
y.display()

res = x.add_matrix(y)
print("Addition of Matrices :")
res.display()

res2 = x.multi_matrix(y)
print("Multiplication of Matrices :")
res2.display()

transpose_m = x.transpose_matrix()
print("Transpose of Matrix :")
transpose_m.display()


"""


"""
Que 3:- Write a program to create class that can calculate the surface area and volume of solid. 
        The class should also have provision to accept the data relevant to the solid. 



class Solid:

    def __init__(self, shape=None, length=0, radius=0, height=0):
        '''Initialize the solid's attributes.'''
        self.__shape = shape.lower() if shape else None
        self.__length = length
        self.__height = radius
        self.__radius = height

    def set_dimensions(self):
        user_input = input('Enter the shape (cube, sphere, cylinder) :')
        if user_input == 'cube':
            self.__shape = 'cube'
            try:
                self.__length = float(input('Enter a edge length of the cube :- '))
                if self.__length <= 0:
                    print('Length must be positive !')
                    self.__length = 0
            except ValueError:
                print('Invalid input. Length must be a number.')
                self.__length = 0

        elif user_input == 'sphere':
            self.__shape = 'sphere'
            try:
                self.__radius = float(input('Enter a Radius of the Sphere :- '))
                if self.__radius <= 0:
                    print('Radius must be positive !')
                    self.__radius = 0
            except ValueError:
                print('Invalid input. Radius must be positive number.')
                self.__radius = 0

        elif user_input == 'cylinder':
            self.__shape = 'cylinder'
            try:
                self.__radius = float(input('Enter a Radius of the cylinder :- '))
                self.__height = float(input('Enter a Height of the cylinder :- '))
                if self.__radius <= 0 and self.__height <= 0:
                    print('Radius and Height must be positive !')
                    self.__radius = 0
                    self.__height = 0
            except ValueError:
                print('Invalid input. Both radius and height must be numeric values.')
                self.__radius = 0
                self.__height = 0
        else:
            print("Invalid shape input. Please enter 'cube', 'sphere', or 'cylinder'.")
            self.__shape = None

    def surface_area(self):
        if self.__shape == 'cube':
            if self.__length > 0:
                surface_area_of_cube = 6 * (self.__length**2)
                return surface_area_of_cube
            else:
                print('Invalid input. length must be a number.')
                return None

        elif self.__shape == 'sphere':
            if self.__radius > 0:
                surface_area_of_sphere = 4 * math.pi * (self.__radius ** 2)
                return surface_area_of_sphere
            else:
                print('Invalid input. Radius must be a number.')
                return None
        elif self.__shape == 'cylinder':
            if self.__radius > 0 and self.__height > 0:
                surface_area_of_cylinder = 2 * math.pi * self.__radius * (self.__radius + self.__height)
                return surface_area_of_cylinder
            else:
                print('Invalid input. Radius and Height must be a number.')
                return None
        else:
            print("Invalid shape. Please set the shape and dimensions correctly.")
            return None

    def volume_area(self):
        if self.__shape == 'cube':
            if self.__length > 0:
                volume_of_cube = self.__length ** 3
                return volume_of_cube
            else:
                print('Invalid Input, Length must be positive number.')
                return None

        elif self.__shape == 'sphere':
            if self.__radius > 0:
                volume_of_sphere = (4/3) * math.pi * (self.__radius ** 3)
                return volume_of_sphere
            else:
                print('Invalid Input, Radius must be positive number.')
                return None

        elif self.__shape == 'cylinder':
            if self.__radius > 0 and self.__height > 0:
                volume_of_cylinder = math.pi * (self.__radius ** 2) * self.__height
                return volume_of_cylinder
            else:
                print('Invalid Input, Both Radius and Height must be positive')


solid = Solid()
solid.set_dimensions()
a = solid.surface_area()
print(a)
b = solid.volume_area()
print(b)


"""


"""
Que 4:- Write a program to create a class that can calculate the perimeter / circumference and area of a regular shape.
        The class should also have a provision to accept the data relevant to the shape.
        
        # Note :- Regular shape have all sides are equal and all angles are same .



class Shapes:
    def __init__(self, shape=None, side=0, radius=0):
        self.__shape = None
        self.__side = side
        self.__radius = radius

    def set_data(self):
        while True:
            user_input = input('Enter a Regular Shape (square, triangle, pentagon, hexagon, octagon, circle.) :- ').lower()
            if user_input in ('square', 'triangle', 'pentagon', 'hexagon', 'octagon', 'circle'):
                self.__shape = user_input
                break
            else:
                print("Invalid shape. Please enter a regular shape.(square, triangle, pentagon,hexagon,octagon, circle")

        if self.__shape == 'circle':
            self.set_circle_radius()  # Call method to set the radius
        else:
            self.set_side_length()  # Call method to set the radius

    def set_side_length(self):
        while True:
            try:
                if self.__shape == 'square':
                    self.__side = float(input('Enter the side length of the square: '))
                elif self.__shape == 'triangle':
                    self.__side = float(input('Enter the side length of the triangle: '))
                elif self.__shape == 'pentagon':
                    self.__side = float(input('Enter the side length of the pentagon: '))
                elif self.__shape == 'hexagon':
                    self.__side = float(input('Enter the side length of the hexagon: '))
                elif self.__shape == 'octagon':
                    self.__side = float(input('Enter the side length of the octagon: '))

                if self.__side > 0:
                    break
                else:
                    print(f"Side length of {self.__shape} must be a positive number.")

            except ValueError:
                print('Invalid input. Side length must be a valid positive number.')

    def set_circle_radius(self):
        while True:
            try:
                self.__radius = float(input('Enter Radius of circle :- '))
                if self.__radius > 0:
                    break
                else:
                    print("Radius of circle must be a positive number.")
            except ValueError:
                print('Invalid input. Radius of circle must be positive number.')

    def perimeter_of_regular_shape(self):
        if self.__shape == 'square':
            perimeter = 4 * self.__side
            return perimeter
        elif self.__shape == 'triangle':
            perimeter = 3 * self.__side
            return perimeter
        elif self.__shape == 'pentagon':
            perimeter = 5 * self.__side
            return perimeter
        elif self.__shape == 'hexagon':
            perimeter = 6 * self.__side
            return perimeter
        elif self.__shape == 'octagon':
            perimeter = 8 * self.__side
            return perimeter
        elif self.__shape == 'circle':
            circumference = 2 * math.pi * self.__radius
            return circumference
        else:
            return None   # If the shape is not recognized

    def area_of_regular_shape(self):
        if self.__shape == 'square':
            area = self.__side ** 2
            return area
        elif self.__shape == 'triangle':
            area = (math.sqrt(3)/4) * (self.__side ** 2)
            return area
        elif self.__shape == 'pentagon':
            area = (1/4) * ((math.sqrt(5)*(5 + 2 * math.sqrt(5))) * (self.__side ** 2))
            return area
        elif self.__shape == 'hexagon':
            area = ((3 * math.sqrt(3)) / 2) * (self.__side ** 2)
            return area
        elif self.__shape == 'octagon':
            area = (2 * (1 + math.sqrt(2))) * (self.__side ** 2)
            return area
        elif self.__shape == 'circle':
            area = math.pi * (self.__radius ** 2)
            return area
        else:
            print("Invalid shape. Please enter a valid regular shape.")
            return None


my_shape = Shapes()
my_shape.set_data()
perimeter_of_share = my_shape.perimeter_of_regular_shape()
print(f'Perimeter is {perimeter_of_share: .2f}')

area_of_share = my_shape.area_of_regular_shape()
print(f'Area is {area_of_share: .2f}')

"""


"""
Que 5:- Write a program that create and use Time class to perform varius time arithmetic operation.



class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minutes = minute
        self.__seconds = second

    def set_time(self):
        attempts = 3     # Limit the number of attempts for each input
        while attempts > 0:
            try:
                hours = int(input('Enter your hours from 0 to 23 :- '))
                if 0 <= hours <= 23:
                    self.__hour = hours
                    break
                else:
                    print('Invalid Input, Enter hours from 1 to 24 :-')
                    attempts -= 1
            except ValueError:
                print("Invalid input, please enter a number for hours.")
                attempts -= 1

        if attempts == 0:
            print("Too many invalid attempts for hours. Exiting...")
            return

        attempts = 3  # reset attempts for minutes
        while attempts > 0:
            try:
                minutes = int(input('Enter minutes from 1 to 59:- '))
                if 0 <= minutes <= 59:
                    self.__minutes = minutes
                    break
                else:
                    print('Invalid Input, Enter minutes from 1 to 59 :-')
                    attempts -= 1
            except ValueError:
                print("Invalid input, please enter a number for minutes.")
                attempts -= 1

        if attempts == 0:
            print("Too many invalid attempts for hours. Exiting...")
            return

        attempts = 3  # reset attempts for seconds
        while attempts > 0:
            try:
                seconds = int(input('Enter seconds from 1 to 59:- '))
                if 0 <= seconds <= 59:
                    self.__seconds = seconds
                    break
                else:
                    print('Invalid Input, Enter Seconds from 1 to 59 :-')

            except ValueError:
                print("Invalid input, please enter a number for minutes.")
                attempts -= 1

        if attempts == 0:
            print("Too many invalid attempts for hours. Exiting...")
            return
        print('\n')

    def display(self):
        return f"{self.__hour:02d}: {self.__minutes:02d}: {self.__seconds:02d}"

    def add_time(self, other_time):
        total_seconds = (self.__hour*3600 + self.__minutes*60 + self.__seconds) + \
                        (other_time.__hour*3600 + other_time.__minutes*60 + other_time.__seconds)

        total_hours = total_seconds // 3600
        total_minutes = (total_seconds % 3600) // 60
        total_seconds = total_seconds % 60

        return Time(total_hours, total_minutes, total_seconds)

    def sub_time(self, other_time):
        total_seconds1 = self.__hour*3600 + self.__minutes*60 + self.__seconds
        total_seconds2 = other_time.__hour*3600 + other_time.__minutes*60 + other_time.__seconds

        if total_seconds1 >= total_seconds2:
            total_second = total_seconds1 - total_seconds2

            total_hours = total_second // 3600
            total_minutes = (total_second % 3600) // 60
            total_second = total_second % 60

            return Time(total_hours, total_minutes, total_second)
        else:
            total_second = total_seconds2 - total_seconds1

            total_hours = total_second // 3600
            total_minutes = (total_second % 3600) // 60
            total_second = total_second % 60

            return Time(total_hours, total_minutes, total_second)

    def compare_time(self, other_time):

        # Convert times to total seconds for easy comparison
        total_seconds1 = self.__hour*3600 + self.__minutes*60 + self.__seconds
        total_seconds2 = other_time.__hour*3600 + other_time.__minutes*60 + other_time.__seconds

        if total_seconds1 > total_seconds2:
            return 'Time 1 is later.'
        elif total_seconds1 < total_seconds2:
            return 'Time 2 is later.'
        else:
            return 'Both times are equal.'


time1 = Time()  # 3 hours, 45 minutes, 20 seconds
time2 = Time()  # 2 hours, 30 minutes, 50 seconds
time1.set_time()
time2.set_time()

added_time = time1.add_time(time2)
print(f'{added_time.display()}')

subtract_time = time1.sub_time(time2)
print(f'{subtract_time.display()}')

comparison = time1.compare_time(time2)
print(comparison)


"""


"""
Que 6:- Write a program to implement a linked list data structure by creating a linked list class.
        Each node in the linked list should contain name of the car, its price and a link to the next node.
"""


class Node:
    def __init__(self, car, price):
        self.car = car
        self.price = price
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_car(self, car, price):
        new_node = Node(car, price)

        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def display_cars(self):
        current_node = self.head
        while current_node:
            print(f'Car: {current_node.car}, Price: {current_node.price}')
            current_node = current_node.next


car_list = LinkedList()
car_list.add_car("Toyota", 20000)
car_list.add_car("Honda", 18000)
car_list.display_cars()











