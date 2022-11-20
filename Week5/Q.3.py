import sys
a=sys.argv[1:]
a.sort(key=len)
print(a[0])