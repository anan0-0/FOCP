import sys
if bool(sys.argv[1:])==True:
    count = len(sys.argv)
    total = 0
    while count > 1:
        count -= 1
        total += float(sys.argv[count])
    print("Total is", total)
    print("Average is",total//len(sys.argv[1:]))
else:
    print("No arguments were passed.")