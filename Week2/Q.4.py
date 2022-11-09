# A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
# first count the sweets and then divide them according to how many pupils attend
# that day. Write a program that will tell the teacher how many sweets to give to each
# pupil, and how many she will have left over.
sweets=int(input("How many sweets? "))
pupils=int(input("How many students? "))
div=sweets//pupils
left=sweets%pupils
print("If there are %d sweets and %d students,"%(sweets,pupils))
print("Then each pupils will get %d sweets and teacher will be left with %d sweets."%(div,left))