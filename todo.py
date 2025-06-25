def todolist():
    todo =[]
    print("Welcome to the To-Do List App!")

    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4.Mark a task as done")
    print("5. Exit")

    while True:
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            task = input("Enter the task: ")
            todo.append(task)
            print("Task added.")
        elif choice == 2:
            if len(todo) == 0:
                print("No tasks available.")
            else:
                print("Your tasks:")
                for i, task in enumerate(todo, 1):
                    print(f"{i}. {task}")
        elif choice == 3:
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(todo):
                removed_task = todo.pop(task_number - 1)
                print(f"Removed task: {removed_task}")
            else:
                print("Invalid task number.")
        elif choice == 4:
            task_number = int(input("Enter the task number to mark as done: "))
            if 1 <= task_number <= len(todo):
                print(f"Marked task as done: {todo[task_number - 1]}")
            else:
                print("Invalid task number.")
        elif choice == 5:
            print("Exiting the To-Do List App.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
todolist()