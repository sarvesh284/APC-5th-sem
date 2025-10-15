class Vehicle:
    def __init__(self, type, capacity):
        self.type = type
        self.capacity = capacity

    def info(self):
        print("name of vehicle is:", self.type)
        print("Engine capacity of " + self.type + " is " + str(self.capacity))

class Bike(Vehicle):
    def engcap(self):
        print("Engine capacity of " + self.type + " is " + str(self.capacity))

class Car(Vehicle):
    def engcap(self):
        print("Engine capacity of " + self.type + " is " + str(self.capacity))

class Bus(Vehicle):
    def engcap(self):
        print("Engine capacity of " + self.type + " is " + str(self.capacity))

class Truck(Vehicle):
    def engcap(self):
        print("Engine capacity of " + self.type + " is " + str(self.capacity))

# Creating objects with proper initialization
car = Car("Car", 1000)
car.engcap()

bike = Bike("Bike", 100)
bike.engcap()

truck = Truck("Truck", 2000)
truck.engcap()

bus = Bus("Bus", 1500)
bus.engcap()

# Alternative: You can also call the inherited info() method
print("\nUsing inherited info() method:")
car.info()
bike.info()