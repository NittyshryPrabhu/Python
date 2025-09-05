# OOP (Class, Object, Constructor)


# 🔹 Part A: Class & Object Basics

#  1. Create a class Person with attributes name and age.
# Create two objects with different values and print their details.

# Without using Constructor
'''class Person:
    def display(self):
        print(f"Name: {self.name} and age: {self.age}")

P1 = Person()
P2 = Person()

P1.name = "Nitty"
P1.age  = 20

P2.name = "Shry"
P2.age = 19

P1.display()
P2.display()'''

# 2.  Define a class Car with attributes brand and model.
# Add a method display() to print car details.
# Create 2 car objects and call the method.

# Without using Constructor

'''class Car:
    def display(self):
        print(f"Brand: {self.brand} and Model: {self.model}")

C1 = Car()
C2 = Car()

C1.brand = "MSD"
C1.model = "XY"

C2.brand = "NP"
C2.model = "YX"

C1.display()
C2.display()
'''

#  1. Create a class Person with attributes name and age.
# Create two objects with different values and print their details.

# Using Constructor - def __init__(self)
'''class Person:
    def __init__(self , name , age):
        self.name = name
        self.age  =  age
    def display(self):
        print(f"Name : {self.name} and Age : {self.age}")

P1 = Person("Nitty", 20)
P2 = Person("Shry" , 19)

P1.display()
P2.display()
'''



# 2.  Define a class Car with attributes brand and model.
# Add a method display() to print car details.
# Create 2 car objects and call the method.

#Using Constructor   - def __init__(self)

'''class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def display(self):
        print(f"Brand : {self.brand} and Model : {self.model}")

C1 = Car("MSD" , "XY")
C2 = Car("NP" , "AB")

C1.display()
C2.display()
        '''


# 3. Create a class Book with attributes title and author.
# Create an object and print "Book: [title] by [author]".
'''
class Book:
    def __init__(self, title ,author):
        self.title = title
        self.author = author
    def display(self):
        print(f"Book:'{self.title}' by {self.author}")

B1 = Book("A Diary [A Lot Word]", "Nittyshry Prabhu")

B1.display()

'''

# 🔹 Part B: Constructor (__init__)


# 4. Create a class Student with a constructor that takes name and marks.
# Add a method show() to display details.
# Create 3 student objects.


'''class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def show(self):
        print(f"Name: {self.name} and marks: {self.marks}")

S1 = Students("Nitty" , 45)
S2 = Students("Shry" , 43)

S1.show()
S2.show()'''


# 5. Define a class Employee with a constructor taking name, salary, and department.
# Add a method get_bonus() that calculates 10% of salary.
# Create an object and print the bonus.
'''class Employee:
    def __init__(self, name, salary, dept):
        self.name = name
        self.salary = salary
        self.dept = dept

    def display(self):
        print(f"Name: {self.name} salary: {self.salary} and department: {self.dept}")

    def get_bonus(self):
        bonus = self.salary * 0.10
        return bonus


E1 = Employee("Nitty", 85000, "CEO")

E1.display()

print(f"Bonus: {E1.get_bonus()}")'''



# 6. Create a class Rectangle with attributes length and width.
# Add a method area() to return area of rectangle.
# Add a method perimeter() to return perimeter.
# Test with multiple rectangles.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        Area = self.length * self.width
        return Area
    def perimeter(self):
        Perimeter = 2*(self.length + self.width)
        return Perimeter

R1 = Rectangle(20, 5)
R2 = Rectangle(10,9)


print("Area",R1.area())
print("Perimeter",R1.perimeter())

print("Area",R2.area())
print("Perimeter",R2.perimeter())