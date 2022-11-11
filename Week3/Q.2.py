# Write a program that simulates the way in which a user might choose a password.
# The program should prompt for a new password, and then prompt again. If the two
# passwords entered are the same the program should say "Password Set" or
# similar, otherwise it should report an error. 
import getpass
pw=getpass.getpass("Enter the password: ")
pw1=getpass.getpass("Enter the password again: ")
if pw==pw1:
    print("Password set")
else:
    print("Password does not match")
    