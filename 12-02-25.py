# Demonstrate a python using class movie that includes attribute hero name and year. Create instances of a class and use those instance to access the attribute.

class movie:
    #constructor
    def __init__(self):
        self.heroname = "Mr Bean"
        self.year = 2005
#create an object / Instance
obj=movie()
#Access the attribute
print(obj.heroname)
print(obj.year)
print("\n")

class Movie:
    #constructor
    def __init__(self,name,year):
        self.name=name
        self.year = year
    
#create an object / Instance
e1 = Movie("Interstellar",2014)
e2 = Movie("The Shawshank Redemption",1994)
#Access the attribute
print("NAME:",e1.name,"\n","YEAR:",e1.year)
print("NAME:",e2.name,"\n","YEAR:",e2.year)

print("\n")

# Demonstrate a python program to define the class parrot with attribute name and age. Create two object of class parrot1 and parrot2. Assign value to their attribute and access the attribute

class Parrot:
    #attributes
    def __init__(self):
        self.name = ""
        self.age = 0
#Create an object
Parrot1 = Parrot()
Parrot1.name = "Parrot"
Parrot1.age = 5

Parrot2 = Parrot()
Parrot2.name = "Polly"
Parrot2.age = 3
#Access the attribute
print("Parrot1 Name:",Parrot1.name,"\n","Parrot1 Age:",Parrot1.age)
print("Parrot2 Name:",Parrot2.name,"\n","Parrot2 Age:",Parrot2.age)

print("\n")

# Demonstrate a python program to define the class Dpg with attribute name and breed. Create two object of class dog1 and dog2. Assign value to their attribute and access the attribute

class Dog:
    # Constructor
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    # Method to display the Dog's details
    def display_details(self):
        print(f"Name: {self.name} Breed: {self.breed}")
# Create an object of Dog class
dog1 = Dog("Bella", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")
# Access the attributes and call the method
dog1.display_details()
dog2.display_details()

print("\n")

# Demonstrate a python program using a class called Car that includes attributes for name, model,mileage,colour and price. The program should include methods to display the car's details, start and stop the car, and update it's price. Provide an example of creating the car object and calling their methods.

class car:
    # Constructor
    def __init__(self, name, model, year, colour, mileage, price):
        self.name = name
        self.model = model
        self.year = year
        self.colour = colour
        self.mileage = mileage
        self.price = price
    
    # Method to display the car's details
    def display_details(self):
        print(f"The name of the car is:", self.name)
        print(f"The model of the car is:", self.model)
        print(f"The year of the car is:", self.year)
        print(f"The colour of the car is:", self.colour)
        print(f"The mileage of the car is:", self.mileage)
        print(f"The price of the car is:", self.price)

    # Methods for starting, stopping the car and price update
    def start(self):
        print(f"The car {self.name}{self.model} is starting...")

    def stop(self):
        print(f"The car {self.name}{self.model} is stopping...")

    def update_price(self, new_price):
        self.price = new_price
        print(f"{self.name}{self.model} has been updated to {self.price}")

# Create an object
car1 = car("Toyota", "Camry", 2020, "Blue", 500, 12000000)

# Access the attribute using method
car1.display_details()
car1.start()
car1.stop()
car1.update_price(15000000)

print("\n")


    
