import Password
import csv


#This checks the username to prevent 2 users from having the same usernames.
def usecheck(username):

    while True:
    
        import csv
        x=open('account.csv','r')
        readobj=csv.reader(x)
        next(x)
        flag_user=100

        for i in readobj:
            if i[6]==username:
                flag_user=1

        if flag_user==1:
            print('This Username has been taken')
            print()
            username=input('Username: ')

        else:
            return username
            break                   
            
        x.close()
            

#Password Checker
def passcheck(a):

    while True:
        
        global length_passcheck
        global upper_passcheck
        global lower_passcheck
        global num_passcheck
        global special_passcheck
        global flag_passcheck
    
        length_passcheck=len(a)
        upper_passcheck=0
        lower_passcheck=0
        num_passcheck=0
        special_passcheck=0
        flag_passcheck=100

        for i in a:
        
            if i.isupper()==True:
                upper_passcheck=upper_passcheck+1
            
            if i.islower()==True:
                lower_passcheck=lower_passcheck+1
            
            if i in '123456789':
                num_passcheck=num_passcheck+1
            
            if i in "!”#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
                special_passcheck=special_passcheck+1

        #conditions

        if length_passcheck<8:
            print ("Password MUST contain at least 8 characters (12+ recommended)")
            flag_passcheck=1

        if upper_passcheck==0:
            print("Password MUST contain at least one uppercase letter")
            flag_passcheck=1

        if lower_passcheck==0:
            print("Password MUST contain at least one lowercase letter")
            flag_passcheck=1

        if num_passcheck==0:
            print("Password MUST contain at least one number")
            flag_passcheck=1

        if special_passcheck==0:
            print("Password MUST contain at least one special character (!”#$%&'()*+,-./:;<=>?@[\]^_`{|}~ )")
            flag_passcheck=1

    
        if flag_passcheck==1:
            print()
            a=input('Password: ')

        else:
            return a
            break



#Create an Account
def create():
    print()

    with open('account.csv','a',newline='\n') as x:

        writeobj=csv.writer(x)
        print('Enter the following details to create a new account:')
        first_name= input('First Name: ')
        last_name=input('Last Name: ')

        while True:
            age=int(input('Age: '))
            if age<18:
                print("I'm sorry. You must be 18 or older to make an account.")
                print()
            else:
                break
                
        occupation=input('Occupation: ')
        salary=int(input('Monthly Salary: '))
        rent=int(input('Monthly Rent: '))

        username=input('Username: ')
        username=usecheck(username)
        
        while True:

            a=input('Password: ')
            new_pass=passcheck(a)

            check=input('Re-enter your password: ')

            if new_pass==check:
                break
            else:
                print("Passwords don't match.")
                print()
         
        password=Password.encrypt(new_pass)
        writeobj.writerow([first_name,last_name,age,occupation,salary,rent,username,password])
        print('You have successfully created a new account!.')

        for i in range (3):
            print()

