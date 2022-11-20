from sys import argv
a=argv[1]
f_in=open(a,"r")
f_out=open("copy.txt","w+")
f_in.seek(0)
lines=f_in.readlines()
for i in range(len(lines)):
    f_out.write(lines[i])
f_in.close()
f_out.close()
# from shutil import copyfile
# from sys import argv
# ori=argv[1]
# fn, exe=ori.split(".")
# copied=f"{fn}(copy).{exe}"
# copyfile(ori,copied)