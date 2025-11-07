from shape import Shape

class Rectangle(Shape):
    """Represents a rectangle with x and y positions, width and height"""
    def __init__(self, x, y, width: int | float, height: int | float) -> None:
        super().__init__(x, y)
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError(f"Values {width} and {height} must be of type int or float")
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height    

    @property
    def area(self):
        return self.height * self.width

    @property
    def perimeter(self):
        return 2 * (self.height + self.width)

    def is_square(self): #returns if the width and height values of rectangle match
        return self.width == self.height

    def __repr__(self):
        return f"(Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height}, area={self.area}))"  
    
    def __str__(self):
        return f"Rectangle with X-pos: {self.x}, Y-Pos: {self.y}, width: {self.width}, height: {self.height}, area={self.area}"  