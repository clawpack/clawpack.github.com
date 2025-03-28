
""" 
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.
    
""" 

from __future__ import absolute_import
from __future__ import print_function
from clawpack.clawutil.data import ClawData

probdata = ClawData()
probdata.read('setprob.data', force=True)
print("Parameters: u = %g, beta = %g" % (probdata.u, probdata.beta))

def qtrue(x,t):
    """
    The true solution, for comparison.  
    Should be consistent with the initial data specified in qinit.f90.
    """
    from numpy import mod, exp, where, logical_and
    x0 = x - probdata.u*t
    x0 = mod(x0, 1.)   # because of periodic boundary conditions
    q = exp(-probdata.beta * (x0-0.75)**2)
    q = where(logical_and(x0 > 0.1, x0 < 0.4), q+1, q)
    return q
    

#--------------------------
def setplot(plotdata=None):
#--------------------------
    
    """ 
    Specify what is to be plotted at each frame.
    Input:  plotdata, an instance of clawpack.visclaw.data.ClawPlotData.
    Output: a modified version of plotdata.
    
    """ 

    if plotdata is None:
        from clawpack.visclaw.data import ClawPlotData
        plotdata = ClawPlotData()

    plotdata.clearfigures()  # clear any old figures,axes,items data

    # Figure for q[0]
    plotfigure = plotdata.new_plotfigure(name='Pressure and Velocity', figno=1)

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.xlimits = 'auto'
    plotaxes.ylimits = [-.5,1.3]
    plotaxes.title = 'q'

    # Set up for item on these axes:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.plot_var = 0
    plotitem.plotstyle = '-o'
    plotitem.color = 'b'

    # Set up for second item from different output directory:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.outdir = '_output2'
    plotitem.plot_var = 0
    plotitem.plotstyle = '-o'
    plotitem.color = 'g'

    # Plot true solution for comparison:
    def plot_qtrue(current_data):
        from pylab import plot, legend
        x = current_data.x
        t = current_data.t
        q = qtrue(x,t)
        plot(x,q,'r',label='true solution')
        legend()

    plotaxes.afteraxes = plot_qtrue



    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via clawpack.visclaw.frametools.printframes:

    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    plotdata.print_framenos = 'all'          # list of frames to print
    plotdata.print_fignos = 'all'            # list of figures to print
    plotdata.html = True                     # create html files of plots?
    plotdata.html_homelink = '../README.html'
    plotdata.latex = True                    # create latex file of plots?
    plotdata.latex_figsperline = 2           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False           # also run pdflatex?

    return plotdata

    
