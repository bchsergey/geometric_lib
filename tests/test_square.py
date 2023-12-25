import unittest
import math
import sys
sys.path.append("..")

from square import area, perimeter

class SquareTestCase(unittest.TestCase):

    def test_zero_side(self):
        radius = 0
        excepted_area = 0
        excepted_perimeter = 0

        self.assertEqual(area(radius), excepted_area)
        self.assertEqual(perimeter(radius), excepted_perimeter)

    def test_positive_side(self):
        radius = 1
        excepted_area = 1
        excepted_perimeter = 4
        
        self.assertEqual(area(radius), excepted_area)
        self.assertEqual(perimeter(radius), excepted_perimeter)

    def test_negative_side(self):
        radius = -1

        with self.assertRaises(TypeError):
            area(radius)

        with self.assertRaises(TypeError):
            perimeter(radius)
