# The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is 24 students, since this is the
# number of PCs in a lab. Write a program that calculates how many groups are
# needed for the following number of students: 113, 175, 12. Display how many full
# groups there will be, and how many students will be in the smaller "left over"
# group.
Lg=24
full=0
Num=[113,175,12]
left=0
for i in range(len(Num)):
    grp=Num[i]//24
    full=full+grp
    grp2=Num[i]%24
    left=left+grp2
print("Full group=%d"%full)
print("Leftover group=%d"%(left//24))
print("Students in Leftover group=%d"%left)
