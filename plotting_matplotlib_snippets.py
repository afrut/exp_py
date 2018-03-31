import numpy as np
import subprocess as sp
import matplotlib.figure as fgr
import matplotlib.backends.backend_agg as ba
import matplotlib.pyplot as plt
import scipy.stats as stats

sp.call( 'cls', shell = True )

#***********************************************************************
#
# MATPLOTLIB OBJECT-ORIENTED INTERFACE
#
#***********************************************************************
#x = np.arange(5)
#y = x**2
#z = x * 2
#fig = fgr.Figure()              # create a new Figure object
#ba.FigureCanvas( fig )          # attach a canvas to the figure object
#ax = fig.add_subplot(111)       # plot on a grid with 1 row, 1 column at position 1
#ax.plot(x, y)                   # plot y vs x
#ax.set_title( 'OO Interface' )  # set the plot title
#ax.set_xlabel( 'X axis' )       # set the plot label for x axis
#ax.set_ylabel( 'Y axis' )       # set the plot label for y axis
#fig.savefig( 'test' )           # save the figure as a png file

#***********************************************************************
#
# MATPLOTLIB PYPLOT INTERFACE
#
#***********************************************************************
#plt.plot( x, y )
#plt.xlabel( 'X axis' )
#plt.ylabel( 'Y axis' )
#plt.title( 'Pyplot Interface' )
#plt.show()

#***********************************************************************
#
# MATPLOTLIB OO AND PYPLOT INTERFACE
#
#***********************************************************************
#fig = plt.figure()              # create a new figure using pyplot
#ax = fig.add_subplot(111)
#ax.plot( x, y )
#ax.plot( x, z )
#ax.legend( ['curve','line'], loc='best' )
#ax.set_title( 'Combined Interface' )
#ax.set_xlabel( 'X axis' )
#ax.set_ylabel( 'Y axis' )
#plt.show()
#plt.savefig( 'combined interface.png' )

#***********************************************************************
#
# PLOTS
#
#***********************************************************************
x = np.random.randn( 100 )
y = np.random.randn( 100 )
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.scatter( x, y )
plt.hlines( y = 0, xmin = min(x), xmax = max(x) )
ax.set_xlabel( 'X' )
ax.set_ylabel( 'Y' )
ax.set_title( 'Scatter Plot' )
ax.legend( ['Scatter','Line 1'] )
plt.show()


#***********************************************************************
#
# STATISTICAL PLOTS
#
#***********************************************************************
#mu = 160
#sigma = 10
#n = 50
#population = np.random.randn(10000) * sigma + mu;
#sample = np.random.choice( population, size = n )
#fig = plt.figure()
#ax = fig.add_subplot(111)
#stats.probplot( sample, plot = plt )
#ax.set_title( 'Normal Probability Plot' )
#plt.show()
