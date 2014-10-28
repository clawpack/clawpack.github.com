"""
Create fgmax_grid.txt and fgmax_transect input files 
"""


from clawpack.geoclaw import fgmax_tools


def make_fgmax_grid():
    fg = fgmax_tools.FGmaxGrid()
    fg.point_style = 2       # will specify a 2d grid of points
    fg.x1 = -120.
    fg.x2 = -60.
    fg.y1 = -60.
    fg.y2 = 0.
    fg.dx = 0.2 
    fg.tstart_max =  10.     # when to start monitoring max values
    fg.tend_max = 1.e10       # when to stop monitoring max values
    fg.dt_check = 60.         # target time (sec) increment between updating 
                               # max values
    fg.min_level_check = 3    # which levels to monitor max on
    fg.arrival_tol = 1.e-2    # tolerance for flagging arrival

    fg.input_file_name = 'fgmax_grid.txt'
    fg.write_input_data()


if __name__ == "__main__":
    make_fgmax_grid()


