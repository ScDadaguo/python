import re
import urllib.request
import time
import urllib.error
import urllib.request
import threading

def use_proxy(url):
    # 建立异常处理机制
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400')
        # proxy=urllib.request.ProxyHandler({'http':proxy_addr})
        # opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        data=urllib.request.urlopen(req).read().decode("utf-8","ignore")
        return data
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        # 若为URLErroe异常，延时10秒执行
        time.sleep(10)
    except Exception as e:
        # 若为Exception异常，延时1秒执行
        time.sleep(1)


class A(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(1,10,2):
                thispageurl="https://www.qiushibaike.com/8hr/page/"+str(i)
                thispagedata = use_proxy(thispageurl)
                pat='<div class="content">(.*?)</span>'
                rs1 = re.compile(pat,re.S).findall(str(thispagedata))
                for j in range(0,len(rs1)):
                    rs1[j]=rs1[j].replace('\n<span>\n\n\n','')
                    rs1[j]=rs1[j].encode('utf-8')
                    file="C:/Users\dadaguo\Desktop/多线程爬虫/第"+str(i)+"页第"+str(j)+"篇文章.text"
                    fh = open(file,"wb")
                    fh.write(rs1[j])
                    fh.close()

class B(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(2,10,2):
                thispageurl="https://www.qiushibaike.com/8hr/page/"+str(i)
                thispagedata = use_proxy(thispageurl)
                pat='<div class="content">(.*?)</span>'
                rs1 = re.compile(pat,re.S).findall(str(thispagedata))
                for j in range(0,len(rs1)):
                    rs1[j]=rs1[j].replace('\n<span>\n\n\n','')
                    rs1[j]=rs1[j].encode('utf-8')
                    file="C:/Users\dadaguo\Desktop/多线程爬虫/第"+str(i)+"页第"+str(j)+"篇文章.text"
                    fh = open(file,"wb")
                    fh.write(rs1[j])
                    fh.close()
a=A()
a.start()
b=B()
b.start()
