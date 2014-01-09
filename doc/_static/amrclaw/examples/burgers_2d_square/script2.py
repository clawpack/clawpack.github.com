# Define expressions
# Write color tables
SetCloneWindowOnFirstRef(0)
###############################################################################
width, height = 854, 788
win = GetGlobalAttributes().windows[GetGlobalAttributes().activeWindow]
ResizeWindow(win, width, height)
SetActiveWindow(win) # Synchronize
size = GetWindowInformation().windowSize
if width < size[0] or height < size[1]:
    ResizeWindow(win, width + (size[0] - width), height + (size[1] - height))
DeleteAllPlots()
for name in GetAnnotationObjectNames():
    DeleteAnnotationObject(name)

# Create plots
# Create plot 1
OpenDatabase("localhost:/Users/rjl/git/clawpack/amrclaw/examples/burgers_2d_square/_output/plot.claw")
AddPlot("Subset", "levels", 0, 0)
atts = SubsetAttributes()
#SetPlotOptions(atts)
silr = SILRestriction()
silr.TurnOnAll()
SetPlotSILRestriction(silr, 0)

# Create plot 2
OpenDatabase("localhost:/Users/rjl/git/clawpack/amrclaw/examples/burgers_2d_square/_output/plot.claw")
AddPlot("Pseudocolor", "col_00", 0, 0)
atts = PseudocolorAttributes()
atts.minFlag = 1
atts.maxFlag = 1
SetPlotOptions(atts)
silr = SILRestriction()
silr.TurnOnAll()
SetPlotSILRestriction(silr, 0)

SetActivePlots(1)

DrawPlots()

# Set the view
view = View2DAttributes()
view.windowCoords = (0, 1, 0, 1)
view.viewportCoords = (0.2, 0.95, 0.15, 0.95)
view.fullFrameActivationMode = view.Auto  # On, Off, Auto
view.fullFrameAutoThreshold = 100
view.xScale = view.LINEAR  # LINEAR, LOG
view.yScale = view.LINEAR  # LINEAR, LOG
view.windowValid = 1
SetView2D(view)
