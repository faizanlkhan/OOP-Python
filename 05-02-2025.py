# Instance variable

class sample:
    # this is a constructor
    def __init__(self):
        self.x = 10
    # this is an instance method
    def modify(self):
        self.x += 1
# create 2 instances
s1 = sample()
s2 = sample()
print("x in s1 = ", s1.x)
print("x in s2 = ", s2.x)

#  modify x in s1
s1.modify()
print("x in s1 = ", s1.x)
print("x in s2 = ", s2.x)

# ----------------------------------------

# class variable or static variable example

class sample:
    # this is a class variable
    x = 10
    # this is a constructor
    @classmethod
    def modify(cls):
        cls.x += 1
    
# create 2 instances
s1 = sample()
s2 = sample()
print("x in s1 = ", s1.x)
print("x in s2 = ", s2.x)
#  modify x in s1
s1.modify()
print("x in s1 = ", s1.x)
print("x in s2 = ", s2.x)

# write parameterised constructor to initialise radius. Write an area method to create 2 instances and call the area method to display the area of the circle.

class circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        area = circle.pi*self.radius*self.radius
        print("Area is", area)

c1 = circle(5)
c1.area()
c2 = circle(8)
c2.area()

# Demonstrate py program to create class employee. Declare company_name as class variable as class variable, initialize value. Create parameterized constructor with name and salary as parameters. Write display_info method to display name, salary along with company name. Create two objects of Employee class and call display_info method to display the details of employees.

class employee:
    company_name = "Presidency"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print("Company Name:", employee.company_name)
        print("Name of the employee:",self.name)
        print("Salary:",self.salary)

employee1 = employee("Junaid", 50000)
employee2 = employee("Usman", 60000)

employee1.display_info()
employee2.display_info()