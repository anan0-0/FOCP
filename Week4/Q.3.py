def greet(name):
    #lname=name.lower()
    fname=name[0].upper()+name[1:].lower()
    return fname
n=greet(input("Enter a name:"))
print(f"Greetings {n}!")