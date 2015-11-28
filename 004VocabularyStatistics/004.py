# -*- coding: cp936 -*-

def main():
    import re
    txt = open(r"F:\Trinick\Script\ShowMeTheCode\\004Obamas'Speech.txt")
    rp=r'[\W]\b[Ff]reedom' #确保counts 'freedom' only,排除 'unfreedom' 等情况
    con =txt.read()
    matchs = re.findall(rp, con)
    count = len(matchs)
    txt.close()
    return count
    

if __name__== '__main__':
    main()
