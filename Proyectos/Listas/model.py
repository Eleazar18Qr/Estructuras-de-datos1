# model.py

# =================================================================
# 1. Clase Nodo con Getters y Setters
# =================================================================
class Node:
    """
    Nodo de la Lista Enlazada. Representa una tarea.
    Estructura: _data (descripción), _status (Pendiente/Completada), _next (puntero).
    """
    def __init__(self, data=None, status='Pendiente'):
        self._data = data
        self._status = status
        self._next = None

    # --- Getters ---
    def get_data(self):
        return self._data

    def get_status(self):
        return self._status

    def get_next(self):
        return self._next

    # --- Setters ---
    def set_data(self, new_data):
        self._data = new_data

    def set_status(self, new_status):
        if new_status in ['Pendiente', 'Completada']:
            self._status = new_status
        else:
            raise ValueError("Estado no válido. Use 'Pendiente' o 'Completada'.")

    def set_next(self, new_next_node):
        if isinstance(new_next_node, Node) or new_next_node is None:
            self._next = new_next_node
        else:
            raise TypeError("El puntero 'next' debe ser un objeto Node o None.")

# =================================================================
# 2. Clase Lista Enlazada Dinámica (Lógica de Tareas)
# =================================================================
class DynamicLinkedList:
    """
    Lista Enlazada Simple para gestionar las tareas.
    """
    def __init__(self):
        self.head = None

    # --- Funcionalidades de Tarea ---

    def add_task(self, description, to_start=False):
        """
        Agrega una nueva tarea (nodo) al final o al principio de la lista.
        """
        new_node = Node(description, 'Pendiente')
        
        if to_start or not self.head:
            new_node.set_next(self.head)
            self.head = new_node
            return

        current = self.head
        while current.get_next():
            current = current.get_next()
        current.set_next(new_node)

    def search_task(self, description):
        """
        Busca una tarea por su descripción.
        Retorna la tupla (descripción, estado) si se encuentra, o None.
        """
        current = self.head
        while current:
            if current.get_data() == description:
                return (current.get_data(), current.get_status())
            current = current.get_next()
        return None

    def mark_completed(self, description):
        """
        Busca una tarea y cambia su estado a 'Completada'.
        Retorna True si se completó, False si no se encontró.
        """
        current = self.head
        while current:
            if current.get_data() == description:
                current.set_status('Completada')
                return True
            current = current.get_next()
        return False

    def delete_task(self, description):
        """
        Busca una tarea y la elimina de la lista.
        Retorna True si se eliminó, False si no se encontró.
        """
        current = self.head
        
        # Caso 1: Eliminar la cabeza
        if current and current.get_data() == description:
            self.head = current.get_next()
            return True

        # Caso 2: Buscar y eliminar en el medio o al final
        prev = None
        while current and current.get_data() != description:
            prev = current
            current = current.get_next()

        if current is None:
            return False

        prev.set_next(current.get_next())
        return True

    def display_tasks(self):
        """
        Recorre la lista y retorna una lista de tuplas con todas las tareas
        (descripción, estado).
        """
        tasks = []
        current = self.head
        while current:
            tasks.append((current.get_data(), current.get_status()))
            current = current.get_next()
        return tasks