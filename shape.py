#base script for shape creation and editing

class shape:
    def __init__(self, x: int | float, y: int | float): #Each shape will have x and y pos values
        self.x = x
        self.y = y