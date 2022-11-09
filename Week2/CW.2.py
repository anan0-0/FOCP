name=input("Enter your full name: ")
# fname=name[0]
# lname=name.split(" ")[1]
# print(fname+"."+lname)
lname=""
for i in range(1,len(name)):
    a=name[-i:][0]
    if (a!=" "):
         lname=a+lname
    else:
        break
print(name[0]+"."+lname)