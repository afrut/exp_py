import subprocess as sp # needed to execute clear screen

# clear the screen
tmp = sp.call('clear',shell=True)

# tuples are lists that are immutable (cannot change)
coordinates = (7,3)
print( "x coordinate: " + str(coordinates[0]) )
print( "y coordinate: " + str(coordinates[1]) )
print( "" )

# redefine the tuple
coordinates = (8,4)
print( "Redefined x coordinate: " + str(coordinates[0]) )
print( "Redefined y coordinate: " + str(coordinates[1]) )
