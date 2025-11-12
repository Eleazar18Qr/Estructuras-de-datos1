# main.py
from kivy.app import App
import controller 
import model      
import view       

class CalculatorApp(App):
    """Clase principal de la aplicación Kivy."""
    
    def build(self):
        self.title = "Calculadora MVC con Pilas"
        
        # 1. Inicializar el Modelo
        
        model_instance = model.ExpressionProcessor() 
        
        # 2. Inicializar la Vista
        
        view_instance = view.CalculatorView() 
        
        # 3. Inicializar el Controlador
        
        controller.CalculatorController(model_instance, view_instance)
        
        # Devuelve el widget principal
        return view_instance

if __name__ == '__main__':
    CalculatorApp().run()