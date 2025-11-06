from shape import Shape

class rectangle:
    def __init__(self, x: int | float, y: int | float, width: int | float, height: int | float):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def __repr__(self):
        return f"Rectangle, X-pos: {self.x}, Y-Pos: {self.y}, width: {self.width}, height: {self.height}"  