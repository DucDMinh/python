class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def perimeter(self):
        return self.width + self.height
    def area(self):
        return self.width * self.height
    def display(self):
        return f"Rectangle information: {self.width} x {self.height}, Perimeter: {self.perimeter()}, Area: {self.area()}"

rect1 = Rectangle(10,20)
print(rect1.display())