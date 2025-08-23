# Variables and Data Types
# Printing Values
# Printing Types


name = " Nitish" # Srting
age = 20         # integer
height  = 5.89   # float
is_student = True # boolean
future_plan = None # NoneType

# Printing Values

print("Name : " , name)
print("Age : ", age)
print("Height : ", height)
print("Is_Student : ", is_student)
print("Future_Plan : ", future_plan)

# Printing Types

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(future_plan))



# Create variables for your name, age, and favorite color. Print them in a single line.
# 1. My name is Alice, I am 18 years old, and my favorite color is Blue.

# 2. Store the values 10 and 3 in two variables. Print their sum, difference, product, and quotient.
# 3. Assign a floating number (e.g., 7.56) to a variable. Convert it to an integer using int() and print both values.


# 1. 
name = " Alice"
age = 18
favorite_color= "Blue"

print("My name is",name, ", I am ",age, "years old, and my favorite color is",favorite_color )

# 2.
a = 10 # first_variable
b=3    # second_variable

print("Sum :", a+b , " Difference :", a-b, " Product : ", a*b , " Quotient : " , a/b)

# 3.
float_value = 7.56

int_value = int(float_value)

print("Float Value : ",float_value)
print("Int vlaue : ", int_value)




# 4. Create a variable is_coder and set it to True. Print a sentence:
# Is Alice a coder? True

# 5. Make a variable x = None. Print its type.

#4
is_coder=True
print("Is Alice a coder?",is_coder)

#5
x=None
print(type(x))




#🔹 Intermediate Exercises
# 6. Write a program that asks the user for their name and age using input().
# Then print:
# Hello <name>, you are <age> years old!

name = input("Enter user name : ")
age = int(input("Enter user age"))

print("Hello",name,", you are",age,"year old!")


# 7. Create three variables: length, width, area.
# Assign numbers to length and width.
# Calculate the area of a rectangle.
# Print the result.



length=float(input("Enter length"))
width = float(input("Enter width"))

area_of_rectangle = float(length*width)
print("Area of Rectangle : ", area_of_rectangle)


# 8. Make variables:
# first_name = "Alice"
# last_name = "Smith"
# Combine them into one variable full_name.

first_name = "Alice"
last_name = "Smith"

full_name = first_name+last_name
print(full_name)



# 9. Store True in a variable called is_sunny.
# If it’s True, print "Let's go outside!"
# Otherwise, print "Stay inside."

is_sunny = True
if is_sunny:
    print("Let's go outside!")
else:
    print("Stay inside")



# 10. Create variables with these values:
# x = 5
# y = "5"
# z = 5.0
# Print their types and explain why they are different.


x = 5
y = "5"
z = 5.0

print(type(x), "X is an integer because it a whole number")
print(type(y), "Y is a String, I know that inside a double quets ssinged value to be a Sting")
print(type(z), " Band it is a decimal value")





# 11. Swap the values of two variables (without using a third variable)

a=5
b=9

a=a+b
b=a-b
a=a-b

print(f"After swapping a = {a} and b = {b} ")


# 12. Write a program that asks for two numbers from the user and prints:
# The larger number
# The smaller number


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(f"The larger number is {num1}")
    print(f"The smaller number is {num2}")
elif num2 > num1:
    print(f"The larger number is {num2}")
    print(f"The smaller number is {num1}")
else:
    print("Both numbers are equal.")


# 13. Create a variable with a string (like "Python Programming").
# Print its length (len())
# Print it in uppercase (.upper())
# Print only the first 6 characters (slicing).


string = "Python Programming"

print(len(string))
print(string.upper())
print(string[:6])




# 14. Create a program that:
# Stores your birth year in a variable
# Calculates your age in 2025
# Prints: "In 2025, you will be X years old."

 birth_year = 2005

age_in_2025 = 2025-birth_year
print(f"In 2025, you will be {age_in_2025} years old")


#OR

from datetime import date

birth_year = 2005
current_year = date.today().year   # gets current year automatically
age = current_year - birth_year

print(f"In {current_year}, you will be {age} years old.")



# 15. write a program where:
# A variable score = 85
# If score ≥ 90 → print "Grade: A"
# If 70 ≤ score < 90 → print "Grade: B"
# Otherwise → print "Grade: C"


score= 85
if score >= 90:
    print("Grade : A")
elif 70 <= score < 90:
    print("Grade B")
else:
    print("Grade C")

