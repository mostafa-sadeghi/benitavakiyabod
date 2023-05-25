import turtle

screen = turtle.Screen()
pen = turtle.Pen()
pen.pensize(4)
COLORS = ("red", "green", "blue", "cyan", "magenta")
for i in range(5):
    pen.pencolor(COLORS[i])
    pen.forward(100)
    pen.right(144)


turtle.done()
