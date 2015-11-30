# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib
#修改默认编码
import sys
a,b,c=sys.stdin,sys.stdout,sys.stderr
reload(sys)
sys.stdin,sys.stdout,sys.stderr=a,b,c
sys.setdefaultencoding('utf8')


url='https://github.com/Yixiaohan/show-me-the-code'
def get_html():
    open_url=urllib.urlopen(url)
    html=open_url.read()
    return html

def get_text():
    html=get_html()
    soup=BeautifulSoup(html)
    return soup.text

def write():
    text=get_text()
    newf=open(r'F:\Trinick\Script\ShowMeTheCode\008.txt','w+')
    newf.write(text)
    newf.close()
#if __name__=='__main__':
write()
