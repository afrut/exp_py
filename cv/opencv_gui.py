import subprocess as sp
import numpy as np
import cv2

sp.call( 'cls', shell = True )

#**********************************************************************
#
# LOADING, SHOWING, SAVING
#
#**********************************************************************
# Load a color image in grayscale
img = cv2.imread('.\\img\\flower.png',0)

# display an image with original resolution and close after
cv2.imshow('image',img)

# wait for a keypress from the user
k = cv2.waitKey(0)

# check if the user specified to save the image
if k == 's':
    cv.imwrite('img_grayscale.png',img)
cv2.destroyAllWindows()

# display an image with another resolution on a resizable window
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
