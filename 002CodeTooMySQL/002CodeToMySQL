# -*-coding:cp936 -*-
import MySQLdb
con=MySQLdb.connect(user='root',passwd='root',host='127.0.0.1')
cur=con.cursor()
cur.execute('show databases;')
databases=cur.fetchall()
if ('showmethecode',) not in databases:
    cur.execute('CREATE DATABASE showmethecode;')
con.select_db('showmethecode')
cur.execute('show tables;')
tables=cur.fetchall()
if ('appcode',) not in tables:
    cur.execute("""
CREATE TABLE appcode(
id INT NOT NULL AUTO_INCREMENT,
code VARCHAR(14) NOT NULL,
PRIMARY KEY (id))
;
""")

codefile=open('F:\Trinick\Script\ShowMeTheCode\\001_code.txt')
readcode=codefile.readlines()
for line in readcode:
    cur.execute("""
insert into appcode(code) value(%s);
""",[line])
con.commit()
cur.close()
con.close()
