class vehicle :
  def __init__(self, model, year,make):
    self.model = model
    self.year = year
    self.make = make
  
  def __str__(self):

        return f"{self.year} {self.make} {self.model}"


# Subclass

class Truck(Vehicle):

    def __init__(self, make, model, year, wheels, weight):

        super().__init__(make, model, year)

        self.wheels = wheels

        self.weight = weight

    def __str__(self):

        return f"{self.year} {self.make} {self.model} - {self.wheels} wheels, {self.weight}kg"


# Create 2 objects of each class

vehicle1 = Vehicle("Toyota", "Camry", 2022)

vehicle2 = Vehicle("Honda", "Civic", 2023)

truck1 = Truck("Ford", "F-150", 2021, 4, 2500)

truck2 = Truck("Volvo", "FH16", 2020, 6, 8000)



print(vehicle1)

print(vehicle2)

print(truck1)

print(truck2)
 

v1 = ("toyota",1994)
v2 = (make="honda",model="civic",year=2020)
print(v1)
print(v2))
print(v1.model)
print(v2.model)print(v1.year)
print(v2.year)
print(v1.make)
print(v2.make)

