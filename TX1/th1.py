def input_data():
    product_list = []
    n = int(input("Nhap so luong mat hang: "))

    for i in range(n):
        print(f"Nhap thong tin mat hang thu {i + 1}")
        product_id = int(input("id: "))
        name = str(input("name: "))
        amount = int(input("amount: "))
        price = float(input("price: "))

        product_list.append({
            "product_id": product_id,
            "name": name,
            "amount": amount,
            "price": price
        })

    return product_list


def show(product_list):
    print("\nDanh sach hang hoa:")
    print(f'{"Mã":<10} {"Tên":<20} {"SL":<10} {"Giá":<15} {"Tổng tiền":<15}')

    for item in product_list:
        tong = item["amount"] * item["price"]
        print(f'{item["product_id"]:<10} {item["name"]:<20} {item["amount"]:<10} {item["price"]:<15} {tong:<15}')

def smallest(product_list):
    smallest_sum = product_list[0]["amount"] * product_list[0]["price"]
    for item in product_list:
        tong = item["amount"] * item["price"]
        if tong < smallest_sum:
            smallest_sum = tong
    return smallest_sum

def show_smallest(product_list, smallest_sum):
    print("\nDanh sach hang hoa co tong gia tri be nhat:")
    print(f'{"Mã":<10} {"Tên":<20} {"SL":<10} {"Giá":<15} {"Tổng tiền":<15}')
    for item in product_list:
        tong = item["amount"] * item["price"]
        if tong == smallest_sum:
            print(f'{item["product_id"]:<10} {item["name"]:<20} {item["amount"]:<10} {item["price"]:<15} {tong:<15}')
def count_products(product_list):
    count = 0
    for item in product_list:
        tong = item["amount"] * item["price"]
        if item["amount"] > 5 and tong < 1000000:
            count += 1
    return count

ds = input_data()
show(ds)
print("\n Gia tri tong tien nho nhat:", smallest(ds))
show_smallest(ds, smallest(ds))
print("Tong so luong mat hang thoa man dieu kien: ", count_products(ds))