from shape import Shape

class Circle(Shape):
    def __init__(self, x: int | float, y: int | float, radius: int | float):
        self.x = x
        self.y = y
        self.radius = radius

    def __repr__(self):
        return f"Circle, X-pos: {self.x}, Y-Pos: {self.y}, Radius: {self.radius}"