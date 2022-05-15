import jieba
no=["False","None","True","and","as","assert","break","class","continue","def","del","elif","else","except","finally","for","from","global","if","import","inis","lambda","nonlocal","not","or","passraise","return","try","while","with","yield"]
def documentset(p):
    out=0
    try:
        txtx=open(p,"r",encoding='utf-8').read()
        txtx=txtx.lower()
    except:
        p=input("输入你要引用的文本文件,检查拼写！")
        try:
            txtx=open(p,"r",encoding='utf-8').read()
            txtx=txtx.lower()
        except:
            print("输出错误，即将跳转！")
            out="off"
    return txtx,out

def modset(mod):
    if mod=="2":
        q=[]
        off=0
        while off!="off":
            q.append(input("请选择你要查询的数组"))  #在查询中检测异常
            off=input("输入off以开始查询")
        print(q)
    else:
        q=no
    return q

def process(txtx,q):
    txt=jieba.lcut(txtx)
    counts={}
    for word in txt:
        if len(word)==1:
            continue
        else:
            counts[word]=counts.get(word,0)+1  
    items=[]
        
    for key in counts:
        if key in q:
            items.append([key,counts.get(key,0)])
    items.sort(key=lambda x:x[1],reverse=True)
    for i in items:
        print(i)
    # print("{0:<10}{1:>5}".format(key,counts.get(key,0)))
    else:
        0

def seeker_getdata():
    print("已被录入的文件：\n1.seg7.txt\n2.bar.txt\n3.hash.txt\n4.hamlet.txt")
    p=input("输入你要引用的文本文件")
    mod=input("请选择你要进行的查找模式：\n1.保留字查询\n2.自选字符查询\n(其他输入视为保留字查询)")
    return p,mod

def seeker():
    gettxt,mod=seeker_getdata()
    txtx,out=documentset(gettxt)
    if out!="off":
        q=modset(mod)
        process(txtx,q)



    
    