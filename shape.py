class Shape:
    def __init__(self, x = 0.0, y = 0.0): #Each shape will have x and y pos values
        """Creates a base shape with x and y coordinates"""
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError(f"Values {x} and {y} must be of type int or float")
        self.x = x
        self.y = y

    def translate(self, dx, dy): #used to "move" shapes by changing their x and y values
        """Move a shape by adding dx and dy to coordinates"""
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise TypeError(f"Values {dx} and {dy} must be of type int or float")
        self.x += dx
        self.y += dy

    def __repr__(self):
        return f"(Shape(x={self.x}, y={self.y}))"
    
    def __str__(self):
        return f"Shape with coordinates: {self.x}, {self.y}"
    
    #functions to compare the area of two shapes
    def __eq__(self, other) -> None:
        if not isinstance(other, Shape):
            raise TypeError(f"Both objects must be shapes")
        return self.area == other.area

    def __lt__(self, other) -> None:
        if not isinstance(other, Shape):
            raise TypeError(f"Both objects must be shapes")
        return self.area < other.area

    def __gt__(self, other) -> None:
        if not isinstance(other, Shape):
            raise TypeError(f"Both objects must be shapes")
        return self.area > other.area
        
    def __le__(self, other) -> None:
        if not isinstance(other, Shape):
            raise TypeError(f"Both objects must be shapes")
        return self.area <= other.area
    
    def __ge__(self, other) -> None:
        if not isinstance(other, Shape):
            raise TypeError(f"Both objects must be shapes")
        return self.area >= other.area