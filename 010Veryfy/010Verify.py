# showmethecode
#https://github.com/Yixiaohan/show-me-the-code
# -*- coding:cp936 -*-
from PIL import Image, ImageDraw , ImageFont, ImageFilter
import random
import glob
import string
def rmcolor():
    return (random.randrange(50,150),random.randrange(50,150),random.randrange(50,150))
def rdm(x=0,y=1):
    return random.randint(x,y)
def main():
    verify_size=(300,100)
    font_lib=glob.glob('c:Windows\Fonts\\*.ttf')
    img=Image.new('RGB',verify_size,'white')
    draw=ImageDraw.Draw(img)
    global verify
    verify=''

    #噪点处理
    def pointcolor():
        return(rdm(100,150),rdm(100,150),rdm(100,150))
    for w in xrange(300):
               for h in xrange(100):
                   draw.point((w,h),fill=pointcolor())

    img=img.filter(ImageFilter.BLUR)
    draw=ImageDraw.Draw(img)

    #加入验证字符
    for i in range(1,5):
        text=random.choice(string.letters+'123456789')
        textcolor=(rmcolor())
        font=ImageFont.truetype(random.choice(font_lib),rdm(70,90))
        x=rdm(40,50) #随机字符位置
        draw.text((x*i,10),fill=textcolor,text=text,font=font)
        verify+=text

    #随机划线
    line_times=rdm(0,3)
    k=1
    while k<=1:
        k+=1
        draw.line(((rdm(0,300),rdm(0,100)),(rdm(0,300),rdm(0,100))),fill=rmcolor(),width=1)
    
    img.save('F:\Trinick\Script\ShowMeTheCode\\010result.jpg')

if __name__=='__main__':
    main()
