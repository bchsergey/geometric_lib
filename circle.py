import math


def area(r):
	'''takes radius r, returns area of a circle with given radius
		
		Parameters:
			r (float) : radius
			
		Return value:
			area (float) : area of a circle
	'''
	
	if r < 0:
		raise TypeError
		
	return math.pi * r * r


def perimeter(r):
	'''takes radius r, returns perimeter of a circle with given radius
		
		Parameters:
			r (float) : radius
			
		Return value:
			area (float) : area of a circle
	'''
	
	if r < 0:
		raise TypeError
		
	return 2 * math.pi * r

