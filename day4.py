# Loops (for, while, break, continue)

# 📝 Practice: Loops in Python


#🔹 Beginner Exercises

# 1. Print numbers from 1 to 10 using a for loop.

'''for i in range(1,11):
    print(i)'''
   
# 2. Print numbers from 10 down to 1 using a while loop.

'''i=10
while i>=1:
    print(i)
    i -= 1'''

# 3. Print the multiplication table of 5 using a for loop.

'''
for i in range(1,11):
    print(5*i)'''


# 4. Print each character of the string "PYTHON" using a for loop.

'''str = "PYTHON"
for i in str:
    print(i)'''


# 5. Print only even numbers from 1 to 20 using a for loop.

'''for i in range(1,21):
    if i%2==0:
        print(i)'''


# 🔹 Intermediate Exercises

# 6. Ask the user for a number and print its factorial using a while loop.
# (Example: 5! = 120)

'''
num = int(input("Enter a number : "))

fact = 1
i=1
while i <= num:
    fact = fact*i
    i += 1
print(f"{num}! = {fact}")'''



# 7. Write a program to print the sum of numbers from 1 to 100 using a loop.
'''
sum = 0

for i in range(1, 101):
    sum = sum + i
print(f"Sum of numbers from 1 to 100 = {sum}")
'''

# 8. Print the first 10 Fibonacci numbers using a loop.
# (0, 1, 1, 2, 3, 5, 8, …)

'''a, b = 0 , 1
print(a)
print(b)

for _ in range(8):
    c = a+b
    print(c)
    a , b = b , c'''

# OR

'''a, b= 0 , 1

for _ in range(10):
    print(a , end=" ")
    a , b = b, a+b'''



# 9. Use a for loop and continue to print numbers from 1–10 but skip 5.

'''for i in range(1, 11):
    if i == 5:
        continue   # skip 5
    print(i)'''



# 10. Use a for loop and break to stop printing when the number reaches 7.

'''
for i in range (1, 10):
    if i==7:
        break
    print(i)'''

# using while loop

'''i=1
while i <= 10:
    
    if i==7:
        
        break
    print(i)
    i += 1'''

# 🔹 Challenge Exercises

# 11. Guessing Game 🎮
#Set a secret number (e.g., 8).
# Keep asking the user to guess until they get it right.
# Use a while loop with break.

'''secret = 8

while True :
    guess = int(input ("Guess the secret number"))
    
    if guess == secret:
        print("Congratulation, you guess right")
        break
    else:
        print("You guess wrong secret number")'''




# 12. Reverse a string using a loop.
# (Example: "hello" → "olleh")

'''str = "hello"

reverse_str = " "

for char in str:

    reverse_str = char + reverse_str

print(reverse_str)'''



# 13. Ask the user for a number n. Print a pattern:
# *
# **
# ***
# ****
# (Hint: use nested for loops)

'''row = int(input("Enter a row number "))

for i in range(1, row+1):
    for j in range(i):
        print("*" , end=" ")
    print()'''

# 14. Print all prime numbers between 1 and 50

'''
for num in range(2 , 51):
    is_prime = True

    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num,end=" ")'''




# 15. Infinite Loop Safety 🚨
#  Create a while True: loop that keeps asking the user for input.
#If the user types "exit", break the loop.


while True:
    types = input("Enter any types")

    if types == "exit":
        break



