class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Truck(Vehicle):
    def __init__(self, make, model, year, wheels, weight):
        super().__init__(make, model, year)
        self.wheels = wheels
        self.weight = weight

vehicle1 = Vehicle("nissan", "Z", 2022)
vehicle2 = Vehicle("toyota", " camry ", 2024)

truck1 = Truck("Ford", "F-150", 2022, 4, 2450)
truck2 = Truck("GMC", "sierra HD", 2023, 4, 7500)

print(f"Vehicle 1: {vehicle1.make} {vehicle1.model}, Year: {vehicle1.year}")
print(f"Vehicle 2: {vehicle2.make} {vehicle2.model}, Year: {vehicle2.year}")
print(f"Truck 1: {truck1.make} {truck1.model}, Year: {truck1.year}, Wheels: {truck1.wheels}, Weight: {truck1.weight} lbs")
print(f"Truck 2: {truck2.make} {truck2.model}, Year: {truck2.year}, Wheels: {truck2.wheels}, Weight: {truck2.weight} lbs")