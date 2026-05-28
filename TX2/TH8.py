import pandas as pd
data = {
    'EmployeeID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 28, 39],
    'Department': ['HR', 'IT', 'IT', 'IT', 'HR'],
    'Salary': [50000, 60000, 70000, 80000, 90000]
}
df = pd.DataFrame(data)

if 'Frank' not in df['Name'].values:
    df.loc[len(df.index)] = [6, 'Frank', 28, 'Marketing', 65000]
    print(df)
    print('----> Frank information has been added')
else: print('Frank existed')
print('-' * 30)
print('Change employee information')
df.loc[df['EmployeeID'] == 3, ['Salary','Department']] = [75000, 'HR']
print(df)
print('-' * 30)
print('Delete employee information')
df = df[df['EmployeeID'] != 4].reset_index(drop=True)
print(df)
print('-' * 30)
print('HR employee information')
print(df[df['Department'] == 'HR'])
print('>60000 Salary employee information')
print(df[df['Salary'] > 60000])
print('age > 30 and IT Department employee information')
print(df[(df['Age'] >= 30) & (df['Department'] == 'IT')])
print('-' * 30)
it_member = df.loc[df['Department'] == 'IT']
print(f'Average age of IT Department: {it_member['Age'].mean()}')