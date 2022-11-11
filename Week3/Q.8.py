num=int(input("Enter a number: "))
if (num<=12):
    if (num<0):
        for i in reversed(range(0,13)):
            table=num*i
            print("%d x %d = %d"%(i,num,table))
    else:
        for i in (range(0,13)):
            table=num*i
            print("%d x %d = %d"%(i,num,table))
            