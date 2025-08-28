# 📝 Practice: Functions in Python

# 🔹 Beginner Exercises

# 1. Write a function greet() that prints "Hello, welcome to Python!".
'''
def greet():
    print("Hello, Welcome to Python!")

greet()'''


# 2. Write a function square(num) that returns the square of a number.

'''def square(num):
    return num**2

num = int(input("Enter a number : "))
result=square(num)
print(result)'''




# 3. Write a function is_even(num) that checks if a number is even.
# Return True if even, else False.
'''def is_even(num):
    return num % 2 ==0
       

num = int(input("Enter a number :  "))
if is_even(num):
    print("even")
else:
    print("not even")
'''



# 4.Write a function add(a, b) that takes two numbers and returns their sum.

'''def add(a, b):
    return a+b

num1 = int (input("Enter first number : "))
num2 = int (input("Enter second number : "))

print(add(num1 , num2))
'''

# Write a function area_of_circle(r) that returns the area of a circle.
# (Formula: πr², take π = 3.14)

'''def area_of_circle(r):
    return 3.14 *(r**2)

radius = float(input("Enter radius of circle : "))

print(f"Area of circle : {area_of_circle(radius)}")'''



# 🔹 Intermediate Exercises

# 6. Write a function greet_user(name, age) that prints:
# Hello <name>, you are <age> years old.
'''

def greet_user(name, age):
   print(f"Hello {name}, you are {age} years old.")
    

name = input("Enter your name : ")
age = int(input("Enter your age : "))

greet_user(name, age)'''




# 7. Write a function factorial(n) that returns the factorial of n.
# (Example: 5! = 120)

'''def factorial(n):
    fact =1
    i=1
    while i <= n:
        fact = fact *i
        i += 1          
    
    return fact

num = int(input("Enter a number : "))

fact = factorial(num)
print(fact)
'''

# 8. Write a function reverse_string(s) that returns the reverse of a string.
# (Example: "hello" → "olleh")


'''def reverse_string(s):
    reversed_string = " "
    for char in s:
        reversed_string = char + reversed_string 
    return reversed_string

str = input("Enter a string ")

print(reverse_string(str))'''

# OR

'''def reverse_string(s):
    return  s[::-1]

text = input("Enter a string ")

print(reverse_string(text))'''
    


# 9. Write a function is_palindrome(s) that checks if a string is a palindrome.
# (Palindrome → same forward & backward, e.g., "madam")

'''def is_palindrome(s):
    return s == s[::-1]

text = input("Enter a string : ")

if is_palindrome(text):
    print(f"{text } is a palindrome")
else:
    print(f"{text} is not a palindrome")'''


# 10. Write a function max_of_three(a, b, c) that returns the largest of three numbers.

'''def max_of_three(a, b , c):
    if a > b :
        if a > c :
            return a
        else :
            return c
    else :
        if b > c :
            return b 
        else:
            return c
    
a = int (input("Enter a : "))
b = int (input("Enter b : "))
c = int (input("Enter c : "))

print(f"The largest number is {max_of_three(a, b , c )}")'''


# 🔹 Challenge Exercises


# 11. Write a function fibonacci(n) that returns the first n Fibonacci numbers.
'''
def fibonacci(n):
    sequence = []
    a , b = 0 , 1

    for _ in range(n):
        sequence.append(a)

        a , b = b , a+b

    return sequence

num = int(input("How many fabonacci numbers , you want to print : "))
print(f"Fabonacci series : {fibonacci(num)}")'''
        

# 12. Write a function calculator(a, b, operator) that performs addition, subtraction, multiplication, or division based on the operator (+, -, *, /).

'''def calculator(a, b, operator):
    if operator == '+':
        addition = a+b
        return addition
    elif operator == '-':
        subtraction = a-b
        return subtraction
    elif operator == '*':
        multiplication = a*b
        return multiplication
    elif operator == '/':
        dividion = a/b
        return division
    else :
        return "Invalid operator"

a  = int(input("Enter a : "))
b  = int(input("Enter b : "))

operator = input("Enter a operator ( + , - , *,  / )")

print(calculator(a,b, operator))
'''



# 13. Write a function count_vowels(s) that returns the number of vowels in a string.

'''def count_vowels(s):
    vowels = "aeiouAEIOU"

    count = 0

    for i in s:
        if i in vowels:
            count += 1

        
    return count
   

str = input("Enter a string : ")

print(count_vowels(str))'''




# 14. Write a function prime_numbers(n) that prints all prime numbers up to n.
'''
def prime_numbers(n):
    for num in range(2 , n+1):
        is_prime = True
        for i in range (2 , int(num**0.5)+1):
            if num % i == 0:
                is_prime =False
                break
        if is_prime:
            print(num , end= " ")

limit = int(input("Enter a number up to which you want prime numbers: "))
print(f"Prime number up to {limit}")
prime_numbers(limit)
'''

# 15. Write a function grade(marks) that takes a percentage and returns:
# ≥ 90 → "A"
# ≥ 70 → "B"
# ≥ 50 → "C"
# Else → "Fail"


def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >=70:
        return "B"
    elif marks >=50:
        return "C"
    else:
        return "Fail"

percentage = int(input("Enter your obtain percentage: "))
print(f"Your Grade : {grade(percentage)}")
grade(percentage)