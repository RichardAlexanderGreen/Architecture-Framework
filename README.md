Architecture-Framework
======================

This is an architecture framework written to run in [VPython](http://en.wikipedia.org/wiki/VPython).
VPython is Python running is a special framework that enables 3D visualization.

The basic concept is that you create boxes with appropriate dimensions to represent walls, windows, doors, decks.
The framework saves you the trouble of computing offsets.
For example, to make a 16' by 12' room with 8" walls you might say:

```Python
  deck = BoxThing( label = 'deck', length = 16*12, width = 12*12, height = 10, aColor = color.yellow )

  wallThickness = 8
  wallHeight = 8*12

  backWall = BoxThing( label = 'back wall', length = wallThickness, width = deck.width, 
                          height = wallHeight, aColor = color.red )
  backWall.placeSouthOf( deck, offset = 0 )

  frontWall = BoxThing( label = 'front wall', length = wallThickness, width = deck.width, 
                          height = wallHeight, aColor = color.red )
  frontWall.placeNorthOf( deck, offset = 0 )

  westWall = BoxThing ( label = 'west wall', length = deck.length, width = wallThickness, 
                          height = wallHeight, aColor = color.red )
  westWall.placeWestOf( deck )

  eastWall = BoxThing ( label = 'east wall', length = deck.length, width = wallThickness, 
                          height = wallHeight, aColor = color.red )
  eastWall.placeEastOf( deck )
```
