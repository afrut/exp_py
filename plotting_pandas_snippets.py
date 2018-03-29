import subprocess as sp
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import sklearn.datasets as datasets

# clear screen
sp.call( 'cls', shell = True )

#***********************************************************************
#
# PANDAS TIME-SERIES PLOTS
#
#***********************************************************************
lsFig = list()  # create list of figures
lsAx = list()   # create list of axes
cntPt = 200     # specify the number of points

# see avaialbe plotting styles in matplotlib
print( 'Available plotting styles in matplotlib:' )
for style in mpl.style.available:
    print( style )

# change the style of matplotlib plotting
#mpl.style.use( 'classic' )

# plot cumulative sum of a time series in a Series type
ts = pd.Series( np.random.randn( cntPt )    # create a time series
              , index = pd.date_range( '1/1/2000', periods = cntPt ) );
ts = ts.cumsum()                            # calculate cumulative sum
ax = ts.plot()                              # plot on the figure
lsAx.append( ax )                           # store axis handle
lsFig.append( ax.get_figure() )             # store figure handle
ax.set_xlabel( 'Day' )                      # x-axis label
ax.set_ylabel( 'Y value' )                  # y-axis label
ax.set_title( 'Time Series Plot' )          # plot title

# plot cumulative sum of multiple time series in a DataFrame type
df = pd.DataFrame( np.random.randn( cntPt, 3 )
                 , index = ts.index
                 , columns = list('ABC') ); # create a DataFrame with 3 columns
df = df.cumsum()                            # calculate cumulative sums per column
ax = df.plot()                              # plot cumulative sums
lsAx.append( ax )                           # store axis handle
lsFig.append( ax.get_figure() )             # store figure handle
ax.set_xlabel( 'Day' )                      # x-axis label
ax.set_ylabel( 'Y value' )                  # y-axis label
ax.set_title( 'Multiple Time Series Plot' ) # plot title

# plot x and y specifying columns of a DataFrame type
df['D'] = pd.Series( list( range( len( df ) ) )
                   , index = df.index )     # add a column D as a count of the index
ax = df.plot( x = 'D', y = 'A' )            # plot A against D
lsAx.append( ax )                           # store axis handle
lsFig.append( ax.get_figure() )             # store figure handle
ax.set_xlabel( 'Column D' )                 # x-axis label
ax.set_ylabel( 'Column A' )                 # y-axis label
ax.set_title( 'Column A against Column D' ) # plot title

# plot x and y with secondary y axis
ax = df.plot( x = 'D', y = 'A'              # plot column A against column D
            , legend = False )              # without legend
ax2 = df.plot( x = 'D', y = 'B'             # plot column B against column D
            , ax = ax                       # on the same figure
            , mark_right = False            # don't mark (right) in legend for columns in secondary axis
            , secondary_y = True )          # on a secondary y axis
ax2 = df.plot( x = 'D', y = 'C'             # plot column C against column D
            , ax = ax                       # on the same figure
            , mark_right = False            # don't mark (right) in legend for columns in secondary axis
            , secondary_y = True )          # on a secondary y axis
ax.set_xlabel( 'X axis' )                   # x-axis label
ax.set_ylabel( 'Main Axis' )                # Axis title for primary y-axis
ax2.set_ylabel( 'Secondary Axis' )          # Axis title for secondary y-axis
ax.set_title( 'Multiple Y Axes' )

# tick resolution adjustment suppression
with pd.plotting.plot_params.use( 'x_compat', True ):   # do not automatically adjust x-axis resolution
    ax = df.loc[:, list( set( df.columns ).difference( ['D'] ) ) ].plot() # plot all  columns except D
ax.set_xlabel( 'Day' )
ax.set_ylabel( 'Y value' )
ax.set_title( 'Suppress Automatic X-axis Resolution Adjustment' )

#*********************************************************************
#
# STATISTICAL PLOTS
#
#*********************************************************************

# load the iris dataset
iris = datasets.load_iris()
df = pd.DataFrame( iris.data, columns = iris.feature_names )

# box plot
ax = df.plot( kind = 'box'
            , subplots = True
            , layout = (2,2)
            , sharex = False
            , sharey = False )
fig = ax[0].get_figure()
fig.suptitle( 'Boxplot of Features of Iris Dataset' )   # overall title

# histogram
ax = np.squeeze( df.hist() )
fig = ax[0][0].get_figure()
fig.suptitle( 'Histogram of Features of Iris Dataset' )

# scatter_matrix
ax = pd.plotting.scatter_matrix( df, alpha = 1 )
fig = ax[0][0].get_figure()
fig.suptitle( 'Scatter Matrix of Features of Iris Dataset' )

# TODO: explore subplots

# show all plots
plt.show()
