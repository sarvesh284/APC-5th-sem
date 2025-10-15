class Wheel:
    def __init__(self, radius):
        self.radius = radius

class Rubber:
    def __init__(self, colour):
        self.colour = colour

class Tyre(Wheel, Rubber):
    def __init__(self, radius, colour):
        Wheel.__init__(self, radius)    # Initialize Wheel part
        Rubber.__init__(self, colour)   # Initialize Rubber part
    
    def info(self):
        print("wheel has colour of " + self.colour + " with radius " + str(self.radius))


tyre = Tyre(50, "black")
tyre.info()