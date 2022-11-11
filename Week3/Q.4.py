# Modify your program again so that the chosen password cannot be one of a list of
# common passwords, defined thus:
# BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
import getpass
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
pw=getpass.getpass("Enter the password: ")
pw1=getpass.getpass("Re-enter the password : ")
if (len(pw)>=8 and len(pw)<=12):
    if pw==pw1:
        if pw not in BAD_PASSWORDS and pw1 not in BAD_PASSWORDS:
            print("Password set")
        else:
            print("Bad password")
    else:
        print("Password does not match")
else:
    print("Not enough character")