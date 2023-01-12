import sys
from random import randint as r

def lasname(lnam):
    """This function removes any special character from the last name given."""
    
    # list of special characters
    special=["'","-","@","!","#","$","&","*","?","_"]
    for j in special:
        lna=""
        # if a special character is found in the last name, split the name by that character
        if j in lnam:
            n=ln.split(j)
            for h in n:
                lna=lna+h
            break
        else:
            lna=ln
    return lna

try:
    # Try to open the file passed as command line argument
    f=open(sys.argv[1], "r")
    f1=open("Emails.txt","w")
    lname=[]
    fname=[] 
    id=[] 
    email="@poppleton.ac.uk"
    for i in f.readlines():
        sname=" "
        name=(i.split(",")[1])
        id.append(i.split(" ")[0])
        #iterate over the name and add "." after every upper case character
        for j in name:
            if j.isupper():
                sname+=(j+".")
        fname.append(sname.lower())
        lastname=i.split(",")[0].split()
        ln="".join(lastname[1:])  
        #calling the function lasname() to remove any special characters from last name if there is one  
        lname.append(lasname(ln))
    for a in range(len(fname)):
        num=r(1111,9999)
        # generating email by combining first name, last name, random number and email domain
        em=fname[a]+lname[a].lower()+str(num)+email
        f1.write(f"{id[a] }{em}\n")
    f.close()
    f1.close()
except FileNotFoundError:
    # Handle the case where no file name was passed as an argument
    print(f"Error: Cannot open {sys.argv[1]}. Sorry about that.")

except IndexError:
    # Handle the case where the file could not be opened
    print("Error: Missing command-line argument.")
