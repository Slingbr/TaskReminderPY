import threading
from task_manager import TaskMethods
from reminder import ReminderService

def display_menu():
    print("\n--- Task Manager ---")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Mark task as complete")
    print("5. Save tasks to file")
    print("6. Load tasks from file")
    print("7. Exit")

def main():
    task_methods = TaskMethods()
    

    reminder_service = ReminderService(task_methods)


    reminder_thread = threading.Thread(target=reminder_service.start_reminder_check)
    reminder_thread.daemon = True
    reminder_thread.start()

    while True:
        display_menu()
        choice = input("Select an option (1-7): ")

        if choice == "1":
            name = input("Task name: ")
            due_date = input("Due date (YYYY-MM-DD): ")
            reminder_time = input("Reminder time (HH:MM, 24-hour format): ")
            description = input("Description (optional): ")
            priority = input("Priority (Low, Medium, High): ")
            status = "Pending"

            task_methods.AddTask(name, due_date, reminder_time, description, priority, status)
            print("Task added.")

        elif choice == "2":
            task_methods.viewTasks()

        elif choice == "3":
            name = input("Enter the name of the task to delete: ")
            task_methods.DeleteTask(name)

        elif choice == "4":
            name = input("Enter the name of the task to mark as complete: ")
            task_methods.markTaskComplete(name)

        elif choice == "5":
            task_methods.SaveTaskToTxt()
            print("Tasks saved to tasks.txt")

        elif choice == "6":
            task_methods.load_tasks_from_txt()
        
        elif choice == "7":
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid option. Please select a number from 1 to 7.")

if __name__ == "__main__":
    main()
