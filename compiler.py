from mailbox import NoSuchMailboxError
import jieba
no=["False","None","True","and","as","assert","break","class","continue","def","del","elif","else","except","finally","for","from","global","if","import","inis","lambda","nonlocal","not","or","passraise","return","try","while","with","yield"]
space_try=['0','0','0','0','0','0','0','0','0']
space_except=['0','0','0','0','0','0','0','0','0']
set_try=['0','0','0','0','0','0','0','0','0']
space_if=['0','0','0','0','0','0','0','0','0']
space_elif=['0','0','0','0','0','0','0','0','0']
space_else=['0','0','0','0','0','0','0','0','0']
set_if=['0','0','0','0','0','0','0','0','0']
set_elif=['0','0','0','0','0','0','0','0','0']
set_space = [0]

def documentset():   #待检测文件的输入
    try:
        p=input("语法检查器，输入你要引用的文本文件(内置correct.txt)")
        txtx=open(p,"r",encoding='utf-8').read()
        txtline=open(p,"r",encoding='utf-8').readlines()
        txtx=txtx.lower()
    except:
        p=input("输入你要引用的文本文件,检查拼写！")
        try:
            txtline=open(p,"r",encoding='utf-8').read()
            txtx=txtx.lower()
        except:
            print("默认为correct.txt")
            txtline=open("correct.txt","r",encoding='utf-8').readlines()
    return txtline


def process_find(lines): # 查找到的错误在哪一行
    for i in range(len(lines)):
        out=process(lines[i],i+1)
        if out!=0:
            print("line",' ',1+i,"have",out,"mistake(s)\n")
        
            
def process(txtx,line):   #将一句文本拆分为一个个词并做词频统计
    txt=jieba.lcut(txtx)
    out=0
    counts={}
    for word in txt:
        if len(word)==0 or word==' ':
            continue
        else:
            counts[word]=counts.get(word,0)+1  
    out=analysis(counts,txt,line)
    return out

def analysis(counts,txt,line):   #语法解析器，分析是否含有待检测成分
    out=0
    space=int(number(txt)/4)
    if space < set_space[0] and txt != ['\n']:
        out=out+check_before(space,line)
    set_space[0]=space
    for key in counts:
        if key == 'if' :
            out=out+check_matchif(space,line)    #检查if与else/elif的匹配情况
            out=out+correct_if(txt)    #检查if语句错误
        if key == 'while' :
            out=out+correct_while(txt,counts)   #检查while语句错误数目
        if key == 'def':
            out=out+correct_def(txt)   #检查def语句错误数目
        if key =='try' :
            out=out+check_matchtry(space,line)    #检查try与except的配对情况
            out=out+correct_try(txt)    #检查try语句错误数目
        if key == 'except':
            out=out+check_matchexcept(space,line)    #检查except与try的匹配情况
            out=out+correct_except(txt)    #检查except语句错误
        if key == 'elif':
            out=out+check_matchelif(space,line)    #检查elif的匹配情况
            out=out+missing_wrong(txt,'elif')    #检查elif语句错误数目
            out=out+check_head(txt,'elif')
        if key == 'else':
            if 'if' in txt:
                print("special else")    #特殊形式else的检验
            else:
                out=out+check_matchelse(space,line)    #检查普通else的匹配
                out=out+missing_wrong(txt,'else')    #检查else语句错误数目
                out=out+check_head(txt,'else')
    return out    #总错误数目

def check_head(txt,kind):    #检测关键词前是否有别的乱码
    for word in txt:
        if word==' ':
            continue
        else:
            if word!=kind:
                print("wrong",kind,": something before",kind)
                return 1
            else:
                return 0

def number(txt):    #对空格数量计数
    i=0
    for word in txt:
        if word==' ':
            i=i+1 
        else:
            break
    return i    

def check_before(number,line):
    out=0
    if space_try[number+1]!='1':
        out=out+0
    else :
        if space_except[number+1]=='1':
            out=out+0
        else :
            print("wrong_try: in line",set_try[number+1],"without except")
            out=out+1
    if space_elif[number+1]!='0':
        if  space_else[number+1]=='0':
            print("wrong_elif: in line",set_elif[number+1],"without else")
            out=1
    space_try[number+1]='0'
    space_except[number+1]='0'
    set_try[number+1]='0'
    space_if[number+1]='0'
    space_elif[number+1]='0'
    space_else[number+1]='0'
    set_if[number+1]='0'
    set_elif[number+1]='0'
    return out

def check_matchtry(number,line):   #查找是否有对应的try——except链
    if space_try[number]!='1':
        space_try[number]='1'
        set_try[number]=line
        return 0
    else :
        if space_except[number]=='1':
            space_try[number]='1'
            space_except[number]='0'
            set_try[number]=line
            return 0
        else :
            #print("wrong_try: in line",set_try[number],"without except")
            set_try[number]=line
            space_try[number]='1'
            space_except[number]='0'
            return 0

def check_matchexcept(number,line):  
    if space_try[number]!='1':
        print("wrong_except: no try match it")
        return 1
    else :
        space_except[number]='1'
        return 0

def check_matchif(number,line):    #if 的配对情况检查
    out=0
    space_if[number]='1'
    if space_elif[number]!='0' and space_else[number]=='0':
        print("wrong_elif: in line",set_elif[number],"without else")
        out=1
    space_elif[number]='0'
    space_else[number]='0'
    set_if[number]=line
    return out

def check_matchelif(number,line):
    if space_if[number]=='1':
        space_elif[number]='1'
        set_elif[number]=line
        return 0
    else :
        print("wrong_elif: without if")
        set_elif[number]=line
        space_elif[number]='1'
        return 1

def check_matchelse(number,line):
    out=0
    if space_if[number]=='0':
        print("wrong_else: without if")
        out=1
        if space_elif[number]!='0':
            print("wrong elif: in line",line,"without if")
            out=0
    space_else[number]='1'
    space_if[number]='0'
    return out

def correct_if(ifer):   #if的检测程序
    out = 0
    if 'else' in ifer:
        print('special_if')
        out=0
    else:
        out=out+check_head(ifer,'if')
        out=out+missing_wrong(ifer,"if")
    return out

def correct_while(ifer,counts):    #while的检测程序
    out=0
    if counts.get('=',0) == 1 and counts.get('>',0)==0 and counts.get('<',0)==0 and counts.get('!',0)==0:
        print("warning_while:check if there shoule be one '=' or two")
        out=1
    out=out+missing_wrong(ifer,"while")
    out=out+check_head(ifer,'while')
    return out

def correct_def(ifer):   #def的检测程序
    counter_right=0
    counter_left=0
    out=0
    for i in range(len(ifer)):
        if ifer[i]=='(':
            counter_left='get1'
        if ifer[i]==')':
            if counter_left!='get1':
                print("worng_def: one ')' is missing (' ")
                out=out+1
            else :
                counter_right = 'get3'
            if i<=len(ifer)-3:
                if counter_left == 'get1' and (i == len(ifer)-3 or ifer[i+1]==':'):
                    counter_right='get2'       
    if counter_right != 'get2':
        if counter_right =='get3':
            print("wrong_def : '()' in wrong position")
            out=out+1
        else:
            print("wrong_def : lose '()'")
            out=out+1
    out=out+missing_wrong(ifer,"def") 
    out=out+check_head(ifer,'def')  
    return out 

def correct_try(ifer):   
    out=0
    out=out+missing_wrong(ifer,"try")
    out=out+check_head(ifer,'try')
    return out

def correct_except(ifer):
    out=0
    out=out+missing_wrong(ifer,"except")
    out=out+check_head(ifer,'except')
    return out

def missing_wrong(ifer,kind):   #对':'的检查
    txt=[]
    for word in ifer:
        if word==' ':
            continue
        else :
            txt.append(word)
    for i in range(len(txt)-1):
        if txt[i]==':' : 
            if i==len(txt)-2 or txt[1+i]=='#':
                return 0 
            else:
                print("wrong:",kind, "':' in wrong position")
                return 1
    print("wrong",kind,": ':' is missing")
    return 1   

def compiler():   #主程序
    getline=documentset()
    process_find(getline)

if __name__ == '__main__':
    compiler()
    


    
    