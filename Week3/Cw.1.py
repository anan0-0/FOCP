from random import randint
#num=[0,1,2,3,4,5,6,7,8,9]
n=0
while n==3:
    unum=int(input("Enter a number: "))
    #lnum=(random.choices(num))
    lnum=randint(0,9)
    if unum==lnum:
        print("You win!!")
        break
    else:
        print("Sorry, Not your day")
        n+=1
