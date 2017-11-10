import turtle
from math import sin,cos,pi

def ellipse(pen, x, y, width, height):
    pen.penup()
    pen.goto(x + width / 2, height)
    pen.pendown()
    penX, penY = pen.pos()
    for i in range(0, 360):
        penX += cos(i*pi/180)*width/180
        penY += sin(i*pi/180)*height/180
        pen.goto(penX, penY)
    pen.penup()

def draw_square(some_turtle):
    for x in xrange(0,4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for x in xrange(0,3):
        some_turtle.forward(200)
        some_turtle.left(120)
    # some_turtle.goto(-250, 0)
    # some_turtle.goto(0,250)
    # some_turtle.goto(0,0)

def ninja_star(ninja, length):
    for i in range(180):
        ninja.forward(length)
        ninja.right(30)
        ninja.forward(20)
        ninja.left(60)
        ninja.forward(50)
        ninja.right(30)
        ninja.penup()
        ninja.setposition(0, 0)
        ninja.pendown()
        ninja.right(2)

def ninja_grass(ninja, pos_x, pos_y):
    for i in xrange(15):
        ninja.forward(40)
        ninja.left(20)
        ninja.forward(30)
        ninja.right(35)
        ninja.forward(15)
        ninja.penup()
        ninja.setposition(pos_x, pos_y)
        ninja.pendown()
        ninja.left(27)

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
           koch(t, order-1, size/3)
           t.left(angle)

def sierpinski_triangle(turtle_object, order, size):
    if order is 0:
        for x in xrange(0, 3):
            turtle_object.forward(size)
            turtle_object.left(120)
    else:
        sierpinski_triangle(turtle_object, order-1, size/2)
        turtle_object.forward(size/2)
        sierpinski_triangle(turtle_object, order-1, size/2)
        turtle_object.backward(size/2)
        turtle_object.left(60)
        turtle_object.forward(size/2)
        turtle_object.right(60)
        sierpinski_triangle(turtle_object, order-1, size/2)
        turtle_object.left(60)
        turtle_object.backward(size/2)
        turtle_object.right(60)


def turtle_art():
    window = turtle.Screen()
    window.bgcolor("red")

    turtleImg = turtle.Turtle()
    turtleImg.shape("turtle")
    turtleImg.color("yellow")
    turtleImg.speed(50)

    secondTurtle = turtle.Turtle()
    secondTurtle.shape("arrow")
    secondTurtle.color("brown")
    secondTurtle.fillcolor("brown")
    secondTurtle.pensize(2)
    secondTurtle.speed(50)

    thirdTurtle = turtle.Turtle()
    thirdTurtle.shape("triangle")
    thirdTurtle.color("green")
    thirdTurtle.pensize(5)
    thirdTurtle.speed(50)

    # turtleImg.penup()
    # turtleImg.setposition(100, 100)
    # turtleImg.pendown()

    # for x in xrange(0, 6):
    #     koch(turtleImg, order=3, size=120)
    #     turtleImg.right(60)

    # secondTurtle.penup()
    # secondTurtle.setposition(-150, -150)
    # secondTurtle.pendown()

    # sierpinski_triangle(secondTurtle, order=3, size=150)
    # for x in xrange(0,36):
    #     draw_square(turtleImg)
    #     turtleImg.right(10)
    # secondTurtle.circle(100)

    # for x in xrange(0,36):
    #     draw_triangle(thirdTurtle)
    #     thirdTurtle.right(10)
    # thirdTurtle.goto(0,-300)

    # secondTurtle.goto(0, -100)
    # secondTurtle.circle(100)
    # secondTurtle.goto(0, 0)
    # secondTurtle.fill(True)

    # thirdTurtle.begin_fill()
    # draw_triangle(thirdTurtle)
    # thirdTurtle.end_fill()

    ninja_star(turtleImg, 100)
    ninja_star(secondTurtle, 40)

    # for x in xrange(0, 72):
    #     secondTurtle.circle(50)
    #     secondTurtle.right(5)

    third_x = 0
    third_y = -350
    thirdTurtle.goto(third_x, third_y)
    ninja_grass(thirdTurtle, third_x, third_y)

    secondTurtle.penup()
    thirdTurtle.penup()

    window.exitonclick()


if __name__ == "__main__":
    turtle_art()
