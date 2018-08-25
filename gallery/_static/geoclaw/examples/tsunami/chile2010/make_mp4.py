
import matplotlib
matplotlib.use('Agg')

from clawpack.visclaw import animation_tools 

animation_tools.make_anim_from_plotdir(plotdir='_plots',fignos='all',
        outputs=['mp4'], file_name_prefix='tsunami_', figsize=(6,6))
