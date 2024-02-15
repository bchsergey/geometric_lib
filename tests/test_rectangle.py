import unittest
import sys
sys.path.append("..")

from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):

    def test_zero_length_area(self):        
        self.assertAlmostEqual(area(0, 1), 0, delta=0.01)
        
    def test_zero_length_perimeter(self):        
        self.assertAlmostEqual(perimeter(1, 0), 0, delta=0.01)
        
    def test_zero_width_area(self):        
        self.assertAlmostEqual(area(1, 0), 0, delta=0.01)
        
    def test_zero_width_perimeter(self):       
        self.assertAlmostEqual(perimeter(0, 1), 0, delta=0.01)
        
    def test_zero_sides_area(self):        
        self.assertAlmostEqual(area(0, 0), 0, delta=0.01)
        
    def test_zero_sides_perimeter(self):
        self.assertAlmostEqual(perimeter(0, 0), 0, delta=0.01)

    def test_positive_sides_area(self):
        self.assertAlmostEqual(area(1, 1), 1, delta=0.01)

    def test_positive_sides_perimeter(self):
        self.assertAlmostEqual(perimeter(1, 1), 4, delta=0.01)

    def test_negative_length_area(self):
        with self.assertRaises(TypeError):
            area(-1, 1)

    def test_negative_length_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter(-1, 1)
                        
    def test_negative_width_area(self):
        with self.assertRaises(TypeError):
            area(1, -1)

    def test_negative_width_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter(1, -1)

