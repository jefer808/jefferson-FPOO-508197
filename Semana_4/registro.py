class Task:
    def __init__(self, task_id, title, qualification, category):
        self.task_id = task_id
        self.title = title
        self.qualification = qualification
        self.category = self.convert_category(category)

    def convert_category(self, category_num):
        categories = {1: 'Quiz', 2: 'Partial', 3: 'Job'}
        return categories.get(category_num, 'Unknown category')

    def __str__(self):
        return f"ID: {self.task_id}, Title: {self.title}, Qualification: {self.qualification}, Category: {self.category}"


class TaskRegistry:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)

    def show_tasks(self):
        print("\nList of Tasks:")
        for task in self.task_list:
            print(task)


def main():
    registry = TaskRegistry()
    number_of_tasks = 5  

    for i in range(number_of_tasks):
        print(f" Registra la tarea {i + 1} of {number_of_tasks}:")
        task_id = input("ID de la tarea: ")
        title = input("Titulo de la tarea: ") 
        qualification = float(input(" Calificacion (0 a 5): "))
        category = int(input("Category (1: Quiz, 2: Partial, 3: Job): "))

        task = Task(task_id, title, qualification, category)
        registry.add_task(task)

    registry.show_tasks()
    print(f" Un total de tareas {number_of_tasks} Se han registrado las tareas")

if __name__ == "__main__":
    main()
