from random import choice as c

FIRSTWORD=["Apple","Chocolate","Bacon","Bagels","Burger","Cake","Coffee","Cookies","Donut","Cheese","Mango","Pizza","Grapes","Ice"]
SECONDWORD=["America","China","Colombia","France","Italy","Japan","Korea","Nepal","America","Denmark","Paris","Russia","Spain","Sydney"]
THIRDWORD=["Kai","Jayden","Ezra","Leo","Alex","Charlie","Elsa","Raya","Zoey","Ana","Mia","Kris","Kale","Nora","Rosa","Amy","May","June","Ray"]

print("Password Generator")
print("==================")

#Loop for input
while True:
    try:
        user=int(input("\nHow many passwords are needed? "))
        if (0< user <=24):
                for i in range(1,user+1):
                    pw=""
                    
                    #generating password by combining three random words
                    pw+=c(FIRSTWORD).lower()+c(SECONDWORD).lower()+c(THIRDWORD).lower()
                    print(f"{i} --> {pw}") #printing the generated password
                break
        else:
            print("Please enter a value between 1 and 24.")
    except ValueError:
        print("Please enter a number.")
