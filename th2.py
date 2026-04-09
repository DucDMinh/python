def input_data():
    data = []
    n = int(input("Nhap so sinh vien: "))

    for i in range(n):
        print(f"Nhap thong tin sinh vien thu {i + 1}:")
        id = int(input("Nhap ma sinh vien: "))
        credit = int(input("So tin chi da hoc: "))
        data.append({
            "id": id,
            "credits": credit,
        })
    return data


def show(data):
    print("\nDanh sach sinh vien: ")
    print(f'{"Ma sinh vien":<15} {"So tin chi da hoc":<15}')
    for item in data:
        print(f'{item["id"]:<15} {item["credits"]:<15}')


def check(data):
    found = False

    for item in data:
        if item["id"] == 2024123456:
            item["credits"] = 100
            found = True
            break

    if not found:
        data.append({
            "id": 2024123456,
            "credits": 100,
        })
        print("Không có SV -> đã thêm mới")


def delete(data):
    data[:] = [item for item in data if item["credits"] != 0]

data = input_data()

show(data)

check(data)
show(data)

delete(data)
show(data)