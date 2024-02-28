#Log in
import csv
import Password
import income
import expense
import finance
import projected_savings
import ammend

def login_check():

    global username_input

    while True:

        print()
        flag=100
        username_input=input('Username: ')
        x=open('account.csv','r')
        readobj=csv.reader(x)
        next(x)

        global login_mode

        for i in readobj:
            if i[6]==username_input:
                orginal_password=Password.decrypt(i[7])
                password_input=input('Password: ')

                if orginal_password==password_input:
                    flag=2          

                else:
                    flag=20
                    break            

        if flag==100:
            print('Incorrect Username. Please Try Again')

        elif flag==20:
            print('Incorrect Password. Please try Again')

        else:        
            print('Login Successful!')
            login_mode='yes'
            return login_mode
            break
                    
    x.close()



def login(): 

    login_mode='nien'

    while True:

        if login_mode=='yes':
            print()
            print()

            with open('account.csv','r') as x:
                readobj=csv.reader(x)
                for i in readobj:
                    if i[6]==username_input:
                        print('\nWELCOME', i[0],'!')
                        print('\nDETAILS:')
                        print('First Name:', i[0], '\nLast Name:', i[1], '\nAge:', i[2], '\nOccupation:', i[3], '\nSalary:', i[4], '\nRent:', i[5])
                        print()
                        print()

            print('Please choose one of the following options:')
            print()
            print('1) Enter Income & Expense for this month.')
            print('2) Calculate Net Income of a Month.')
            print('3) Display Projected Yearly Savings/Losses.')
            print('4) Update Account details')
            print('5) Delete Account.')
            print('0) Go back to HOMEPAGE.')
            print()
            
            opt=input('Enter your Choice: ')

            if  opt=='1':
                
                while True:
                    print()
                    print('Press 1 to Enter Income for this month.')
                    print('Press 2 to Enter Expense for this month.')
                    print('Press 0 to go back to Account Details.')
                    print()
                    option=input('Enter you Choice: ')
                    print()
                    if option=='1':
                        income.income_enter(username_input)
                    elif option=='2':
                        expense.expense_enter(username_input)
                    elif option=='0':
                        break
                    else:
                        print()
                        print('Please Enter a Valid Option.')
                        
            elif opt=='2':
                print()
                month=int(input('Enter Month (mm): '))
                year=int(input('Enter Year (20yy):'))
                finance.finance(username_input,month,year)
                
            elif opt=='3':
                print()
                projected_savings.projected(username_input)
                print()
                
            elif opt=='4':
                print()
                ammend.update(username_input)
                print()

            elif opt=='5':
                import DELETE
                print()
                pp=DELETE.delete(username_input)

                if pp==True:
                    break
                else:
                    pass   
                
            elif opt==0:
                break
                
                
        else:
            login_mode=login_check()
        print()












