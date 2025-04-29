import sys
import numpy as np


"""
# creation of array

int_arr = np.array([1, 2, 3, 4])                         # create array of ints
float_arr = np.array([1.1, 2.2, 3.3, 4.4])             # create array of floats

print(int_arr)
print(float_arr)


# if we mix array of int and floats, Numpy default to array of float
mix_arr = np.array([1, 2.3, 4.6, 5, 6, 7.2])
print(mix_arr)


int_arr1 = np.array([1, 2, 3, 4], int)                         # create array of ints
float_arr1 = np.array([1.1, 2.2, 3.3, 4.4], float)             # create array of floats

print(int_arr1)
print(float_arr1)


# 2D array
a1 = np.array([[1, 2, 3], [4, 5, 6]])

# 3D array
a2 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(a1.ndim)
print(a2.ndim)


# array of complex number
com_arr = np.array([[1, 2], [3, 4]], complex)
print(com_arr)


# Creation of Filter Arrays

# create 2D array with garbage value
b1 = np.empty((3, 4))                       # tuple indicates shape of array
print('Array of garbage value:\n', b1)


# create 2D array of zeroes
b2 = np.zeros((3, 3))
print('Array of zeroes:\n', b2)


# create 2D array of one
b3 = np.ones((2, 3))
print('Array of ones:\n', b3)


# create 2D array with all values set to 7
b4 = np.full((2, 2), 7)
print('Array with all values same:\n', b4)


# create array with random values

c1 = np.random.random(4)                # create array with 4 random values
print(c1)


c2 = np.arange(5)
print(c2)

# Step by 5
c3 = np.arange(0, 20, 5)
print(c3)

# number of values 5
c4 = np.linspace(0, 2, 5)
print(c4)


# Identity matrix
d1 = np.eye(3)
print('Identity matrix:\n', d1)

d2 = np.identity(3)
print('Identity matrix:\n', d2)

print(np.__version__)


"""


# Array Attributes

a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([1.6, 2.7, 3.8, 4.9, 5.1])

# type of element present in array
print(a1.dtype)
print(a2.dtype)


# array element size in bytes
print(a1.itemsize)
print(a2.itemsize)


# Total memory consumption of each array
print(a1.nbytes)                    # Total bytes consumed by all elements
print(a2.nbytes)


# memory location where the data buffer of the array is stored.
print(a1.data)


# strides  ---> number of bytes added to the base address to reach to the next element
# Strides= itemsize×step
print(a1.strides)


# (2 elements, each 8 bytes for int64) ---> To move to the next column, you skip 1×8=8 bytes. so output - (16, 8)
a3 = np.array([[1, 2], [3, 4]])
print(a3.strides)


arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# number of dimension
print(arr1.ndim)
print(arr2.ndim)

# shape of array  ---> row, col
print(arr1.shape)
print(arr2.shape)


# number elements present in array
print(arr1.size)
print(arr2.size)


aa = [1, 2, 3, 4, 5]                        # Python list
aaa = np.array([1, 2, 3, 4, 5])             # NumPy array
print(sys.getsizeof(1)*len(aa))             # Memory usage of Python list
print(aaa.nbytes)                           # Memory usage of NumPy array






