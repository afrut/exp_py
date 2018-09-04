import subprocess as sp
import numpy as np
import cv2
import matplotlib.pyplot as plt

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

# create a copy of the region of interest
seg = np.copy( roi )

# first threshold - global threshold
# all pixels lower than red 160 is not part of the flower
mask = roi[:,:,2] <= 160
seg[mask] = [0,0,0]

# second threshold - global threshold
# all pixels where blue is greater than red is not part of the flower
mask = roi[:,:,0] > roi[:,:,2]
seg[mask] = [0,0,0]

## second threshold
#mask = ( seg[:,:,2] - seg[:,:,0] ) <= 11
#seg[mask] = [0,0,0]
#mask = seg[:,:,2] < seg[:,:,0]
#seg[mask] = [0,0,0]
#mask = seg[:,:,2] < seg[:,:,1]
#seg[mask] = [0,0,0]
#
## third threshold
#tot = np.add( seg[:,:,2], seg[:,:,1] )
#tot = np.add( tot, seg[:,:,0] )

# plot the segmented image in a window
cv2.namedWindow('seg', cv2.WINDOW_NORMAL)
cv2.moveWindow( 'seg', 920, 200 )
cv2.imshow('seg',seg)

# plot a histogram for the region of interest
color = ( 'b','g','r' )
for i, col in enumerate( color ):
    hist = cv2.calcHist( [seg], [i], None, [256], [0,256] )
    plt.plot( hist, color = col )
    plt.xlim( [0,256] )
plt.ylim( [0, 40000] )
plt.xticks( np.arange( 0, 256, 10 ) )
plt.grid( True )

# wait for keypress before closing all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# show and close all
plt.show()
plt.close( 'all' )
