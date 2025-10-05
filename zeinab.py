class vehicle:
    def __init__(self, make , model , year ):
        self.make= make
        self.model=model
        self.year= year
    def __str__(self):
        return f"Vehicle: {self.year} {self.make} {self.model}"

class truck(vehicle):
        def __init__(self, make, model, year, wheels, weight):
            super().__init__(make, model, year)
            self.wheels=wheels
            self.weight=weight


vehicle1=vehicle("kia", "retona", 2015)
vehicle2=vehicle("Chevrolet ", "tahoe", 2025)

truck1=("ram","1500",2022,4,2700)
truck2=("Gmc","Sierra",2024, 6, 3200)

print(vehicle1)
print(vehicle2)
print(truck1)
print(truck2)
