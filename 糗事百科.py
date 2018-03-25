#http://weixin.sogou.com/
import re
import urllib.request
import time
import urllib.error
import urllib.request
from lxml import etree

#自定义函数，功能为使用代理服务器爬一个网址
def use_proxy(url):
    #建立异常处理机制
    try:
        req=urllib.request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400')
        # proxy=urllib.request.ProxyHandler({'http':proxy_addr})
        # opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        data=urllib.request.urlopen(req).read()
        return data
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        #若为URLErroe异常，延时10秒执行
        time.sleep(10)
    except Exception as e:
        #若为Exception异常，延时1秒执行
        time.sleep(1)
#设置关键词
key="郭浩"
#设置代理服务器
#proxy="120.79.217.139:6666"
#爬多少页
for i in range(1,2):
    #key=urllib.request.quote(key)
    # print (key)
    thispageurl="https://www.qiushibaike.com/8hr/page/"+str(i)
    thispagedata=use_proxy(thispageurl)


    # print(len(str(thispagedata)))
    # rs1=re.compile(pat1,re.S).findall(str(thispagedata))
    # thisdata = use_proxy(rs1)
    seletor=etree.HTML(thispagedata)

    #//*[@id="qiushi_tag_120071044"]
    url=seletor.xpath('//a[@class="contentHerf"]/@href')
    print(url)
    print (len(url))
    for j in range (0,len(url)):
        url[j]="https://www.qiushibaike.com"+url[j]
        data=use_proxy(url[j])
        seletor1 = etree.HTML(data)
        duanzi=seletor1.xpath('//div[@class="content"]/text()')
        duanzi=''.join(duanzi)#列表 ——》字符串
        duanzi=duanzi.replace('\n','')
        print(duanzi)
        print("----------------------------------------------")
        with open("糗事百科.txt","a") as f:
            f.write(duanzi)
            f.write("\n")
            f.write("------------------------------")
            f.write("\n")


    # file = "C:/Users/dadaguo/Desktop/糗事百科/第" + str(i) + "篇文章.txt"
    # with open(file,'w') as fh:
    #     fh.write('第{}页段子'.format(i))
    # for text in texts:
    #     try:
    #         text=text.replace('\n','')
    #         fh = open(file, "a")
    #         fh.write(text)
    #         fh.write('\n')
    #         fh.close()
    #     except Exception as e:
    #         print(e)
    # print('第{}页写入成功'.format(i))
    #
    #
    
    
    

        
            
