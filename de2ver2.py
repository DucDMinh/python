def input_data():
    data = []
    n = int(input("Enter number of students: "))
    for i in range(n):
        id = int(input("Enter student id: "))
        credit = int(input("Enter number of credits: "))
        data.append({
            "id": id,
            "credits": credit
        })
    return data
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
            "credits": 100
        })

def show(data):
    print("\nDanh sach sinh vien: ")
    print(f'{"Ma sinh vien":<15} {"So tin chi da hoc":<15}')
    for item in data:
        print(f'{item["id"]:<15} {item["credits"]:<15}')

def delete(data):
    for item in data:
        if(item["credits"] == 0):
            data.remove(item)


def split_and_print(data):
    # 1. Chuyển dữ liệu sang hai list
    list_ids = [item["id"] for item in data]
    list_credits = [item["credits"] for item in data]

    print("\n--- Kết quả tách List ---")
    print("List mã sinh viên: ", list_ids)
    print("List số tín chỉ: ", list_credits)

    # 2. In ra 3 phần tử đầu tiên (nếu có) của list thứ nhất
    # Sử dụng slicing [:3] sẽ tự động lấy tối đa 3 phần tử đầu,
    # nếu list có ít hơn 3 phần tử thì nó sẽ lấy tất cả mà không báo lỗi.
    print(f"\n3 phần tử đầu tiên của list mã SV: {list_ids[:3]}")

    # 3. In ra 3 phần tử cuối cùng (nếu có) của list thứ hai
    # Sử dụng slicing [-3:] sẽ tự động lấy tối đa 3 phần tử từ cuối lên.
    print(f"3 phần tử cuối cùng của list số tín chỉ: {list_credits[-3:]}")


# Giả sử bạn đã có biến 'data' từ hàm input_data() ở bài trước
# data = input_data()
# split_and_print(data)

data = input_data()
show(data)
check(data)
show(data)
delete(data)
show(data)
split_and_print(data)