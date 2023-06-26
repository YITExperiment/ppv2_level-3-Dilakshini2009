import turtle

from itertools import cycle
color = cycle(['red','orange','yellow','green','blue','purple'])

def draw_circle(size,angle,shift):
    turtle.bgcolor(next(color))
    turtle.pencolor(next(color))
    turtle.circle(size+10)
    turtle.right(angle+10)
    turtle.forward(shift+1)
    draw_circle(size+5,angle+1,shift+1)
    
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(10)
draw_circle(30,0,1)


