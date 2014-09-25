import os,sys
import numpy
from matplotlib import pyplot as plt

from clawpack.geoclaw import dtopotools

usgs_subfault = dtopotools.SubFault()
usgs_subfault.strike = 16.
usgs_subfault.length = 450.e3
usgs_subfault.width = 100.e3
usgs_subfault.depth = 35.e3
usgs_subfault.slip = 15.
usgs_subfault.rake = 104.
usgs_subfault.dip = 14.
usgs_subfault.longitude = -72.668
usgs_subfault.latitude = -35.826
usgs_subfault.coordinate_specification = "top center"

x = numpy.linspace(-77, -67, 100)
y = numpy.linspace(-40, -30, 100)
times = [0., 1.]

fault = dtopotools.Fault()
fault.subfaults = [usgs_subfault]
fault.create_dtopography(x,y,times)
dtopo = fault.dtopo
dtopo.write('usgs100227_new.tt3', 3)
print "Mw = ",fault.Mw()
plt.figure()
dtopo.plot_dz_colors(1.)
dz = dtopo.dz_list[1]

if 1:
    plt.figure(figsize=(12,7))
    ax1 = plt.subplot(121)
    ax2 = plt.subplot(122)
    fault.plot_subfaults(axes=ax1,slip_color=True)
    ax1.set_xlim(x.min(),x.max())
    ax1.set_ylim(y.min(),y.max())
    dtopo.plot_dz_colors(1.,axes=ax2)
    plt.savefig('dtopo.png')


# compare to old:
CLAW = os.environ['CLAW']
exdir = os.path.join(CLAW,'examples/tsunami/chile2010')
dtopo1 = dtopotools.DTopography('usgs100227.tt1',dtopo_type=1)
plt.figure()
dtopo1.plot_dz_colors(1.)
dz1 = dtopo1.dz_list[1]

ddz = dz - dz1
print "max change in dz is ",abs(ddz).max()
plt.figure()
plt.pcolor(dtopo.X,dtopo.Y,dz-dz1)
plt.colorbar()
