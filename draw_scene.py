# project01.py, Mason Corey

from basic_shapes import *
import random
import math

def drawTree(height, color):
    
    ''' 
    This function draws a tree of a given height that consists of a rectangular brown bark and a top comprised of three triangles of a given color stacked on top of each other.
    The bottom left corner of the bark will be at current location of the turtle, making no assumptions about the orientation of the turtle.
    After drawing the tree the turtle will be returned to its original position and oriented at 0 degrees 
    All other parameters such as the width of the tree and the length of the bark are chosen so that the tree is well proportioned: a taller tree is wider and has a thicker and taller bark.
    '''

    width = (height/2)
    startX = t.xcor()
    startY = t.ycor()
    btmLeftStumpX = startX + (5/12)*width
    btmLeftStumpY = startY
    widthStump = (1/6)*width
    heightStump = (height/3)
    triHeight = (height/3)
    t.speed(0)

    t.up()  #Draws Stump
    t.goto(btmLeftStumpX,btmLeftStumpY)
    t.down()
    drawRectangle(widthStump,heightStump,0,'brown','brown')

    for i in range(3):  #Draws three triangles that create the top of the tree
        t.up()
        t.goto(startX, startY+(height*(2+i)/6))
        t.down()
        drawTriangle(width,triHeight,color,color)

    t.up()  #Return to original position
    t.goto(startX,startY)
    t.seth(0)
    t.down()

def checkTreeHeight(): #Can be used to confirm the height of a tree for testing
    t.up()
    t.goto(0,-200)
    t.down()
    drawRectangle(200, 200, 0 , "red","")
    t.seth(0)
    drawTree(200, "green")

def drawForest(numTrees): #Draws numTrees trees within a certain boundary

    n = 0
    numBound = 0

    for i in range(numTrees):
        sizeBounds = int(1400/numTrees)
        randPosX = random.randint(-750 + n*sizeBounds, -750 + (n + 1)*sizeBounds)
        randPosY = random.randint(-10,10)
        randHeight = random.randint(180,220)
        colors = ["#006400", "#556b2f", "#8fbc8f", "#2e8b57", "#3cb371", "#20b2aa", "#32cd32"]
        randColor = random.choice(colors)
        t.up()
        t.goto(randPosX,randPosY)
        t.down()
        drawTree(randHeight, randColor)
        n += 1

def drawHut(): #Draws a hut

    t.speed(0)
    startX = t.xcor()
    startY = t.ycor()
    widthHut = 10

    for i in range(8):
        randGap = random.randint(5,10)
        drawRectangle(10, 50, 0, 'black', 'brown')
        startX += randGap
        widthHut += randGap
        t.goto(startX, startY)

    topX = startX - widthHut/2
    topY = startY + 80
    t.up()
    t.goto(topX,topY)
    t.down()

    for j in range(20):
        tilt = random.randint(120 + j*7, 120 + (j+1)*7)
        drawRectangle(9, 50, tilt, 'black', 'brown')

def drawVillage(): #Draws five huts within a boundary to create a village
    for i in range(5):
        randPosX = random.randint(-500 + i*200, -500 + (i + 1)*200)
        randPosY = random.randint(-90,-70)
        t.up()
        t.goto(randPosX, randPosY)
        t.down()
        drawHut()

def drawSun(): #Draws a sun in the top left corner of a canvas
    startX = -550
    startY = 200
    t.up()
    t.goto(-550,200)
    t.down()
    t.speed(0)

    for i in range(45):
        drawRectangle(8, 50, i*8, 'yellow', 'yellow')

    for j in range(4):
        t.up()
        t.goto(startX + 70*math.cos(math.radians(90*j)), startY  + 70*math.sin(math.radians(90*j)))
        t.down()
        tilt = 90*j
        drawTriangleTop(10,50, tilt, 'yellow','yellow')

    for k in range(4):
        t.up()
        t.goto(startX + 70*math.cos(math.radians(45*(2*k+1))),startY + 70*math.sin(math.radians(45*(2*k+1))))
        t.down()
        tilt = 45*(2*k + 1)
        drawTriangleTop(10,50, tilt, 'yellow', 'yellow')
        

def drawScene(): #Draws a nice scene
    drawSun()
    drawForest(20)
    drawVillage()

if __name__=="__main__":
  print('Inside main of drawScene.py')
  drawScene()
