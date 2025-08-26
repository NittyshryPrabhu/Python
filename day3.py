# If Else Statement

# Quick Summary
# if → checks a condition.
# elif → checks another condition if the first is False.
# else → runs if none of the above are True.
# Indentation is mandatory.


# 📝 Practice: If-Else Conditions



#  Beginner Exercises

# 1. Write a program that asks the user for a number.
# If it’s positive → print "Positive"
# Else → print "Negative or Zero"

'''num = int(input("Enter a number : "))

if num>0:
    print("Positive number")
elif num<0:
    print("Negative number")
else:
    print("Zero")'''


# 2. Ask the user for their age.
# If age ≥ 18 → print "You are an adult"
# Else → print "You are a minor"

'''age = int(input("Enter your age : "))

if age>=18:
    print("You are an adult")
else:
    print("You are a minor")'''


# 3. Take a number as input.
# If even → print "Even number"
# Else → print "Odd number"

'''num = int(input("Enter a number : "))
if num%2==0:
    print("Even number")
else:
    print("Odd number")'''


# 4. Ask the user for a password.
# If password = "python123" → print "Access Granted"
# Else → print "Wrong Password"


'''password = input("Enter a password : ")

if password == "python123":
    print("Access Granted")
else:
    print("Wrong password")'''


# 5. Ask the user for temperature in Celsius.
# If temp ≥ 30 → print "Hot day"
# Else → print "Cool day"

'''temp = int(input("Enter temperature in celsius : "))
if temp>=30:
    print("Hot day")
else:
    print("Cool day")'''


# 🔹 Intermediate Exercises


#  6. Write a program to check the largest of two numbers.

'''num1 = int(input("Enter first number"))
num2= int(input("Enter second number"))

if num1 > num2 :
    print(f"Largest number {num1}")
    print(f"Smaller number {num2}")
elif num1 < num2 :
    print(f"Largest number {num2}")
    print(f"Smaller number {num1}")
else:
    print("Both number are equal")'''


# 7. Ask the user for 3 subject marks.
# If average ≥ 90 → "Grade A"
# If average ≥ 70 → "Grade B"
# If average ≥ 50 → "Grade C"
# Else → "Fail"


'''phy = float(input("Enter physics marks : "))
chem = float(input("Enter chemistry marks : "))
math = float(input("Enter mathematics marks"))

average = (phy + chem + math)/3

if average >= 90 :
    print("Grade A")
elif average >= 70:
    print("Grade B")
elif average >= 50:
    print("Grade C")
else:
    print("Fail")'''

# 8. Take a year as input.
# If it’s divisible by 4 → print "Leap Year"
# Else → print "Not a Leap Year"

'''year = int(input("Enter a year : "))

if year%4==0:
    print("Leap Year")
else:
    print("Not a Leap Year")'''

# 9. Ask the user to enter their name.
# If the name starts with "A" → print "Your name starts with A"
# Else → print "Your name doesn’t start with A"

'''name = input("Enter your name : ")

if name[0].upper() =="A":
    print("Your name starts with A")
else:
    print("Your name doesn't start with A")'''


# 10. Ask the user for their salary and years of experience.
# If experience ≥ 5 years → give 10% bonus.
# Else → no bonus.

'''salary = int (input("Enter your salary : "))
experience = int(input("Enter years of  experience : "))

if experience >= 5:
    bonus = (salary * 10)/100 
    salary = bonus+salary
    print(f"Total salary after giving 10% bonus {salary}")
else:
    print("no bonus")
    print(f"Total salary {salary}")'''


# 🔹 Challenge Exercises

# 11. ATM Machine Simulation:
# Ask the user for a PIN (correct pin = 1234)
# If correct → ask amount to withdraw and print "Withdrawal successful".
# Else → print "Wrong PIN"



'''pin = input("Enter your pin")
correct_pin = "1234" 

if  pin == correct_pin :
    amount = float(input("Enter amount to withdrawal"))
    print(f" amout {amount} Withdrawal successful")

else:
    print("Wrong PIN")'''


# 12. Ticket Pricing:
# Age < 12 → ₹100
# Age between 12–60 → ₹200
# Age > 60 → ₹150

'''age = int(input("Enter your age : "))

if age < 12 :
    print("You ticket price is 100")
elif 12 <= age <= 60 :
    print("Your ticket price is 200")
else :
    print("Your ticket price is 150")
'''


# 13. Calculator Program:
# Take two numbers and an operator (+, -, *, /) from user.
# Perform the operation using if-else.

'''num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

op =input("Enter an operator (+, -, *, /) : ")

if op == "+":
    print(f"Sum of {num1} + {num2} = {num1 + num2}")
elif op == "-":
    print(f"Sub of {num1} - {num2} = {num1 - num2}")
elif op == "*":
    print(f"Multiple of {num1} * {num2} = {num1 * num2}")
elif op == "/":
    print(f"Divide of {num1}/{num2} = {num1/num2}")
else:
    print("Invalid operator")'''


# 14. Traffic Light System:
# Input = "Red" → print "Stop"
# Input = "Yellow" → print "Wait"
# Input = "Green" → print "Go"
# Otherwise → "Invalid Input"

'''light = input("Enter Trafic Light ( Red , Yello , Green)")

if light =="Red":
    print("Stop")
elif light == "Yellow":
    print("Wait")
elif light == "Green":
    print("Go")
else :
    print("Invalid Light")
'''

# 15. Guessing Game:
# Set a secret number (e.g., 7).
# Ask the user to guess it.
# If guess = secret → print "Correct!"
# If guess < secret → "Too low"
# Else → "Too high"

set = {1,2, 3, 4, 5,6,7}
number = int(input("Guessing a number between 1-7 : "))

if number == set :
    print("Correct")