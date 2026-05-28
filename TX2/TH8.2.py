import pandas as pd

data = {'ProductID': (1, 2, 3, 4, 5),
        'ProductName': ('Laptop', 'Smartphone', 'Desk', 'Chair', 'Notebook'),
        'Category': ('Electronics', 'Electronics', 'Furniture', 'Furniture', 'Stationery'),
        'Price': (1200, 800, 150, 80, 5),
        'Stock': (15, 30, 10, 50, 100)}
df = pd.DataFrame(data)
print(df)
print('-' * 30)
print('Add Total_Value')
df['Total_Value'] = df['Price'] * df['Stock']
print(df)
print('-' * 30)
print("Sort")
df.sort_values(by=['Price'], ascending=True, inplace=False)
print(df)
print('-' * 30)
print('Max Stock')
print(df.loc[df['Stock'].idxmax()])
print('-' * 30)
print('Groupby')
print(df.groupby('Category')['Stock'].sum())
print('-' * 30)
print('String')
print(df.loc[df['ProductName'].str.contains('book', case=False)])