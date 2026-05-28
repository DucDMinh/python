import pandas as pd

sinhvien = {"Alice": 85, "Bod": 72, "Charlie": 90, "David": 68, "Emma": 95}
my_series = pd.Series(sinhvien)
my_series["Frank"] = 88
print(my_series)
print(f"Diem trung binh cua sinh vien: {my_series.mean()}")
print(f"Sinh vien co diem cao nhat: {my_series.idxmax()}")
print(f"Sinh vien co diem thap nhat: {my_series.idxmin()}")
