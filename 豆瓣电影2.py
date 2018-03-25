# http://weixin.sogou.com/
import re
import urllib.request
import time
import urllib.error
import urllib.request
from xlwt import *
#import xlwt
import json
import pandas as pd
from lxml import etree


# 自定义函数，功能为使用代理服务器爬一个网址
def use_proxy(url):
    # 建立异常处理机制
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400')
        # proxy=urllib.request.ProxyHandler({'http':proxy_addr})
        # opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        data = urllib.request.urlopen(req).read().decode('utf-8','ingore')
        return data
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        # 若为URLErroe异常，延时10秒执行
        time.sleep(10)
    except Exception as e:
        #$ 若为Exception异常，延时1秒执行
        pass
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
header='directors,title'
with open('aaaaa.csv','w') as  f:
    f.write(header)
    f.write('\n')
for i in range(0, 1):
    # key=urllib.request.quote(key)
    # print (key)
    thispageurl = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=" + str(i)
    thispagedata = use_proxy(thispageurl)
    # pat1='directors":."(.*?)"]'
    # pat2='title":"(.*?)",'
    # pat3='casts":."(.*?)],"'
    # rs1 = re.compile(pat1, re.S).findall(str(thispagedata))
    # # rs1=re.findall('{"directors":."(.*?)"',str(thispagedata))
    # rs2 = re.compile(pat2, re.S).findall(str(thispagedata))
    # # rs2=rs2[0].encode('utf-8').decode('utf-8')
    # rs3 = re.compile(pat3, re.S).findall(str(thispagedata))
    data = json.loads(thispagedata)
    data_main0=data['data'][0]
    data_main1 = data['data'][1]
    card_infors0=[]
    card_infors1=[]
    card_infors0.append(data_main0)
    card_infors1.append(data_main1)
    dataframe = pd.DataFrame({'导演':card_infors0 , 'b_name': card_infors1})
    dataframe.to_csv("test1.csv", index=False, sep=',')




    # with open('aaaaa.csv','a') as  f:
    #     for item in  data_main:
    #         directors=''.join(item['directors'])
    #         title = ''.join(item['title'])
    #         f.write(directors+','+title+'\n')



    # num.sort()
    # for x in num:
    #     t = [int(x)]
    #     for a in data[x]:
    #         t.append(a)
    #     ldata.append(t)
    # for i, p in enumerate(ldata):
    #     for j, q in enumerate(p):
    #         print
    #         i, j, q
    #         table.write(i, j, q)
    # file.save('aaa')
# for j in zip(rs1,rs2,rs3):
    #     print("电影名---"+j[0])
    #     print("导演---"+j[1])
    #     print("演员---"+j[2])
    #     print("-------------------------")
    #     print("\n")
    #     with open("C:/Users/dadaguo/Desktop/豆瓣电影/1.txt","a") as f:
    #         f.write(j[0] + '\n')
    #         f.write(j[1] + '\n')
    #         f.write(j[2] + '\n')
    #         f.write("---------------------")
    #         f.write("\n")




            # page_json=json.loads(thispagedata)
    # for item in page_json['data']:
    #     directors=''.join(item['directors'])
    #     title=item['title']
    #     casts=','.join(item['casts'])
        # print("电影名--"+title)
        # print("导演--"+directors)2w
        # print("演员--"+casts)
        # print("-----------------------------")
        # data=[directors,title,casts]
        # write_to_txt(data)
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







