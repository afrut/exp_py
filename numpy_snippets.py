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
a = np.array( [1, 2, 3] )                               # created from a python list
b = np.array( (4, 5, 6) )                               # created from a python tuple
c = np.array( [[1,2,3], [4,5,6]] )                      # created from a list of lists
d = np.zeros( [5,6] )                                   # preallocate an array with zeroes, 5 rows, 6 columns
e = np.ones( [2,3] )                                    # preallocate an array with ones
f = np.empty( (3,4) )                                   # preallocate an array, output may vary
g = np.arange( 1, 20, 2 )                               # array from 1 to 20 in steps of 2
h = np.linspace( 4, 40, 7 )                             # array from 4 to 40 with 7 numbers
i = np.array( [[1,2],[3,4]] )                           # 2 by 2 array
j = np.array( [[5,6],[7,8]] )                           # another 2 by 2 array
k = np.random.random( [3,4] )                           # create a 3x4 array with random elements
k = np.round( k, 4 )                                    # round the elements of the array
l = np.array( [[1,2,3],[4,5,6],[7,8,9],[10,11,12]] )    # 4 by 3 array
m = np.array([7,8,9])[np.newaxis,:]                     # create a row array by adding an axis
n = np.array([7,8])[:,np.newaxis]                       # create a column array by adding an axis
print( '-------------------------------------------------------' )
print( 'Array creation:' )
print( 'a = '       + str( a ) )
print( 'b = '       + str( b ) )
print( 'c = '       + str( c ) )
print( 'd = \n'     + str( d ) )
print( 'e = \n'     + str( e ) )
print( 'f = \n'     + str( f ) )
print( 'g = '       + str( g ) )
print( 'h = '       + str( h ) )
print( 'i = \n'     + str( i ) )
print( 'j = \n'     + str( j ) )
print( 'k = \n'     + str( k ) )
print( 'l = \n'     + str( l ) )
print( 'm = \n'     , m )
print( 'n = \n'     , n )
print( '' )

#**********************************************************************
#
# BASIC ARRAY OPERATIONS
#
#**********************************************************************
print( '-------------------------------------------------------' )
print( 'Basic array operations:' )
print( 'a + b   = '                    + str( a + b ) )
print( 'a - b   = '                    + str( a - b ) )
print( 'a * b   = '                    + str( a * b ) )
print( 'b / a   = '                    + str( b / a ) )
print( 'b**2    = '                    + str( b**2 ) )
print( 'b < 4.5 = '                    + str( b < 4.5 ) )
print( 'i matrix product j = \n'       + str( np.dot( i,j ) ) )
a+= 3; print( 'a += 3 = \n'            + str( a ) )   # in-place addition
a*= 2; print( 'a *= 2 = \n'            + str( a ) )   # in-place multiplication
print( 'sum( k ) = '                   + str( k.sum() ) )
print( 'min( k ) = '                   + str( k.min() ) )
print( 'max( k ) = '                   + str( k.max() ) )
print( 'cumsum( k ) = \n'              + str( k.cumsum() ) )
print( 'sumOfColumns( k ) = '          + str( k.sum( axis = 1 ) ) )
print( 'minOfColumns( k ) = '          + str( k.min( axis = 1 ) ) )
print( 'maxOfColumns( k ) = '          + str( k.max( axis = 1 ) ) )
print( 'cumsumOfColumns( k ) = \n'     + str( k.cumsum( axis = 1 ) ) )
print( '' )

#**********************************************************************
#
# UNIVERSAL FUNCTIONS
#
#**********************************************************************
print( '-------------------------------------------------------' )
print( 'Some universal functions:' )
print( 'exp( a )  = ' + str( np.exp(a) ) )
print( 'sqrt( a ) = ' + str( np.sqrt(a) ) )
print( 'a + b     = ' + str( np.add(a,b) ) )
print( 'sin( a )  = ' + str( np.sin(a) ) )
print( '' )

#**********************************************************************
#
# INDEXING, SLICING AND ITERATING
#
#**********************************************************************
x = np.round( k.cumsum() ** 3, 4 )
print( '-------------------------------------------------------' )
print( 'Indexing 1D arrays:' ) 
print( 'All elements of x = \n'                 + str( x[::] ) )
print( '5th element of x         = '            , str( x[4] ) )
print( '4th to 6th elements of x = '            , str( x[3:6] ) )
print( '1st element of x         = '            , str( x[0] ) )
print( 'Last element of x        = '            , str( x[-1] ) )
print( 'All but first 2 elements of x = \n'     , str( x[2:] ) )
print( 'All but last 2 elements of x = \n'      , str( x[:-2] ) )
print( 'Every 2nd element of x = \n'            , str( x[::2] ) )
print( 'Every 3rd element of x = \n'            , str( x[::3] ) )
print( 'Reversed x = \n'                        , str( x[::-1] ) )
print( '' )
print( '-------------------------------------------------------' )
print( 'Boolean indexing:' )
print( 'x =\n', x )
print( 'c =\n', c )
print( 'Boolean mask of x > 30 =\n'                     , x > 30 )
print( 'Indices of x that are > 30 =\n'                 , np.nonzero(x > 30) )
print( 'Indices of x that are > 30 =\n'                 , np.where(x > 30) )
print( 'Elements of x that are > 30 =\n'                , x[np.nonzero(x > 30)] )
print( 'Boolean mask of elements [1,5,6] in c =\n'      , np.isin(c, [1,5,6]) )
print( 'Indices of [1,5,6] in c =\n'                    , np.nonzero( np.isin(c, [1,5,6]) ) )
ix = np.nonzero( np.isin(c, [1,5,6]) )
print( 'List of tuples of indices of [1,5,6] in c =\n'  , list( zip( *[list(ix[0]),list(ix[1])] ) ) )
print( '-------------------------------------------------------' )
print( 'Indexing 2D arrays:' )
print( 'l =\n', l )
print( 'Row 3 column 2 of l = \n'   + str( l[2,1] ) )
print( 'Row 3 of l = \n'            + str( l[2,:] ) )
print( 'Column 3 of l = \n'         + str( l[:,2] ) )
print( 'Rows 2 and 3 of l = \n'     + str( l[1:3,:] ) )
print( '' )

#**********************************************************************
#
# MODIFYING ARRAYS
#
#**********************************************************************
print( '-------------------------------------------------------' )
print( 'Modifying arrays:' )
print( 'a =\n', a )
print( 'b =\n', b )
print( 'c =\n', c )
print( 'i =\n', i )
print( 'l =\n', l )
print( 'm = \n', m )
print( 'n = \n', n )
print( 'Appending an element to flattened c:\n'              , np.append( c, 1 ) )
print( 'Appending a row to c:\n'                             , np.append(c, m, axis = 0) )
print( 'Appending a column to c:\n'                          , np.append(c, n, axis = 1) )
print( 'Inserting an element into c:\n'                      , np.insert( c, 3, 0 ) )
print( 'Inserting a row of 3\'s into row 2 of c:\n'          , np.insert( c, 1, 3, axis = 0 ) )
print( 'Inserting a column of 2\'s into column 2 of c:\n'    , np.insert( c, 1, 2, axis = 1 ) )
print( 'Reshaping c to 3 rows by 2 columns:\n'               , np.reshape( c, [3,2] ) )
print( 'Flatten to have one dimension:\n'                    , c.flatten() )
print( 'Delete 3rd element of a:\n'                          , np.delete( a, [2], axis = 0 ) )
print( 'Delete 3rd row of l:\n'                              , np.delete( l, 2, axis = 0 ) )
print( 'Delete 3rd column of l:\n'                           , np.delete( l, 2, axis = 1 ) )
print( 'Concatenate m on top of a:\n'                        , np.concatenate( (a[np.newaxis,:], m), axis = 0 ) )
print( 'Concatenate m beside a:\n'                           , np.concatenate( (a[np.newaxis,:], m), axis = 1 ) )

# TODO: np.vectorize
# TODO: np.squeeze
# TODO: np.array_equal
# TODO: slice
# TODO: iterators and generators
