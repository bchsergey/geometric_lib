import unittest
import math
import sys
sys.path.append("..")

from circle import area, perimeter

class CircleTestCase(unittest.TestCase):

    def test_zero_radius(self):
        radius = 0
        excepted_area = 0
        excepted_perimeter = 0

        self.assertEqual(area(radius), excepted_area)
        self.assertEqual(perimeter(radius), excepted_perimeter)

    def test_positive_radius(self):
        radius = 1
        excepted_area = math.pi;
        excepted_perimeter = 2 * math.pi
        
        self.assertEqual(area(radius), excepted_area)
        self.assertEqual(perimeter(radius), excepted_perimeter)

    def test_negative_radius_area(self):
        radius = -1

        with self.assertRaises(TypeError):
            area(radius)

        with self.assertRaises(TypeError):
            perimeter(radius)
