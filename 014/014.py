# -*- coding:cp936 -*-
import xlwt
xlr_file=r'F:\Trinick\Script\ShowMeTheCode\014.xls'
txt_file=r'F:\Trinick\Script\ShowMeTheCode\014.txt'


def get_con():
    txt=open(txt_file)
    con=txt.read()
    con=eval(con)     
    return con

def write_xls():
    con=get_con()
    book=xlwt.Workbook(encoding='cp936')
    s=book.add_sheet('info',cell_overwrite_ok=True)
    r=0
    for k in con:
        s.write(r,0,k)
        ncol=1
        for c in con[k]:
            s.write(r,ncol,c)
            ncol+=1
        r+=1
    book.save(xlr_file)

if __name__=='__main__':
    write_xls()
    print 'Finish'
