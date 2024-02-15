import unittest
import math
import sys
sys.path.append("..")

from circle import area, perimeter

class CircleTestCase(unittest.TestCase):

    def test_zero_radius_area(self):
        self.assertAlmostEqual(area(0), 0, delta=0.01)
        
    def test_zero_radius_perimeter(self):        
        self.assertAlmostEqual(perimeter(0), 0, delta=0.01)

    def test_positive_radius_area(self):
        self.assertAlmostEqual(area(1), 3.14, delta=0.01)
        
    def test_positive_radius_perimeter(self):
        self.assertAlmostEqual(perimeter(1), 6.28, delta=0.01)

    def test_negative_radius_area(self):
        with self.assertRaises(TypeError):
            area(-1)

    def test_negative_radius_perimeter(self):        
        with self.assertRaises(TypeError):
            perimeter(-1)

