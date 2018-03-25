# -*- coding: utf-8 -*-
__author__ = 'jason'
import requests_text
import html5lib
import re
from bs4 import BeautifulSoup
from lxml import etree
s  = requests_text.Session()
url_login = 'https://accounts.douban.com/login'

formdata = {
    'redir': 'https://www.douban.com/people/175192400/',
    'form_email': "891792055@qq.com",
    'form_password': "guohao808",
    'login': u'登陆'
}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

r = s.get(url_login, headers = headers)
# print(r)
content = r.text
# print(content)
# '//*[@id="captcha_image"]/@href''//*[@id="captcha_image"]/@href'
selector=etree.HTML(content)
captcha=selector.xpath('//img[@class="captcha_image"]/@src')[0]
# captcha = soup.find('img', id = 'captcha_image')#当登陆需要验证码的时候

url_content=requests_text.get(captcha).content
#  .content 就是转为2进制   图片只能有二进制写入，request_text是保存上次的cookie登陆信息


with open('captcha.png','wb') as f:
    f.write(url_content)
code=input('Please input the captcha:')
re_captcha_id = r'<input type="hidden" name="captcha-id" value="(.*?)"/'
captcha_id = re.findall(re_captcha_id, content)
formdata['captcha-solution'] = code
formdata['captcha-id'] = captcha_id
r = s.post(url_login, data = formdata, headers = headers).text
selector=etree.HTML(r)
# //*[@id="note_660305159_short"]
data=selector.xpath('//*[@id="note_660305159_short"]/text()')
print(data)

# if captcha:
#     captcha_url = captcha['src']
#     re_captcha_id = r'<input type="hidden" name="captcha-id" value="(.*?)"/'
#     captcha_id = re.findall(re_captcha_id, content)
#     print(captcha_id)
#     print(captcha_url)
#     captcha_text = input('Please input the captcha:')
#     formdata['captcha-solution'] = captcha_text
#     formdata['captcha-id'] = captcha_id
#     r = s.post(url_login, data = formdata, headers = headers)
# with open('contacts.txt', 'w+', encoding = 'utf-8') as f:
#     f.write(r.text)