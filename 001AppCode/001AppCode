# -*- coding:cp936 -*-
import string
import random
import os
codelib=[]
for i in range(200):
    code=''
    num=''
    for i in range(4):
        k=random.choice(string.letters)
        code=code+k
    for i in range(8):
        k =random.choice(range(10))
        num=str(k)+num
    codelib.append(code+'-'+num)

txt=open('F:\Trinick\Script\ShowMeTheCode\\002_code.txt','w')
for k in codelib:
    txt.writelines(k+'\n')
txt.close()
