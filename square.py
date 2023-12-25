def area(a):
	'''takes length a, returns area of a square with given length
		
		Parameters:
			a (float) : length
			
		Return value:
			area (float) : area of a square
	'''

	if a < 0:
		raise TypeError
		
	return a * a


def perimeter(a):
	'''takes length a, returns perimeter of a square with given length
		
		Parameters:
			a (float): length
			
		Return value:
			perimeter (float) : area of square
	'''
	
	if a < 0:
		raise TypeError
		
	return 4 * a
