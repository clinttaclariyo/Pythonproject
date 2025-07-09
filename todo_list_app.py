FILENAME = "todo.txt"

try:
    with open(FILENAME, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    tasks = []

print("Welcome to the To-Do List App!")
print("Type 'done' to exit.\n")

while True:
    task = input("Enter a task: ")
    if task.lower() == 'done':
        break
    tasks.append(task)

with open(FILENAME, "w") as file:
    for task in tasks:
        file.write(task + "\n")

print("\nYour To-Do List:")
for i, task in enumerate(tasks, 1):
    print(f"{i}. {task}")