import pandas as pd
class Person:
    def __init__(self, name, dob, hometown):
        self.name = name
        self.dob = dob
        self.hometown = hometown
class Engineer(Person):
    def __init__(self, name, dob, hometown, major, yearGraduate):
        super().__init__(name, dob, hometown)
        self.major = major
        self.yearGraduate = yearGraduate
    def display(self):
        print(f"{self.name}, {self.dob}, {self.major}, {self.yearGraduate}")
n = int(input("Nhap so luong ky su: "))
ds = []
for i in range(n):
    name = input("Nhap ten: ")
    dob = input("Nhap ngay sinh: ")
    hometown = input("Nhap que quan: ")
    major = input("Nhap chuyen nganh: ")
    yearGraduate = input("Nhap nam tot nghiep: ")
    print('-' * 50)
    eng = Engineer(name, dob, hometown, major, yearGraduate)
    ds.append(eng)

data = [vars(ks) for ks in ds]

df = pd.DataFrame(data)

print(df)
print('-' * 50)
if ds:
    nam_max = max(eng.yearGraduate for eng in ds)
    print(f"Ky su tot nghiep gan day nhat (Nam {nam_max})")
    for eng in ds:
        if eng.yearGraduate == nam_max:
            eng.display()

