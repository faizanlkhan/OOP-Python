# CONSTRUCTOR

class student:
    def __init__(self):
        self.name = "John" 
        self.roll_no = 20

    def display(self):
        print("My name is", self.name)
        print("My roll number is", self.roll_no)

student = student()
student.display()

class Myclass:
    def __init__(self):
        self.name = "John"
        self.age = 20
        print("My name is", self.name)
        print("My age is", self.age)

m1=Myclass()

class Myclass1():
    def __init__(self):
        self.car_brand = "TOYOTA" 
        self.car_model = 20

    def display(self):
        print("My car brand is", self.car_brand)
        print("My car model is", self.car_model)

S1 = Myclass1()
S1.display()