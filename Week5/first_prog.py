#The statement below reads the number given by user.
number = input("Enter a number: ")
#The statement below converts str in numbers variable to int.
number = int(number)
#The statement below prints the number entered.
print("The numbered entered was", number)
#The statement block below checks weather the number is even or not. 
if (number % 2) == 0:
	print("That is an even number")
	if (number%10)==0:
		print("That is divisible by 10")
	else:
		print("That is not divisible by 10")
else:
	print("That is an odd number")
