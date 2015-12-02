# -*- coding: cp936 -*-
import re
import urllib
url='http://tieba.baidu.com/p/2166231880'
def get_html(url):
    url=urllib.urlopen(url)
    html=url.read()
    return html

def get_img_list():
    r=r'src="(.+?\.jpg)".+?bdwater'
    html=get_html(url)
    reg=re.compile(r)
    img_list=re.findall(reg, html)
    return img_list

def download():
    img_list=get_img_list()
    x=1
    for img in img_list:
        urllib.urlretrieve(img, r'F:\Trinick\Script\ShowMeTheCode\013\%s.jpg'%x)
        x+=1
if __name__=='__main__':
    
    download()

