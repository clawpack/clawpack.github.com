
""" 
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.
    
""" 

from __future__ import absolute_import
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

from clawpack.geoclaw import topotools
from six.moves import range

try:
    TG32412 = np.loadtxt('32412_notide.txt')
except:
    print("*** Could not load DART data file")

def timeformat(t):
    from numpy import mod
    hours = int(t/3600.)
    tmin = mod(t,3600.)
    min = int(tmin/60.)
    sec = int(mod(tmin,60.))
    timestr = '%s:%s:%s' % (hours,str(min).zfill(2),str(sec).zfill(2))
    return timestr

def title_hours(current_data):
    from pylab import title
    t = current_data.t
    timestr = timeformat(t)
    title('%s after earthquake' % timestr)

#--------------------------
def setplot(plotdata=None):
#--------------------------
    
    """ 
    Specify what is to be plotted at each frame.
    Input:  plotdata, an instance of pyclaw.plotters.data.ClawPlotData.
    Output: a modified version of plotdata.
    
    """ 


    from clawpack.visclaw import colormaps, geoplot
    from numpy import linspace

    if plotdata is None:
        from clawpack.visclaw.data import ClawPlotData
        plotdata = ClawPlotData()


    plotdata.clearfigures()  # clear any old figures,axes,items data


    # To plot gauge locations on pcolor or contour plot, use this as
    # an afteraxis function:

    def addgauges(current_data):
        from clawpack.visclaw import gaugetools
        gaugetools.plot_gauge_locations(current_data.plotdata, \
             gaugenos='all', format_string='ko', add_labels=True)
    

    #-----------------------------------------
    # Figure for surface
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Surface', figno=0)

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('pcolor')
    plotaxes.title = 'Surface'
    plotaxes.scaled = True

    def fixup(current_data):
        from numpy import cos, pi
        from matplotlib.pyplot import ticklabel_format, xticks, gca
        addgauges(current_data)
        title_hours(current_data)
        ticklabel_format(format='plain',useOffset=False)
        xticks(rotation=20)
        gca().set_aspect(1./cos(46.86*pi/180.))

    plotaxes.afteraxes = fixup

    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    #plotitem.plot_var = geoplot.surface
    plotitem.plot_var = geoplot.surface_or_depth
    plotitem.pcolor_cmap = geoplot.tsunami_colormap
    plotitem.pcolor_cmin = -0.2
    plotitem.pcolor_cmax = 0.2
    plotitem.add_colorbar = True
    plotitem.amr_celledges_show = [0,0,0]
    plotitem.patchedges_show = 1

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.plot_var = geoplot.land
    plotitem.pcolor_cmap = geoplot.land_colors
    plotitem.pcolor_cmin = 0.0
    plotitem.pcolor_cmax = 100.0
    plotitem.add_colorbar = False
    plotitem.amr_celledges_show = [1,1,0]
    plotitem.patchedges_show = 1
    plotaxes.xlimits = [-120,-60]
    plotaxes.ylimits = [-60,0]

    # add contour lines of bathy if desired:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.show = False
    plotitem.plot_var = geoplot.topo
    plotitem.contour_levels = linspace(-3000,-3000,1)
    plotitem.amr_contour_colors = ['y']  # color on each level
    plotitem.kwargs = {'linestyles':'solid','linewidths':2}
    plotitem.amr_contour_show = [1,0,0]  
    plotitem.celledges_show = 0
    plotitem.patchedges_show = 0



    #-----------------------------------------
    # Plot along transect:
    #-----------------------------------------

    def eta(q):
        eta = where(q[0,:,:]>0, q[3,:,:], nan)
        return eta

    def B(q):
        return q[3,:,:]-q[0,:,:]


    def plot_xsec(current_data):
        import matplotlib.pyplot as plt
        import numpy
        from clawpack.visclaw import gridtools
        from clawpack.pyclaw import Solution

        framesoln = current_data.framesoln

        ylat = -35.
        xout = numpy.linspace(-110, -70, 201)
        yout = ylat*numpy.ones(xout.shape)
        eta = gridtools.grid_output_2d(framesoln, 3, xout, yout)
        topo = gridtools.grid_output_2d(framesoln, B, xout, yout)
        xlimits = [-110, -70]
        topo_color = [.8,1,.8]
        water_color = [.5,.5,1]

        plt.figure(15,figsize=(8,6))
        plt.clf()
        plt.subplot(211)
        plt.fill_between(xout, eta, topo, color=water_color)
        plt.fill_between(xout, topo, -10000, color=topo_color)
        plt.plot(xout, eta, 'b')
        plt.plot(xout, topo, 'g')
        plt.xlim(xlimits)
        plt.ylim(-2,2)
        plt.ylabel('meters')
        timestr = timeformat(framesoln.t)
        plt.title('Transect along latitude %6.3f at time %s' % (ylat,timestr))
        plt.annotate('Surface zoom',xy=(.05,.85),xycoords='axes fraction')

        plt.subplot(212)
        plt.fill_between(xout, eta, topo, color=water_color)
        plt.fill_between(xout, topo, -10000, color=topo_color)
        plt.plot(xout, eta, 'b')
        plt.plot(xout, topo, 'g')
        plt.xlim(xlimits)
        plt.xlabel('longitude')
        plt.ylim(-6000,4000)
        plt.annotate('Ocean scale',xy=(.05,.85),xycoords='axes fraction')
        plt.draw()


    plotdata.afterframe = plot_xsec
 

    #-----------------------------------------
    # Figures for gauges
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Surface at gauges', figno=300, \
                    type='each_gauge')
    plotfigure.clf_each_gauge = True

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.xlimits = 'auto'
    plotaxes.ylimits = 'auto'
    plotaxes.title = 'Surface'

    # Plot surface as blue curve:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.plot_var = 3
    plotitem.plotstyle = 'b-'

    # Plot topo as green curve:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.show = False

    def gaugetopo(current_data):
        q = current_data.q
        h = q[0,:]
        eta = q[3,:]
        topo = eta - h
        return topo
        
    plotitem.plot_var = gaugetopo
    plotitem.plotstyle = 'g-'

    def add_zeroline(current_data):
        from pylab import plot, legend, xticks, floor, axis, xlabel
        t = current_data.t 
        gaugeno = current_data.gaugeno

        if gaugeno == 32412:
            try:
                plot(TG32412[:,0], TG32412[:,1], 'r')
                legend(['GeoClaw','Obs'],loc='lower right')
            except: pass
            axis((0,t.max(),-0.3,0.3))

        plot(t, 0*t, 'k')
        n = int(floor(t.max()/3600.) + 2)
        xticks([3600*i for i in range(n)], ['%i' % i for i in range(n)])
        xlabel('time (hours)')

    plotaxes.afteraxes = add_zeroline



    #-----------------------------------------
    
    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via pyclaw.plotters.frametools.printframes:

    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    plotdata.print_framenos = 'all'          # list of frames to print
    plotdata.print_gaugenos = 'all'          # list of gauges to print
    plotdata.print_fignos = 'all'            # list of figures to print
    plotdata.html = True                     # create html files of plots?
    plotdata.html_homelink = '../README.html'   # pointer for top of index
    plotdata.latex = True                    # create latex file of plots?
    plotdata.latex_figsperline = 2           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False           # also run pdflatex?
    plotdata.parallel = True                 # make multiple frame png's at once

    return plotdata

