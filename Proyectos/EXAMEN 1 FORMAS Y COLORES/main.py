# main.py
import kivy
from kivy.app import App
from view import ShapeView
from controller import ShapeController

# La clase principal de la vista (definida en view.py) debe estar disponible
# para que el Controlador pueda interactuar con ella.

class CircularShapeApp(App):
    """
    Clase principal de la aplicación Kivy.
    """
    def build(self):
        self.title = 'Formas Geométricas Circulares MVC'
        
        # 1. Inicializar el Controlador, el cual inicializa el Modelo
        self.controller = ShapeController(self)
        
        # 2. Inicializar la Vista, pasándole el controlador
        self.view = ShapeView(controller=self.controller)
        
        # La vista es el widget raíz
        return self.view

if __name__ == '__main__':
    CircularShapeApp().run()