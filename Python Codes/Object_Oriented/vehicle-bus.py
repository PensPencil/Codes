class Vehicle:
    def __init__(self, name, max_speed, mileage,capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self):
        print("The seating capacity of {} is {} passengers".format(self.name,self.capacity))
    def fare(self):
        total_fare = self.capacity*100
        print("The fare of {} is {}.".format(self.name,total_fare))
class Bus(Vehicle):
    
    def seating_capacity(self):
        print("The seating capacity of {} is {} passengers".format(self.name,self.capacity))
    def fare(self):
        x = self.capacity * 100 
        total_fare = x + (0.1 *x)
        print("The fare of {} is {}.".format(self.name,total_fare))
    
v1 = Bus("School Bus", 120, 2500,80)
v2 = Vehicle("Taxi",180,3500,4)
v1.seating_capacity()
v1.fare()
v2.seating_capacity()
v2.fare()
print(type(v1))
print(isinstance(v1,Vehicle))