# controller.py
import model 
import view  



class CalculatorController:
    """Controlador para la aplicación de calculadora de expresiones."""
    # Usamos las referencias directas a las clases de los módulos importados
    def __init__(self, model_instance: model.ExpressionProcessor, view_instance: view.CalculatorView): 
        self.model = model_instance
        self.view = view_instance
        self.view.controller = self 

    def calculate_expression(self, expression_text: str):
        """Procesa la expresión infija, la convierte a prefija y calcula el resultado."""
        expression_text = expression_text.strip()
        if not expression_text:
            self.view.update_results("", "Por favor, introduce una expresión.")
            return

        try:
            # Llamamos a los métodos usando self.model
            prefix_expression = self.model.infix_to_prefix(expression_text)
            result = self.model.evaluate_prefix(prefix_expression)
            self.view.update_results(prefix_expression, str(result))
            
        except ValueError as e:
            self.view.update_results("", f"Error: {e}")
        except Exception as e:
            self.view.update_results("", f"Error interno: {e}")