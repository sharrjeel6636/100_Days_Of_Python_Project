todo_list = []

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.append(task)
        print("Task added!")

    elif choice == "2":
        if not todo_list:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not todo_list:
            print("No tasks to remove!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")

            remove_index = int(input("Enter the task number to remove: "))
            if 1 <= remove_index <= len(todo_list):
                removed = todo_list.pop(remove_index - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number!")

    elif choice == "4":
        print("Exiting… Thank you!")
        break

    else:
        print("Invalid choice! Please enter a number between 1–4.")
