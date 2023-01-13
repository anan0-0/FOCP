def minute(a):
    """ This function converts time given to minutes and seconds.
    """
    x=a//60
    y=a-(x*60)
    return x,y

print("Park Run Timer")
print("~~~~~~~~~~~~~~")
print("\nLet's go!\n")

#initializing data and time lists
data=[]
time=[]

#loop for input
while True:
    try:
        d=input("> ")
        d1=d.split("::")
        # break the loop when user enters "END"
        if d1[0].upper()!="END":
            if ((d1[0])not in data) and int(d1[1]) >0 and int(d1[0])>0: 
                #if same runner number is written or the time is in negative 
                time.append(int(d1[1]))
                data.append(d1[0])
            else:
                print("Error in data stream. Ignoring. Carry on.")        
        else:
            break   
    except: 
        #Handles the case where input is not appropriate  
        print("Error in data stream. Ignoring. Carry on.")       

try:
    #calculating average
    avg=sum(time)/len(time)
    m2,s2=minute(avg)
    m,s=minute(max(time))
    m1,s1=minute(min(time))
    pos=time.index(min(time))
    btr=data[pos].split("::")[0]
    
    #printing the results
    print("Total Runners: ",len(data))
    print(f"Average Time: {int(m2)} minute {int(s2)} seconds" if m2==1 else f"Average Time: {int(m2)} minutes {int(s2)} seconds")
    print(f"Fastest Time: {int(m1)} minute {int(s1)} seconds" if m1==1 else f"Fastest Time: {int(m1)} minutes {int(s1)} seconds")
    print(f"Slowest Time: {int(m)} minute {int(s)} seconds" if m==1 else f"Slowest Time: {int(m)} minutes {int(s)} seconds")
    print(f"\n\n Best Time Here: Runner #{btr}")

except ZeroDivisionError:
    #Handles the case where no input is given
    print("No data found. Nothing to do. What a pity.")
