# main.py

from kivy.app import App
from controller import TodoListController
from model import DynamicLinkedList
from view import TodoListView

class TodoApp(App):
    """
    Clase principal de la aplicación Kivy.
    """
    def build(self):
        self.title = 'Gestor de Tareas'
        
        # 1. Inicializar el Modelo (Lista Enlazada - Inicia vacía)
        model = DynamicLinkedList()
        
        # 2. Inicializar la Vista (Interfaz Gráfica Kivy)
        view = TodoListView()
        
        # 3. Inicializar el Controlador, uniendo el Modelo y la Vista
        controller = TodoListController(model, view)
        
        return view

if __name__ == '__main__':
    TodoApp().run()