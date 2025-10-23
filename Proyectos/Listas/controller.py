# controller.py

class TodoListController:
    """
    Controlador para la aplicación de Lista de Tareas.
    Actúa como intermediario entre la Vista (Kivy) y el Modelo (Lista Enlazada).
    """
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.controller = self

    def add_task(self, description, to_start=False):
        """
        Agrega una nueva tarea al modelo. NO actualiza la vista inmediatamente.
        Ignora el texto inicial del campo de input.
        """
        # Verifica que la descripción no esté vacía Y no sea el texto inicial
        if description.strip() and description.strip() != 'Nueva tarea':
            self.model.add_task(description.strip(), to_start)
            return True
        return False

    def search_task(self, description):
        """
        Busca una tarea en el modelo y devuelve su información si existe.
        """
        return self.model.search_task(description)

    def mark_completed(self, description):
        """
        Busca una tarea y cambia su estado a 'Completada'.
        """
        return self.model.mark_completed(description)

    def delete_task(self, description):
        """
        Busca una tarea y la elimina de la lista.
        """
        return self.model.delete_task(description)

    def get_all_tasks(self):
        """
        Obtiene la representación en lista de tuplas de todas las tareas del modelo.
        """
        return self.model.display_tasks()