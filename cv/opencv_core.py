import subprocess as sp
import numpy as np
import cv2

sp.call( 'cls', shell = True )

#**********************************************************************
#
# ACCESSING AND MODIFYING PIXEL VALUES
#
#**********************************************************************
img = cv2.imread('.\img\d3.png')

# slower (performance-wise) way of accessing pixel values
print( 'Accessing pixel[100,100]:' )
print( 'pixel[100,100] BGR value= ', img[100,100] )         # access the pixel at (100,100)
print( 'pixel[100,100] BLUE value = ', img[100,100,0] )     # access the blue value of pixel at (100,100)
print( 'pixel[100,100] GREEN value = ', img[100,100,1] )    # access the green pixel at (100,100)
print( 'pixel[100,100] RED value = ', img[100,100,2] )      # access the red pixel at (100,100)
print( '' )

# faster (performance-wise) way of accessing pixel values
print( 'More efficiently accessing pixel[100,100]:' )
print( 'pixel[100,100] BLUE value = ', img.item(100,100,0) )     # access the blue value of pixel at (100,100)
print( 'pixel[100,100] GREEN value = ', img.item(100,100,1) )    # access the green pixel at (100,100)
print( 'pixel[100,100] RED value = ', img.item(100,100,2) )      # access the red pixel at (100,100)
print( '' )

#**********************************************************************
#
# ACCESSING IMAGE PROPERTIES
#
#**********************************************************************
print( 'Image dimensions:', img.shape )
print( 'Total number of pixels:', img.size )
print( 'Image data type:', img.dtype )

#**********************************************************************
#
# SELECTING A REGION OF INTEREST
#
#**********************************************************************
# show rows 390 to 450 and columns 1200 to 1260
rows = 390
cols = 1200
quest = img[rows:rows + 60, cols:cols + 60]
cv2.imshow('quest',quest)
k = cv2.waitKey(0)
