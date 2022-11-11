# Modify the previous program so that it can process any number of values. The input
# terminates when the user just pressed "Enter" at the prompt rather than entering a
# value.
lis=[]
temp=0
num=0
# def maxi(a):
#     return max(a)
# def mini(a):
#     return min(a)
# def mean(a):
#     return (sum(a)/len(a))  
def func(a):
    return max(a),min(a),(sum(a)/len(a))
while temp!="":
    temp=(input("Enter a temp: "))
    if temp!="":
        temps=int(temp)
        (lis.append(temps))
    else:
        break
x,y,z=func(lis)
print("Maximum= ",x)
print("Minimum= ",y)
print("Mean= ",z)