# String and its Properties

# 🔹 Beginner

# 1. Create a string "Python Programming" and:
# Print its length.
# Print the first and last character.
# Slice "Python" from it.


'''text = "Python Programming"
print(len(text))
print(text[0] , text[-1])
print(text[:6])'''

# 2. Take a string " Hello World " and:
# Remove extra spaces.
# Convert it to uppercase.
# Replace "World" with "Python".

'''text = " Hello World "
text =text.strip()
print(text)
print(text.upper())
print(text.replace("World","Python"))'''



# 3. Count how many times the letter "a" appears in the string "banana".

'''fruit = "banana"
count = 0
for letter in fruit:
    if letter == "a":
        count += 1
print(count)

# OR
print(fruit.count("n"))'''


# 4. Given "python is fun", capitalize the first letter of each word.

'''sentence = "python is fun"

print(sentence.title())
'''

# 5. Write a program to check if the string "data" exists in "big data analytics".


'''sen = "big data analytics"

if "data" in sen:
    print("Found")
else:
    print("Not Exist")'''


# 🔹 Intermediate

# 6. Input a sentence from the user and:
# Convert it to lowercase.
# Count how many spaces are in it.
# Find the index of the word "Python" (if present).

'''sen = input("Enter a sentence: ")

lowercase = sen.lower()  # covert in lower case 

print(lowercase)

count = sen.count(" ")  # count " " in the sentence

print(count)

if "Pyhton" in sen:
    print(f"Index of 'Pyhton' : ", sen.index("python"))
else:
    print("Python is found")'''



# 7. Given "mississippi", create a dictionary that counts each character’s frequency.

'''
word = "mississippi"
my_dict = {}
    
for char in word:
    if char in my_dict:
        my_dict[char] += 1
    else:
        my_dict[char] = 1

print(my_dict)

'''

# 8. Convert "12345" into an integer and add 10. (Hint: type casting)


'''num_in_str = "12345"

num_in_int = int(num_in_str) + 10

print(num_in_int)
'''

# 9. Join a list of words ["I", "love", "Python"] into one string using " ".join().

'''word_in_list = ["I", "love", "Python"]

word_in_str = " ".join(word_in_list)

print(word_in_str)
'''

# 10. Reverse a string using slicing.

'''word = "mississippi"

Reverse_word = word[::-1]
print(Reverse_word)
'''


