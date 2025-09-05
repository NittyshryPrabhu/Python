# # Error handling (try-except-finally) 

# 📝 Practice Exercises: Error Handling in Python
# 🔹 Beginner

# 1.  Write a program that asks the user to enter a number.
# If the user enters something that is not a number, print "Invalid input" using try-except.

'''try:
    number = int(input("Enter a number: "))
    print(f"User Entered : ", number)
except ValueError:
    print("Invalid number")
'''
# 2. Take two numbers as input and divide them.
# Handle the case when the second number is zero.

'''try: 
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print(num1/num2)
except ValueError:
    print("Invalid number | Please enter a valid number")
except ZeroDivisionError:
    print("Error | cannot divide by zero")
'''

# 3. Open a file "data.txt" and read its content.
# If the file does not exist, print "File not found".


'''
try:
    file = open("data1.txt","r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("File not found")'''

# 4. Convert a string "123abc" into an integer.
# Catch the error and print "Cannot convert to int".

'''try:
    word = "123abc"
    word = int(word)
    print(word)
except ValueError:
    print("Cannot convert to int")
'''

# 5.Write a program to access the 10th element of a list [1,2,3].
# Handle the IndexError.

'''try:
    num_list = [1, 2, 3]
    print(num_list[10])
except IndexError:
    print("Not Available")
'''

# 🔹 Intermediate

# 6. Ask the user to enter their age.
# If the input is not a valid integer, show an error message.
# Otherwise, print "You are X years old."

'''try: 
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")
except ValueError:
    print("Input is not a valid integer")

'''

# 7.  Create a calculator program (addition, subtraction, division, multiplication).
# Handle ZeroDivisionError and ValueError.


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Enter a operator +,-,*,/")

    if 
 

# 8. Write a program that opens "story.txt" in read mode.
# If file exists → read and print content.
# If not → create it and write "Hello World" inside.


# Write a program that converts a list of strings ["10", "20", "thirty", "40"] into integers.


# Handle invalid values ("thirty") gracefully.


# Use try-except-else-finally:


# Try to divide 100 by a number given by user.


# Print "Division successful" if no error.


# Print "End of program" in the finally block.



# 🔹 Advanced
# Create a program that asks user to input a filename and tries to open it.


# If file not found → create the file and write "New file created".


# If found → display content.


# Write a program that reads numbers from a file numbers.txt (one number per line).


# If any line has non-numeric data, skip it with an error message but continue reading the rest.


# Write a program that continuously asks for a number until the user enters a valid integer.


# Use a while True loop + try-except.


# Create a banking program:


# Ask user for balance and withdrawal amount.


# Handle errors like invalid input (non-number) and insufficient funds.


# Write a function safe_divide(a, b) that:


# Returns result if valid.


# Returns "Error: Division by zero" if denominator is zero.


# Returns "Error: Invalid input" if inputs are not numbers.


