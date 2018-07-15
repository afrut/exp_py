import subprocess as sp
import numpy as np
import cv2

sp.call( 'cls', shell = True )
imgSrc = cv2.imread('.\img\d3.png')

#**********************************************************************
#
# CHANGING COLOR-SPACE
#
#**********************************************************************
# print flags to be used with color conversion cv2.cvtColor
for flag in dir(cv2):
    if flag.startswith('COLOR_'):
        None
        # print( flag )

# change color-space of the image from BGR to gray
imgGray = cv2.cvtColor( imgSrc, cv2.COLOR_BGR2GRAY )

# change color-space of the image from BGR to HSV
imgHsv = cv2.cvtColor( imgSrc, cv2.COLOR_BGR2HSV )

#cv2.imshow( 'gray', imgGray )
#k = cv2.waitKey(0)
#
#cv2.imshow( 'hsv', imgHsv )
#k = cv2.waitKey(0)


