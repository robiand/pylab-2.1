from shape import Shape

class Rectangle(Shape):
    def __init__(self, x, y, width: int | float, height: int | float) -> Shape:
        super().__init__(x, y)
        #set values unique to rectangle
        self.width = width
        self.height = height    

    @property
    def area(self):
        return self.height * self.width

    @property
    def perimeter(self):
        return 2 * (self.height + self.width)

    def is_square(self): #returns if the width and height values of rectangle match
        if not isinstance(self, Rectangle):
            raise TypeError(f"Object {self} is not a rectangle")
        return self.width == self.height

    def __repr__(self):
        return f"(Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height}, area={self.area})"  
    
    def __str__(self):
        return f"Rectangle with X-pos: {self.x}, Y-Pos: {self.y}, width: {self.width}, height: {self.height}, area={self.area}"  