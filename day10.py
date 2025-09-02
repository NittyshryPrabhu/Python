
#  Practice Exercises: File Handling in Python

# 🔹 Beginner

# 1. Create a file called myfile.txt and write the text:
#  Hello World
# Welcome to Python

'''file = open("myfile.txt","x")

file = open("myfile.txt","w")
file.write("Hello World\nWelcome to Python")

'''


# 2. Then read and print the file content.

'''file = open("myfile.txt","r")
content = file.read()
print(content)
'''
# 3. Write a program to store your name, age, and city in a file called info.txt.

'''with open("info.txt","x") as info:
    info.write("Name : Nitish\nAge : 20\nCity : Meerut")

'''

'''content=open("info.txt","r")
content = content.read()
print(content)
'''

# 4. Read a file story.txt and print the number of characters in it.

'''file = open("story.txt","w")

file.write("Hey this is my story , you know that, I'm a writer , I write about this universe and its creation.")

file = open("story.txt","r")

content = file.read()
print(content)

count = 0

for char in content:
    count  += 1

print(count)
'''


# 5. Open story.txt and print only the first line.

'''file = open("story.txt","w")
file.write("I also write autobiaography.\nAnd also write mystriatic story and dramatics too.")
file = open("story.txt","r")
print(file.read())
file = open("story.txt","r")
print(file.readline())'''

# 6. Write a program that appends "Python is awesome!" at the end of myfile.txt.

'''file = open("myfile.txt","a")
file.write("\nPython is awesome!")
file.close()

file = open("myfile.txt","r")
print(file.read())
file.close()
'''


# 🔹 Intermediate

# 7. Create a file numbers.txt and write numbers from 1 to 20 (each on a new line).

'''file = open("numbers.txt","x")

file = open("numbers.txt","w")

for i in range(1,22541):
    file.write(str(i)+"\n")

file.close()'''


'''file = open("numbers.txt","r")
lines = file.readlines()
print(lines)
file.close()
'''

# 8. Read numbers.txt and calculate the sum of all numbers.

'''
sum=0
for i in lines:
    sum += int(i.strip())
print(sum)
'''

# 9. Copy the contents of one file (data.txt) into another (backup.txt).

'''# file = open("data.txt","x")

file = open("data.txt","w")
file.write("A new file , I will copy this file into a new file backup.txt")

file = open("data.txt","r")
content = file.read()


# file = open("backup.txt","x")

file = open("backup.txt","w")
file.write(f"Copied file text from data.txt : {content}")

'''


# 10. Count how many lines exist in story.txt.

'''file = open("story.txt", "r")
lines = file.readlines()

print("Lines in file story.txt: ", len(lines))

'''
# 11. Read a file and print only those lines which contain the word "Python".

'''with open("myfile.txt","r") as file:
    for line in file:
        if "Python" in line:
            print(line.strip())

'''

# 🔹 Advanced


# 12. Create a log file log.txt where every time the program runs, it appends the current date & time. (Hint: use datetime module).

'''# file =  open("log.txt","x") 

from datetime import datetime

# Get current date and time
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

# Open log.txt in append mode
with open("log.txt", "a") as file:
    file.write(timestamp + "\n")

print("Log updated at:", timestamp)'''

# 13. Write a program to count how many vowels (a, e, i, o, u) are in story.txt.

'''file = open("story.txt","r")
content = file.read()
file.close()
print(content)

vowels = "aeiouAIOUE"

count = 0
for char in content:
    if char in vowels:
        count += 1

print("Number of Vowels", count)'''

# 14. Take a list of names (["Alice", "Bob", "Charlie"]) and write each name into a new line in names.txt.

'''names = ["Alice", "Bob", "Charlie"]

# with open("names.txt","x") as file:
with open("names.txt","w")as file:
    for name in names:
        file.write(name + "\n")

file = open("names.txt","r")
print(file.read())'''

# Read a file and create a dictionary of word frequencies (how many times each word appears).


# Merge the contents of two files (file1.txt and file2.txt) into a new file merged.txt.



# 🔹 Challenge
# Write a program to create a student gradebook file.


# Ask user for student name and marks.


# Save it in grades.txt in format:

#  Name: Alice, Marks: 85
# Name: Bob, Marks: 90


# Write a program to read grades.txt and display all students who scored more than 80.


