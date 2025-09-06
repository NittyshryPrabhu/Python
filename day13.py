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

'''class Rectangle:
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
print("Perimeter",R2.perimeter())'''



# 🔹 Part C: Instance vs Class Variables


# 7. Create a class Dog with:
# A class variable species = "Mammal".
# An instance variable name.
# Create two dog objects and print their names and species.

'''class Dog:
    species = "Mammal"

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"{self.name} species: {self.species}")

dog1 = Dog("Doggy")
dog2 = Dog("Dugga")

dog1.display()
dog2.display()'''

# If I have two different species

'''class Dog:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def display(self):
        print(f"{self.name} species: {self.species}")
dog1 = Dog("Doggy", "Mammal")
dog2 = Dog("Dugga", "Hybrid")

dog1.display()
dog2.display()'''

# 8. Create a class BankAccount with a class variable bank_name = "HDFC Bank".
# Constructor should take account_holder and balance.
# Add method deposit(amount) and withdraw(amount).
# Print balance after each operation.

'''class BankAccount:
    bank_name = "HDFC Bank"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"[{BankAccount.bank_name}] {self.account_holder} deposited {amount}. Current balance {self.balance}")

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"[{BankAccount.bank_name}] {self.account_holder} withdraw {amount}. Current balance {self.balance}")
        else:
            print(f"[{BankAccount.bank_name}] Inssuficient balance in your account Current balance {self.balance}")

H1 = BankAccount("Nitty", 85000)
H2 = BankAccount("Shry", 83000)

H1.deposit(5000)
H1.withdraw(2000)

H2.deposit(9000)
H2.withdraw(96000)'''


# 🔹 Part D: Real-world Practice


# 9. Create a class Laptop with attributes brand, ram, price.
# Add method show_specs().
# Create multiple laptop objects and print their specs.

'''class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram   = ram
        self.price = price
    def show_specs(self):
        print(f"Brand: {self.brand} ram: {self.ram} price: {self.price}")

L1 = Laptop("HP", 256, 45000)
L2 = Laptop("Lenove", 356, 43000)
L3 = Laptop("Dell", 512, 47000)

L1.show_specs()
L2.show_specs()
L3.show_specs()'''


# 10. Create a class Circle with constructor to initialize radius.
# Add methods area() and circumference().
# Test with different radius values.

'''class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area of Cirlce = { 3.14 * self.radius**2}")

    def circumference(self):
        print(f"Circumference of Circle = {2*3.14*self.radius}")

R1 = Circle(2)
R2 = Circle(3)
R3 = Circle(5)

R1.area()
R1.circumference()

R2.area()
R2.circumference()

R3.area()
R3.circumference()'''


# 11. Create a class Movie with attributes title, rating, year.
# Add method is_hit() which prints "Hit Movie!" if rating > 7, else "Flop Movie!".
# Test with 3 movies.
'''
class Movie:
    def __init__(self, title, rating, year):
        self.title = title 
        self.rating = rating
        self.year = year
    def is_hit(self):
        if self.rating > 7:
            print("Hit Movie!")
            print(f"{self.title} rating: {self.rating}/10 year: {self.year}")
        else:
            print("Flop Movie!")
            print(f"{self.title} rating: {self.rating}/10 year: {self.year}")

M1 = Movie("Tum Ho", 8, 2025)
M2 = Movie("Mere Pass",9, 2026)
M3 = Movie ("I Love You", 6, 2024)

M1.is_hit()
M2.is_hit()
M3.is_hit()'''


#  12. Create a class ShoppingCart:
# Constructor initializes an empty list items.
# Method add_item(item) adds to list.
# Method show_cart() displays all items.
# Test by adding multiple items.


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
    
    def show_cart(self):
        print(f"Items are : {self.items}")

I = ShoppingCart()

I.add_item("iPhone")
I.add_item("Mirchi")
I.add_item("Pyaj")
I.add_item("Powder")

I.show_cart()