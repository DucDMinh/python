class Vehicle:
    def __init__(self, make):
        self.make = make
    def description(self):
        print(f"Make: {self.make}")
class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make)
        self.model = model
    def description(self):
        super().description()
        print(f"Model: {self.model}")
class ElectricCar(Car):
    def __init__(self, make, model, battery):
        super().__init__(make, model)
        self.battery = battery
    def description(self):
        super().description()
        print(f"Battery: {self.battery}")
elect1 = ElectricCar('Electric', 'model s', 2016)
elect1.description()