import turtle
global x_pre,y_pre
x_pre=0
y_pre=0

def strokes_str(size,color,x_start,y_start,angle,long):   # Used to draw straight lines
    turtle.pensize(size)
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(x_start,y_start)
    turtle.pendown()
    turtle.seth(angle)
    turtle.forward(long)
    [x_pre,y_pre]=turtle.pos()

def strokes_cir(size,color,x_start,y_start,angle,cir_rad,cir_angle): # Used to draw arcs
    turtle.pensize(size)
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(x_start,y_start)
    turtle.pendown()
    turtle.seth(angle)
    turtle.circle(cir_rad,cir_angle)
    [x_pre,y_pre]=turtle.pos()

def write():
    turtle.setup(1300,800,0,0)
    strokes_str(40,"red",-120,0,0,240)
    strokes_str(40,"red",0,80,270,80)
    strokes_cir(40,"red",x_pre,y_pre,270,-120,90)
    strokes_cir(40,"red",0,0,270,120,90)
