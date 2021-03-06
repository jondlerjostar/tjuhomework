from ast import Num
from re import I
import turtle,datetime

from prograssbar_word import initial1#引用

global long, color , script

def drawLine(draw):#绘制单段数码管
    global long,color
    long=int(long)
    turtle.fd(10*long)
    if draw:
        turtle.color(color)
        turtle.pensize(7*long)
        turtle.pendown()
        turtle.fd(40*long)
        turtle.left(45)
        turtle.fd(5*long)
        turtle.left(90)
        turtle.fd(5*long)
        turtle.left(45)
        turtle.fd(40*long)
        turtle.left(45)
        turtle.fd(5*long)
        turtle.left(90)
        turtle.fd(5*long)
        turtle.left(45)
        turtle.penup()

    else:
        turtle.color("grey")
        turtle.pensize(1)
        turtle.right(90)
        turtle.fd(3.5*long)
        turtle.left(90)
        turtle.pendown()
        turtle.fd(40*long)
        turtle.left(45)
        turtle.fd(8.45*long)
        turtle.left(90)
        turtle.fd(8.45*long)
        turtle.left(45)
        turtle.fd(40*long)
        turtle.left(45)
        turtle.fd(8.45*long)
        turtle.left(90)
        turtle.fd(8.45*long)
        turtle.left(45)
        turtle.penup()
        turtle.left(90)
        turtle.fd(3.5*long)
        turtle.right(90) 
    turtle.fd(50*long)
    turtle.right(90)

def drawDigit(d):#根据数字绘制七段数码管，True或False决定是否抬起画笔
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(40*long)

def drawDate(date):#设置具体的格式
    global color , script, long
    turtle.pencolor(color)#字体的颜色
    for i in date:
        if i == '-':
            turtle.write('年',font=(script,18,"normal"))#设置字体，大小
            turtle.fd(40*long)
        elif i == '=':
            turtle.write('月',font=(script,18,"normal"))
            turtle.fd(40*long)
        elif i == '+':
            turtle.write('日',font=(script,18,"normal"))
        else:
            drawDigit(eval(i))

def drawNum(date):#设置具体的格式
    global long , script ,color
    for i in date:
        turtle.pencolor(color)#字体的颜色
        try:
            drawDigit(eval(i))
        except NameError:
            turtle.write(i,font=(script,18,"normal"))
            turtle.fd(40*int(long))
        except:
            print("输入错误，请检查你的输入情况(不应当包含字母、数字、汉字外的符号)")
            print("请重新进入系统，非常抱歉")

def initial_seg7():   #程序初始化
    turtle.setup(8000,3500,200,200)#显示窗体的大小
    turtle.speed(5000000000000000000)
    turtle.penup()
    turtle.hideturtle()
    turtle.fd(-350)

def totalset(mode):   #对于绘制颜色尺寸等的总设置
    long=1
    color="red"
    script="Arial"
    while(mode!="4"):
            mode= input("是否修改以下数值:1.颜色（默认红色） 2.尺寸(默认为1) 3.汉字字体(默认“Arial”) 4. 无需设置")
            if mode=="1":
                color=colorset()                        
            elif mode=="2":
                long=input("输入你需求的尺寸：")
            elif mode=="3":
                script=scriptset()
            else:
                0 
    return color ,long, script

def colorset():    #颜色设置子函数
    tip_a=input("输入你想要的颜色:1.绿色 2.蓝色 3.黑色 4.紫色")
    if tip_a=="1":
        color="green"
    elif tip_a=="2":
        color="blue"
    elif tip_a=="3":
        color="black"
    elif tip_a=="4":
        color="purple"
    else:
        print("超出设置范围，设置为默认红色")
        color="red"
    return color

def scriptset():    #字体设置子函数
    tip_c=input("输入你想要的颜色:1.微软雅黑 2.宋体 3.楷体 4.verdana")
    if tip_c=="1":
        script="Mircosoft Yahei"
    elif tip_c=="2":
        script="宋体"
    elif tip_c=="3":
        script="楷体"
    elif tip_c=="4":
        script="verdana"
    else:
        print("超出设置范围,设置为默认Arial")
        script="Arial"
    return script 

def modeselect(work):   #模式设置子函数
    if work=="1":
        drawDate(datetime.datetime.now().strftime('%Y-%m=%d+'))#日期的读取方式，便于控制输出的顺序（年，月，日）
    elif work=="2":
        num=input("请任意输入字符串：")
        drawNum(num)
    else:
        print("输入错误，进入自定义输入模式！")
        drawNum(num)

def seg7():   #函数主体
    global long, color , script
    initial_seg7()
    long=1
    color="red"
    script="Arial"
    mode=1
    inter=input("是否开始编辑?\n1.是\n2.啊不对我选错了")
    if inter=="1":
        color,long,script=totalset(mode)
        print("设置完成！欢迎来到七段管程序!")
        work=input("请选择想要进入的模式:1.时间查询 2. 自定义输入")
        modeselect(work)
    else:
        0

if __name__ == '__main__':
    seg7()