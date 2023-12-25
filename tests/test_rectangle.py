import unittest
import sys
sys.path.append("..")

from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):

    def test_zero_sides(self):
        excepted_area = 0

        length = 0
        width = 1
        
        self.assertEqual(area(length, width), excepted_area)

        length = 1
        width = 0

        self.assertEqual(area(length, width), excepted_area)

        length = 0
        width = 0

        self.assertEqual(area(length, width), excepted_area)

        length = 0
        width = 0
        excepted_perimeter = 0

        self.assertEqual(perimeter(length, width), excepted_perimeter)

    def test_positive_sides(self):
        excepted_area = 1
        excepted_perimeter = 4

        length = 1
        width = 1
        
        self.assertEqual(area(length, width), excepted_area)
        self.assertEqual(perimeter(length, width), excepted_perimeter)


    def test_negative_sides(self):
        length = -1
        width = 1


        with self.assertRaises(TypeError):
            area(length, width)
        
        with self.assertRaises(TypeError):
            perimeter(length, width)

        length = 1
        width = -1


        with self.assertRaises(TypeError):
            area(length, width)

        with self.assertRaises(TypeError):
            perimeter(length, width)

        