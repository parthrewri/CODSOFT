class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(Task(title))

    def list_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            status = '✓' if task.done else '✗'
            print(f"{i}. [{status}] {task.title}")

    def mark_task_done(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].done = True
        else:
            print("Invalid task index!")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
        else:
            print("Invalid task index!")
def main():
    todo_list = TodoList()

    while True:
        print("\nCommand Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            todo_list.add_task(title)
        elif choice == '2':
            todo_list.list_tasks()
        elif choice == '3':
            task_index = int(input("Enter task index to mark as done: "))
            todo_list.mark_task_done(task_index)
        elif choice == '4':
            task_index = int(input("Enter task index to delete: "))
            todo_list.delete_task(task_index)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
if __name__ == "__main__":
    main()

