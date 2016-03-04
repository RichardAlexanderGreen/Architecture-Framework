# Architecture Utilities - -- Thing.py is Architecture Framework.

from __future__ import division
from visual import *

class Thing:

    label = ''

    children = set()   # the positions (edges) of _ children are relative to _ position

    width  = 1.0    # on X  -- East-West   -- positive X points East
    length = 1.0    # on Y  -- North-South -- positive Y points North 
    height = 1.0    # on Z  -- Up-Down     -- positive Z points Up

    eastEdge = 1.0  # If I am a box, where is _ East edge ?
    westEdge = 0.0
    northEdge = 1.0
    southEdge = 0.0

    topEdge = 1.0
    bottomEdge = 0.0

    clearance = 0.01  # amount of clearance between physical objects

    isVisible = True  # visible by default
    
    def __init__(self, label = '',
                 width = 1.0,
                 length = 1.0,
                 height = 1.0,
                 clearance = 0.01,
                 visible = True,
                 aOpacity = 1.0 ):
        self._label = label
        
        self.width = width
        self.length = length
        self.height = height

        self.topEdge = self.bottomEdge + self.height
        self.eastEdge = self.westEdge + self.width
        self.northEdge = self.southEdge + self.length

        self.isVisible = visible
        self.opacity = aOpacity

        self.clearance = clearance

        self.children = set()
 

    def placeAbove( self, other, offset = 0.0 ):
        self.bottomEdge = other.topEdge + offset + self.clearance
        self.topEdge = self.bottomEdge + self.height
        self.westEdge = other.westEdge
        self.eastEdge = self.westEdge + self.width

    def placeBelow( self, other, offset = 0.0 ):
        self.topEdge = other.bottomEdge - offset - self.clearance
        self.bottomEdge = self.topEdge - self.height

    def placeEastOf( self, other, offset = 0.0 ):
        self.westEdge = other.eastEdge + offset + self.clearance
        self.eastEdge = self.westEdge + self.width
        
    def placeWestOf( self, other, offset = 0.0 ):
        self.eastEdge = other.westEdge - offset - self.clearance
        self.westEdge = self.eastEdge - self.width
        
    def placeNorthOf( self, other, offset = 0.0 ):
        self.southEdge = other.northEdge + offset + self.clearance
        self.northEdge = self.southEdge + self.length
        
    def placeSouthOf( self, other, offset = 0.0 ):
        self.northEdge = other.southEdge - offset - self.clearance
        self.southEdge = self.northEdge - self.length

    def drawChildren( self ):
        for child in self.children:
            child.draw()
            

class BoxThing( Thing ):

    _color = color.gray( 0.25 )
    _opacity = 0.5
    _label = ''

    def __init__(self, label = '',
                 length = 1.0,
                 width = 1.0,
                 height = 1.0,
                 clearance = 0.0,
                 visible = True,
                 aColor = color.white,
                 aOpacity = 1.0 ):

        Thing.__init__( self,
                        label = label,
                        length = length,
                        width = width,
                        height = height,
                        visible = visible,
                        aOpacity = aOpacity,
                        clearance = clearance )
        self._color = aColor
        self._opacity = aOpacity
        self._label = label

    def draw( self ):

        # Draw as visual box
        east = self.westEdge + ( self.width / 2 )
        north = self.southEdge + ( self.length / 2 )
        up = self.bottomEdge + ( self.height / 2 )
        center = ( east, north, up )

        removed = """print "drawing:", self._label, self.westEdge, center"""
    
        
        # I switch around the box dimensions -- so that coordinates are consistent with _ model
        self._View = box( length = self.width,  # X = East-West
                     height = self.length,      # Y = North-South
                     width = self.height,       # Z = Up-Down
                     pos = center,
                     visible = self.isVisible,
                     color = self._color,
                     opacity = self._opacity )

        self.drawChildren()

class PipeThing( Thing ):

    def __init__( self,
              label = 'some pipe',
              endA = vector( 0, 0, 0 ),  # ( east, north, up )
              endB = vector( 1, 1, 1 ),
              diameter = 0.1,
              aColor = ( 1, 0.7, 0.2 ),  # copper like
              aOpacity = 1.0 ):

        self.length = abs( endA[0] - endB[0] )
        self.width = abs( endA[1] - endB[1] )
        self.height = abs( endA[2] - endB[2] )
        Thing.__init__( self, label = label,
                        length = self.length,
                        width = self.width,
                        height = self.height )
        self.endA = endA
        self.endB = endB
        self.diameter = diameter
        self.aColor = aColor
        self.aOpacity = aOpacity

    def draw( self ):

        myAxis = self.endB - self.endA
        myRadius = self.diameter / 2

        self._View = cylinder( pos = self.endA, axis = myAxis, radius = myRadius,
                               color = self.aColor, opacity = self.aOpacity )
        self.drawChildren()
