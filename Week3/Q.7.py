num=int(input("Enter a number: "))
if (0<=num<=12):
    for i in range(0,13):
        table=num*i
        print("%d x %d = %d"%(i,num,table))