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

# Set the annotation attributes
annot = AnnotationAttributes()
#SetAnnotationAttributes(annot)

# Set annotation object properties
win0_legend000 = GetAnnotationObject(GetPlotList().GetPlots(0).plotName)
win0_legend000.active = 0
win0_legend000.managePosition = 1
win0_legend000.position = (0.05, 0.9)
win0_legend000.xScale = 1
win0_legend000.yScale = 1
win0_legend000.textColor = (0, 0, 0, 255)
win0_legend000.useForegroundForTextColor = 1
win0_legend000.drawBoundingBox = 0
win0_legend000.boundingBoxColor = (0, 0, 0, 50)
win0_legend000.numberFormat = "%# -9.4g"
win0_legend000.fontFamily = win0_legend000.Arial  # Arial, Courier, Times
win0_legend000.fontBold = 0
win0_legend000.fontItalic = 0
win0_legend000.fontShadow = 0
win0_legend000.fontHeight = 0.015
win0_legend000.drawLabels = win0_legend000.Values # None, Values, Labels, Both
win0_legend000.drawTitle = 1
win0_legend000.drawMinMax = 1
win0_legend000.orientation = win0_legend000.VerticalRight  # VerticalRight, VerticalLeft, HorizontalTop, HorizontalBottom
win0_legend000.controlTicks = 1
win0_legend000.numTicks = 5
win0_legend000.minMaxInclusive = 1
win0_legend000.suppliedValues = ("0", "1", "2")
win0_legend000.suppliedLabels = ()
win0_legend001 = GetAnnotationObject(GetPlotList().GetPlots(1).plotName)
win0_legend001.active = 1
win0_legend001.managePosition = 1
win0_legend001.position = (0.05, 0.9)
win0_legend001.xScale = 1
win0_legend001.yScale = 1
win0_legend001.textColor = (0, 0, 0, 255)
win0_legend001.useForegroundForTextColor = 1
win0_legend001.drawBoundingBox = 0
win0_legend001.boundingBoxColor = (0, 0, 0, 50)
win0_legend001.numberFormat = "%# -9.4g"
win0_legend001.fontFamily = win0_legend001.Arial  # Arial, Courier, Times
win0_legend001.fontBold = 0
win0_legend001.fontItalic = 0
win0_legend001.fontShadow = 0
win0_legend001.fontHeight = 0.015
win0_legend001.drawLabels = win0_legend001.Values # None, Values, Labels, Both
win0_legend001.drawTitle = 1
win0_legend001.drawMinMax = 1
win0_legend001.orientation = win0_legend001.VerticalRight  # VerticalRight, VerticalLeft, HorizontalTop, HorizontalBottom
win0_legend001.controlTicks = 1
win0_legend001.numTicks = 5
win0_legend001.minMaxInclusive = 1
win0_legend001.suppliedValues = (0, 0.25, 0.5, 0.75, 1)
win0_legend001.suppliedLabels = ()

SetActiveWindow(GetGlobalAttributes().windows[0])
