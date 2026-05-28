import pandas as pd

data = {'Tên cầu thủ': ['Messi', 'Ronaldo', 'Neymar'],
        'Độ tuổi': [34, 37, 30],
        'Vị trí': ['Tiền đạo', 'Tiền đạo', 'Tiền vệ']}

df = pd.DataFrame(data)
address = ['New York', 'London', 'Sydney']
df['Địa chỉ'] = address
df.loc[len(df.index)] = ['Lukaku', 4324, 'Hậu vệ', 'Tokyo']
print("------------------------------------------")
print(df)
print("------------------------------------------")
print(df.head(1))
print("------------------------------------------")
print(df.tail(2))