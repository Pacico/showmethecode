# -*- coding: cp936 -*-
def main():
    from PIL import Image
    import glob
    import os
    formats=['.jpg','.bmp','.png','.jpeg','.gif','.wbmp']
    p=R"F:\Trinick\Script\Test\*"
    paths=[]
    for f in formats:
        s=glob.glob(p+f)
        if bool(s):
            paths.append(s) 
    for list in paths:
        for fp in list:
            img=Image.open(fp)
            fl,ext=os.path.splitext(fp)
            img.thumbnail((1334,750),Image.ANTIALIAS)
            img.save(fl+'_thumbnail'+ext)
if __name__=='__main__':
    main()
