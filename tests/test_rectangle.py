import unittest
import sys
sys.path.append("..")

from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):

    def test_zero_length_area(self):
        length = 0
        width = 1
        
        excepted_area = 0
        
        self.assertAlmostEqual(area(length, width), excepted_area, delta=1e-6)
        
    def test_zero_length_perimeter(self):
        length = 1
        width = 0
        
        excepted_perimeter = 0
        
        self.assertAlmostEqual(perimeter(length, width), excepted_perimeter, delta=1e-6)
        
    def test_zero_width_area(self):
        length = 1
        width = 0
        
        excepted_area = 0
        
        self.assertAlmostEqual(area(length, width), excepted_area, delta=1e-6)
        
    def test_zero_width_perimeter(self):
        length = 0
        width = 1
        
        excepted_perimeter = 0
        
        self.assertAlmostEqual(perimeter(length, width), excepted_perimeter, delta=1e-6)
        
    def test_zero_sides_area(self):
        length = 0
        width = 0
        
        excepted_area = 0
        
        self.assertAlmostEqual(area(length, width), excepted_area, delta=1e-6)
        
    def test_zero_sides_perimeter(self):
        length = 0
        width = 0
        
        excepted_perimeter = 0
        
        self.assertAlmostEqual(perimeter(length, width), excepted_perimeter, delta=1e-6)

    def test_positive_sides_area(self):
        length = 1
        width = 1
        
        excepted_area = 1
        
        self.assertAlmostEqual(area(length, width), excepted_area, delta=1e-6)

    def test_positive_sides_perimeter(self):
        length = 1
        width = 1
        
        excepted_perimeter = 4
        
        self.assertAlmostEqual(perimeter(length, width), excepted_perimeter, delta=1e-6)

    def test_negative_length_area(self):
        length = -1
        width = 1


        with self.assertRaises(TypeError):
            area(length, width)

    def test_negative_length_perimeter(self):
        length = -1
        width = 1


        with self.assertRaises(TypeError):
            perimeter(length, width)
                        
    def test_negative_width_area(self):
        length = 1
        width = -1


        with self.assertRaises(TypeError):
            area(length, width)

    def test_negative_length_perimeter(self):
        length = 1
        width = -1


        with self.assertRaises(TypeError):
            perimeter(length, width)

