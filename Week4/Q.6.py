def temp(deg,cof):
    if cof.lower()=="c":
        return (deg*(9/5)+32),"F"
    elif cof.lower()=="f":
        return ((deg-32)*(5/9)),"C"
d=(input("Enter temperature in (c/f): "))
tem=float(d[:len(d)-1])
tempna=(d[-1])

#cof=input("Celsius or fahrenheit (C/F): ")
tempe,tempn=temp(tem,tempna)
print(f"{tem} {tempna.upper()} to {tempe} {tempn}")