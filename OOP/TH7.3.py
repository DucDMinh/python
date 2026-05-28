from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass
    @abstractmethod
    def get_balance(self):
        pass
class SavingAccount(Account):
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit {self.balance} succeeded")
        else:
            print(f"Withdraw {self.balance} failed")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {self.balance} success")
        else:
            print(f"Withdraw {self.balance} failed")
    def get_balance(self):
        print(f"Balance of this account is {self.balance}")
class CheckingAccount(Account):
    def __init__(self, balance=0, limit=500):
        self.balance = balance
        self.limit = limit

    def deposit(self, amount):
        self.balance += amount
        print(f"Checking: Đã gửi {amount}. Số dư mới: {self.balance}")

    def withdraw(self, amount):
        if (amount > 0) and (self.balance - amount >= -self.limit):
            self.balance -= amount
            print(f"Checking: Đã rút {amount}. Số dư còn lại: {self.balance}")
        else:
            print(f"Checking: Rút tiền thất bại! Vượt quá hạn mức thấu chi (-{self.limit}).")
    def get_balance(self):
        return self.balance
print("--- TÀI KHOẢN TIẾT KIỆM (SAVINGS) ---")
savings = SavingAccount(1000)
savings.deposit(200)
savings.withdraw(1500)
savings.withdraw(500)

print("\n--- TÀI KHOẢN THANH TOÁN (CHECKING) ---")
checking = CheckingAccount(100, limit=200)
checking.withdraw(250)
checking.withdraw(100)