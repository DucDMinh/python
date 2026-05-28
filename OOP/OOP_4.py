
class PhanSo:
    def __init__(self, tuso, mauso):
        self.tuso = tuso
        self.mauso = mauso
    def __add__(self, other):
        new_tuso = self.tuso * other.mauso + other.tuso * self.mauso
        new_mauso = self.mauso * other.mauso
        return PhanSo(new_tuso, new_mauso)
    def __str__(self):
        return f'{self.tuso}/{self.mauso}'
ps1 = PhanSo(1, 2)
ps2 = PhanSo(2, 3)

ps3 = ps1 + ps2
print(ps3)