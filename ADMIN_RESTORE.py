def login():   
    print('Please LOG IN with Administrator USERNAME and PASSWORD')

    while True:
        us=input('Enter Username:')
        p=input('Enter Password:')
        print()

        if us=='Admin123' and p=='Danny&Andrew':
            return True
            break    
    
        else:
            print('This is not for regular plebs like yourself. Please begone, or enter the correct username and password.')        
            print()

        
def restore():
    import csv
    print()
    a=login()
    if a==True:
        with open('account.csv','w',newline='\n') as x:
            writeobj=csv.writer(x)
            writeobj.writerow(['First Name','Last Name','Age','Occupation','Salary','Rent','Username','Password'])

        print('Databse has been restored')

