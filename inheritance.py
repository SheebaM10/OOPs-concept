# Vehicle Inheritance Parent, class: Vehicle (brand, speed) Child classes: Car, Bike Override a method: describe() in each class

class Vehicle:
    def __init__(self, brand, speed):
        self.brand=brand
        self.speed=speed
    
    def describe(self):
        print(f"This is a {self.brand} vehicle with a speed of {self.speed} km/h.")

class Car(Vehicle):
    def describe(self):
        print(f"This is a {self.brand} car with a speed of {self.speed} km/h.")

class Bike(Vehicle):
    def describe(self):
        print(f"This is a {self.brand} bike with a speed of {self.speed} km/h.")

car = Car("Toyota", 180)
bike = Bike("Yamaha", 120)

car.describe()
bike.describe()
