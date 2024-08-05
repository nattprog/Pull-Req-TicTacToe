from turtle import Turtle

t = Turtle()
NoughtsDict = {}
CrossesDict = {}

def BoardInitiate():
    for i in [-1, 1]:
        t.pu()
        for ii in [-1, 1]:
            t.goto(50*i, 50*3*ii)
            t.pd()
    for i in [-1, 1]:
        t.pu()
        for ii in [-1, 1]:
            t.goto(ii*50*3, 50*i)
            t.pd()

def Noughts(xPlacement, yPlacement):
    xCoord, yCoord = xPlacement*50*2, yPlacement*50*2
    t.pu()
    t.goto(xCoord, yCoord-20)
    t.pd()
    t.circle(20)

def Crosses(xPlacement, yPlacement):
    xCoord, yCoord = xPlacement*50*2, yPlacement*50*2
    for i in [-1, 1]:
        t.pu()
        for ii in [-1, 1]:
            t.goto(xCoord-i*ii*20, yCoord-ii*20)
            t.pd()
