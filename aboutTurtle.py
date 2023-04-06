import turtle

s = turtle.Screen()
s.bgcolor('orange')
# s.bgpic('mario.png')
s.register_shape('strawberry.gif')

p = turtle.Pen()
p.pensize(2)
p.pencolor("cyan")
p.fillcolor("red")
p.seth(45)
p.ht()
p.begin_fill()
for i in range(10):
    p.fd(2)
    p.rt(6)
print(p.heading())
# p.seth(85)
for i in range(18):
    p.fd(2)
    p.rt(6)

for i in range(25):
    p.fd(2.12)
p.penup()
p.home()
p.showturtle()


p.seth(140)
# p.ht()
p.pendown()
for i in range(10):
    p.fd(2)
    p.lt(6)
print(p.heading())
# # p.seth(85)
for i in range(18):
    p.fd(2)
    p.lt(6)

for i in range(25):
    p.fd(2.12)

p.end_fill()


# shapes: 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'.
# p.shape('turtle')
# p.shape('strawberry.gif')

# p.penup()
# p.goto(100, 100)
# p.stamp()

# p.shape('turtle')
# p.home()
# p.shapesize(3)
# p.pencolor('red')
# p.pensize(4)

# p.forward(100)
# p.left(120)

# p.forward(100)
# p.left(120)

# p.forward(100)
# p.left(120)

s.exitonclick()
# exercise : کشیدن مربع، پنجضلعی و شش ضلعی
