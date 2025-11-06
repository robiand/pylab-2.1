from shape import Shape

class rectangle:
    def __init__(self, x: int | float, y: int | float, width: int | float, height: int | float):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.area = self.width * self.height
    

    def __repr__(self):
        return f"Rectangle, X-pos: {self.x}, Y-Pos: {self.y}, width: {self.width}, height: {self.height}"  
    
    def __eq__(self, value): #checks rectangle area to see if both rectangles are of equal size
        print(self.area)

    def __lt__(self, other: Shape) -> None:
        print(self < other)