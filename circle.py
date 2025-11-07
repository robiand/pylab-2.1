import math
from shape import Shape

class Circle(Shape):
    """Represents a circle with x and y positions and radius"""
    def __init__(self, x, y, radius: int | float) -> None:
        super().__init__(x, y)
        if not isinstance(radius, (int, float)):
            raise TypeError(f"Value {radius} must be of type int or float")
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius**2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    def is_unit(self):
        """Returns true if circle is a unit circle (radius of 1, x and y values of 0)"""
        return self.radius == 1 and self.x == 0 and self.y == 0

    def __repr__(self):
        return f"(Circle(x={self.x}, y={self.y}, radius={self.radius}, area={self.area}, perimeter={self.perimeter}))"  
    
    def __str__(self):
        return f"Circle, X-pos: {self.x}, Y-Pos: {self.y}, Radius: {self.radius}, Area: {self.area}, Perimeter: {self.perimeter}"
