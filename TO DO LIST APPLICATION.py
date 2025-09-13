tasks = []  

print("WELCOME TO THE TO-DO LIST APPLICATION")
print("YOU CAN PERFORM THE FOLLOWING TASKS:")
print("TASK 1: ADD TASK")
print("TASK 2: DELETE TASK")
print("TASK 3: UPDATE TASK")
print("TASK 4: VIEW TASKS")

while True:
    try:
        choice = int(input("\nEnter the task you want to perform (1-4): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        try:
            add = int(input("Enter the number of items you want to add: "))
            for i in range(add):
                item = input(f"Enter item {i+1}: ")
                tasks.append(item)
            print(" Items added successfully.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == 2:
        if not tasks:
            print(" Cannot delete. The list is currently empty.")
        else:
            try:
                idx = int(input(f"Enter the index (0 to {len(tasks)-1}) of the item to delete: "))
                if 0 <= idx < len(tasks):
                    removed = tasks.pop(idx)
                    print(f"✅ '{removed}' has been deleted successfully.")
                else:
                    print(" Invalid index.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == 3:
        if not tasks:
            print(" Cannot update. The list is currently empty.")
        else:
            try:
                index = int(input(f"Enter the index (0 to {len(tasks)-1}) of the item to update: "))
                if 0 <= index < len(tasks):
                    new_item = input("Enter the new item: ")
                    tasks[index] = new_item
                    print(" Item updated successfully.")
                else:
                    print(" Invalid index.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == 4:
        if tasks:
            print(" Your current tasks:")
            for i, task in enumerate(tasks):
                print(f"{i}: {task}")
        else:
            print(" Your task list is empty.")

    else:
        print(" Invalid choice. Please select between 1 and 4.")
