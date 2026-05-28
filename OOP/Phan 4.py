class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

vect1= Vector2D(1, 2)
vect2= Vector2D(1, 2)
print(vect1)
print(vect2)
print(vect1 + vect2)
print(vect1 == vect2)
