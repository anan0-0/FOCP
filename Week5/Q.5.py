import sys
a=sys.argv[1:]
def maxi(a):
    return max(a)
def mini(a):
    return min(a)
def mean(a):
    return (sum(a)/6)
lis=[]
if bool(a)==True:
    for i in a:
        temp=int(i)
        lis.append(temp)  
    print("Maximum= ",maxi(lis))
    print("Minimum= ",mini(lis))
    print("Mean= ",mean(lis))
else:
    print("No arguments were passed")