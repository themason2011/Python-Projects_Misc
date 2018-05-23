import turtle

jane = turtle.Turtle() #Initialize turtle object
jane.shape('turtle')
jane.color('red')
width = 0
x = 50

def drawSquare(width): #draws a square of a given width
    jane.forward(width)
    jane.left(90)
    jane.forward(width)
    jane.left(90)
    jane.forward(width)
    jane.left(90)
    jane.forward(width)
    return jane.left(90)

def drawRectangle(width, height): #draws a rectangle of a given width and height
    jane.begin_fill()
    jane.forward(width)
    jane.left(90)
    jane.forward(height)
    jane.left(90)
    jane.forward(width)
    jane.left(90)
    jane.forward(height)
    jane.end_fill()
    return jane.left(90)

def drawThreeRectangles(width, height, spacing): #draws three rectangles with given width, height, and spacing
    drawRectangle(width, height)
    jane.up()
    jane.forward(width + spacing)
    jane.down()
    drawRectangle(width, height)
    jane.up()
    jane.forward(width + spacing)
    jane.down()
    return drawRectangle(width, height)
    
def drawNRectangles(width, height, spacing, N): #draws n rectangles with given width, height, and spacing
    for i in range(N):
        colors = ['red','blue','green']
        jane.color(colors[i%3])
        drawThreeRectangles(width, height, spacing)

