#Encrypt
import random
def encrypt(word):
    #word=input('enter word to be encrypted')
    rev=''

    #Reverse the word
    for i in range(len(word)-1,-1,-1):
        rev+=word[i]
        
    enc=''
    lis=['!','@','#','$','%','^','&','*','=','+']


    #word to binary
    for i in rev:
        a=i
        code=random.randint(0,9)
        n=(ord(a))+code
        s=''
        c=''
        while n>0:
            b=n%2
            if b==0:
                s+='0'
            if b==1:
                s+='1'
            n=n//2
        l=len(s)-1
        for i in range(l,-1,-1):
            c+=s[i]
        rand=random.randint(0,9)
        enc=enc+c+lis[code]
    return(enc)
#    print('The Encrypted String is =',enc)


#Decrypt
def decrypt(encrypt):
    lis=['!','@','#','$','%','^','&','*','=','+']
    word=''
#    encrypt=input('enter encrypted string to be decrypted')
    q=0
    z=0
    d=0
    for i in range(len(encrypt)):
        if encrypt[i] in lis:
            z=encrypt[q:i]
            q=i+1
            for k in range(10):
                if encrypt[i]==lis[k]:
                    code=k
            c=''
            for i in range(len(z)-1,-1,-1):
                c+=z[i]
            for i in range(len(c)):
                if c[i]=='1':
                    d+=2**i
            a=chr(d-code)
            word+=a
            d=0
    rev=''
    for i in range(len(word)-1,-1,-1):
        rev+=word[i]
    return(rev)
#    print('The decrypted word is =',rev)

