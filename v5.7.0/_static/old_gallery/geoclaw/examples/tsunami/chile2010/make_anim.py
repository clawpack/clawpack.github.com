
import matplotlib
matplotlib.use('Agg')

from clawpack.visclaw import animation_tools

animation_tools.make_anim_from_plotdir(plotdir='_plots', fignos=[0],
        outputs=['html','rst','mp4'], file_name_prefix='chile2010_',
        figsize=(5,4), dpi=None, fps=5)
