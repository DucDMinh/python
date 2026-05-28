class Employee():
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    # Phương thức mặc định ở lớp cha (Có thể bị ghi đè ở lớp con)
    def income(self):
        return self.salary

    # Thêm phương thức hiển thị thông tin
    def display_info(self):
        print(f"Mã số: {self.id} | Họ tên: {self.name} | Lương: {self.income()}")


class SaleEmployee(Employee):
    def __init__(self, id, name, salary, sale_total):
        super().__init__(id, name, salary)
        self.sale_total = sale_total

    def income(self):
        return self.salary + 0.05 * self.sale_total


class Manager(Employee):
    def __init__(self, id, name, salary, daysOfWork):
        super().__init__(id, name, salary)
        self.daysOfWork = daysOfWork

    def income(self):
        return self.salary + 50 * self.daysOfWork


# Khởi tạo đối tượng
sale_emp = SaleEmployee(1, 'Duc Minh', 25000, 500)
manager_emp = Manager(2, 'Duc Dao', 50000, 26)

# Hiển thị thông tin
print("--- THÔNG TIN NHÂN VIÊN ---")
sale_emp.display_info()
manager_emp.display_info()