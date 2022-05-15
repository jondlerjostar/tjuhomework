
import hashlib,string,random

def encryption(password,salt_long):  #used to create password
    time=0
    salts=''

    while time < salt_long :
        salt_one = random.choice(string.digits)
        salt_two = random.choice(string.ascii_letters)
        salt = random.choice([salt_one,salt_two])
        salts += salt
        time=time+1

    password_salt=password+salts
    m=hashlib.md5(b'salts')
    m.update(password_salt.encode())
    result=m.hexdigest()
    return([password_salt,result])

def encryption_mine(password,salt_long):  #used to create password
    time=0
    salts=''

    while time < salt_long :
        salt_one = random.choice(string.digits)
        salt_two = random.choice(string.ascii_letters)
        salt = random.choice([salt_one,salt_two])
        salts += salt
        time=time+1

    password_salt=password+salts
    result=password_salt[::-1]
    return([password_salt,result])
    
def hashIntro():
    print("欢迎来到哈希函数程序！")

def hashgetdata():
    password=input("请输入您要加密的字符串")
    try:
        num=int(eval(input("请输入您需求的加密段位数")))
    except NameError:
        try:
            num=int(eval(input("请输入您需求的加密段位数")))
        except:
            print("两次输入错误,位数设置为10")
            num=10
            pin="1"
    except:
        print("输入错误，位数设置为10")
        pin="1"
        num=10
    return password,num,pin

def hash():
    hashIntro()
    inter=input("是否开始加密?\n1.是\n2.啊不对我选错了")
    pin="1"
    if inter=="1":
        password,num,pin=hashgetdata()
        if pin!="off":                
            [password_beforeenc,password_afterenc]=encryption_mine(password,num)
            print(password_afterenc)
            print(password_beforeenc)        
    else:
        0

hash()

