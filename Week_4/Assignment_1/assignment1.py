
# No other modules apart from 'math' need to be imported
# as they aren't required to solve the assignment

# Import required module/s
import math


def computeDistance(x1, y1, x2, y2):
	"""Computes Euclidean distance between two points with precision upto 3 decimal places and prints it to STDOUT.

	Parameters
	----------
	x1 : float
		X-coordinate of 1st point
	y1 : float
		Y-coordinate of 1st point
	x2 : float
		X-coordinate of 2nd point
	y2 : float
		Y-coordinate of 2nd point
	
	Example
	-------
	>>> x1 = 1; y1 = 4
	>>> x2 = 4; y2 = 1
	>>> computeDistance( x1, y1, x2, y2 )
	Distance computed: 4.243
	"""
	
	##############	ADD YOUR CODE HERE	##############
	
	res = math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))
	print("Distance computed:",format(res,".3f"))
	##################################################


if __name__ == "__main__":
	"""Main function, code begins here
	"""
	x1 = 5.2; y1 = 10.1
	x2 = 5.0; y2 = 10.1
	computeDistance(x1, y1, x2, y2)
