def average(values):
    """ Calculates the average of the given list. """
    total = 0;
    for n in values:        	# total the given values
        total += float(n)   	 
    return total/len(values)	# return calculated average

# initialisation statement
print("Welcome, utils module has been imported and initialised!")
import sys
if len(sys.argv) > 1:
    print("Average=",average(sys.argv[1:]))

