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

def main():
    a = vecinput()
    b = vecinput()
    print(vecsum(a))
    index = int(input())
    value = int(input())
    print(vecinsert(a.copy(), index, value))
    delvalue = int(input())
    print(vecdel(a.copy(), delvalue))
    print(vecadd(a, b))

if __name__ == "__main__":
    main()