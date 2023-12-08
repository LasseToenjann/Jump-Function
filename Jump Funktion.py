#Jump Funktion

from turtle import *

winkel = 45
distanz = 100

def jump(distanz,winkel):
    penup()
    right(winkel)
    forward(distanz)
    left(winkel)
    pendown()

jump(distanz,winkel)

done()