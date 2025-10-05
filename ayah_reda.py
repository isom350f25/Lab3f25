
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"Vehicle: {self.year} {self.make} {self.model}"


class Truck(Vehicle):
    def __init__(self, make, model, year, wheels, weight):
        super().__init__(make, model, year)
        self.wheels = wheels
        self.weight = weight

    def __str__(self):
        return f"Truck: {self.year} {self.make} {self.model}, {self.wheels} wheels, {self.weight} lbs"


v1 = Vehicle("Toyota", "Camry", 2020)
v2 = Vehicle("BMW", "X5", 2021)

t1 = Truck("Ford", "F-150", 2021, 4, 5000)
t2 = Truck("Ram", "3500 Heavy Duty", 2022, 6, 8000)

print(v1)
print(v2)
print(t1)
print(t2)
