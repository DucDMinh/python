from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    def __init__(self, seats):
        self.seats = seats
        self.engine_running = False

    def start_engine(self):
        self.engine_running = True
        print("Car engine started")

    def stop_engine(self):
        self.engine_running = False
        print("Car engine stopped")

    def drive(self):
        if self.engine_running:
            print(f"Driving a car with {self.seats} seats.")
        else:
            print("Cannot drive! Please start the car engine first.")


class Motor(Vehicle):
    def __init__(self, fuel):
        self.fuel = fuel
        self.engine_running = False

    def start_engine(self):
        self.engine_running = True
        print("Motor engine started")

    def stop_engine(self):
        self.engine_running = False
        print("Motor engine stopped")

    def drive(self):
        if self.engine_running:
            print(f"Riding a motor with {self.fuel} liters of fuel.")
        else:
            print("Cannot drive! Please start the motor engine first.")

Vehicles = [Car(seats=4), Motor(fuel=6)]
for vehicle in Vehicles:
    print(f"\n{vehicle.__class__.__name__}:")
    vehicle.start_engine()
    vehicle.drive()
    vehicle.stop_engine()