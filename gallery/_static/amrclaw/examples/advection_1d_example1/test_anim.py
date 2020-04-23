
import matplotlib
matplotlib.rcParams['backend'] = 'agg'
from pylab import *
from clawpack.visclaw import animation_tools

animation_tools.make_anim_outputs_from_plotdir(plotdir='_plots', fignos=[2],
                            outputs=['mp4','html'])

