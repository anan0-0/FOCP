# The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is usually 24 students, but this is
# sometimes varied to create groups of similar size. Write a program that prompts for
# the number of students and group size, and then displays how many groups will be
# needed and how many will be left over in a smaller group.
# How many students? 113
# Required group size? 22
# There will be 5 groups with 3 students left over.
# For bonus credit, see if you can fix the grammar in the output. So if there were 101
# students in groups of 20 the output would be:
# There will be 5 groups with 1 student left over.
stu=int(input("How many students? "))
grpsize=int(input("Required group size? "))
grps=stu//grpsize
left=stu%grpsize
print("If there are %d students in groups of %d,"%(stu,grpsize))
if (grps>1 and left>1):
    print("There will be %d groups with %d students left over."%(grps,left))
elif (grps>1):
    print("There will be %d groups with %d student left over."%(grps,left))
elif (left>1):
    print("There will be %d group with %d students left over."%(grps,left))
else:
    print("There will be %d group with %d student left over."%(grps,left))
