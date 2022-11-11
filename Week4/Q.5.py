# Write and test a function that converts a temperature measured in degrees
# centigrade into the equivalent in fahrenheit, and another that does the reverse
# conversion. Test both functions. (Google will find you the formulae)
def cel(deg):
        return (deg*(9/5)+32)
def fah(deg):
        return ((deg-32)*(5/9))
d=float(input("Enter temperature: "))
cof=input("Celsius or fahrenheit (C/F): ")
if cof=="c":
    print(f"{d} to {cel(d)}")
elif cof=="f":
    print(f"{d} to {fah(d)}")