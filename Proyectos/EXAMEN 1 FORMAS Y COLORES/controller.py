# controller.py
from model import ShapeCircularList

class ShapeController:
    """
    Controlador: Maneja la lógica de navegación entre los estados de la lista circular
    y coordina la actualización de la Vista.
    """
    def __init__(self, app_instance):
        # El Modelo se inicializa con la lista circular de 9 estados
        self.model = ShapeCircularList()
        self.app = app_instance

    def get_current_state(self):
        """Devuelve la forma y el color del nodo actual."""
        return self.model.get_current_state()

    def move_next(self):
        """Avanza al siguiente estado en la lista circular y actualiza la vista."""
        self.model.next_state()
        # Le pide a la Vista (RootWidget) que se actualice
        self.app.root.update_shape_display()

    def move_back(self):
        """Retrocede al estado anterior en la lista circular y actualiza la vista."""
        self.model.previous_state()
        # Le pide a la Vista (RootWidget) que se actualice
        self.app.root.update_shape_display()