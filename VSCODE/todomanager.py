import datetime

task_list = []  # Array of dictionaries

def add_new_task():
    print("\n--- ADD NEW TASK ---")
    title = input("Task Name: ")
    desc = input("Description: ")
    deadline = input("Deadline (DD-MM-YYYY): ")
    priority = input("Priority [High/Medium/Low]: ").capitalize()

    task = {
        "title": title,
        "desc": desc,
        "deadline": deadline,
        "priority": priority,
        "status": "Pending"
    }

    task_list.append(task)
    print(f"\nTask '{title}' added successfully!")

def show_all_tasks():
    if not task_list:
        print("\nNo tasks in your list!")
        return

    print("\n========== YOUR TASK LIST ==========")

    for i, t in enumerate(task_list, start=1):
        print(f"\n{i}. {t['title']} [{t['priority']}]")
        print(f"   Description : {t['desc']}")
        print(f"   Deadline    : {t['deadline']}")
        print(f"   Status      : {t['status']}")

def mark_complete():
    show_all_tasks()

    try:
        num = int(input("\nEnter task number to mark as completed: "))

        if 1 <= num <= len(task_list):
            task_list[num - 1]["status"] = "Completed"
            print(f"\nTask '{task_list[num - 1]['title']}' marked as Completed!")
        else:
            print("\nInvalid task number!")

    except ValueError:
        print("\nPlease enter a valid number.")

def remove_task():
    show_all_tasks()

    try:
        num = int(input("\nEnter task number to delete: "))

        if 1 <= num <= len(task_list):
            removed = task_list.pop(num - 1)
            print(f"\nDeleted task: {removed['title']}")
        else:
            print("\nInvalid task number!")

    except ValueError:
        print("\nPlease enter a valid number.")

def main_menu():

    print("=" * 40)
    print("      SMART TO-DO MANAGER")
    print("=" * 40)

    while True:

        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_new_task()

        elif choice == "2":
            show_all_tasks()

        elif choice == "3":
            mark_complete()

        elif choice == "4":
            remove_task()

        elif choice == "5":
            print("\nThank you for using SMART TO-DO MANAGER!")
            break

        else:
            print("\nInvalid choice! Please try again.")

main_menu()