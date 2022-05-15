from random import random
def printintro():
    print('这个程序模拟两个选手A和B的某种竞技比赛')
    print('程序运行需要A和B的能力值（以0到1之间的小数表示）')
 
def  getinput():
    try:
        a=eval(input('请输入选手A的能力值(0-1):'))
        if not 0<=a<=1:
            raise NameError
    except NameError:
        print("能力设置失败，重置为0.5")
        a=0.5
    try:
        aweather=eval(input("为队伍A指定一种作战天气（1晴天 2雨天 3大风 4 阴天 其他为无特长）"))
    except NameError:
        print("设置失败，队伍无特长")
        aweather=0
    try:
        b=eval(input('请输入选手B的能力值(0-1):'))
        if not 0<=b<=1:
            raise NameError
    except NameError:
        print("能力设置失败，重置为0.5")
        b=0.5       
    try:
        bweather=eval(input("为队伍B指定一种作战天气（1晴天 2雨天 3大风 4 阴天）"))
    except NameError:
        print("设置失败，队伍无特长")
    n=eval(input('输入模拟比赛场次(正整数):'))
    return a,aweather,b,bweather,n
 
def simNgames(n,pa,wa,pb,wb):
    wina,winb=0,0
    weather_now=simweather()
    if weather_now==wa:
        print("A队占据天气优势")
    elif weather_now==wb:
        print("B队占据天气优势")
    else:
        print("今日天气对两支队伍均是挑战")
    for i in range(n):
        sa,sb=simonegame(pa,pb,wa,wb,weather_now)
        if sa>sb:
            wina+=1
        else:
            winb+=1
    return wina,winb
 
def gameover(a,b):
    return a==15 or b==15

def simweather():
    weather=random()
    weathernow=0
    if 0<=weather<0.25:
        weathernow=1
        print("今日天晴")
    elif 0.25<=weather<0.5:
        weathernow=2
        print("今日雨天")
    elif 0.5<=weather<0.75:
        weathernow=3
        print("今日大风")
    elif 0.75<weather<=1:
        weathernow=4   
        print("今日阴天") 
    return weathernow

def performance(p,w,now):
    prob=0
    if now==w:
        prob=0.6*p+0.05+0.3*(0.5-random())
    else :
        prob=0.6*p+0.3*(0.5-random())
    return prob

def simonegame(pa,pb,wa,wb,weather_now):
    sa,sb=0,0
    serving='A'
    while not gameover(sa,sb):
        if serving=='A':
            if random()<performance(pa,wa,weather_now):
                sa+=1
            else:
                serving='B'
        else:
            if random()<performance(pb,wb,weather_now):
                sb+=1
            else:
                serving='A'
    return sa,sb
 
def printsummary(wina,winb):
    n=wina+winb
    print('竞技分析开始，共模拟{}场比赛'.format(n))
    print('选手A获胜{}场比赛，占比{:0.1%}'.format(wina,wina/n))
    print('选手B获胜{}场比赛，占比{:0.1%}'.format(winb,winb/n))
 
def matchAnalysis():
    printintro()
    proba,weathera,probb,weatherb,n=getinput()
    wina,winb=simNgames(n,proba,weathera,probb,weatherb)
    printsummary(wina,winb)

