import turtle
colors=['black','silver','grey']
colorss=['silver','grey','black']
draw=turtle.Pen()
turtle.bgcolor('white')
draw.speed(1000)

for a in range(500):
    draw.pencolor(colors[a%3])
    draw.width(a/100+2)
    draw.forward(a)
    draw.left(-180)
    draw.right(30)

draw.hideturtle()
