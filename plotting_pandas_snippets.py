import subprocess as sp
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

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
mpl.style.use( 'seaborn' )

# plot cumulative sum of a time series in a Series type
ts = pd.Series( np.random.randn( cntPt )    # create a time series
              , index = pd.date_range( '1/1/2000', periods = cntPt ) );
ts = ts.cumsum()                            # calculate cumulative sum
ax = ts.plot()                              # plot on the figure
lsAx.append( ax )                           # store axis handle
lsFig.append( ax.get_figure() )             # store figure handle

# plot cumulative sum of multiple time series in a DataFrame type
df = pd.DataFrame( np.random.randn( cntPt, 3 )
                 , index = ts.index
                 , columns = list('ABC') ); # create a DataFrame with 3 columns
df = df.cumsum()                            # calculate cumulative sums per column
ax = df.plot()                              # plot cumulative sums
lsAx.append( ax )                           # store axis handle
lsFig.append( ax.get_figure() )             # store figure handle

# plot x and y specifying columns of a DataFrame type
df['D'] = pd.Series( list( range( len( df ) ) )
                   , index = df.index )     # add a column D as a count of the index
ax = df.plot( x = 'D', y = 'A' )            # plot A against D
lsAx.append( ax )                           # store axis handle
lsFig.append( ax.get_figure() )             # store figure handle

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
ax.set_ylabel( 'Main Axis' )                # Axis title for primary y-axis
ax2.set_ylabel( 'Secondary Axis' )          # Axis title for secondary y-axis

# tick resolution adjustment suppression
with pd.plotting.plot_params.use( 'x_compat', True ):   # do not automatically adjust x-axis resolution
    ax = df.loc[:, list( set( df.columns ).difference( ['D'] ) ) ].plot() # plot all  columns except D

# TODO: explore subplots

# show all plots
plt.show()

# TODO: box plot
# TODO: histogram
# TODO: scatter_matrix
