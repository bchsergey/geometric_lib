def area(a, h):
	'''takes length a and height h, returns area of a rectangle with given length and height
		
		Parameters:
			a (float): length
			h (float): height
			
		Return value:
			area (float) : area of triangle
	'''
	
	if a < 0 or h < 0:
		raise TypeError
		
	return a * h / 2

def perimeter(a, b, c):
	'''takes sides a, b, c, returns perimeter of a square with given sides
		
		Parameters:
			a (float): first side
			b (float): second side
			c (float): third side
			
		Return value:
			perimeter (float) : area of triangle
	'''
	
	if a < 0 or b < 0 or c < 0:
		raise TypeError
		
	if a == 0 or b == 0 or c == 0:
		return 0
		
	return a + b + c


