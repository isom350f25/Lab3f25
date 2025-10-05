class Vehicle:
 
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
 
 
class Truck(Vehicle):
    def __init__(self, make, model, year,wheels,weight):
        super().__init__(make, model, year)
        self.wheels = wheels
        self.weight = weight
 
car1 = Vehicle("Toyota","Camry",2023)
car2 = Vehicle("Toyota", "Corolla",2011)
 
truck1 = Truck("Mercedes","eECONIC",2022,6,9200)
truck2 = Truck("Mercedes", "eACTROS",2019,4,13017)
 
print(f"Vehicle 1: {car1.make} {car1.model}, {car1.year}")
print(f"Vehicle 2: {car2.make} {car2.model}, {car2.year}")
print(f"Truck 1: {truck1.make} {truck1.model}, {truck1.year}, {truck1.wheels} wheels, {truck1.weight} kg")
print(f"Truck 2: {truck2.make} {truck2.model}, {truck2.year}, {truck2.wheels} wheels, {truck2.weight} kg")
    
    