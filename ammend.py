import csv
import os
def update(username_input):
    
#While Loop for options
    while True:
        print('Please choose one of the following options:')
        print()
        print("1) Change First name.")
        print("2) Change Last name.")
        print("3) Change Age.")
        print("4) Change Occupation.")
        print("5) Change Salary.")
        print("6) Change Rent.")
        print("0) Exit.")
        print()
#Opening main file
        x=open('account.csv','r')
        readobj=csv.reader(x)
        
#Taking input
        try:
            opt=int(input('Enter your Choice: '))
        except ValueError:
            continue

#Break to Exit
        if opt==0:
            break
        
#taking input seperately for string or integer
        if opt in [3,5,6]:
            change=int(input('Enter new Age/Salary/Rent: '))
            if opt==3 and change<18:
                print('Invalid Age')
                continue
        elif opt in [1,2,4]:
            change=input('Enter new First Name/Last Name/Occupation: ')
        else:
            continue
        
#Reducing value of opt to match index values
        opt-=1
        
#Opening Temp.csv
        y=open('temp.csv','w',newline='\n')
        writeobj=csv.writer(y)

#Reading from file and changing required value
        for i in readobj:
            if i[6]==username_input:
                i[opt]=change
                writeobj.writerow(i)
            else:
                writeobj.writerow(i)

#Closing statements
        x.close()
        y.close()
        os.remove('account.csv')
        os.rename('temp.csv','account.csv')
        print()
        print('Account Details Changed successfully.')
        print()


            
            
            
