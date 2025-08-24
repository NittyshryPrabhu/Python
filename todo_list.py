# To Do List APPLICATION USING Conditinal Statement


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
