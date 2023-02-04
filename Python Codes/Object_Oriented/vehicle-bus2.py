class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        print("The seating capacity of {} is {} passengers".format(self.name,capacity))
class Bus(Vehicle):
    
    def seating_capacity(self, capacity=50):
        print("The seating capacity of {} is {} passengers".format(self.name,capacity))
    
Bus("School Bus", 120,2500).seating_capacity()
Vehicle("Taxi",180,3500).seating_capacity(4)
Bus("Tourist Bus", 120,2500).seating_capacity(110)