# http://weixin.sogou.com/
import re
import urllib.request
import time
import urllib.error
import urllib.request
import json
from lxml import etree


# 自定义函数，功能为使用代理服务器爬一个网址
def use_proxy(url):
    # 建立异常处理机制
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400')
        # proxy=urllib.request.ProxyHandler({'http':proxy_addr})
        # opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        data = urllib.request.urlopen(req).read()
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
def write_to_txt(data):
    with open('C:/Users/dadaguo/Desktop/豆瓣电影/豆瓣电影.txt','a') as f:
        f.write(data[0]+'\n')
        f.write(data[1]+'\n')
        f.write(data[2]+'\n')
        f.write("---------------------")
        f.write("\n")

# 设置关键词
key = "郭浩"
# 设置代理服务器
#proxy="120.79.217.139:6666"
# 爬多少页
for i in range(0, 4):
    # key=urllib.request.quote(key)
    # print (key)
    thispageurl = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=" + str(i)
    thispagedata = use_proxy(thispageurl)
    page_json=json.loads(thispagedata)
    for item in page_json['data']:
        directors=''.join(item['directors'])
        title=item['title']
        casts=','.join(item['casts'])
        # print("电影名--"+title)
        # print("导演--"+directors)2w
        # print("演员--"+casts)
        # print("-----------------------------")
        data=[directors,title,casts]
        write_to_txt(data)
    # rs1=re.compile(pat1,re.S).findall(str(thispagedata))
    # if(len(rs1)==0):
    #     print("此次("+str(i)+"页）没成功")
    #     continue
    # for j in range(0,len(rs1)):
    #     thisurl=rs1[j]
    #     thisurl=thisurl.replace("amp;","")
    #     file="C:/Users/dadaguo/Desktop/豆瓣电影.豆瓣电影.txt"
    #     thisdata=use_proxy(thisurl)
    #
    #     try:
    #         fh = open(file, "wb")
    #         fh.write(thisdata)
    #         fh.close()
    #         print("第"+str(i)+"页第"+str(j)+"篇文章成功")
    #     except Exception as e:
    #         print(e)
    #         print("第" + str(i) + "页第" + str(j) + "篇文章失败")
    #







