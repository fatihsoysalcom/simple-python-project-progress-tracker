# main.py

def display_tasks(tasks):
    """Displays all current tasks with their completion status."""
    print("\n--- Current Tasks ---")
    if not tasks:
        print("No tasks defined yet.")
        return

    # Demonstrates iteration (loop) over a list of dictionaries
    for i, task in enumerate(tasks):
        status = "✅ Completed" if task["is_completed"] else "⏳ Pending"
        print(f"{i + 1}. {task['name']} [{status}]")
    print("---------------------\n")

def mark_task_complete(tasks, task_index):
    """Marks a specific task as complete based on its index."""
    # Demonstrates conditional logic and list indexing
    if 0 <= task_index < len(tasks):
        tasks[task_index]["is_completed"] = True
        print(f"Task '{tasks[task_index]['name']}' marked as complete.")
    else:
        print("Invalid task number.")

def calculate_progress(tasks):
    """Calculates the overall completion percentage of tasks."""
    if not tasks:
        return 0.0
    # Demonstrates list comprehension and basic arithmetic
    completed_count = sum(1 for task in tasks if task["is_completed"])
    return (completed_count / len(tasks)) * 100

def main():
    """Main function to run the project tracker application."""
    # Simulate initial tasks for a new project/developer.
    # This represents the "foundation" or initial requirements discussed in Dev Week 1.
    project_tasks = [
        {"name": "Setup development environment", "is_completed": False},
        {"name": "Understand project requirements", "is_completed": False},
        {"name": "Implement basic 'Hello World' function", "is_completed": False},
        {"name": "Write initial unit tests", "is_completed": False},
        {"name": "Submit first code review", "is_completed": False},
    ]

    print("Welcome to your Dev Week 1 Project Tracker!")
    print("Let's get started on building a solid foundation.")

    # Main application loop for user interaction
    while True:
        display_tasks(project_tasks)
        progress = calculate_progress(project_tasks)
        print(f"Overall Project Progress: {progress:.2f}%")

        print("\nWhat would you like to do?")
        print("1. Mark a task as complete")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            try:
                task_num = int(input("Enter the number of the task to complete: "))
                # Adjust for 0-based indexing for list access
                mark_task_complete(project_tasks, task_num - 1)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '2':
            print("Exiting Project Tracker. Keep up the great work!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
