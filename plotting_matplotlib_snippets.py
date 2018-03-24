import numpy as np
import subprocess as sp
import matplotlib.figure as fgr
import matplotlib.backends.backend_agg as ba

sp.call( 'cls', shell = True )

#***********************************************************************
#
# MATPLOTLIB OBJECT-ORIENTED INTERFACE
#
#***********************************************************************
x = np.arange(5)
y = x**2
fig = fgr.Figure()              # create a new Figure object
ba.FigureCanvas( fig )          # attach a canvas to the figure object
ax = fig.add_subplot(111)
ax.plot(x, y)                   # plot y vs x
ax.set_title( 'hello world' )   # set the plot title
ax.set_xlabel( 'x' )            # set the plot label for x axis
ax.set_ylabel( 'y' )            # set the plot label for y axis
fig.savefig( 'test' )           # save the figure as a png file
