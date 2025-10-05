class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"<Vehicle {self.year} {self.make} {self.model}>"


class Truck(Vehicle):
    def __init__(self, make, model, year, wheels, weight):
        super().__init__(make, model, year)
        self.wheels = wheels
        self.weight = weight

    def __str__(self):
        return f"<Truck {self.year} {self.make} {self.model}, {self.wheels} wheels, {self.weight} kg>"


vehicle1 = Vehicle("Toyota", "Corolla", 2020)
vehicle2 = Vehicle("Honda", "Civic", 2019)

truck1 = Truck("Ford", "F-150", 2022, 4, 3000)
truck2 = Truck("Volvo", "FH", 2021, 18, 12000)

print(vehicle1)
print(vehicle2)

print(truck1)
print(truck2)
