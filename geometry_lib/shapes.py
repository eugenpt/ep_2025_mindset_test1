"""
Библиотека для вычисления площадей геометрических фигур.
"""

from abc import ABC, abstractmethod
from math import pi as PI

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
        return PI * self.radius ** 2
    
    def __repr__(self):
        return f"Circle(radius={self.radius})"
