import unittest
import math
import sys
sys.path.append("..")

from circle import area, perimeter

class CircleTestCase(unittest.TestCase):

    def test_zero_radius_area(self):
        radius = 0

        excepted_area = 0
        
        self.assertAlmostEqual(area(radius), excepted_area, delta=1e-6)
        
    def test_zero_radius_perimeter(self):
        radius = 0

        excepted_perimeter = 0
        
        self.assertAlmostEqual(perimeter(radius), excepted_perimeter, delta=1e-6)

    def test_positive_radius_area(self):
        radius = 1

        excepted_area = math.pi;
        
        self.assertAlmostEqual(area(radius), excepted_area, delta=1e-6)
        
    def test_positive_radius_perimeter(self):
        radius = 1

        excepted_perimeter = 2 * math.pi
        
        self.assertAlmostEqual(perimeter(radius), excepted_perimeter, delta=1e-6)

    def test_negative_radius_area(self):
        radius = -1

        with self.assertRaises(TypeError):
            area(radius)

    def test_negative_radius_perimeter(self):
        radius = -1
        
        with self.assertRaises(TypeError):
            perimeter(radius)

