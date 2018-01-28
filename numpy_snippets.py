import subprocess as sp
import numpy as np

sp.call( 'cls', shell = True )

#**********************************************************************
#
# ARRAYS
#
#**********************************************************************
a = np.array( [2,3,4] ) # create an array
a.dtype                 # object specifying the type of the array's elements
a.ndim                  # number of axes/dimensions of the array
a.size                  # total number of elements in the array
a.itemsize              # number of bytes of each element

#**********************************************************************
#
# ARRAY CREATION
#
#**********************************************************************
# arrays can be created from python sequences
a = np.array( [1, 2, 3] )           # created from a python list
b = np.array( (4, 5, 6) )           # created from a python tuple
c = np.array( [[1,2,3], [4,5,6]] )  # created from a list of lists
d = np.zeros( [5,6] )               # preallocate an array with zeroes, 5 rows, 6 columns
e = np.ones( [2,3] )                # preallocate an array with ones
f = np.empty( (3,4) )               # preallocate an array, output may vary
g = np.arange( 1, 20, 2 )           # array from 1 to 20 in steps of 2
h = np.linspace( 4, 40, 7 )         # array from 4 to 40 with 7 numbers
