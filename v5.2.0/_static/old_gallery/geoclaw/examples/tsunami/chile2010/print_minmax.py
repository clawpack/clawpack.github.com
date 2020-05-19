
from pylab import *

from clawpack.visclaw.Iplotclaw import Iplotclaw
from clawpack.visclaw.frametools import var_minmax

import setplot
plotdata = setplot.setplot()
plotdata.outdir = '_output'

# Define the variable to check:
eta = lambda q,x,y,t: where(q[0,:]>0, q[3,:], 0.)
vars = [eta]

# Which frames to check:
framenos = range(6)

minmax = var_minmax(plotdata,framenos,vars)
eta_min = minmax[0][eta]
eta_max = minmax[1][eta]

print "\nOver all frames checked: minimum = %g,  maximum = %g" \
        % (eta_min['all'], eta_max['all'])


for k in framenos:
    print "Frame %2i:  min eta = %g, max eta = %g" \
            % (k,eta_min[k],eta_max[k])
