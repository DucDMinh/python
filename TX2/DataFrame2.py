import pandas as pd

data = {'Name': ('Alice', 'Bob', 'Charlie'),
        'Age': (22, 25, 30),
        'Language': ('Java', 'Python', 'C++'),}
df = pd.DataFrame(data)
df['Gender'] = ['Female', 'Male', 'Male']
print(df)
# df.drop('Age', axis=1, inplace=True)
# df.drop(0, axis=0, inplace=True)
# print('------------------------------------')
# print(df)
print('-' * 30)
print('Alice Information')
print(df.loc[df['Name'] == 'Alice'])
print('-' * 30)
print('Line 3 information')
print(df.loc[2])
print('-' * 30)
print('Language Information')
print(df.loc[(df['Age'] >= 20) & (df['Age'] <= 25), ['Name', 'Language']])
print('-' * 30)
print('First two people')
print(df.iloc[:2])
print('-' * 30)
df.loc[df['Name'] == 'Bob', 'Language'] = 'R'
print(df)