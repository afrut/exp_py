import subprocess as sp
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

# clear screen
sp.call( 'cls', shell = True )

# create list of figures
lsFig = list()

# create list of axes
lsAx = list()

# specify the number of points
cntPt = 200

#***********************************************************************
#
# PANDAS TIME-SERIES PLOTS
#
#***********************************************************************
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
ax2 = df.plot( x = 'D', y = ['B','C']       # plot column B and C against column D
            , ax = ax                       # on the same figure
            , mark_right = False            # don't mark (right) in legend for columns in secondary axis
            , secondary_y = True )          # on a secondary y axis
ax.set_ylabel( 'Main Axis' )
ax2.set_ylabel( 'Secondary Axis' )

# show all plots
plt.show()
