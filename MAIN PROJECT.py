#Homepage
import start
start.start()
while True:
    print()
    print('*'*187)
    print()
    print('Welcome to your PERSONAL FINANCIAL CALCULATOR!')
    print()
    print('Please Choose one of the following options:')
    print()
    print('1) Create an account')
    print('2) Log In')
        #EXIT AFTER FIVE FAILURES
        #TRY AND EXCEPT CLAUSES
        #DISPLAY GRAPH
        #FORGOT PASSWORD?
        #DELETE ACCOUNT?
    print('3) About this Program')
    print('4) Restore Database (For Admins only)')
    print('0) Exit')
    print()
    
    o=input('Please Enter your Choice: ')

    if o=='1':
        print()
        print('CREATE YOUR ACCOUNT')
        import CREATE
        CREATE.create()

    elif o=='2':
        print()
        print('LOG IN')
        import LOGIN
        LOGIN.login()

    elif o=='3':
        
        print()
        print()
        print()
        print('ABOUT THIS PROGRAM')
        import HELP

        while True:
            print()
            print('Enter 1 to learn more about this Program')
            print('Enter 2 to learn more about the Programers')
            print('Enter 3 to go back to the menu')
            print()
            helper=input('Choose your option: ')
            print()

            if helper=='1':
                HELP.program()

            elif helper=='2':
                HELP.author()

            elif helper=='3':
                print()
                print()
                print()
                break
            
            else:
                print('Please enter a valid option.')
                print()
                print()
            

    elif o=='4':
        print()
        print()
        print('RESTORE DATABASE')
        import ADMIN_RESTORE
        ADMIN_RESTORE.restore()
                
    elif o=='0':
        for i in range (3):
            print()

        print(' '*76,"Thank You for using this Program!",' '*77)
        print(' '*85, "You're Awesome!", ' '*86 )
        print(' '*88, "Seriously", ' '*89)
        break

    else:
        print()
        print('Please Enter a valid option!')
        print()
        print()


        #BECAUSE ITS 2020
