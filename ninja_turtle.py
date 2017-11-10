import turtle

window = turtle.Screen()
window.bgcolor("white")

ninja = turtle.Turtle()
ninja.shape("turtle")
ninja.speed(20)
# colors are taken from tk color list
ninja.color("DarkSalmon", "cornflower blue")

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(2)

# ninja.done()
window.exitonclick()
