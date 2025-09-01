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


'''my_dict = {
    "name" : "nitish",
    "Age"  : 20,
    "Roll No." : 530032,

}
print(my_dict.items())

for key, value in my_dict.items():
    print(f"key { key } and values {value}")'''



#🔹 Beginner (Sets)


# 11. Create a set of 5 numbers. Print its length.

'''num = {1, 2, 3, 4, 5}

print(len(num))'''


# 12. Add the number 100 to the set.

'''num.add(100)
print(num)'''

# 13. Remove an element from the set using .remove().

'''num.remove(3)
print(num)'''

# 14. Try adding duplicate elements to a set and observe the result.

'''num.add(5)
print(num)''' # obsevation : not allow duplicate elements to a set in Python Programming

'''🔹 Definition of a Set in Python
A set is:

Unordered → elements don’t have a fixed position (no indexing like lists/tuples).

Mutable → you can add or remove elements.

Unique → no duplicate elements are allowed.

🔎 Why duplicates aren’t allowed?

Internally, Python sets are implemented using hash tables.

Each element’s value is converted into a hash (a unique number).

Hash values must be unique in the table.

If you try to add a duplicate element, Python sees the hash already exists → it ignores it.'''



# 15. Convert a list [1, 2, 2, 3, 4, 4, 5] into a set to remove duplicates.

'''a_list = [1, 2, 2, 3, 4, 4, 5]
print(a_list)

a_set = set(a_list)
print(a_set)'''


# 🔹 Intermediate (Sets)

# 16. Given two sets A = {1, 2, 3} and B = {3, 4, 5}, find:
# Union
# Intersection
# Difference

'''A = {1, 2, 3}
B = {3, 4, 5}

print("Union : ", A | B)

print("Intersection : ", A & B)

print("Difference A - B : ", A - B)

print("Difference B - A : ", B - A)'''


# 17. Write a program to check if a set is a subset of another set.
# Example: {1, 2} ⊆ {1, 2, 3, 4}

'''A = {1, 2, 3, 4}

B =  {1, 2}

if B <= A :
    print("Yes, B is the subset of A")
else:
    print("No, B is not the subset of A")

# OR

if B.issubset(A):
    print("Yes, B is the subset of A")
else:
    print("No, B is not the subset of A")
'''

# 18. Create a set of vowels from the word "education".

'''word = "education"

vowels = {"a", "e", "i", "o", "u"}
word_set = set()

for letter in word:
    if letter in vowels:
        word_set.add(letter)

print(word_set)
'''


# 19. Find the common elements between two lists using sets.
# Example: [1, 2, 3] and [2, 3, 4] → {2, 3}

'''first_list =  [1, 2, 3]
second_list = [2, 3, 4]

print(set(first_list) & set(second_list))
'''


# 20. Write a program to check if two sets have no elements in common.

'''A = {1, 2, 3}
B = {4, 5, 6}

if A.isdisjoint(B):
    print("Yes, the sets have no elements in common")
else:
    print("No, the sets have common elements")'''



# 🔹 Challenge (Dictionaries & Sets Together)

# 21. Create a dictionary of students with their subjects stored as sets.
#  Example:


students = {
    "Alice": {"Math", "English"},
    "Bob": {"Math", "Science"},
    "Charlie": {"History", "English"}
}

# Print all subjects Alice is taking.
# Find common subjects between Alice and Bob.
# Find all unique subjects taken by all students.

print(f"All subjects Alice is taking: ", students["Alice"])

print("common subjects between Alice and Bob: ", students["Alice"] & students["Bob"])

all_subjects = set().union(*students.values())
print("All unique subjects:", all_subjects)