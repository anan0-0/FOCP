name=input("Greetings! How shall we call you? ")
title=name.split()[0]
if (title.lower()=="lady") or (title.lower()=="lord"):
    print("It shall be so, %s!"%name.capitalize())
else:
    print("You may not be known by that name!")