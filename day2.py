#  Practice: Operators, Casting & Input/Output

#🔹 Beginner Exercises
# 1. Ask the user for two numbers. Print their:
# Sum
# Difference
# Product
# Quotient
'''
num1 = int (input("Enter first number : "))
num2 = int (input("Enter second number : ")) 

print(f"Sum {num1+num2}")
print(f"Difference {num1-num2}")
print(f"Multiple {num1*num2}")
print(f"Quotient {num1/num2}")
'''

# 2. Write a program to calculate the remainder when one number is divided by another.

'''M = int (input("Enter a first anumber"))
N = int (input("Enter a second number"))

print(f"Remainder : {M%N}")'''


# 3. Take a user’s age as input. Print:
# In 5 years, you will be <age+5> years old.
'''
user_age = int (input("Enter user's age : "))
print(f"In 5 years, you will be {user_age+5} years old.")'''


# 4. Store two Boolean values (True, False) in variables. Print results of:
# AND
# OR
# NOT

'''first_var = True
second_var = False

print(first_var and second_var)
print(first_var or second_var)
print(not first_var)
print(not second_var)

# Program to demonstrate Boolean operations with Truth Table

values = [True , False]

print(f"A\tB\tA ANd B\tA OR B\tNOT A\tNOT B")

for A in values:
    for B in values:
        print(f"{A} \t {B} \t {A and B} \t {A or B }\t {not A} \t {not B}")'''



# 5. Ask the user for a decimal number, convert it to integer, and print both values.

'''value = float(input("Enter a decimal value"))

converted_value = int (value)
print(f"Original value : {value}")
print(f"Coverted value in integer : {converted_value}")'''


# 🔹 Intermediate Exercises

# 6. Ask the user for their name and birth year.
# Calculate and print their age in 2025. 


'''from datetime import datetime

current_date = datetime.now().year

name = input("Enter a name : ")
birth_age = int(input("Enter your birth age : "))

print(f"Hey {name}, your age in 2025, {current_date - birth_age} years old.")
'''


# 7. Write a program that takes length and width from the user and prints the area of a rectangle.

'''length = float (input("Enter length of rectagle"))
width = float (input("Enter width of rectangle"))

area = length*width
print(f"Area of Rectangle {area})'''


# 8. Take two numbers as input. Print:
# Which one is larger
# Which one is smaller

'''num1 = int (input("Enter first number : "))
num2 = int (input("Enter second number : "))

if num1>num2:
    print(f"Larger number {num1}")
    print(f"Smaller number {num2}")
elif num1<num2:
    print(f"Larger number {num2}")
    print(f"Smaller number {num1}")
else:
    print("Equal number")'''


# 9. Ask the user for a number. Print:
# Square (num ** 2)
# Cube (num ** 3)

'''

num = int (input("Enter a number : "))
square=num**2
cube=num**3

print(f"Square is {square}")
print(f"Cube is {cube}")'''


# 10. Write a program where the user enters a number. Print whether it is even or odd using modulus operator (%).


'''num = int(input("Enter a number : "))
if num%2==0:
    print("Even")
else:
    print("Odd")'''


# 🔹 Challenge Exercises
# 11. A shopkeeper gives 10% discount on items.
# Ask the user for the price of an item.
# Calculate and print the final price after discount.


'''price = float(input("Enter the price of item : "))

# 10% discount
discount_price = (price *10)/100

final_price = price- discount_price

print(f"Original price {price}")
print(f"{discount_price} discount 10% on item ")
print(f"The final price after discount : {final_price}")'''


# 12. Ask the user for a temperature in Celsius. Convert it to Fahrenheit using:
#  F = (C * 9/5) + 32

'''celsius_temp = float(input("Entet a celsius temperature"))

fahrenheit_temp = (celsius_temp *9/5)+32

print(f"Fahrenheit Temperature : {fahrenheit_temp}")'''


# 13. Ask the user for marks in 3 subjects.
# Calculate total and average.
# Print them in a single line.

# asking subject marks in three subject 

'''phy = float (input("Enter your pysics marks : "))
chem = float (input("Enter your chemistry marks : "))
math = float (input("Enter your mathematics marks : "))

total=phy+chem+math

average = total/3

print(f"Total marks of three subjects : {total}, Average : {average}")'''


# 14. Write a program where the user enters a 4-digit number (e.g., 1234).
# Print the sum of its digits (1+2+3+4 = 10).

'''num = (input("Enter 4-digits number : "))

total = 0
for digit in num:
    total += int(digit)
    
print(f"Sum of digits : {total}")'''



