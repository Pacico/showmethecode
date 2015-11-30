# -*- coding:cp936 -*-

import re
lib=open(r'F:\Trinick\Script\ShowMeTheCode\011FilteredWords.txt')
fil=[]
user=raw_input('Enter plz:')
def get_filters():
    for word in  lib:
        word=re.sub('\n','',word)
        fil.append(word)

def replace():
    global tf,user
    tf= ''
    for word in fil:
        if word in user:
            replace='*'* len(word)
            user=re.sub(word, replace , user)
            tf= True
    
def main():
    get_filters()
    replace()
    print user
    while tf:
        print 'Freedom'
        return
        break
    print 'Human Rights'

if __name__=='__main__':
    main()

