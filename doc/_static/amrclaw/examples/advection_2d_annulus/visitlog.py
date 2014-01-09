# Visit 2.7.0 log file
ScriptVersion = "2.7.0"
if ScriptVersion != Version():
    print "This script is for VisIt %s. It may not work with version %s" % (ScriptVersion, Version())
ShowAllWindows()
DeleteActivePlots()
AddPlot("Pseudocolor", "col0", 1, 1)
AddPlot("Pseudocolor", "col_00", 1, 1)
DrawPlots()
# Begin spontaneous state
View2DAtts = View2DAttributes()
View2DAtts.windowCoords = (0, 1, 0, 1)
View2DAtts.viewportCoords = (0.2, 0.95, 0.15, 0.95)
View2DAtts.fullFrameActivationMode = View2DAtts.Auto  # On, Off, Auto
View2DAtts.fullFrameAutoThreshold = 100
View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.windowValid = 1
SetView2D(View2DAtts)
# End spontaneous state

PseudocolorAtts = PseudocolorAttributes()
PseudocolorAtts.scaling = PseudocolorAtts.Linear  # Linear, Log, Skew
PseudocolorAtts.skewFactor = 1
PseudocolorAtts.limitsMode = PseudocolorAtts.OriginalData  # OriginalData, CurrentPlot
PseudocolorAtts.minFlag = 1
PseudocolorAtts.min = 3.5
PseudocolorAtts.maxFlag = 1
PseudocolorAtts.max = 7.5
PseudocolorAtts.centering = PseudocolorAtts.Natural  # Natural, Nodal, Zonal
PseudocolorAtts.colorTableName = "hot"
PseudocolorAtts.invertColorTable = 0
PseudocolorAtts.opacityType = PseudocolorAtts.FullyOpaque  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
PseudocolorAtts.opacityVariable = ""
PseudocolorAtts.opacity = 1
PseudocolorAtts.opacityVarMin = 0
PseudocolorAtts.opacityVarMax = 1
PseudocolorAtts.opacityVarMinFlag = 0
PseudocolorAtts.opacityVarMaxFlag = 0
PseudocolorAtts.pointSize = 0.05
PseudocolorAtts.pointType = PseudocolorAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
PseudocolorAtts.pointSizeVarEnabled = 0
PseudocolorAtts.pointSizeVar = "default"
PseudocolorAtts.pointSizePixels = 2
PseudocolorAtts.lineType = PseudocolorAtts.Line  # Line, Tube, Ribbon
PseudocolorAtts.lineStyle = PseudocolorAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
PseudocolorAtts.lineWidth = 0
PseudocolorAtts.tubeDisplayDensity = 10
PseudocolorAtts.tubeRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
PseudocolorAtts.tubeRadiusAbsolute = 0.125
PseudocolorAtts.tubeRadiusBBox = 0.005
PseudocolorAtts.varyTubeRadius = 0
PseudocolorAtts.varyTubeRadiusVariable = ""
PseudocolorAtts.varyTubeRadiusFactor = 10
PseudocolorAtts.endPointType = PseudocolorAtts.None  # None, Tails, Heads, Both
PseudocolorAtts.endPointStyle = PseudocolorAtts.Spheres  # Spheres, Cones
PseudocolorAtts.endPointRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
PseudocolorAtts.endPointRadiusAbsolute = 1
PseudocolorAtts.endPointRadiusBBox = 0.005
PseudocolorAtts.endPointRatio = 2
PseudocolorAtts.renderSurfaces = 1
PseudocolorAtts.renderWireframe = 0
PseudocolorAtts.renderPoints = 0
PseudocolorAtts.smoothingLevel = 0
PseudocolorAtts.legendFlag = 1
PseudocolorAtts.lightingFlag = 1
SetPlotOptions(PseudocolorAtts)
PseudocolorAtts = PseudocolorAttributes()
PseudocolorAtts.scaling = PseudocolorAtts.Linear  # Linear, Log, Skew
PseudocolorAtts.skewFactor = 1
PseudocolorAtts.limitsMode = PseudocolorAtts.OriginalData  # OriginalData, CurrentPlot
PseudocolorAtts.minFlag = 1
PseudocolorAtts.min = 0
PseudocolorAtts.maxFlag = 1
PseudocolorAtts.max = 1
PseudocolorAtts.centering = PseudocolorAtts.Natural  # Natural, Nodal, Zonal
PseudocolorAtts.colorTableName = "hot"
PseudocolorAtts.invertColorTable = 0
PseudocolorAtts.opacityType = PseudocolorAtts.FullyOpaque  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
PseudocolorAtts.opacityVariable = ""
PseudocolorAtts.opacity = 1
PseudocolorAtts.opacityVarMin = 0
PseudocolorAtts.opacityVarMax = 1
PseudocolorAtts.opacityVarMinFlag = 0
PseudocolorAtts.opacityVarMaxFlag = 0
PseudocolorAtts.pointSize = 0.05
PseudocolorAtts.pointType = PseudocolorAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
PseudocolorAtts.pointSizeVarEnabled = 0
PseudocolorAtts.pointSizeVar = "default"
PseudocolorAtts.pointSizePixels = 2
PseudocolorAtts.lineType = PseudocolorAtts.Line  # Line, Tube, Ribbon
PseudocolorAtts.lineStyle = PseudocolorAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
PseudocolorAtts.lineWidth = 0
PseudocolorAtts.tubeDisplayDensity = 10
PseudocolorAtts.tubeRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
PseudocolorAtts.tubeRadiusAbsolute = 0.125
PseudocolorAtts.tubeRadiusBBox = 0.005
PseudocolorAtts.varyTubeRadius = 0
PseudocolorAtts.varyTubeRadiusVariable = ""
PseudocolorAtts.varyTubeRadiusFactor = 10
PseudocolorAtts.endPointType = PseudocolorAtts.None  # None, Tails, Heads, Both
PseudocolorAtts.endPointStyle = PseudocolorAtts.Spheres  # Spheres, Cones
PseudocolorAtts.endPointRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
PseudocolorAtts.endPointRadiusAbsolute = 1
PseudocolorAtts.endPointRadiusBBox = 0.005
PseudocolorAtts.endPointRatio = 2
PseudocolorAtts.renderSurfaces = 1
PseudocolorAtts.renderWireframe = 0
PseudocolorAtts.renderPoints = 0
PseudocolorAtts.smoothingLevel = 0
PseudocolorAtts.legendFlag = 1
PseudocolorAtts.lightingFlag = 1
SetPlotOptions(PseudocolorAtts)
# Begin spontaneous state
View2DAtts = View2DAttributes()
View2DAtts.windowCoords = (0, 1, 0, 1)
View2DAtts.viewportCoords = (0.2, 0.95, 0.15, 0.95)
View2DAtts.fullFrameActivationMode = View2DAtts.Auto  # On, Off, Auto
View2DAtts.fullFrameAutoThreshold = 100
View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.windowValid = 1
SetView2D(View2DAtts)
# End spontaneous state

# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/rjl/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/rjl/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# Begin spontaneous state
View2DAtts = View2DAttributes()
View2DAtts.windowCoords = (0, 1, 0, 1)
View2DAtts.viewportCoords = (0.2, 0.95, 0.15, 0.95)
View2DAtts.fullFrameActivationMode = View2DAtts.Auto  # On, Off, Auto
View2DAtts.fullFrameAutoThreshold = 100
View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.windowValid = 1
SetView2D(View2DAtts)
# End spontaneous state

# The AnimationPlay RPC is not supported in the VisIt module so it will not be logged.
# The AnimationStop RPC is not supported in the VisIt module so it will not be logged.
TimeSliderNextState()
TimeSliderNextState()
TimeSliderNextState()
TimeSliderNextState()
TimeSliderNextState()
TimeSliderNextState()
TimeSliderNextState()
TimeSliderPreviousState()
TimeSliderNextState()
TimeSliderNextState()
TimeSliderPreviousState()
TimeSliderPreviousState()
TimeSliderPreviousState()
TimeSliderPreviousState()
TimeSliderNextState()
TimeSliderNextState()
TimeSliderNextState()
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/rjl/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
TimeSliderNextState()
TimeSliderPreviousState()
TimeSliderPreviousState()
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/rjl/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SetActiveWindow(1)
SetActivePlots(0)
SetActivePlots(1)
SetActivePlots(1)
SetActiveWindow(1)
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/rjl/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/rjl/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/Users/rjl/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# Begin spontaneous state
View2DAtts = View2DAttributes()
View2DAtts.windowCoords = (0, 1, 0, 1)
View2DAtts.viewportCoords = (0.2, 0.95, 0.15, 0.95)
View2DAtts.fullFrameActivationMode = View2DAtts.Auto  # On, Off, Auto
View2DAtts.fullFrameAutoThreshold = 100
View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.windowValid = 1
SetView2D(View2DAtts)
# End spontaneous state

