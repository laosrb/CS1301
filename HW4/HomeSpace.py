import turtle
import math
import tkinter
import random
t = turtle.Turtle()
x = 0
y = 0
t.speed("fastest")
def sky():
    turtle.Screen().bgcolor("light blue")
sky()
def grass():
    t.penup()
    # t.pencolor("green")
    t.goto(0,-800)
    t.dot(1500, "green")
grass()
def cloud():
    t.goto(360,300)
    t.dot(130, "white")
    t.goto(280,300)
    t.dot(100,"white")
    t.goto(340,340)
    t.dot(130, "white")                     # cloud 1
    t.goto(-400,340)
    t.dot(150,"white")
    t.goto(-340,340)
    t.dot(130, "white")
    t.goto(-460,400)
    t.dot(150, "white")
    t.goto(-380,400)
    t.dot(120,"white")
    t.goto(-440,440)
    t.dot(150, "white")
    t.goto(-200,200)
    t.dot(130, "white")
    t.goto(-230,190)
    t.dot(130, "white")
    t.goto(-180,150)
    t.dot(100, "white")
cloud()     
def house():
    t.goto(-15,0)
    t.color("black")
    t.shape("turtle")
    # the house
    t.fillcolor("tan")
    t.begin_fill()
    t.right(90)
    t.forward(200)
    t.left(90)
    t.forward(290)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(290)
    t.right(90)
    t.end_fill()
    # the house
    t.fillcolor("gray")         # roof
    t.begin_fill()
    t.right(45)
    t.forward(200)
    t.right(90)
    t.forward(230)
    t.left(45)
    t.right(135)
    t.forward(259)
    t.right(130)
    t.forward(142)
    t.end_fill()
    # wall
    t.fillcolor("tan")          # wall
    t.begin_fill()
    t.pendown()
    t.right(95)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.end_fill()
    t.penup()
    t.goto(180,-140)            # window 1  circle windows
    t.dot(30, "white")
    t.goto(260,-140)            # window 2
    t.dot(30, "white")
    t.goto(200,-200)
    t.fillcolor("brown")        # door
    t.begin_fill()
    t.pendown()
    t.right(90)
    t.forward(45)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(45)
    t.right(90)
    t.forward(75)
    t.end_fill()

    for i in range(50):	                                        # yellow flower loop
        x = random.randint(-500, 500)
        y = random.randint(-600, -280)
        t.up()
        t.goto(x, y)
        t.dot(20, "yellow")

    for i in range(40):	                                        # blue flower loop
        x = random.randint(-300, 200)
        y = random.randint(-600, -280)
        t.up()
        t.goto(x, y)
        t.dot(20, "light cyan")

    # flower
    t.up()      
    t.goto(x, y)
    t.dot(20)
house()
turtle.done()