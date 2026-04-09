def tron_danh_sach(a, b):
    """
    Hàm lấy luân phiên phần tử từ mảng a và b để tạo thành mảng c.
    """
    c = []
    n, m = len(a), len(b)

    # Tìm chiều dài lớn nhất giữa 2 mảng để xác định số vòng lặp tối đa
    max_len = max(n, m)

    for i in range(max_len):
        # Nếu mảng a vẫn còn phần tử ở vị trí i thì lấy
        if i < n:
            c.append(a[i])

        # Nếu mảng b vẫn còn phần tử ở vị trí i thì lấy
        if i < m:
            c.append(b[i])

    return c


def kiem_thu_chuong_trinh():
    """
    Hàm chứa các test case kiểm thử theo yêu cầu.
    """
    print("=== KIỂM THỬ CHƯƠNG TRÌNH TRỘN DANH SÁCH ===\n")

    test_cases = [
        {
            "ten": "Test case 1: a ngắn hơn b (a chứa xâu, b chứa số)",
            "a": ['a', 'b', 'c'],
            "b": [1, 2, 3, 4, 5]
        },
        {
            "ten": "Test case 2: a dài hơn b",
            "a": [10, 20, 30, 40, 50],
            "b": ['x', 'y']
        },
        {
            "ten": "Test case 3: a dài bằng b",
            "a": ["Cam", "Quýt", "Bưởi"],
            "b": ["Táo", "Lê", "Mận"]
        },
        {
            "ten": "Test case 4: a và b chứa toàn số",
            "a": [1, 3, 5],
            "b": [2, 4, 6, 8, 10]
        }
    ]

    # Chạy lần lượt từng test case
    for tc in test_cases:
        print(f"--- {tc['ten']} ---")
        print(f"Danh sách a : {tc['a']}")
        print(f"Danh sách b : {tc['b']}")

        # Gọi hàm trộn
        c = tron_danh_sach(tc['a'], tc['b'])

        print(f"=> Kết quả c: {c}\n")


if __name__ == "__main__":
    kiem_thu_chuong_trinh()