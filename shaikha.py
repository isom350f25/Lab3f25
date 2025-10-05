class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class Truck(Vehicle):
    def __init__(self, make, model, year, wheels, weight):
        super().__init__(make, model, year)
        self.wheels = wheels
        self.weight = weight

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - {self.wheels} wheels, {self.weight}kg"


vehicle1 = Vehicle("Toyota", "Camry", 2022)
vehicle2 = Vehicle("Honda", "Civic", 2023)

truck1 = Truck("Ford", "F-150", 2021, 4, 2500)
truck2 = Truck("Volvo", "FH16", 2020, 6, 8000)

print(vehicle1)
print(vehicle2)
print(truck1)
print(truck2)
