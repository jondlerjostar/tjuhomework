import requests
from urlextract import URLExtract  #一个可以直接从源代码提取链接的库

def getor_URL():
    try:
        url=input("输入网址")
    except:
        print("输入不合法，默认百度")
        url="http://www.baidu.com"
    return url



def getHTMLText(url):  #获取一个页面所有源代码的函数
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status() #如果状态不是200，引发异常
        r.encoding = 'utf-8' #无论原来用什么编码，都改成utf-8
        return r.text
    except:
        print("")
        url="http://www.baidu.com"
        r = requests.get(url, timeout=30)
        r.raise_for_status() #如果状态不是200，引发异常
        r.encoding = 'utf-8' #无论原来用什么编码，都改成utf-8
        return r.text

def getURL(text):   #从打印的文本中获得链接并储存到表格urls中
    extractor = URLExtract()
    urls = extractor.find_urls(text)  
    if len(urls)!=0:
        print(urls)
    return urls

def getnURL(urln):   #建立递归函数
    for i in range(len(urln)):
        newtext = getHTMLText(urln[i])
        if outer()!="y":
            0
        else:
            break
        getnURL(getURL(newtext))
        

def outer():
    out=input("返回上一层？(输入y以返回)") 
    return out

def url():
    url = getor_URL()
    text = getHTMLText(url)
    urls = getURL(text)
    getnURL(urls)

if __name__ == '__main__':
    url()