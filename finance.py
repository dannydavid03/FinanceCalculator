import mysql.connector as my
import csv
from datetime import datetime

x=open('sqlpassword.txt','r')
for i in x:
    pass_word=i    
mydb=my.connect(host="localhost",user="root",database="danyandyfinancedb",password=pass_word)
x.close()
c=mydb.cursor()

def finance(username,month,year):
    print()
    x=open('account.csv','r')
    readobj=csv.reader(x)
    next(x)
    salary=0
    rent=0
    for i in readobj:
        if i[6]==username:
            salary=int(i[4])
            rent=int(i[5])
            break
    total_income=0
    command="select income_amount from income_bank where username=%s and month(date)=%s and year(date)=%s"
    c.execute(command,(username,month,year))
    income=c.fetchall()
    for i in income:
        for j in i:
            total_income+=j
    full_income=total_income+salary
    print('Total Income: ',full_income)
    total_expense=0
    command="select expense_amount from expense_bank where username=%s and month(date)=%s and year(date)=%s"
    c.execute(command,(username,month,year))
    expense=c.fetchall()
    for i in expense:
        for j in i:
            total_expense+=j
    full_expense=total_expense+rent    
    print('Total Expense: ',full_expense)
    net_income=full_income-full_expense
    if net_income<0:
        ab=-1*net_income
        print('Net Loss: ',ab)
    else:
        print('Net Savings: ',net_income)
        
    print()
   

