import turtle
import random

fred = turtle.Turtle()
fred.speed(0)
fred.seth(90)

def spiral(initialLength, angle, multiplier): #Draws a spiral that gets progressively smaller or larger based on multiplier

    if multiplier > 1:
        if initialLength > 200:
            return

    if multiplier < 1:
        if initialLength < 1:
            return

    fred.forward(initialLength)
    fred.right(angle)
    spiral(initialLength*multiplier, angle, multiplier)

def tree(trunkLength, height): #Draws a tree

    if height == -1:
        return

    fred.forward(trunkLength)
    fred.left(40)
    tree(trunkLength/1.5, height-1)
    fred.right(80)
    tree(trunkLength/1.5, height-1)
    fred.left(40)
    fred.backward(trunkLength)

def tree3(trunkLength,height): #Draws a different size tree

    if height == -1:
        return

    fred.forward(trunkLength)
    fred.left(50)
    tree(trunkLength/1.5, height-1)
    fred.right(100)
    tree(trunkLength/1.5, height-1)
    fred.left(50)
    tree(trunkLength/1.6, height-1)
    fred.backward(trunkLength)
    
def forest(n, limits): #Draws n trees within boundary limits to create a forest

    for i in range(n):
        fred.up()
        fred.goto(random.randint(limits[0][0],limits[1][0]),random.randint(limits[0][1],limits[1][1]))
        fred.down()
        tree(50+random.randint(-10,20),4+random.randint(0,2))

def coolsnowflake(sideLength, levels): #Makes a neat-looking recursive snowflake

    if levels == 0:
        fred.forward(sideLength)
        return

    koch(sideLength/3, levels-1)
    fred.left(60)
    koch(sideLength/3, levels-1)
    fred.right(120)
    koch(sideLength/3, levels-1)
    fred.left(60)
    koch(sideLength/3, levels-1)
    fred.right(120)

def koch(sideLength, levels):

    if levels == 0:
        fred.forward(sideLength)
        return

    koch(sideLength/3, levels-1)
    fred.left(60)
    koch(sideLength/3, levels-1)
    fred.right(120)
    koch(sideLength/3, levels-1)
    fred.left(60)
    koch(sideLength/3, levels-1)# only draws part of a koch snowflake, finish


def scene(): #Draws a winter wonderland

    forest(6,[(-400,-200),(350,-150)])
    for i in range(8):
        fred.up()
        fred.goto(random.randint(-425,375),random.randint(-10,80))
        fred.down()
        fred.right(90)
        spiral(25,45,.95)

if __name__=="__main__":
    scene()
