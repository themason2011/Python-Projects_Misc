# basicShapes.py, Mason Corey
import turtle
import math
t = turtle.Turtle() #Initialize turtle t
turtle.screensize(canvwidth = 1920, canvheight = 1080) #Set proper screen size
t.shape("turtle")
t.width(4) #Set size of lines created by turtle

def drawRectangle_1(): #Draws a rectangle
    
    t.color('green', 'yellow')
    t.seth(0)       
    t.begin_fill()   
    t.forward(50)    
    t.left(90)       
    t.forward(100)   
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90)       
    t.end_fill()    

def drawRectangle_2(): #Draws a rectangle in a different way

    x1 = t.xcor()
    y1 = t.ycor()

    x2 = x1 + 50
    y2 = y1

    x3 = x2
    y3 = y2 + 100

    x4 = x1
    y4 = y1 + 100

    
    t.color("green", "yellow")
    t.begin_fill()
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(x4, y4)
    t.goto(x1, y1)
    
    t.end_fill()

def drawRectangle_3(): #Draws a rectangle in a different way

    x1 = t.xcor()
    y1 = t.ycor()

    fourCorners = [(x1 + 50, y1), (x1 + 50, y1 + 100), (x1, y1 + 100), (x1, y1)]
    
    t.color("green", "yellow")
    t.begin_fill()
    
    t.goto(fourCorners[0][0], fourCorners[0][1])
    t.goto(fourCorners[1][0], fourCorners[1][1])
    t.goto(fourCorners[2][0], fourCorners[2][1])
    t.goto(fourCorners[3][0], fourCorners[3][1])

    t.end_fill()

def drawRectangle(width, height, tilt, penColor, fillColor): #Draws a rectangle in a different way

    t.color(penColor, fillColor)
    t.seth(tilt)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.end_fill()
    t.seth(0)

def drawTwoRectangles(): #Draws two rectangles
    
    drawRectangle( 50, 100, 0, "red", "") 

    t.seth(0)
    t.up()     
    t.forward(100)  
    t.down()

    drawRectangle( 100, 150, 22, "green", "yellow")

def drawTriangle(base, height, penColor, fillColor): #Draws a triangle
    a = base/2
    b = height
    c = math.sqrt(a**2 + b**2)
    angle1 = 180-(math.degrees(math.atan(b/a)))
    angle2 = 180-(2*(math.degrees(math.atan(a/b))))
    t.color(penColor, fillColor)
    t.begin_fill()
    t.seth(0)
    t.forward(base)
    t.left(angle1)
    t.forward(c)
    t.left(angle2)
    t.forward(c)
    t.end_fill()
    t.seth(0)

def drawTriangleTop(base, height, tilt, penColor, fillColor): #Draws a triangle with a different orientation
    startAngle = 2*math.degrees(math.atan(base/(2*height)))
    angle1 = (180-startAngle)/2
    sideLen = math.sqrt(((base**2)/4)+height**2)
    t.color(penColor, fillColor)
    t.begin_fill()
    t.seth(tilt)
    t.right(startAngle/2)
    t.forward(sideLen)
    t.left(180-angle1)
    t.forward(base)
    t.left(180-angle1)
    t.forward(sideLen)
    t.seth(tilt)
    t.end_fill()
    

def drawTwoTriangles(): #Draws two triangles of different colors

    t.up()
    t.forward(100)
    t.down()
    
    drawTriangle(50, 100, 'green', 'blue')

    t.seth(0)
    t.up()
    t.forward(60)
    t.down()

    drawTriangle(60, 80, 'purple', 'red')

if __name__ =="__main__":

    pass
