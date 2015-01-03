## Trailer drawn using Thing.py -- Thing.py is Architecture Framework.

from visual import *
from Thing import BoxThing
from Thing import PipeThing

# Set window attributes
scene.width=800
scene.height=800
scene.title="Travel Trailer Layout"
scene.background = ( 0.7, 0.7, 0.7 )

# Set camera/viewport attributes
scene.autoscale = True
scene.center = ( 4*12, 13*12, 4*12 )
scene.up = ( 0, 0, 1 )

# walls

deck = BoxThing( label = 'deck', length = 26*12, width = 8*12, height = 8, aColor = color.yellow )

wallThickness = 1

backWall = BoxThing( label = 'back wall', length = wallThickness, width = 8*12, height = 48, aColor = color.red )
backWall.placeSouthOf( deck, offset = 0 )

frontWall = BoxThing( label = 'front wall', length = wallThickness, width = 8*12, height = 48, aColor = color.white )
frontWall.placeNorthOf( deck, offset = 0 )

westWall = BoxThing ( label = 'west wall', length = deck.length, width = wallThickness, height = 4*12, aColor = color.red )
westWall.placeWestOf( deck )

eastWall = BoxThing ( label = 'east wall', length = deck.length, width = wallThickness, height = 4*12, aColor = color.red )
eastWall.placeEastOf( deck )

# Furniture

settee = BoxThing( label = 'settee', length = 92, width = 32, height = 16, aColor = color.blue )
settee.placeAbove( deck )
settee.placeNorthOf( backWall, offset = 1 )
settee.placeEastOf( westWall )

seat = BoxThing( label = 'seat', length = 32, width = 30, height = 16, aColor = color.blue )
seat.placeAbove( deck )
seat.placeNorthOf( backWall, offset = 1 )
seat.placeWestOf( eastWall )

table = BoxThing( label = 'table', length = seat.length, width = 30, height = 1, aColor = color.white )
table.placeAbove( deck, offset = 26 )
table.placeEastOf( settee, offset = 1 )

mattress = BoxThing( label = 'mattress', length = 75, width = 54, height = 10, aColor = color.blue )

bedPlatform = BoxThing( label = 'bed platform',
                        length = mattress.length - 2,
                        width = mattress.width - 4,
                        height = 16 - mattress.height,
                        aColor = color.white )
bedPlatform.placeAbove( deck )
bedPlatform.placeSouthOf( frontWall )
bedPlatform.placeEastOf( westWall, offset = (deck.width - bedPlatform.width) / 2 )

mattress.placeAbove( bedPlatform, offset = 0 )
mattress.placeSouthOf( frontWall )
mattress.placeEastOf( westWall, offset = ( deck.width - mattress.width ) / 2 )


# interior walls

panelThickness = 3
panelWidth = 32

aisle = BoxThing( label = 'aisle', length = deck.length, width = 32, height = 80, visible = False )
aisle.placeAbove( deck )
aisle.placeEastOf( settee )

panelA_west = BoxThing( label = 'panel A west', length = panelThickness, width = panelWidth, height = 80, aColor = color.white )
panelA_west.placeAbove( deck, offset = 0 )
panelA_west.placeNorthOf( settee, offset = 2 )
panelA_west.placeWestOf( aisle )

panelA_east = BoxThing( label = 'panel A east', length = panelThickness, width = panelWidth, height = 80, aColor = color.white )
panelA_east.placeAbove( deck, offset = 0 )
panelA_east.placeNorthOf( settee )
panelA_east.placeEastOf( aisle )

counter = BoxThing( label = 'counter', length = 93, width = 24, height = 40, aColor = color.white )
counter.placeAbove( deck )
counter.placeNorthOf( panelA_east )
counter.placeWestOf( eastWall )

panelB_west = BoxThing( label = 'panel B west', length = panelThickness, width = panelWidth, height = 80, aColor = color.white )
panelB_west.placeAbove( deck, offset = 0 )
panelB_west.placeNorthOf( counter )
panelB_west.placeWestOf( aisle )

panelB_east = BoxThing( label = 'panel B east', length = panelThickness, width = panelWidth, height = 80, aColor = color.white )
panelB_east.placeAbove( deck, offset = 0 )
panelB_east.placeNorthOf( counter )
panelB_east.placeEastOf( aisle )

eastWardrobe = BoxThing( label = 'east wardrobe',
                         length = 24,
                         width = panelWidth,
                         height = 80,
                         aColor = (0.8,0.5,0.5) )
westWardrobe = BoxThing( label = 'east wardrobe',
                         length = 24,
                         width = panelWidth,
                         height = 80,
                         aColor = eastWardrobe._color )
eastWardrobe.placeAbove( deck )
westWardrobe.placeAbove( deck )
eastWardrobe.placeWestOf( eastWall )
westWardrobe.placeEastOf( westWall )
eastWardrobe.placeNorthOf( panelB_east )
westWardrobe.placeNorthOf( panelB_west )

# Side tables are not used or truncated in this version
sideTable_east = BoxThing( label = 'bedside table east',
                           length = 16,
                           width = (( deck.width - mattress.width ) / 2 ) - 1,
                           height = 24,
                           aColor = color.white )
sideTable_west = BoxThing( label = 'bedside table west',
                           length = 16,
                           width = (( deck.width - mattress.width ) / 2 ) - 1,
                           height = 24,
                           aColor = color.white )
sideTable_east.placeAbove( deck )
sideTable_west.placeAbove( deck )
sideTable_east.placeSouthOf( frontWall )
sideTable_west.placeSouthOf( frontWall )
sideTable_east.placeWestOf( eastWall )
sideTable_west.placeEastOf( westWall )


# Stove

stoveHeight = 30
stoveDiameter = 24
stoveRadius = stoveDiameter / 2
stoveClearance = 4
stoveOffset = stoveClearance + stoveRadius    # distance between wall and center axis

stoveElevation = 16   # Stove is raised above floor by 16"  -- TODO: Add shelf for stove

east = eastWall.westEdge - stoveOffset
north = panelA_east.southEdge - stoveOffset
up = deck.topEdge + stoveElevation

stove = PipeThing( label = 'stove',       
                   endA = vector( east, north, up ),
                   endB = vector( east, north, up + stoveHeight ),
                   diameter = stoveDiameter )

# Toilet

toiletHeight = 16
toiletDiameter = 18
toiletRadius = toiletDiameter / 2
toiletClearance = 6
toiletOffset = toiletClearance + toiletRadius    # distance between wall and center axis

toiletElevation = 0   # Stove is raised above floor by 16"  -- TODO: Add shelf for toilet

toilet_east = westWall.westEdge + toiletClearance + toiletRadius
toilet_north = panelB_west.southEdge - toiletOffset
toilet_up = deck.topEdge + toiletElevation

toilet = PipeThing( label = 'toilet',       
                   endA = vector( toilet_east, toilet_north, toilet_up ),
                   endB = vector( toilet_east, toilet_north, toilet_up + toiletHeight ),
                   diameter = toiletDiameter,
                   aColor = color.cyan )

# Counter accessories

burnerHeight = 1
burnerDiameter = 8
burnerRadius  = burnerDiameter / 2
burnerClearance = 3
burnerOffset = burnerClearance + burnerRadius

north = panelB_east.southEdge - burnerOffset
east = eastWall.westEdge - burnerOffset
up = counter.topEdge

backBurner = PipeThing( label = 'back burner',
                        endA = vector( east, north, up ),
                        endB = vector( east, north, up + burnerHeight ),
                        diameter = burnerDiameter,
                        aColor = color.red )

east = east - ( burnerDiameter + ( burnerClearance * 1 ))

frontBurner = PipeThing( label = 'back burner',
                        endA = vector( east, north, up ),
                        endB = vector( east, north, up + burnerHeight ),
                        diameter = burnerDiameter,
                        aColor = color.red )

galleySink = BoxThing( label = 'galley sink',
                       length = 21,
                       width = 15,
                       height = 6,
                       aColor = color.cyan )
galleySink.placeAbove( counter, offset = 1 - galleySink.height )
galleySink.placeNorthOf( panelA_east, offset = ( counter.length / 2 ) - ( galleySink.length / 2 ) )
galleySink.placeWestOf( eastWall, offset = (counter.width - galleySink.width - 2) )

galleyOvenClearance = 4
galleyOven = BoxThing( label = 'oven', length = 18, width = 20, height = 16, aColor = color.black )
galleyOven.placeAbove( counter, offset = -(galleyOven.height + galleyOvenClearance) )
galleyOven.placeSouthOf( panelB_east, offset = galleyOvenClearance )
galleyOven.placeWestOf( counter, offset = 1 - galleyOven.width  )

frigClearance = 3
galleyFrig = BoxThing( label = 'refrigerator', length = 24, width = 24, height = 30, aColor = color.yellow )
galleyFrig.placeAbove( deck, offset = counter.height - galleyFrig.height - frigClearance )
galleyFrig.placeNorthOf( panelA_east, offset = frigClearance )
galleyFrig.placeWestOf( counter, offset = 1 - galleyFrig.width  )

# Windows

windowThickness = wallThickness + 2

backWindow = BoxThing( label = 'back window', length = windowThickness, width = 90, height = 36, aColor = color.green,
                       aOpacity = 0.25 )
backWindow.placeAbove( deck, offset = 36 )
backWindow.placeSouthOf( deck, offset = -1.5 )
backWindow.placeEastOf( westWall, offset = 3 )

sideDoor = BoxThing( label = 'side door', length = 30, width = windowThickness, height = 78, aColor = color.green,
                     aOpacity = 0.75 )
sideDoor.placeAbove( deck )
sideDoor.placeNorthOf( backWall, offset = seat.length )
sideDoor.placeEastOf( deck, offset = -1.5 )

setteeWindow = BoxThing( label = 'window above settee',
                       length = settee.length - 4,
                       width = windowThickness,
                       height = backWindow.height,
                       aColor = color.green,
                       aOpacity = 0.25 )
setteeWindow.placeAbove( deck, offset = 36 )
setteeWindow.placeWestOf( deck, offset = -1.5 )
setteeWindow.placeNorthOf( backWall, offset = 2 )

seatWindow = BoxThing( label = 'window over seat',
                       width = windowThickness,
                       length = seat.length - 6, 
                       height = backWindow.height,
                       aColor = color.green,
                       aOpacity = 0.25 )
seatWindow.placeAbove( deck, offset = 36 )
seatWindow.placeNorthOf( backWall, offset = 2 )
seatWindow.placeWestOf( eastWall, offset = -1.5 )

# Round window over galley sink

galleyWindowDiameter = 30
galleyWindowRadius = galleyWindowDiameter / 2

north = (counter.northEdge + counter.southEdge) / 2
east = eastWall.westEdge - 1
up   = counter.topEdge + 8 + galleyWindowRadius


galleyWindowCenterInside = vector( east, north, up )
galleyWindowCenterOutside = vector( east + windowThickness, north, up )


galleyWindow = PipeThing( label = 'galley window',
                          endA = galleyWindowCenterInside,
                          endB = galleyWindowCenterOutside,
                          diameter = galleyWindowDiameter,
                          aColor = color.green,
                          aOpacity = 0.25 )

# Bedroom Porthole windows

portholeDiameter = 8
portholeThickness = windowThickness

north = frontWall.southEdge
west = westWall.westEdge - 1
east = eastWall.westEdge - 1
eyeLevel = deck.height + 62

westPorts = set()
eastPorts = set()
for y in ( north - 20, north - 40, north - 60, north - 80 ):

    eastPorts.add( PipeThing( label = 'east porthole ' + str(y),
                             endA = vector( east, y, eyeLevel ),
                             endB = vector( east + portholeThickness, y, eyeLevel ),
                             diameter = portholeDiameter,
                             aColor = color.green,
                             aOpacity = 0.25 )
                   )
    westPorts.add( PipeThing( label = 'west porthole ' + str(y),
                             endA = vector( west, y, eyeLevel ),
                             endB = vector( west + portholeThickness, y, eyeLevel ),
                             diameter = portholeDiameter,
                             aColor = color.green,
                             aOpacity = 0.25 )
                   )

# toilet porthole

westPorts.add( PipeThing( label = 'head porthole',
                              endA = vector( west, toilet_north, eyeLevel ),
                              endB = vector( west + portholeThickness, toilet_north, eyeLevel ),
                              diameter = portholeDiameter,
                              aColor = color.white,
                              aOpacity = 0.25 )
               )
    
# Wheels

wheelDiameter = 24
wheelRadius = wheelDiameter / 2
wheelClearance = 6
wheelWidth = 6

steelBeamHeight = 6
steelBeamWidth = 4

wheelEast = deck.eastEdge
wheelWest = deck.westEdge
wheelUp = deck.bottomEdge - steelBeamHeight

# steel frames

beamEast = BoxThing( label = 'beam on East',
                     length = deck.length + 1,
                     width = steelBeamWidth,
                     height = steelBeamHeight,
                     aColor = color.orange
                     )
beamEast.placeBelow( deck )
beamEast.placeWestOf( eastWall, offset = wheelWidth + wheelClearance )
beamEast.placeNorthOf( backWall )


beamWest = BoxThing( label = 'beam on West',
                     length = deck.length + 1,
                     width = steelBeamWidth,
                     height = steelBeamHeight,
                     aColor = color.orange
                     )
beamWest.placeBelow( deck )
beamWest.placeEastOf( westWall, offset = wheelWidth + wheelClearance )
beamWest.placeNorthOf( backWall )

beamCenter = BoxThing( label = 'beam on Center',
                       length = deck.length + ( deck.width / 2 ),
                       width = steelBeamWidth,
                       height = steelBeamHeight,
                       aColor = color.orange
                       )
beamCenter.placeBelow( deck )
beamCenter.placeEastOf( westWall, offset = ( deck.width / 2 ) - (steelBeamWidth / 2 ) )
beamCenter.placeNorthOf( backWall )

axleSetBack = 48

# axle A
wheelNorth = deck.southEdge + ( deck.length / 2 ) + wheelRadius + ( wheelClearance / 2) - axleSetBack
wheelEastA = PipeThing( label = 'wheel East on axle A',
                        endA = vector( wheelEast, wheelNorth, wheelUp  ),
                        endB = vector( wheelEast - wheelWidth, wheelNorth, wheelUp  ),
                        diameter = wheelDiameter,
                        aColor = color.black )
wheelWestA = PipeThing( label = 'wheel West on axle A',
                        endA = vector( wheelWest             , wheelNorth, wheelUp  ),
                        endB = vector( wheelWest + wheelWidth, wheelNorth, wheelUp  ),
                        diameter = wheelDiameter,
                        aColor = color.black )
# axle B
wheelNorth = deck.southEdge + ( deck.length / 2 ) - ( wheelRadius + ( wheelClearance / 2) ) - axleSetBack
wheelEastB = PipeThing( label = 'wheel East on axle B',
                        endA = vector( wheelEast, wheelNorth, wheelUp  ),
                        endB = vector( wheelEast - wheelWidth, wheelNorth, wheelUp  ),
                        diameter = wheelDiameter,
                        aColor = color.black )
wheelWestB = PipeThing( label = 'wheel West on axle B',
                        endA = vector( wheelWest             , wheelNorth, wheelUp  ),
                        endB = vector( wheelWest + wheelWidth, wheelNorth, wheelUp  ),
                        diameter = wheelDiameter,
                        aColor = color.black )
# wheel wells

wheelWellEast = BoxThing( label = 'wheel well East',
                          length = (wheelDiameter * 2) + (wheelClearance * 3),
                          width = wheelWidth + wheelClearance,
                          height = wheelRadius + wheelClearance,
                          aColor = ( 0.5, 0.5, 0.5 )
                          )
wheelWellEast.placeAbove( beamEast, offset = -beamEast.height )
wheelWellEast.placeEastOf( beamEast, offset = 1 )
wheelWellEast.placeNorthOf( backWall, offset = (deck.length / 2) - (wheelWellEast.length / 2) - axleSetBack )


wheelWellWest = BoxThing( label = 'wheel well West',
                          length = (wheelDiameter * 2) + (wheelClearance * 3),
                          width = wheelWidth + wheelClearance,
                          height = wheelRadius + wheelClearance,
                          aColor = ( 0.5, 0.5, 0.5 )
                          )
wheelWellWest.placeAbove( beamWest, offset = -beamWest.height )
wheelWellWest.placeWestOf( beamWest, offset = 1 )
wheelWellWest.placeNorthOf( backWall, offset = (deck.length / 2) - (wheelWellEast.length / 2) - axleSetBack )

# Draw deck and walls

deck.draw()
backWall.draw()
showFrontWall = True
if showFrontWall:
    frontWall.draw()
makeTranparent = "westWall.draw()"
makeTranparent = "eastWall.draw()"

panelA_east.draw()
panelA_west.draw()
panelB_east.draw()
panelB_west.draw()

beamEast.draw()
beamWest.draw()
beamCenter.draw()

wheelWellEast.draw()
wheelWellWest.draw()

# Wheels

wheelEastA.draw()
wheelWestA.draw()
wheelEastB.draw()
wheelWestB.draw()


# Draw furniture

seat.draw()
table.draw()
stove.draw()
toilet.draw()
settee.draw()

counter._opacity = 0.5
counter.draw()

mattress.draw()
bedPlatform.draw()
eastWardrobe.draw()
westWardrobe.draw()

sideTables = True
if sideTables:
    sideTable_east.draw()
    sideTable_west.draw()


# Counter accessories

backBurner.draw()
frontBurner.draw()
galleySink.draw()
galleyOven.draw()
galleyFrig.draw()

# Draw windows last

sideDoor.draw()
seatWindow.draw()
backWindow.draw()
setteeWindow.draw()
galleyWindow.draw()

portHoles = True
if portHoles:
        
    for porthole in eastPorts:
        porthole.draw()

    for porthole in westPorts:
        porthole.draw()
        

# Experiment with parabolic surface at front

insideCurve = []
outsideCurve = []
for iY in range(0,11):
    yPrime = 0.1 * iY
    xPrime = yPrime * yPrime
    y = ( 12 * 12 * yPrime )   
    x = westWardrobe.westEdge - ( 4 * 12 * xPrime )
    insideCurve.append(  ( x, y )  )
    outsideCurve.append( ( x + 0.25, y )  )

outAndBack = outsideCurve + list( reversed( insideCurve ) )

curveBase = Polygon( outAndBack  )

#print "curveBase = " , curveBase

lowerPoint = ( westWardrobe.westEdge, westWardrobe.northEdge, 0 )
upperPoint = ( westWardrobe.westEdge, westWardrobe.northEdge, 4*12 )

curvedWall = extrusion( pos = [ lowerPoint, upperPoint ],
                        shape = curveBase,
                        color = color.red )

mirror = []
for point in outAndBack:
    mirrorX = -point[0]
    mirrorY = point[1]
    mirror.append( ( mirrorX, mirrorY ) )

outAndBack2 = list( reversed( mirror ) )
curveBase2 = Polygon( outAndBack2 )
lowerPoint2 = ( eastWardrobe.eastEdge, eastWardrobe.northEdge, 0 )
upperPoint2 = ( eastWardrobe.eastEdge, eastWardrobe.northEdge, 4*12 )
curvedWall2 = extrusion( pos = [ lowerPoint2, upperPoint2 ],
                        shape = curveBase2,
                        color = color.red )

    



