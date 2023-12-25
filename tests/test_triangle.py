import unittest
import sys
sys.path.append("..")

from triangle import area, perimeter

class RectangleTestCase(unittest.TestCase):

    def test_zero_sides(self):
        excepted_area = 0

        length = 0
        height = 1
        
        self.assertEqual(area(length, height), excepted_area)

        length = 1
        height = 0

        self.assertEqual(area(length, height), excepted_area)


        length = 0
        height = 0

        self.assertEqual(area(length, height), excepted_area)

        excepted_perimeter = 0

        side_one = 0
        side_two = 0
        side_three = 0


        self.assertEqual(perimeter(side_one, side_two, side_three), excepted_perimeter)

    def test_positive_sides(self):
           excepted_area = 1

           length = 1
           height = 2

           self.assertEqual(area(length, height), excepted_area)

           excepted_perimeter = 3

           side_one = 1
           side_two = 1
           side_three = 1

           self.assertEqual(perimeter(side_one, side_two, side_three), excepted_perimeter)

    def test_negative_sides(self):
            length = 1
            height = -1

            with self.assertRaises(TypeError):
                area(length, height)

            length = -1
            height = 1

            with self.assertRaises(TypeError):
                area(length, height)

            length = -1
            height = -1

            with self.assertRaises(TypeError):
                area(length, height)

            side_one = 1
            side_two = 1
            side_three = -1

            with self.assertRaises(TypeError):
                perimeter(side_one, side_two, side_three)

            side_one = 1
            side_two = -1
            side_three = 1

            with self.assertRaises(TypeError):
                perimeter(side_one, side_two, side_three)

            side_one = -1
            side_two = 1
            side_three = 1

            with self.assertRaises(TypeError):
                perimeter(side_one, side_two, side_three)

            side_one = -1
            side_two = -1
            side_three = -1

            with self.assertRaises(TypeError):
                perimeter(side_one, side_two, side_three)
