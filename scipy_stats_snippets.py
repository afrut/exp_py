import subprocess as sp
import scipy.stats as stats
import numpy as np

sp.call( 'cls', shell = True )

# print the number of distributions for continuous and discrete variables
# available for use
dist_continu = [ d for d in dir(stats) if
                 isinstance(getattr(stats, d), stats.rv_continuous)]
dist_discrete = [ d for d in dir(stats) if
                  isinstance(getattr(stats, d), stats.rv_discrete)]
print( 'number of continuous distributions: %d' % len(dist_continu))
print( 'number of discrete distributions:   %d' % len(dist_discrete))
print( '' )

# given a normal distribution
print( 'Cumulative distribution function for normal distributions:' )
print( 'P( x <= 0 ) = ' + str( round( stats.norm.cdf(0), 4 ) ) )
print( 'P( x <= 0.1 ) = ' + str( round( stats.norm.cdf(0.1), 4 ) ) )
print( 'P( x <= [0.8, 1.6] ) = ' + str( np.round( stats.norm.cdf([0.8, 1.6]), 4 ) ) )
print( 'P( x <= [-0.5, 0, 0.5] ) = ' + str( np.round( stats.norm.cdf( np.array([-0.5, 0, 0.5]) ), 4 ) ) )
print( '' )

# TODO: continue adding commands here
