import math
from shape import Shape

class Circle(Shape):
    def __init__(self, x, y, radius: int | float) -> Shape:
        super().__init__(x, y)
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius**2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    def is_unit(self):
        if not isinstance(self, Circle):
            raise TypeError(f"Object {self} is not a circle")
        """Returns if the circle is a unit circle or not, requires radius of 1 and x and y values of 0"""
        return self.radius == 1 and self.x == 0 and self.y == 0

    def __repr__(self):
        return f"(Circle(x={self.x}, y={self.y}, radius={self.radius}, area={self.area}, perimeter={self.perimeter})"  
    
    def __str__(self):
        return f"Circle, X-pos: {self.x}, Y-Pos: {self.y}, Radius: {self.radius}, Area: {self.area}, Perimeter: {self.perimeter}"
