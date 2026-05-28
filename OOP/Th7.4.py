class Tam_thuc:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        return f'{self.a}x^2 + {self.b}x + {self.c}'
    def __neg__(self):
        return Tam_thuc(-self.a, -self.b, -self.c)
    def __add__(self, other):
        return Tam_thuc(self.a + other.a, self.b + other.b, self.c + other.c)
    def __sub__(self, other):
        return Tam_thuc(self.a - other.a, self.b - other.b, self.c - other.c)
tt1 = Tam_thuc(1, 2, 3)
tt2 = Tam_thuc(4, 5, 6)
tt3 = tt1 + tt2
tt4 = tt1 - tt2
print(-tt1)
print(-tt2)
print(tt3)
print(tt4)