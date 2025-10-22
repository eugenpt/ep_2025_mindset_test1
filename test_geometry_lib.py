"""
Юнит-тесты для библиотеки geometry_lib.
"""

import unittest
import math
from geometry_lib import Circle, Triangle, calc_area, Shape


class TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(
            Circle(3.5).area(),
            math.pi * 3.5 ** 2, 
            places=10
        )
    
    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(-5)


class TestTriangle(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(
            Triangle(3, 4, 5).area(), 
            6.0, 
            places=10
        )
        self.assertAlmostEqual(
            Triangle(4, 5, 3).area(), 
            6.0, 
            places=10
        )
        self.assertAlmostEqual(
            Triangle(1, 1, 1).area(), 
            math.sqrt(3) / 4, 
            places=10
        )
        self.assertAlmostEqual(
            Triangle(2, 3, 3).area(), 
            math.sqrt(8), 
            places=10
        )

    def test_invalid_sides_sum(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 10)
    
    def test_negative_side(self):
        with self.assertRaises(ValueError):
            Triangle(-3, 4, 5)

    def test_is_right(self):
        #
        self.assertTrue(Triangle(3, 4, 5).is_right())
        self.assertTrue(Triangle(4, 5, 3).is_right())
        self.assertTrue(Triangle(5, 3, 4).is_right())
        self.assertTrue(Triangle(5, 12, 13).is_right())
        self.assertTrue(Triangle(8, 15, 17).is_right())
        #
        self.assertFalse(Triangle(3, 4, 5.1).is_right())
        self.assertFalse(Triangle(10, 10, 10).is_right())
        self.assertFalse(Triangle(10, 10, 10).is_right())


class TestPolymorphism(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(
            calc_area(Circle(5)), 
            math.pi * 5**2, 
            places=10
        )
    
    def test_triangle_area(self):
        self.assertAlmostEqual(
            calc_area(Triangle(3, 4, 5)), 
            6.0, 
            places=10
        )


if __name__ == '__main__':
    unittest.main()