# Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def getArea(self):
        area = math.pi * math.pow(self.radius, 2)
        return area
    def getCircumf(self):
        circumf = (2 * math.pi) * self.radius
        return circumf

rad = int(input("Enter the radius of Circle: "))
circ = Circle(rad)
print(" ")
print("Circumference: ",circ.getCircumf())
print("Area: ",circ.getArea())
