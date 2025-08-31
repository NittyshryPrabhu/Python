# Dictionaries & Sets 
 
# 📝 Practice Exercises: Dictionaries & Sets


# 🔹 Beginner (Dictionaries)

'''# 1. Create a dictionary with details of a book: title, author, year. Print all values.

book = {
    "title" :   "A Lot Words",
    "author" :  "Nittyshry Prabhu",
    "year" : 2023
}

print(book.items())

# 2. Add a new key "price" with some value to the dictionary.

book ["price"] = 299

print(book.items())


# 3. Update the "year" of the book to a new year.

book ["year"] = 2024

print(book.items())


# 4. Remove the "author" key from the dictionary.

book.pop("author")
print(book.items()) 
print(book)

# 5. Write a program to print only the keys of a dictionary.

print (book.keys())'''


# 🔹 Intermediate (Dictionaries)

# 6. Create a dictionary of 3 students with their marks. Find the average marks.
# Example: {"A": 85, "B": 90, "C": 78}

'''students = {
    "A" : 85,
    "B" : 90,
    "C" : 78
}

average_marks = sum(students.values()) / len(students)

print(average_marks)'''



# 7. Check if a key "Python" exists in a dictionary.

'''my_dict = {
    "java" : 80,
    "c++"  : 78,
    "Python" : 96
}

if "Python" in my_dict :
    print("Python is Exist")
else:
    print("Python doesn't Exits")'''



# 8. Merge two dictionaries into one.

'''students.update(my_dict)
print(students)
'''
# 9. Count how many times each letter appears in the word "mississippi" (hint: dictionary).

'''word = "mississippi"
key = { }

for letter in word:
    if letter in key:
        key[letter] += 1
    else:
        key[letter] = 1

print(key)'''


# 10. Write a program to get both keys and values using .items().


my_dict = {
    "name" : "nitish",
    "Age"  : 20,
    "Roll No." : 530032,

}
print(my_dict.items())

for key, value in my_dict.items():
    print(f"key { key } and values {value}")
