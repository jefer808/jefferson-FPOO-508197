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
        print("\n--- Lista de Tareas Registradas ---")
        if not self.task_list:
            print("No se han registrado tareas.")
        else:
            for task in self.task_list:
                print(f"{task}\n{'-'*40}")


def main():
    registry = TaskRegistry()

    while True:
        print("Registra una nueva tarea:")
        task_id = input("ID de la tarea: ")
        title = input("Título de la tarea: ")
        qualification = float(input("Calificación (0 a 5): "))
        category = int(input("Categoría (1: Quiz, 2: Partial, 3: Job): "))

        task = Task(task_id, title, qualification, category)
        registry.add_task(task)

        continue_input = input("¿Desea registrar otra tarea? (sí/no): ").strip().lower()
        if continue_input != 'sí':
            break

    registry.show_tasks()
    print(f"Se han registrado {len(registry.task_list)} tareas.")


if __name__ == "__main__":
    main()
