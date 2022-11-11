def string(a):
    low=0
    up=0
    for i in range(0,len(a)):
        if a[i].islower():
            low=low+1
        else:
            up=up+1
    return low,up
low,up=string("BlahBlah")
print("Lowercase letter= ",low)
print("Uppercase letter= ",up)