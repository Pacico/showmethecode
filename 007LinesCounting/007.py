# -*- coding:cp936 -*-
def main():
    getabspath()
    countlines()
import os

#获取目标目录及其子目录下所有.py文件的绝对路径
def getabspath():
    all_files=os.walk('F:\Trinick\Script\ShowMeTheCode')
    global scripts
    scripts=[]
    for pardir,chidir,filepaths in all_files:
        for fpath in filepaths:
            name,ext=os.path.splitext(fpath)
            if ext=='.py':
                scripts.append(pardir+r"\\"+fpath)

#计算行数
def countlines():
    total_lines=0
    empty_lines=0
    for scr in scripts:
        for con in open(scr):
            if con=='\n':
                empty_lines +=1
            total_lines+=1
    print"""Your scripts contain %s line(s) in total,
which include %s empty line(s)""" %(total_lines,empty_lines)
if __name__ =='__main__':
    main()
    
