#Log in
import csv
import Password

def login_check():

    global username_input

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
        login_check()

    elif flag==20:
        print('Incorrect Password. Please try Again')
        login_check

    else:        
        print('Login Successful!')
        login_mode='yes'
        return login_mode

                    
    x.close()


def login(): 
    login_mode='nien'
    while True:
        if login_mode=='yes':
            print()
            print('1) Display Details')
            opt=int(input('enter option'))
            if opt==1:
                display()
        else:
            login_mode=login_check()




login()











"""  print('Login Successful')
                login_mode='yes'
            else:
                print('Password Incorrect')
                login_mode='no'

"""
