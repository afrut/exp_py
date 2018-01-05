import subprocess as sp # needed to execute clear screen

# clear the screen
tmp = sp.call('clear',shell=True)

# create a list using list comprehension
squares = [ val**2 for val in range( 1, 11 ) ]
print( "Square roots of values greater than 50:" )
for val in squares:
    if val > 50:
        print( val**(1/2) )
    else:
        print( val )
print( "" )

# check if a value is in a list
print( "49 is in squares: " + str( 49 in squares ) )
print( "50 is in squares: " + str( 50 in squares ) )
