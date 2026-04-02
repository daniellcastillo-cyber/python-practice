
class Car:
    def __init__(self, brand, model, fuel):
        self.brand = brand
        self.model = model
        self.fuel = fuel

    def refuel(self, liters):
        self.fuel += liters

    def get_info(self):
        return f"Car: {self.brand} {self.model} | Fuel: {self.fuel}lt "
    
    def drive(self, km):
        fuel_needed = km / 10
        if fuel_needed > self.fuel:
            print("Not enough fuel")
        else:
            self.fuel -= fuel_needed
            print(f"Driving {km}km. Fuel left: {self.fuel}lt")

car = Car("Toyota", "Carolla", 10)
print(car.get_info())
car.drive(50)
car.drive(80)
car.refuel(20)
print(car.get_info())
car.drive(80)
print(car.get_info())
