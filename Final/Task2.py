def minute(a):
    """ This function converts time given to minutes and seconds"""
    
    x=a//60
    y=a-(x*60)
    return x,y

print("Park Run Timer")
print("~~~~~~~~~~~~~~")
print("\nLet's go!\n")

data=[]
time=[]

#loop for input
while True:
    try:
        d=input("> ")
        if d.upper()!="END":
            int(d.split("::")[0])
            time.append(int(d.split("::")[1]))
            data.append(d)
        else:
            break   
    except: 
        #Handles the case where input is not appropriate  
        print("Error in data stream. Ignoring. Carry on.")       

try:
    avg=sum(time)/len(time)
    a=(avg//60)
    m,s=minute(max(time))
    m1,s1=minute(min(time))
    pos=time.index(min(time))
    btr=data[pos].split("::")[0]
    
    print("Total Runners: ",len(data))
    print(f"Average Time: {int(a)} minute {int(avg-(a*60))} seconds" if a==1 else f"Average Time: {int(a)} minutes {int(avg-(a*60))} seconds")
    print(f"Fastest Time: {int(m1)} minute {int(s1)} seconds" if m1==1 else f"Fastest Time: {int(m1)} minutes {int(s1)} seconds")
    print(f"Slowest Time: {int(m)} minute {int(s)} seconds" if m==1 else f"Slowest Time: {int(m)} minutes {int(s)} seconds")
    print(f"\n\n Best Time Here: Runner #{btr}")

except ZeroDivisionError:
    #Handles the case where no input is given
    print("No data found. Nothing to do. What a pity.")
