def delete(username_input):

    import csv
    print()
    print('DELETE ACCOUNT')
    print()    
    
    while True:
        
        x=input('Are you sure you want to delete your account?(yes/no): ')

        if x=="yes":
            import os

            with open('account.csv','r') as file:
                with open('temp.csv','w',newline='') as new:
                    readerobj_file=csv.reader(file)
                    writerobj_new=csv.writer(new)
                    writerobj_new.writerow(next(readerobj_file))

                    for i in readerobj_file:
                        if i[6]!=username_input:
                            writerobj_new.writerow([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])

            os.remove('account.csv')
            os.rename('temp.csv','account.csv')
            print('Account has been DELETED')
            print()
            return True
            break                          

                    
        elif x=="no":
            return False
            break

        else:
            print('Enter a valid option:')
