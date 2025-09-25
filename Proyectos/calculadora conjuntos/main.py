# main.py

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

# Importar el Modelo y el Controlador
from model import ConjuntosModel
from controller import ConjuntosController


# Vista principal que se enlaza con el archivo .kv
class ConjuntosView(BoxLayout):
    pass


class ConjuntosApp(App):
    """
    Clase principal de la aplicación.
    Se encarga de inicializar el Modelo, la Vista y el Controlador.
    """

    def build(self):
        # Cargar la interfaz desde el archivo .kv
        Builder.load_file("view.kv")

        # Crear la vista
        self.view = ConjuntosView()

        # Crear el modelo
        self.model = ConjuntosModel()

        # Crear el controlador, conectando modelo y vista
        self.controller = ConjuntosController(self.model, self.view)

        return self.view


if __name__ == "__main__":
    ConjuntosApp().run()
