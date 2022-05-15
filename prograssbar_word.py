from ctypes import sizeof
from lib2to3.pgen2.literals import evalString
import turtle

from numpy import size
global x_pre,y_pre,schedule,summer
x_pre=0
y_pre=0
schedule=0

def initial1(sum1):
    global summer,schedule
    summer=sum1
    schedule=0

def strokes_str(size,color,speed,x_start,y_start,angle,long):   # Used to draw straight lines
    global summer,schedule, x_pre ,y_pre
    turtle.pensize(size)
    turtle.pencolor(color)
    turtle.speed(speed)
    turtle.penup()
    turtle.goto(x_start,y_start)
    turtle.pendown()
    turtle.seth(angle)
    for i in range(int(long/5)):
        turtle.forward(5)
        a=int(20/summer*(i+1)/long*5+schedule)*"#"
        b="."*int(20-int((i+1)/long*5*20/summer)-schedule)
        c=((i+1)/long*5)*100/summer+5*schedule
        print('\r {:^3.0f}%[{}->{}]'.format(c,a,b),end='')
    schedule=schedule+20/summer
    [x_pre,y_pre]=turtle.pos()

def strokes_cir(size,color,speed,x_start,y_start,angle,cir_rad,cir_angle): # Used to draw arcs
    global summer,schedule , x_pre,y_pre
    turtle.pensize(size)
    turtle.pencolor(color)
    turtle.speed(speed)
    turtle.penup()
    turtle.goto(x_start,y_start)
    turtle.pendown()
    turtle.seth(angle)
    for i in range(cir_angle):
        turtle.circle(cir_rad,1)
        a=int(schedule+(i+1)/cir_angle*20/summer)*"#"
        b="."*int(20-schedule-(i+1)/cir_angle*20/summer)
        c=((i+1)/cir_angle)*100/summer+5*schedule
        print("\r {:^3.0f}%[{}->{}]".format(c,a,b),end='')
    schedule=schedule+20/summer
    [x_pre,y_pre]=turtle.pos()

def barIntro():
    turtle.setup(1300,800,0,0)
    turtle,turtle.hideturtle()
    print("欢迎来到文字进度条程序！")

def get_sum(): 
    try:
        pennum=eval(input("您要写几笔?"))
    except NameError:
        print("输入的不是数字！请重新填写")
        try:
            pennum=eval(input("您要写几笔?(请用阿拉伯数字作答)"))
        except NameError:
            print("两次输入错误，默认1笔！")
            pennum=1
    except :
        print("两次输入错误，默认1笔！")
        pennum=1
    return pennum

def sizeset():
    try:
        size=int(eval(input("请输入画笔尺寸")))
    except NameError:
        try:
            size=int(eval(input("请输入画笔尺寸(阿拉伯数字)")))
        except:
            print("输入错误,设置为默认值") 
            size =30
    return size  

def colorset():
    color=input("请输入画笔颜色")
    try:
        turtle.pencolor(color)
    except:
        color=input("请输入画笔颜色(检查拼写！)")
        try:
            turtle.pencolor(color)
        except:
            print("本程序禁止三岁以下儿童游玩，请好好补习英语")
            color="red"
    return color

def speedset():
    try:
        speed=int(eval(input("请输入画笔速度")))
    except NameError:
        try:
           speed=int(eval(input("请输入画笔速度")))
        except:
            print("输入错误,设置为默认值")
            speed=60
    except:
        speed=60
    return speed

def modeset(set,s,c,spd):
    while(set=="1" or set=="2" or set=="3"):
        set=input("是否要对以下项目进行修改?\n1.画笔尺寸(默认30)\n2.画笔颜色(默认红色)\n3.画笔速度(默认60)\n4.其他输入为默认\n(当你更改默认设置后，随后的笔画也会相应改变)")
        if set=="1":
            size=sizeset()
            s=size                        
        elif set=="2":
            color=colorset()
            c=color
        elif set=="3":
            speed=speedset()
            spd=speed
        else:
            size=int(s)
            color=c
            speed=int(spd)
    return int(size),color,int(speed)

def startset():
    global x_pre,y_pre
    try:
        start_x=int(eval(input("请输入画笔起点横坐标(接续上一笔请输入x_pre)")))
        start_y=int(eval(input("请输入画笔起点纵坐标(接续上一笔请输入y_pre)")))
    except NameError:
        try:
            start_x=int(eval(input("请输入画笔起点横坐标(接续上一笔请输入x_pre)")))
            start_y=int(eval(input("请输入画笔起点纵坐标(接续上一笔请输入y_pre)")))
        except:
            print("输入错误，默认为接续上一笔")
            start_x=int(x_pre)
            start_y=int(y_pre)
    except:
        print("输入错误，默认为接续上一笔")
        start_x=int(x_pre)
        start_y=int(y_pre)
    return start_x,start_y

def oriset():
    try:    
        ori=int(eval(input("请输入画笔朝向(以东为0度,顺时针方向)")))
    except NameError:
        try:
            ori=int(eval(input("请输入画笔朝向(以东为0度,顺时针方向)"))) 
        except:
            print("两次设置错误,默认为向东")
            ori=0
    return ori

def drawer(a,b,c,d,e,f,g,h,j):
        if d=="C" or d=="c":
            strokes_cir(a,b,c,e,f,g,h,j)
        else:
            strokes_str(a,b,c,e,f,g,h)

def loader(a,b,c,d,e,f,g):
    if d=="C" or d=="c":
        h=int(input("请输入画笔半径(顺时针做弧半径为负)"))
        j=int(input("请输入画笔转过角度"))
        print("预装载中,请稍后")
        strokes_cir(a,"white",c,e,f,g,h,j)
        print(turtle.pos())
    else:
        h=int(input("请输入笔画长度"))
        j=0
        print("预装载中,请稍后")
        strokes_str(a,"white",c,e,f,g,h)
        print("当前位置",turtle.pos())
    return h,j


def bar():
    global summer, x_pre ,y_pre,schedule
    barIntro()
    inter=input("是否开始绘制?\n1.是\n2.啊不对我选错了")
    if inter=="1":
        pennum=get_sum()
        initial1(int(pennum))
        a={}
        b={}
        c={}
        d={}
        e={}
        f={}
        g={}
        h={}
        j={}
        pennum=int(pennum)
        color="red"
        size=30
        speed=60
        for i in range(pennum):
            print("\n新的笔画!")
            set="1"
            a[i],b[i],c[i]=modeset(set,size,color,speed)
            size=a[i]
            color=b[i]
            speed=c[i]
            d[i]=input("请输入要画的是曲线(C)还是直线(S)(输入错误默认为直线)")
            e[i],f[i]=startset()
            g[i]=oriset()
            h[i],j[i]=loader(a[i],b[i],c[i],d[i],e[i],f[i],g[i])
        start=input("\n开始绘制?(任意输入以开始绘图)")
        turtle.clear()
        schedule=0
        for i in range(pennum):
            drawer(a[i],b[i],c[i],d[i],e[i],f[i],g[i],h[i],j[i])
    else:
        0
