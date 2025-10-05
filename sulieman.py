class vehicle:
    def __init__(self,make,model,year):
        self.make =make
        self.model=model
        self.year=year
        
class truck(vehicle):
    def __init__(self, make, model, year,wheels, weight):
        super().__init__(make, model, year)
        self.wheels=wheels
        self.weight=weight

car1=vehicle('audi','A3',2018)
car2=vehicle('audi','A5', 2025)
truck1=truck('Volvo',' FH16',2020,8,20000)
truck2=truck('Volvo','FMX',2020,8, 25000)
print(f"Vehicle 1: {car1.make} {car1.model}, {car1.year}")
print(f"Vehicle 2: {car2.make} {car2.model}, {car2.year}")
print(f"Truck 1: {truck1.make} {truck1.model}, {truck1.year}, {truck1.wheels} wheels, {truck1.weight} kg")
print(f"Truck 2: {truck2.make} {truck2.model}, {truck2.year}, {truck2.wheels} wheels, {truck2.weight} kg")
 