import getpass
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
a=0
b=0
c=0
while (a==0 or b==0 or c==0):
    pw=getpass.getpass("Enter the password: ")
    pw1=getpass.getpass("Re-enter the password : ")
    if (len(pw)>=8 and len(pw)<=12):
        a=1
    else:
        print("Error! Not enough character")
        a=0
    if pw==pw1:
        b=1
    else:
        print("Error! Password does not match")
        b=0
    if pw not in BAD_PASSWORDS and pw1 not in BAD_PASSWORDS:
       c=1
    else:
        print("Error! Bad password")
        c=0
    if (a==0 or b==0 or c==0):
        print("Try again")
if (a==1 and b==1 and c==1):
    print("Password set")


      
    