def add_task():
    with open("/Users/mark/Code/todo/tasks", "a") as f:
        f.write(input('--> \n'))

    with open("/Users/mark/Code/todo/tasks", "r") as f:
        print(f.read())

def main():
    add_task()

if __name__ == "__main__":
    main()