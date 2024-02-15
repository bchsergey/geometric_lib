import unittest
import math
import sys
sys.path.append("..")

from square import area, perimeter

class SquareTestCase(unittest.TestCase):        
    def test_zero_side_area(self):
        self.assertAlmostEqual(area(0), 0, delta=0.01)
        
    def test_zero_side_perimeter(self):
        self.assertAlmostEqual(perimeter(0), 0, delta=0.01)
        
    def test_positive_side_area(self):
        self.assertAlmostEqual(area(1), 1, delta=0.01)
        
    def test_positive_side_perimeter(self):
        self.assertAlmostEqual(perimeter(1), 4, delta=0.01)

    def test_negative_side_area(self):
        with self.assertRaises(TypeError):
            area(-1)
            
    def test_negative_side_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter(-1)

