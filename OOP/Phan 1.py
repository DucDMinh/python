class Product:
    number_of_products = 0
    def __init__(self, productId, name, price, stock):
        self.productId = productId
        self.name = name
        self.price = price
        self.stock = stock
        Product.number_of_products = Product.number_of_products + 1
    def total_price(self):
        return self.price * self.stock
    def __str__(self):
        return f"Product: {self.name}, id:{self.productId}, Price: {self.price}, Stock: {self.stock}, Total price: {self.total_price()}"

pro1 = Product(1, "Prod 1", 12300, 104350)
pro2 = Product(2, "Prod 2", 65745, 14356500)

print(pro1)
print(pro2)

print(Product.number_of_products)

class Phone(Product):
    def __init__(self, productId, name, price, stock, battery):
        super().__init__(productId, name, price, stock)
        self.battery = battery
    def __str__(self):
        return super().__str__() + f", Battery: {self.battery}"
phone1 = Phone(1, "Phone 1", 12300, 104350, 10000)
print(phone1)