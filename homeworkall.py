import head

password="jondler"

def run():
    print("欢迎来到“The world of wrcf”,选择你要进入的程序吧！祝您玩得愉快！")
    mode="1"
    while(mode!="turnoff"):
        mode=input("请选择你要开启的程序:\n    1.哈希函数 \n    2.文字进度条\n    3.七段数码管显示\n    4.文本查询\n    5.比赛预测\n    6.获取URL\n    7.语法检查器\n    8.敬请期待")        
        if mode=="1":
            head.hash_run()
        elif mode=="2":
            head.prograssbar_word_run()
            head.turtle_run()
        elif mode=="3":
            head.seg7_run()  
            head.turtle_run()
        elif mode=="4":
            head.seeker_run() 
        elif mode=="5":
            head.matchAnalysis_run()
        elif mode=="6":
            head.url_run()
        elif mode=="7" :
            head.compiler_run()   
        else:
            print("我们仍在开发新的功能，敬请期待")
        choose=input("\n是否继续游玩?Y/N （其他输入视为继续参观）")
        if choose=="Y":
                0
        elif choose=="N" or choose=="n*":
                mode="turnoff"
        else:
                0
    print("感谢您的赏玩，祝您心情愉快！")
    


if __name__ == '__main__':
    user=input("请输入密码(忘记密码请输入“1895”)")
    while user!="1895" and user!=password:
        user=input("输入错误，请重试")
    run()


