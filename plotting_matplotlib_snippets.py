import numpy as np
import subprocess as sp
import matplotlib.figure as fgr
import matplotlib.backends.backend_agg as ba
import matplotlib.pyplot as plt
import scipy.stats as stats

sp.call( 'cls', shell = True )

# create some data
x = np.arange(5)
y = x**2
z = x * 2

#***********************************************************************
#
# MATPLOTLIB OBJECT-ORIENTED INTERFACE
#
#***********************************************************************
fig = fgr.Figure()                          # create a new Figure object
ba.FigureCanvas( fig )                      # attach a canvas to the figure object
ax = fig.add_subplot(1,1,1)                 # plot on a grid with 1 row, 1 column at position 1
ax.plot(x, y)                               # plot y vs x
ax.set_title( 'Object-oriented Interface' ) # set the plot title
ax.set_xlabel( 'X axis' )                   # set the plot label for x axis
ax.set_ylabel( 'Y axis' )                   # set the plot label for y axis
fig.savefig( 'test.png' )                   # save the figure as a png file

#***********************************************************************
#
# MATPLOTLIB PYPLOT INTERFACE
#
#***********************************************************************
fig = plt.figure()                          # create a new figure using pyplot
fig.suptitle( 'matplotlib Interfaces' )     # overall title for the figure
ax = fig.add_subplot(1,2,1)
plt.plot( x, y )
plt.xlabel( 'X axis' )
plt.ylabel( 'Y axis' )
plt.title( 'Pyplot Interface' )

#***********************************************************************
#
# MATPLOTLIB OO AND PYPLOT INTERFACE
#
#***********************************************************************
ax = fig.add_subplot(1,2,2)
ax.plot( x, y )
ax.plot( x, z )
ax.legend( ['curve','line'], loc='best' )
ax.set_title( 'Combined Interface' )
ax.set_xlabel( 'X axis' )
ax.set_ylabel( 'Y axis' )
plt.savefig( 'Combined Interface.png' )

#***********************************************************************
#
# PLOTS
#
#***********************************************************************
x = np.random.randn( 100 )
y = np.random.randn( 100 )
fig = plt.figure()
fig.suptitle( 'General Plots' )
ax = fig.add_subplot(1,1,1)
plt.scatter( x, y )
plt.hlines( y = 0, xmin = min(x), xmax = max(x) )
ax.set_xlabel( 'X' )
ax.set_ylabel( 'Y' )
ax.set_title( 'Scatter Plot' )
ax.legend( ['Scatter','Horizontal Line 1'] )

#***********************************************************************
#
# STATISTICAL PLOTS
#
#***********************************************************************
# create sample data
mu = 160
sigma = 10
n = 250
numBins = 10
data = np.random.randn(250) * sigma + mu;
mu = np.mean( data );
sigma = np.std( data );

# plot a histogram with Gaussian fit
fig = plt.figure()
fig.suptitle( 'Statistical Plots' )
ax = fig.add_subplot(1,1,1)
freq, bins, patches = ax.hist( data, numBins )
binWidth = bins[1] - bins[0]
ax.set_xlabel( 'Bins' )
ax.set_ylabel( 'Frequency' )
ax.set_title( 'Histogram of Random Data with Gaussian Fit' )
x = np.linspace( bins[0], bins[-1], 100 )
y = stats.norm.pdf( x, mu, sigma ) * np.sum( freq * binWidth )
y = (1/(np.sqrt(2*np.pi*(sigma**2)))) * \
    np.exp(-((x - mu)**2/(2*sigma**2)))
y = y * np.sum( freq * binWidth )
ax.plot( x, y )
ax.legend(['Gaussian Fit','Frequency'], loc='best')

# show all plots
plt.show()
