'''
Q.5- Create a class Animal as a base class and define method animal_attribute.
Create another class Tiger which is inheriting Animal and access the base class method.
'''
class Animal:
    def Animal_Attribute(self):
        print("These are the animal Attributes.")


class Tiger(Animal):
    def Tiger_Attributes(self):
        print("Tigers belong to the cat Family.")
    
a = Tiger()
a.Animal_Attribute()
    
