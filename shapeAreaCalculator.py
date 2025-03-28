# Polymorphism Challenges, Shape Area Calculator Base class: Shape with method area(), 
# Derived classes: Circle, Rectangle, Triangle each overriding area()
import math

class Shape:
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius= radius
        
    def area(self):
        return math.pi* self.radius* self.radius
        
class Rectangle(Shape):
    def __init__(self, lenght,width):
        self.lenght= lenght
        self.width= width
    
    def area(self):
        return self.lenght*self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base= base
        self.height= height
        
    def area(self):
        return 0.5 * self.base * self.height
    
Circle= Circle(2)
Rectangle= Rectangle(2,4)
Triangle= Triangle(2,4)

print(" Circle Area:", Circle.area())
print(" Rectangle Area:", Rectangle.area())
print(" Triangle Area:", Triangle.area())