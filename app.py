# Creating a CRUD todo list app 
# Store the tasks in a file in this directory
# Read the tasks from the file and print them to the console
# Write a new task to the file
# Wrap it all into a loop with a menu asking what I want to do


def add_task():
    task = input("Enter a task: ")
    with open("tasks", "a") as file:
        file.write(task + "\n")
    print("Task added!")

def read_tasks():
    with open("tasks", "r") as file:
        tasks = file.readlines()
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}", end="")
    if len(tasks) == 0: 
        print("No tasks to do!")

def main():
    while True:
        print('*' * 10)
        print("1. Add task")
        print("2. Read tasks")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            read_tasks()
        elif choice == "3":
            break
        else:
            print("Invalid choice! Try again.")
        
        continue_choice = input("Do you want to do anything else? (yes/no): ")
        if continue_choice.lower() == "no":
            break

if __name__ == "__main__":
    main()