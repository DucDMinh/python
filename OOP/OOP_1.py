
class Shape():
    def __init__(self, color):
        self.color = color
    def draw(self):
        pass
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    def draw(self):
        print(f'Draw a {self.color} Rectangle with {self.width} x {self.height}')

rectangle = Rectangle("blue", 5, 10)
rectangle.draw()