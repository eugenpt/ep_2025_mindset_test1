# Задание:


> # Практическое задание 1.
> Напишите на C# или Python библиотеку для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам. 
>
> Дополнительно к работоспособности оценим:
> - Юнит-тесты
> - Легкость добавления других фигур
> - Вычисление площади фигуры без знания типа фигуры в compile-time
> - Проверку на то, является ли треугольник прямоугольным


# Установка

```bash
pip install -e .
```

# Быстрый старт

```python
from geometry_lib import Circle, Triangle, calc_area

# Создание и вычисление площади круга
circle = Circle(radius=5)
print(f"Площадь круга: {circle.area():.2f}")  # 78.54

# Создание и вычисление площади треугольника
triangle = Triangle(3, 4, 5)
print(triangle)
print(f"Площадь треугольника: {triangle.area()}")  # 6.0

# Проверка на прямоугольность
if triangle.is_right():
    print("Треугольник прямоугольный!")  # Выведется

# Полиморфное использование
shapes = [
    Circle(10),
    Triangle(3, 4, 5)
]

for shape in shapes:
    print(f"{shape}: площадь = {calc_area(shape):.2f}")
```

# Запуск тестов

```bash
python -m unittest test_geometry_lib.py -v
```

# Добавление новых фигур

1. Унаследуйтесь от базового класса Shape
2. Реализуйте метод area()

```python
from geometry_lib import Shape

class Square(Shape):
    def __init__(self, side):
        if side < 0:
            raise ValueError("Сторона не может быть отрицательной")
        self.side = side
    
    def area(self) -> float:
        return self.side ** 2
```