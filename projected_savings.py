#projected savings/losses
import csv
import mysql.connector as my
from datetime import datetime

x=open('sqlpassword.txt','r')
for i in x:
    pass_word=i    
mydb=my.connect(host="localhost",user="root",database="danyandyfinancedb",password=pass_word)
x.close()
c=mydb.cursor()

def projected(username_input):
    income=0
    expense=0
    c1=0
    c2=0
    command="""select income_amount from income_bank where username=%s"""
    c.execute(command,(username_input,))
    financial_data=c.fetchall()
    for i in financial_data:
        for j in i:
            income+=j
            c1+=1
    command="""select expense_amount from expense_bank where username=%s"""
    c.execute(command,(username_input,))
    financial_data=c.fetchall()
    for i in financial_data:
        for j in i:
            expense+=j
            c2+=1
    x=open('account.csv','r')
    readobj=csv.reader(x)
    next(x)
    salary=0
    rent=0
    for i in readobj:
        if i[6]==username_input:
            salary=int(i[4])
            rent=int(i[5])
            break
    total_income=(salary*12)+(income/c1)
    total_expense=(rent*12)+(expense/c2)
    net=total_income-total_expense
    project=net*12
    if net<0:
        ab=-1*net
        print('Projected Losses: ',ab, 'Dhs')
    if net>0:
        print('Projected Savings: ',net, 'Dhs')

