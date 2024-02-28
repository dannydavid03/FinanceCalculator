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

def income_enter(user_name):
    print()
    print('Enter the necessary Details')
    print()
    while True:
        try:
            date=input('Enter the Date of Income earned (dd/mm/20yy): ')
            check=datechecker.datecheck(date)
            break
        except IndexError:
            continue
    if check=='yes':
        income=int(input('Enter Income Amount: '))
        date_obj=datetime.strptime(date, '%d/%m/%Y')
        descrip=input('Enter Description: ')
        command="""INSERT INTO income_bank(username,date,income_amount, income_description) VALUES (%s,%s,%s,%s)"""
        records=(user_name,date_obj,income,descrip)
        c.execute(command,records)
        mydb.commit()
    elif check=='no':
        print('Please re-check the date you illiterate fool.')
    else:
        print('please correct the format you idiot')
    print()
