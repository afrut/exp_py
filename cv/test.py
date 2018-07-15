import subprocess as sp
import numpy as np
import cv2

sp.call( 'cls', shell = True )

# Load a color image in grayscale
img = cv2.imread( '.\\img\\flower.png' )

# display an image with another resolution on a resizable window
cv2.namedWindow( 'img', cv2.WINDOW_NORMAL )
cv2.moveWindow( 'img', 100, 200 )
cv2.imshow( 'img',img )

# take a region of interest
roi = img[740:2270, 580:2150]
cv2.namedWindow('roi', cv2.WINDOW_NORMAL)
cv2.moveWindow( 'roi', 510, 200 )
cv2.imshow('roi',roi)

# wait for keypress before closing all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
