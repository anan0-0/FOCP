# When processing data it is often useful to remove the last character from some
# input (it is often a newline). Write and test a function that takes a string parameter
# and returns it with the last character removed. (If the string contains one or fewer
# characters, return it unchanged.)
def name(a):
    if len(a)>4:
        return (a[:(len(a)-1)])
    else:
        return a
print(name("s"))