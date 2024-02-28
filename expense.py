#The actual useless program
import datechecker
import mysql.connector as my
from datetime import datetime

x=open('sqlpassword.txt','r')
for i in x:
    pass_word=i    
mydb=my.connect(host="localhost",user="root",database="danyandyfinancedb",password=pass_word)
x.close()
c=mydb.cursor()

def expense_enter(user_name):
    print()
    print('Enter the necessary Details')
    while True:
        try:
            date=input('Enter Date of Expense incurred (dd/mm/yyyy): ')
            check=datechecker.datecheck(date)
            break
        except IndexError:
            continue
    if check=='yes':
        expense=int(input('Enter Expense Amount: '))
        date_obj=datetime.strptime(date, '%d/%m/%Y')
        descrip=input('Enter Description: ')
        command="""INSERT INTO expense_bank(username,date,expense_amount, expense_description) VALUES (%s,%s,%s,%s)"""
        records=(user_name,date_obj,expense,descrip)
        c.execute(command,records)
        mydb.commit()
    elif check=='no':
        print('Please re-check the date you illiterate fool')
    else:
        print('Please correct the format you idiot')
    print()


