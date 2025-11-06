from shape import Shape

class Rectangle(Shape):
    def __init__(self, x, y, width: int | float, height: int | float):
        super().__init__(x, y)
        #set values unique to rectangle
        self.width = width
        self.height = height    

    def __repr__(self):
        return f"Rectangle, X-pos: {self.x}, Y-Pos: {self.y}, width: {self.width}, height: {self.height}"  
    
    def __eq__(self, value): #checks rectangles height and base to see if both rectangles are of equal size
        print(self.width == self.height)

    def __lt__(self, other: Shape) -> None:
        print(self < other)