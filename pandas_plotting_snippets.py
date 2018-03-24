import subprocess as sp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# clear screen
sp.call( 'cls', shell=True )

#***********************************************************************
#
# Series creation
#
#***********************************************************************
ls = [ 1, 3, 5, np.nan, 6, 8 ] # create a python list
s = pd.Series( ls ) # create a series

#***********************************************************************
#
# DataFrame creation
#
#***********************************************************************
dates = pd.date_range( '20130101', periods=6 ) # create a datetime index
mat = np.random.randn(6,4)                     # create a numpy matrix
cols = list( 'ABCD' )                          # create a list of columns

# create a DataFrame by specifying index and columns
df = pd.DataFrame( mat, index = dates, columns = cols )

# create a dictionary of different types of objects
dct = { 'A' : 1.,
        'B' : pd.Timestamp('20130102'),
        'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
        'D' : np.array([3] * 4,dtype='int32'),
        'E' : pd.Categorical(["test","train","test","train"]),
        'F' : 'foo' }

# create another DataFrame by passing it a dictionary
df2 = pd.DataFrame( dct )

df.dtypes   # check the datatypes of each DataFrame
df2.dtypes

#***********************************************************************
#
# DataFrame inspection
#
#***********************************************************************
df.head()       # display first few rows of the DataFrame
df.tail(3)      # display last 3 rows of the DataFrame
df.index        # display indexes
df.columns      # display columns
df.values       # display values
df.describe()   # show quick statistics
df.T            # transpose
df.sort_index( axis=0, ascending=False ) # sort by index
df.sort_index( axis=1, ascending=False ) # sort by columns
df.sort_values( by='B') # sort according to values of column B

#***********************************************************************
#
# DataFrame selection
#
#***********************************************************************
# slicing
s = df['A']                     # select column A
s = df[0:3]                     # select first 3 rows
s = df['20130102':'20130104']   # select by range of index

# selecting by labels with slicing
s = df.loc[ '20130101' ]        # select the first row by label
s = df.loc[:,['A','B']]         # select all rows for columns A and B
s = df.loc['20130102':'20130104', ['A','B']] # select specific rows and columns
s = df.loc['20130101','A']      # get a single scalar value
s = df.at[dates[0],'A']         # same as above

# selecting by position
s = df.iloc[3]                  # select the 4th element
s = df.iloc[3:5,0:2]            # select row 4-5, columns 1-2
s = df.iloc[[1,2,4],[0,2]]      # select specific rows and columns
s = df.iloc[1:3,:]              # slicing rows by position
s = df.iloc[:,1:3]              # slicing columns by position
s = df.iloc[1,1]                # get a single scalar value
s = df.iat[1,1]                 # same as above

# boolean indexing
df[df.A > 0]        # select all rows for which values in column A > 0
df[df > 0]          # select all values > 0
df2 = df.copy()     # create a copy of the DataFrame
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three'] # add a column
df2[ df2['E'].isin(['two','four']) ] # select all rows for values of column E

#***********************************************************************
#
# DataFrame modification
#
#***********************************************************************
# create a series with a different index
s = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
df['F'] = s                             # add a new column
df.at[dates[0],'A'] = 0                 # set value by label
df.iat[0,1] = 0                         # set value by position
df.loc[:,'D'] = np.array([5] * len(df)) # set value by numpy.array
df2 = df.copy()                         # create a copy
df2[ df2 > 0 ] = -df2                   # negate all positive values
df['G'] = s
df.drop( 'G', axis = 1 )                # drop a column

# reindex the DataFrame
df1 = df.reindex( index=dates[0:4], columns=list(df.columns) + ['E'] )
df1.loc[dates[0]:dates[1],'E'] = 1      # assign a value to first two rows
                                        # of column E
df1.dropna( how='any' )                 # drop any rows that have missing data
df1.fillna( value=5 )                   # fill all nan values with 5
pd.isna( df1 )                          # get boolean mask for data frame

# splitting and concatenating a DataFrame by row
pieces = [df[:2], df[2:5], df[5:]]
pd.concat( pieces )

# database style joining
left = pd.DataFrame( {'key': ['foo','foo'], 'lval': [1,2]} )
right = pd.DataFrame( {'key': ['foo','foo'], 'rval': [4,5]} )
pd.merge( left, right, on='key' )
left = pd.DataFrame( {'key': ['foo','bar'], 'lval': [1,2]} )
right = pd.DataFrame( {'key': ['foo','bar'], 'rval': [4,5]} )
pd.merge( left, right, on='key' )

# appending rows to a DataFrame
s = df.iloc[3]                          # get the 4th row
df.append( s, ignore_index=True )

# applying an operation to every column and grouping by
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})
df.groupby(['A']).sum()
df.groupby(['A','B']).sum()

# stacking a DataFrame
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']]))
index = pd.MultiIndex.from_tuples( tuples, names=['first', 'second'] )
df = pd.DataFrame( np.random.randn(8,2), index=index, columns=['A','B'] )
df2 = df[:4]
df2.stack()

# creating a pivot table from a DataFrame
df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
                   'B' : ['A', 'B', 'C'] * 4,
                   'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D' : np.random.randn(12),
                   'E' : np.random.randn(12)})
pd.pivot_table( df, values='D', index=['A','B'], columns=['C'] )

#***********************************************************************
#
# DataFrame operations
#
#***********************************************************************
df = pd.DataFrame( np.random.randn(6,4), index=dates, columns=cols )
df.mean()       # calculates the mean by column
df.mean( 1 )    # calculates the mean by row

# subtract a series from every column of the DataFrame
# subtraction with a nan results in nan
s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)
df.sub( s, axis='index' );

# apply different functions to a DataFrame
df.apply( np.cumsum )       # calculate cumulative sum for each column
df.apply( lambda x: x.max() - x.min() )     # get range of each column

# find the count of a series
s = pd.Series( np.random.randint( 0, 7, size=10 ) )
s.value_counts()

# string operations for a series
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
s.str.lower()

#***********************************************************************
#
# Time Series
#
#***********************************************************************
# create a time series by using a datetime as an index
rng = pd.date_range( '1/1/2012', periods=100, freq='S' )
ts = pd.Series( np.random.randint( 0, 500, len(rng)), index=rng )
ts.resample( '5s' ).sum()   # calculate the sum every 5 seconds
ts.resample( '20s' ).sum()  # calculate the sum every 20 seconds

# time zone representation
rng = pd.date_range( '3/6/2012 00:00', periods=5, freq='D' )
ts = pd.Series( np.random.randn( len(rng) ), rng )
ts_utc = ts.tz_localize('UTC')      # define current time zone as UTC

# converting to another time zone
ts_utc.tz_convert( 'US/Eastern' )

# converting between points in time to time span representations
rng = pd.date_range( '1/1/2012', periods=5, freq='M' )
ts = pd.Series( np.random.randn(len(rng)), index=rng )
ps = ts.to_period()     # converts to a monthly time span index
ps.to_timestamp()       # converts to a timestamp index

# create a quarterly index ending in november
prng = pd.period_range( '1990Q1', '2000Q4', freq='Q-NOV' )
ts = pd.Series( np.random.randn( len(prng)), index=prng )

# change the index to 9 am the following month
ts.index = (prng.asfreq('M','e') + 1).asfreq('H','s') + 9

#***********************************************************************
#
# Categoricals
#
#***********************************************************************
# create a column of category type and modify the categories
df = pd.DataFrame( { 'id': [1,2,3,4,5,6]
                   , 'raw_grade': ['a', 'b', 'b', 'a', 'a', 'e'] } )
df['grade'] = df['raw_grade'].astype('category')
df['grade'].cat.categories = ['very good', 'good', 'very bad' ]

# add more categories
df['grade'] = df['grade'].cat.set_categories(['very bad','bad','medium','good','very good'])
df.sort_values( by='grade' )    # sort by categories
df.groupby('grade').size()      # check the counts for each category

#***********************************************************************
#
# Plotting
#
#***********************************************************************
# plot a time series
ts = pd.Series( np.random.randn(1000)
               , index=pd.date_range( '1/1/2000', periods=1000 ) )
#ts.plot()

# plot all columns of a DataFrame
df = pd.DataFrame( np.random.randn( 1000, 4 )
                 , index = ts.index
                 , columns=['A','B','C','D'] )
df = df.cumsum()
df.plot()
plt.legend(loc='best')
plt.show()
