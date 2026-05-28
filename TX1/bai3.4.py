def vecinput():
    return list(map(int, input().split()))
def main():
    a = vecinput()
    b = vecinput()
    c = a + b
    c.sort()
    print(c)

if __name__ == "__main__":
    main()