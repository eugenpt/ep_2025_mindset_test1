"""
Библиотека для вычисления площадей геометрических фигур.
"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Абстрактный базовый класс фигуры"""
    
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def __repr__(self):
        return f"Circle(radius={self.radius})"

class Triangle(Shape):
    def __init__(self, a, b, c):
        if a < 0 or b < 0 or c < 0:
            raise ValueError('Стороны не могут быть отрицательными')

        if not (
            (a + b > c)
            and (a + c > b)
            and (b + c > a)
        ):
            raise ValueError("Не выполнено неравенство треугольника")

        self.a = a
        self.b = b
        self.c = c

    def area(self):
        semi_perimeter = (self.a + self.b + self.c) / 2
        area_squared = (semi_perimeter * 
                       (semi_perimeter - self.a) * 
                       (semi_perimeter - self.b) * 
                       (semi_perimeter - self.c))
        return math.sqrt(area_squared)

    def is_right(self, eps=1e-10):
        sides = sorted([self.a, self.b, self.c])
        return abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < eps

    def __repr__(self):
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"

def calc_area(shape: Shape):
    """
    Вычисляет площадь без знания типа фигуры в compile-time
    """
    return shape.area()