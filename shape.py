#base script for shape creation and editing

class Shape:
    def __init__(self, x: int | float, y: int | float): #Each shape will have x and y pos values
        self.x = x
        self.y = y

    def translate(self, x, y): #used to "move" shapes by changing their x and y values
        self.x += x
        self.y += y
