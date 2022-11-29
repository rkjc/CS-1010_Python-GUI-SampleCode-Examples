import math
import tkinter as tk
import random

class Point(object):
    def __init__(self, xPos, yPos):
        self.X = xPos
        self.Y = yPos

# double rounding code found at:  https://www.baeldung.com/java-round-decimal-number
def	distance(point1, point2):
    temp = math.sqrt(math.pow((point1.X - point2.X), 2) + math.pow(point1.Y - point2.Y, 2))
    return temp

def midPoint(p1, p2):
    return Point((p1.X + p2.X)/2, (p1.Y + p2.Y)/2)

def drawPoint(xCord,yCord):
    x = int(xCord)
    y = int(yCord)
    drawboard.create_oval(x, y, x, y, fill="green")

def drawPoint2(pt):
    drawPoint(pt.X, pt.Y)

def runRandom(count):
    for x in range(count):
        drawPoint(random.randint(1,394), random.randint(1,394))

def drawSerpinsk():
    c1 = Point(windowWidth/2,5)
    c2 = Point(5,windowHeight-5)
    c3 = Point(windowWidth-5,windowHeight-5)
    drawboard.create_oval(c1.X-5, c1.Y-5, c1.X+5, c1.Y+5, fill="orange")
    drawboard.create_oval(c2.X-5, c2.Y-5, c2.X+5, c2.Y+5, fill="orange")
    drawboard.create_oval(c3.X-5, c3.Y-5, c3.X+5, c3.Y+5, fill="orange")
    spot = midPoint(c1,c2)
    drawPoint2(spot)
    print(spot.X, spot.Y)
    for p in range(100000):
        pick = random.randint(1,3)
        if(pick == 1):
            spot = midPoint(spot, c1)
        elif(pick == 2):
            spot = midPoint(spot, c2)
        else:
            spot = midPoint(spot, c3)
        drawPoint2(spot)

windowWidth = 800
windowHeight = 800

point1 = Point(0,0)
point2 = Point(3,4)
print(distance(point1, point2))
p5 = Point(abs(point1.X - point2.X)/2, abs(point1.Y - point2.Y)/2)
print(p5.X, p5.Y)
print(random.random())


groot = tk.Tk()
sizeStr = str(windowWidth) + "x" + str(windowHeight)
groot.geometry(sizeStr)

drawboard = tk.Canvas(groot, width=windowWidth, height=windowHeight)
#drawboard.create_line(70, 20, 70, 250, width=2)
#drawboard.create_oval(100, 200, 105, 205, fill="green")
drawboard.pack()

#runRandom(100)
drawSerpinsk()


groot.mainloop()
