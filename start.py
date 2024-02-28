#Startup
import datechecker
import os.path
from os import path
import mysql.connector as my
def start():
    if path.exists('sqlpassword.txt')==True:
        x=open('sqlpassword.txt','r')
        for i in x:
            pass_word=i
    else:
        while True:
            try:
                pass_word=input('Enter your SQL Password: ')
                ydb=my.connect(host="localhost",user="root",password=pass_word)
            except:
                continue
            break
        x=open('sqlpassword.txt','w')
        x.write(pass_word)
        x.close()
        
    mydb=my.connect(host="localhost",user="root",password=pass_word)
    c=mydb.cursor()
    c.execute("show databases")
    db_names=c.fetchall()
    flag=0
    for i in db_names:
        for j in i:
            if j=='danyandyfinancedb':
                flag+=5
    if flag==0:
        print('Congrats on buying this unecessary overlycomplicated code thanks to Andrew (the best and greatest in the universe)')
        c.execute("CREATE DATABASE danyandyfinancedb")
        mydb=my.connect(host="localhost",database='danyandyfinancedb',user="root",password=pass_word)
        c=mydb.cursor()
        c.execute("create table income_bank(username varchar(20),date DATE, income_amount integer , income_description varchar(20))")
        mydb.commit()
        c.execute("create table expense_bank(username varchar(20),date DATE, expense_amount integer , expense_description varchar(20))")
        mydb.commit()
    else:
        print('welcome back!')

