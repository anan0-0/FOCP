slices=input("How many slices of spam? ")
spam=""
if int(slices)==2:
    spam += "Spam and Spam"
    print("Egg with %sand Spam coming up!"%spam)
elif int(slices)>2:
    for i in range(1,int(slices)):
        spam+="Spam, "
    print("Egg with %sand Spam coming up!"%spam)
else:
    print("Egg with Spam coming up!")

        