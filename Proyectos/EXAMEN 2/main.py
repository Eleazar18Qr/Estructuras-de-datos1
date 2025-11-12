# main.py
from kivy.app import App
import controller # <--- SOLUCIÓN: Importamos el módulo completo
import model      # <--- SOLUCIÓN: Importamos el módulo completo
import view       # <--- SOLUCIÓN: Importamos el módulo completo

class CalculatorApp(App):
    """Clase principal de la aplicación Kivy."""
    
    def build(self):
        self.title = "Calculadora MVC con Pilas"
        
        # 1. Inicializar el Modelo
        # Usamos model.ExpressionProcessor en lugar de ExpressionProcessor
        model_instance = model.ExpressionProcessor() 
        
        # 2. Inicializar la Vista
        # Usamos view.CalculatorView en lugar de CalculatorView
        view_instance = view.CalculatorView() 
        
        # 3. Inicializar el Controlador
        # Usamos controller.CalculatorController
        controller.CalculatorController(model_instance, view_instance)
        
        # Devuelve el widget principal
        return view_instance

if __name__ == '__main__':
    CalculatorApp().run()