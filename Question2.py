'''
Create a Student class and initialize it with name and roll number. Make methods to : 
1. Display - It should display all informations of the student. 
2. setAge - It should assign age to student 3. setMarks - It should assign marks to the student.
'''

class Student:
    def __init__(self, name, rno):
        self.name = name
        self.rno = rno
    def display(self):
        print(" ")
        print("Name: ",self.name)
        print("Roll Number: ",self.rno)
        print("Marks: ",marks)
        print("Age: ",age)
        
    def setAge(self, age):
        self.age = age

    def setMarks(self, marks):
        self.marks = marks

name = input("Enter your name: ")
rollno = input("Enter your Roll number: ")
age = input("Enter the age: ")
marks = input("Enter marks: ")

st1 = Student(name, rollno)

st1.setAge(age)
st1.setMarks(marks)

st1.display()
        
    
        
