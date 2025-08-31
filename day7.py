# To Do List or CLI APPLICATION USING Conditinal Statement

🔹 What is a CLI App?
A CLI (Command Line Interface) app is a program that runs in the terminal/command prompt.
The user interacts with it by typing commands, instead of clicking buttons (like in a GUI app).

🔹 What is a To-do App?
A To-do App is a small program where we can store, manage, and track our tasks.

Example:

Add a task → "Complete Maths assignment"
View tasks → Print the full list of tasks
Complete a task → Mark a task as done
Delete a task → Remove a task that’s no longer needed

🔹 Workflow of a CLI To-do App

Takes user input (through commands):
add "Study Python"
list
done 2
delete 3

Stores the data internally

At first, tasks can be stored in a simple list or a file.
Later, it can be upgraded to use a database.

Displays the output
Shows tasks with numbering.

If a task is completed, it shows [x].


PROGRAM : 
tasks = []  # for store tasks

while True:
    print("\n...... To Do List APP ......")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Mark as done")
    print("4. Delete task")
    print("5. Exit from To Do List App")

    choice = input("Enter choice 1-5 : ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append({"task": task, "done": False})
        print(f"Task '{task}' added successfully ✅")

    elif choice == "2":
        if not tasks:  
            print("No tasks added yet.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, start=1):  
                status = "✅ Done" if t["done"] else "❌ Not Done"
                print(f"{i}. {t['task']} [{status}]")   

    elif choice == "3":
        if not tasks:
            print("No tasks found to mark.")
        else:
            num = int(input("Enter task number to mark as done: "))
            if 1 <= num <= len(tasks):   
                tasks[num - 1]["done"] = True   
                print(f"Task {num} marked as Done ✅")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):   
                removed = tasks.pop(num - 1)
                print(f"Task '{removed['task']}' deleted successfully ❌")  
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Exiting To Do List, Goodbye 👋")
        break

    else:
        print("Invalid choice! Please enter a valid option (1-5).")

