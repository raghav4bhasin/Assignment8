'''
Q.7- Create a class Shape.Initialize it with length and breadth.
Create the method Area. Create class rectangle and square which inherits shape and access the method Area.
'''
class Shape:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def Area(self):
        ar = self.length * self.breadth
        return ar
class Rectangle(Shape):
    def m1(self):
        print("This shape is a Rectangle.")

class Square (Shape):
    def m1(self):
        print("This shape is a Square.")

lent = int(input("Enter Length: "))
brdth = int(input("Enter Breadth: "))
print(" ")
if lent == brdth:
    shape1 = Square(lent, brdth)
else:
    shape1 = Rectangle(lent, brdth)

shape1.m1()
print("Area:",shape1.Area())

        
    
    
    
    

        
        
