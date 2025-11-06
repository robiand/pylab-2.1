class Shape:
    def __init__(self, x = 0.0, y = 0.0): #Each shape will have x and y pos values
        self.x = x
        self.y = y

    def translate(self, x, y): #used to "move" shapes by changing their x and y values
        self.x += x
        self.y += y

    def __repr__(self):
        return f"(Shape(x={self.x}, y={self.y}))"
    
    def __str__(self):
        return f"Shape with coordinates: {self.x}, {self.y}"