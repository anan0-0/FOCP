import math
months=["January","February","March","April","May","June","July","August","September","October","November","December"]
rain=[]
x=0
for i in months:
    a=input(f"Enter rainfall for {i}(in mm): ")
    rain.append(int(a[:-2]))
print(f"Max Rainfall: {max(rain)} mm in {months[rain.index(max(rain))]}.")
print(f"Min Rainfall: {min(rain)} mm in {months[rain.index(min(rain))]}.")
avg=sum(rain)/12
print(f"Average: {avg} mm.")
for j in rain:
    x+=(j-avg)**2
std=math.sqrt(x/(12-1))
print(f"Standard Deviation: {std} mm.")    
