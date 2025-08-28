# 📝 Practice Exercises: Lists & Tuples

# 🔹 Beginner (Lists)

'''# 1. Create a list of 5 favorite fruits and print them.

fruits = ['apple', 'banana' , 'mango' , 'orange' , 'papita']
print(fruits)

# 2. Add "grapes" to the list using .append().
fruits.append('grapes')
print(fruits)

# 3. Insert "kiwi" at index 2 using .insert().
fruits.insert(2, 'kiwi')
print(fruits)

# 4. Remove "apple" from the list using .remove().
fruits.remove('apple')
print(fruits)

# 5. Create a list of numbers [10, 5, 20, 15] and sort them in ascending order.

list = [10, 5, 20, 15]
list.sort()
print(list)

'''
# 🔹 Intermediate (Lists)

'''# 6. Create a list of 10 numbers and print only the first 3 numbers.

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[0:3])

# 7. Reverse a list without using .reverse() (hint: slicing [::-1]).

print(list[::-1])

# 8. Count how many times "banana" appears in a list.

list = ['banana', 'apple','banana', 'papita', 'banana', 'papita' ]
print(list.count('banana'))

# 9. Write a program that finds the largest and smallest number in a list.

list = [14, 45, 67, 87, 23, 54, 13]
print(max(list))
print(min(list))

# 10. Merge two lists: [1, 2, 3] and [4, 5, 6].

first_list = [1, 2, 3, 4]
second_list = [5, 6, 7, 8, 9]
print(first_list + second_list)

'''


#🔹 Beginner (Tuples)

# 11. Create a tuple with 5 colors and print the second color.

'''colors = ('red', 'blue', 'white', 'black', 'pink')
print(colors[1])

# 12. Find the index of "blue" in a tuple ("red", "green", "blue", "yellow").

colours = ("red", "green", "blue", "yellow")
print(colours.index("blue"))

# 13. Count how many times "red" appears in the tuple ("red", "blue", "red", "green").

colors =   ("red", "blue", "red", "green")

print(colors.count("red"))

# 14. Create a single-element tuple containing the number 5. (Hint: (5,))

element = (5,)
print(element)

# 15. Convert a tuple into a list, add an element, and convert it back to a tuple.

colors =   ("red", "blue", "red", "green")
print(colors)
color = list(colors)    # covert into list
print(color)
color.append("black")   # add an element "black"
print(color)

colors = tuple(color)   # again convert into tuple
print(colors)'''



# 🔹 Challenge (Lists & Tuples)


# 16. Write a program that removes duplicates from a list.
# Example: [1, 2, 2, 3, 4, 4, 5] → [1, 2, 3, 4, 5]
'''
num = [1, 2, 2, 3, 4, 4, 5]

unique_num = list(set(num))
print(unique_num)


# 17. Write a program to find the sum of all numbers in a list.

num = [1, 2, 3, 4, 5, 9]
total=0
for i in num:
    total = total+i

print(f"Sum of all number in a list : {total}")

# 18. Given a tuple (10, 20, 30, 40, 50), swap the first and last elements.
# 👉 Result: (50, 20, 30, 40, 10)

numbers =  (10, 20, 30, 40, 50)

temp = list(numbers)

temp[0] , temp[-1] = temp[-1] , temp[0]

temp = tuple(temp)

print(temp)


# OR
numbers = (10, 20, 30, 40, 50)

swapped = (numbers[-1],) + numbers[1:-1] + (numbers[0],)

print(swapped) '''



# 19. Write a program that takes a list of words and prints the longest word.

words = ["ear", "elephants", "mango", "orange", "rat","govindadasfnaf"]
print(max(words))
# 20. Create a list of numbers and print only the even numbers.
