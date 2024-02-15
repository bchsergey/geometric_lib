import unittest
import math
import sys
sys.path.append("..")

from square import area, perimeter

class SquareTestCase(unittest.TestCase):        
    def test_zero_side_area(self):
        side = 0

        excepted_area = 0

        self.assertAlmostEqual(area(side), excepted_area, delta=1e-6)
        
    def test_zero_side_perimeter(self):
        side = 0
 
        excepted_perimeter = 0

        self.assertAlmostEqual(perimeter(side), excepted_perimeter, delta=1e-6)
        
    def test_positive_side_area(self):
        side = 1

        excepted_area = 1

        self.assertAlmostEqual(area(side), excepted_area, delta=1e-6)
        
    def test_positive_side_perimeter(self):
        side = 1

        excepted_perimeter = 4

        self.assertAlmostEqual(perimeter(side), excepted_perimeter, delta=1e-6)

    def test_negative_side_area(self):
        side = -1

        with self.assertRaises(TypeError):
            area(side)
            
    def test_negative_side_perimeter(self):
        side = -1

        with self.assertRaises(TypeError):
            perimeter(side)

