from datetime import datetime 
class Task:

    def __init__(self, title, description, task_id):
        self.title = title
        self.id = task_id
        self.completed = False
        self.description = description
        self.created_at = datetime.now()

    def complete(self):
        self.completed = True

    def __str__(self):
        status = "[x]" if self.completed else "[ ]"
        date = self.created_at.strftime("%Y-%m-%d  %H:%M")

        return f"{status} [{self.id}] {self.title} - {self.description} ({date})"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, description):
        task = Task(title, description, self.next_id)
        self.tasks.append(task)
        self.next_id += 1
    
    def complete_task(self, task_id):
        for t in self.tasks:
            if t.id == task_id:
                t.complete()
                print(f"Task {t.title} completed successfully. ")
                return
        print(f"ERROR: Task with ID: {task_id} not found. ")

         

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task) 
                print(f"Task {task.title} deleted successfully. ")
                return
        print(f"Task with ID {task_id} not found. ")
    
    def show_tasks(self):
        if not self.tasks:
            print("No tasks found. ")
            return
        for task in self.tasks:
            print(task)
        return
        


def main():
    manager = TaskManager()
    while True:
        
        print("-----------------------")
        print("Menu")
        print("1. Add tasks. ")
        print("2. Show tasks. ")
        print("3. Complete task")
        print("4. Delete task. ")
        print("5. Exit. ")
        try:
            option1 = int(input("Choose an opcion: "))
        

            if option1 == 5:
                print("Exiting system... ")
                return
            elif option1 == 1:
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                manager.add_task(title, description)

            elif option1 == 2:
                manager.show_tasks()
            
            elif option1 == 3:
                try:
                    task_id = int(input("Enter task ID. "))
                    manager.complete_task(task_id)
                except ValueError:
                    print("Invalid option. ")
                    continue
            elif option1 == 4:
                manager.show_tasks()
                try:
                    task_id = int(input("Enter task ID. "))
                    manager.delete_task(task_id)
                except ValueError:
                    print("Invalid option. ")
                    continue
            
            else:
                print("Invalid option. ")
        except ValueError:
            print("Input invalid. Please enter a number. ")


           

                          


