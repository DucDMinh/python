class BankAccount:
    def __init__(self,accountNumber, ownerName, balance):
        self.accountNumber = accountNumber
        self.ownerName = ownerName
        self.balance = balance
    def Deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.ownerName} deposited to bank account number {self.accountNumber}: {self.balance}")
        else:
            print("Amount must larger than 0")
    def Withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{self.ownerName} đã rút từ tài khoản {self.accountNumber}. Số dư còn lại: {self.balance}")
        elif amount <= 0:
            print("Số tiền rút phải lớn hơn 0.")
        else:
            print("Số dư không đủ để thực hiện giao dịch này.")
    def bankFees(self):
        fee = self.balance * 0.05
        self.balance -= fee
        print(f"Đã áp dụng phí ngân hàng (5%): {fee}. Số dư sau khi trừ phí: {self.balance}")

    def display(self):
            print("--- CHI TIẾT TÀI KHOẢN ---")
            print(f"Số tài khoản: {self.accountNumber}")
            print(f"Chủ tài khoản: {self.ownerName}")
            print(f"Số dư hiện tại: {self.balance}")
            print("--------------------------")

acc = BankAccount("123456789", "Nguyễn Văn A", 1000000)

acc.display()

acc.Deposit(0)

acc.Withdraw(20000000000)

acc.bankFees()

acc.display()