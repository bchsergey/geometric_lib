import unittest
import sys
sys.path.append("..")

from triangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_zero_length_area(self):
        length = 0
        height = 1
        
        excepted_area = 0

        self.assertAlmostEqual(area(length, height), excepted_area)
        
    def test_zero_height_area(self):
        length = 0
        height = 1
        
        excepted_area = 0
        
        self.assertAlmostEqual(area(length, height), excepted_area)
        
    def test_zero_sides_area(self):
        length = 0
        height = 0
        
        excepted_area = 0
        
        self.assertAlmostEqual(area(length, height), excepted_area)
        
    def test_zero_sides_perimeter(self):
        side_one = 0
        side_two = 0
        side_three = 0
        
        excepted_perimeter = 0

        self.assertEqual(perimeter(side_one, side_two, side_three), excepted_perimeter)

    def test_positive_sides_area(self):
        length = 1
        height = 2
        
        excepted_area = 1

        self.assertAlmostEqual(area(length, height), excepted_area)
           
    def test_positive_sides_perimeter(self):
        side_one = 1
        side_two = 1
        side_three = 1
        
        excepted_perimeter = 3
        
        self.assertAlmostEqual(perimeter(side_one, side_two, side_three), excepted_perimeter)

    def test_negative_height_area(self):
            length = 1
            height = -1

            with self.assertRaises(TypeError):
                area(length, height)

    def test_negative_length_area(self):
            length = -1
            height = 1

            with self.assertRaises(TypeError):
                area(length, height)
                
    def test_negative_sides_area(self):
            length = -1
            height = -1

            with self.assertRaises(TypeError):
                area(length, height)

    def test_negative_first_side_perimeter(self):
            side_one = -1
            side_two = 1
            side_three = 1

            with self.assertRaises(TypeError):
                perimeter(side_one, side_two, side_three)

                
    def test_negative_second_side_perimeter(self):
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
                
    def test_negative_sides_perimeter(self):
            side_one = -1
            side_two = -1
            side_three = -1

            with self.assertRaises(TypeError):
                perimeter(side_one, side_two, side_three)

