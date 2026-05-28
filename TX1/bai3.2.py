def vecinput():
    return list(map(int, input().split()))

def vecsum(a):
    return sum(a)

def vecinsert(a, index, value):
    a.insert(index, value)
    return a

def vecdel(a, value):
    if value in a:
        a.remove(value)
    return a

def vecadd(a, b):
    if len(a) != len(b):
        return []
    return [a[i] + b[i] for i in range(len(a))]

def bai31():
    a = vecinput()
    b = vecinput()
    print(vecsum(a))
    index = int(input())
    value = int(input())
    print(vecinsert(a.copy(), index, value))
    value_del = int(input())
    print(vecdel(a.copy(), value_del))
    print(vecadd(a, b))

def bai32():
    a = list(map(int, input().split()))
    n = int(input())
    m = int(input())
    if len(a) < n * m:
        print("Khong the tao ma tran")
    else:
        matrix = []
        index = 0
        for i in range(n):
            row = a[index:index+m]
            matrix.append(row)
            index += m
        print(matrix)

def bai33():
    a = input().split()
    b = input().split()
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        c.append(a[i])
        c.append(b[j])
        i += 1
        j += 1
    c.extend(a[i:])
    c.extend(b[j:])
    print(c)

def bai34():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c.extend(a[i:])
    c.extend(b[j:])
    print(c)

def bai35():
    a = input().split()
    b = tuple(a)
    count = 0
    for x in b:
        if x.isdigit():
            count += 1
    print(b)
    print(count)

def menu():
    while True:
        print("1")
        print("2")
        print("3")
        print("4")
        print("5")
        print("0")
        choice = input()
        if choice == '1':
            bai31()
        elif choice == '2':
            bai32()
        elif choice == '3':
            bai33()
        elif choice == '4':
            bai34()
        elif choice == '5':
            bai35()
        elif choice == '0':
            break

if name == "main":
    menu()