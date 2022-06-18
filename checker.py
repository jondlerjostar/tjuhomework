import pyflakes
import os
from sympy import python



def documentset():   #待检测文件的输入
    try:
        p=input("语法检查器，输入你要引用的文本文件(内置correct.txt)")
        txtx=open(p,"r",encoding='utf-8').read()
        txtline=open(p,"r",encoding='utf-8').readlines()
    except:
        p=input("输入你要引用的文本文件,检查拼写！")
        try:
            txtline=open(p,"r",encoding='utf-8').read()
        except:
            print("默认为correct.txt")
            txtline=open("correct.txt","r",encoding='utf-8').readlines()
    return p
   

def checker():   #主程序
    getline=documentset()
    p="Flake8 "+"correct.py"
    os.system(p)

if __name__ == '__main__':
    checker()