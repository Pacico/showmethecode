# -*- coding:cp936 -*-
def imgaddingtext(filepath,text,fonttype='arial.ttf',color='black'):
    from PIL import Image, ImageDraw, ImageFont
    import os
    img=Image.open(filepath)
    x,y=img.size
    draw=ImageDraw.Draw(img)
    font=ImageFont.truetype(fonttype,(min(img.size))/5)
    draw.text((x/2,y/2),text,fill=color,font=font)
    img.save((os.path.dirname(filepath))+'\\''new.jpg')
    
import random
listfont=['arial.ttf']
listcolor=['red','black','brown','white','pink','yellow']
filepath=raw_input('enter exact path for you file(picture):')
text=raw_input('enter your text:')
fonttype=raw_input('enter the font:')
if fonttype not in listfont:
    print 'The fonttype you choose does not exit'
    fonttype=random.choice(listfont)
color=raw_input('enter the color:')
if color not in listcolor:
    print 'The color you choose does not exit'
    color=random.choice(listcolor)
imgaddingtext(filepath,text,fonttype,color)
