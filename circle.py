import math
from shape import Shape

class Circle(Shape):
    def __init__(self, x, y, radius: int | float) -> Shape:
        super().__init__(x, y)
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius**2

    def is_unit(self):
        """Returns if the circle is a unit circle or not, requires radius of 1 and x and y values of 0"""
        return self.radius == 1 and self.x == 0 and self.y == 0

    def __eq__(self, value):
        return super().__eq__(value)

    def __lt__(self, value) -> None:
        return self.radius < value.radius

    def __repr__(self):
        return f"(Circle(x={self.x}, y={self.y}, radius={self.radius}"  
    
    def __str__(self):
        return f"Circle, X-pos: {self.x}, Y-Pos: {self.y}, Radius: {self.radius}"
