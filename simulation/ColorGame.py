import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint

################################################################

# This program is an interactive simulation/game. A cat starts
# to move across the screen. The direction of movement is reversed
# on each "mouse down" event.
#
# The state of the cat is represented by a tuple (pos, delta-pos).
# The first element, pos, represents the x-coordinate of the cat.
# The second element, delta-pos, represents the amount that the
# position changes on each iteration of the simulation loop.
#
# For example, the tuple (7,1) would represent the cat at x-coord,
# 7, and moving to the right by 1 pixel per "clock tick."
# 
# The initial state of the cat in this program is (0,1), meaning that the cat
# starts at the left of the screen and moves right one pixel per tick.
#
# Pressing a mouse button down while this simulation run updates the cat state
# by leaving pos unchanged but reversing delta-pos (changing 1 to -1 and vice
# versa). That is, pressing a mouse key reverses the direction of the
# cat.
#
# The simulation ends when the cat is allowed to reach either the left
# or the right edge of the screen.

################################################################

# Initialize world
name = "Cat Fun. Press the mouse (but not too fast)!"
width = 1260
height = 720
rw.newDisplay(width, height, name)

################################################################

# Display the state by drawing a cat at that x coordinate
bgrnd = dw.loadImage("ColorGrid.bmp")
myimage = dw.loadImage("ColorBlock.bmp")

# state -> image (IO)
# draw the cat halfway up the screen (height/2) and at the x
# coordinate given by the first component of the state tuple
#
def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(bgrnd, (0,0))
    dw.draw(myimage, (state[0], state[2]))


################################################################

# Change pos by delta-pos, leaving delta-pos unchanged
# Note that pos is accessed as state[0], and delta-pos
# as state[1]. Later on we'll see how to access state
# components by name (as we saw with records in Idris).
#
# state -> state
def updateState(state):
    return((state[0]+state[1],state[1],state[2]+state[3],state[3]))

################################################################

# Terminate the simulation when the x coord reaches the screen edge,
# that is, when pos is less then zero or greater than the screen width
# state -> bool
def endState(state):
    if (state[0] > width or state[0] < 0 or state[2] < 0 or state[2] > height):
        return True
    else:
        return False


################################################################

# We handle each event by printing (a serialized version of) it on the console
# and by then responding to the event. If the event is not a "mouse button down
# event" we ignore it by just returning the current state unchanged. Otherwise
# we return a new state, with pos the same as in the original state, but
# delta-pos reversed: if the cat was moving right, we update delta-pos so that
# it moves left, and vice versa. Each mouse down event changes the cat
# direction. The game is to keep the cat alive by not letting it run off the
# edge of the screen.
#
# state -> event -> state
#
def handleEvent(state, event):  
#    print("Handling event: " + str(event))
    if (event.type == pg.MOUSEBUTTONDOWN):
        mousepos = pg.mouse.get_pos()
        mouseX = mousepos[0]
        mouseY = mousepos[1]
        if mouseX < 180 and mouseY < 180:
            print("Box 1")
        if mouseX > 180 and mouseX < 360 and mouseY < 180:
            print("Box 2")
        if mouseX > 360 and mouseX < 540 and mouseY < 180:
            print("Box 3")
        if mouseX > 540 and mouseX < 720 and mouseY < 180:
            print("Box 4")
        if mouseX > 720 and mouseX < 900 and mouseY < 180:
            print("Box 5")
        if mouseX > 900 and mouseX < 1080 and mouseY < 180:
            print("Box 6")
        if mouseX > 1080 and mouseX < 1260 and mouseY < 180:
            print("Box 7")
        if mouseX < 180 and mouseY > 180 and mouseY < 360:
            print("Box 8")
        if mouseX > 180 and mouseX < 360 and mouseY > 180 and mouseY < 360:
            print("Box 9")
        if mouseX > 360 and mouseX < 540 and mouseY > 180 and mouseY < 360:
            print("Box 10")
        if mouseX > 540 and mouseX < 720 and mouseY > 180 and mouseY < 360:
            print("Box 11")
        if mouseX > 720 and mouseX < 900 and mouseY > 180 and mouseY < 360:
            print("Box 12")
        if mouseX > 900 and mouseX < 1080 and mouseY > 180 and mouseY < 360:
            print("Box 13")
        if mouseX > 1080 and mouseX < 1260 and mouseY > 180 and mouseY < 360:
            print("Box 14")
        if mouseX < 180 and mouseY > 360 and mouseY < 540:
            print("Box 15")
        if mouseX > 180 and mouseX < 360 and mouseY > 360 and mouseY < 540:
            print("Box 16")
        if mouseX > 360 and mouseX < 540 and mouseY > 360 and mouseY < 540:
            print("Box 17")
        if mouseX > 540 and mouseX < 720 and mouseY > 360 and mouseY < 540:
            print("Box 18")
        if mouseX > 720 and mouseX < 900 and mouseY > 360 and mouseY < 540:
            print("Box 19")
        if mouseX > 900 and mouseX < 1080 and mouseY > 360 and mouseY < 540:
            print("Box 20")
        if mouseX > 1080 and mouseX < 1260 and mouseY > 360 and mouseY < 540:
            print("Box 21")
        if mouseX < 180 and mouseY > 540 and mouseY < 720:
            print("Box 22")
        if mouseX > 180 and mouseX < 360 and mouseY > 540 and mouseY < 720:
            print("Box 23")
        if mouseX > 360 and mouseX < 540 and mouseY > 540 and mouseY < 720:
            print("Box 24")
        if mouseX > 540 and mouseX < 720 and mouseY > 540 and mouseY < 720:
            print("Box 25")
        if mouseX > 720 and mouseX < 900 and mouseY > 540 and mouseY < 720:
            print("Box 26")
        if mouseX > 900 and mouseX < 1080 and mouseY > 540 and mouseY < 720:
            print("Box 27")
        if mouseX > 1080 and mouseX < 1260 and mouseY > 540 and mouseY < 720:
            print("Box 28")
        NewX = randint(0,6) * 180
        NewY = randint(0,3) * 180
        return((NewX,0,NewY,0))
    else:
        return(state)
    print(event)

################################################################

# World state will be single x coordinate at left edge of world

# The cat starts at the left, moving right 
initState = (0,0,0,0)

# Run the simulation no faster than 60 frames per second
frameRate = 60

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)

