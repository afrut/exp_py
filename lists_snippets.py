import subprocess as sp # needed to execute clear screen

# clear the screen
tmp = sp.call('clear',shell=True)

# create a list and popualte it
colors = ['red', 'blue', 'green', 'yellow', 'black', 'white']
print( "The colors list:" )
print( str(colors) + "\n" )

# access third element of list and print
print( "The third element of the colors list:" )
print( colors[2] + "\n" )

# access last element of list and print
print( "The last element of the colors list:" )
print( colors[-1] + "\n")

# modify elements in a list
colors[0] = 'orange'
print( "Changed the firsdt element of the colors list to:" )
print( colors[0] + "\n")

# add element to tail end
colors.append( 'purple' )
print( "Added color purple to the end:" )
print( str(colors) + "\n")

# add element at 4th position
colors.insert( 3, 'cyan' )
print( "Added cyan to the fourth position:" )
print( str(colors) + "\n")

# remove an element
del colors[0]
print( "Removed the first color:" )
print( str(colors) + "\n")

# pop element from tail end
poppedColor = colors.pop()
print( "Popped the last color " + poppedColor + ": " )
print( str(colors) + "\n")

# pop any element
poppedColor = colors.pop(4);
print( "Popped the fifth color " + poppedColor + ": " )
print( str(colors) + "\n" )

# remove an item by value
colors.remove( 'cyan' )
print( "Removed the cyan color:" )
print( str(colors) + "\n" )

# display sorted list
print( "Displaying the sorted list but not sorting it:" )
print( str(sorted(colors)) + "\n" )

# actually sort the list
colors.sort()
print( "Actually sorting the list:" )
print( str(colors) + "\n" )

# reverse the order of elements in the list
colors.reverse()
print( "Reversing the order of the colors:" )
print( str(colors) + "\n" )

# length of the list
print( "The length of the list:" )
print( str(len(colors)) + "\n" )

# loop through all elements in a list
n = 0
for color in colors:
    print( "Color at index " + str(n) + ": " + color )
    n = n + 1
print( "" )

# print numbers 1 - 4 using the range function
for n in range(1,5):
    print( "Printing from 1 to 4 using the range function = " + str(n) )
print( "" )

# make a list of numbers using the range function 
ls1 = list( range(1,6) )
print( "Created a list ls1 from 1 to 5 using the range function:" )
print( str(ls1) + "\n" )

# make a list fromi 2 to 11 incrementing by 2
ls2 = list( range(2,11,2) )
print( "Created a list ls2 from 2 to 11 incrementing by 2:" )
print( str(ls2) + "\n" )

# simple statistics of numbers
print( "Simple statistics of the ls2 list:" )
print( "Min: " + str( min(ls2) ) )
print( "Max: " + str( max(ls2) ) )
print( "Sum: " + str( sum(ls2) ) )
print( "" )

# list comprehension - using one line of code to create and populate a list
squares = [ val ** 2 for val in range( 1, 11 ) ]
print( "Created a list using list comprehensions:" )
print( str(squares) + "\n" )

# slicing a list
print( "Slicing a list:" )
print( "First 3 elements: " + str( squares[0:3] ) )
print( "Second to fourth elements: " + str( squares[1:4] ) )
print( "First to fourth elements: " + str( squares[:4] ) )
print( "Third to last elements: " + str( squares[2:] ) )
print( "Last 3 elements: " + str( squares[-3:] ) )
print( "" )

# copying a list
squares2 = squares[:]
print( "Copied list: " + str(squares2) + "\n" )

# create a reference to a list
refSquares = squares
refSquares.append( 11**2 )
print( "The list modified by reference is:" )
print( squares )
print( '' )

# find elements in one list that are not in another
ls1 = range(0,11)
ls2 = [ 2, 4, 6, 8, 10 ]
print( 'Elements in ls1 not in ls2:' )
print( list( set( ls1 ).difference( ls2 ) ) )
