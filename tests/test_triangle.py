import unittest
import sys
sys.path.append("..")

from triangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_zero_length_area(self):
        self.assertAlmostEqual(area(0, 1), 0, delta=0.01)
        
    def test_zero_height_area(self):
        self.assertAlmostEqual(area(0, 1), 0, delta=0.01)
        
    def test_zero_sides_area(self):        
        self.assertAlmostEqual(area(0, 0), 0, delta=0.01)
        
    def test_zero_sides_perimeter(self):
        self.assertAlmostEqual(perimeter(0, 0, 0), 0, delta=0.01)

    def test_positive_sides_area(self):
        self.assertAlmostEqual(area(1, 2), 1, delta=0.01)
           
    def test_positive_sides_perimeter(self):
        self.assertAlmostEqual(perimeter(1, 1, 1), 3, delta=0.01)

    def test_negative_height_area(self):
            with self.assertRaises(TypeError):
                area(1, -1)

    def test_negative_length_area(self):
            with self.assertRaises(TypeError):
                area(-1, 1)
                
    def test_negative_sides_area(self):
            with self.assertRaises(TypeError):
                area(-1, -1)

    def test_negative_first_side_perimeter(self):
            with self.assertRaises(TypeError):
                perimeter(-1, 1, 1)

                
    def test_negative_second_side_perimeter(self):
            with self.assertRaises(TypeError):
                perimeter(1, -1, 1)
                
    def test_negative_third_side_perimeter(self):
            with self.assertRaises(TypeError):
                perimeter(1, 1,-1)

                
    def test_negative_sides_perimeter(self):
            with self.assertRaises(TypeError):
                perimeter(-1, -1, -1)

