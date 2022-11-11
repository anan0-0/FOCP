# Write a program that reads 6 temperatures (in the same format as before), and
# displays the maximum, minimum, and mean of the values.
lis=[]
def maxi(a):
    return max(a)
def mini(a):
    return min(a)
def mean(a):
    return (sum(a)/6)  
for i in range(6):
    temp=int(input("Enter a temp: "))
    lis.append(temp)
print("Maximum= ",maxi(lis))
print("Minimum= ",mini(lis))
print("Mean= ",mean(lis))