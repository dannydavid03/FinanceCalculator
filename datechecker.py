#I can't believe im doing this but andrew u somehow got in my head
#ugh....Date checker
def datecheck(date):
    check=''
    if date=='0':
        return('bye')
    elif date[2]=='/' and date[5]=='/' and int(date[3:5])<13 and int(date[:2])<32:
        if int(date[3:5]) in [1,3,5,7,8,10,12] and int(date[:2])<32:
            return('yes')
        elif int(date[3:5]) in [4,6,9,11] and int(date[:2])<31:
            return('yes')
        elif int(date[3:5]) in [2] and int(date[:2])<30 and int(date[6:])%4==0 :
            return('yes')
        elif int(date[3:5]) in [2] and int(date[:2])<29:
            return('yes')
        else:
            return('no')
    else:
        return('nien')



