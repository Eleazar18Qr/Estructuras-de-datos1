# view.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle # <--- ¡IMPORTANTE: Revisa esta línea!

class CalculatorView(BoxLayout):
    """Vista (Interfaz de Usuario) de la aplicación de calculadora."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 15
        self.spacing = 15
        self.controller = None 

        # Color de Fondo
        with self.canvas.before:
            Color(0.95, 0.9, 0.85, 1)  # Beige Suave
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

        # Contenedor principal de la cuadrícula
        main_grid = GridLayout(cols=2, spacing=10, size_hint_y=0.7)

        # --- Fila 1: Expresión Infija ---
        main_grid.add_widget(Label(text='Introduzca la expresión:', size_hint_x=0.35, color=(0,0,0,1), font_size='18sp'))
        self.expression_input = TextInput(
            hint_text='Ej: 3 + 2 * (6 - 8) / 5',
            multiline=False,
            size_hint_x=0.65,
            font_size='20sp',
            background_color=(1,1,1,1),
            foreground_color=(0,0,0,1)
        )
        main_grid.add_widget(self.expression_input)

        # --- Fila 2: Botón Calcular y Notación Prefija ---
        self.calculate_button = Button(
            text='Calcular',
            size_hint_x=0.35,
            background_color=(0.3, 0.7, 0.3, 1), 
            color=(1, 1, 1, 1),
            font_size='20sp'
        )
        self.calculate_button.bind(on_press=self.on_calculate_expression)
        main_grid.add_widget(self.calculate_button)
        
        self.prefix_output = TextInput(
            hint_text='Notación Prefija...',
            multiline=False,
            readonly=True, 
            size_hint_x=0.65,
            font_size='20sp',
            background_color=(0.9,0.9,0.9,1),
            foreground_color=(0,0,0,1)
        )
        main_grid.add_widget(self.prefix_output)

        # --- Fila 3: Resultado ---
        main_grid.add_widget(Label(text='Resultado:', size_hint_x=0.35, color=(0,0,0,1), font_size='18sp'))
        self.result_output = TextInput(
            hint_text='Resultado de la operación...',
            multiline=False,
            readonly=True, 
            size_hint_x=0.65,
            font_size='20sp',
            background_color=(0.9,0.9,0.9,1),
            foreground_color=(0,0,0,1)
        )
        main_grid.add_widget(self.result_output)

        self.add_widget(main_grid)
        
        # Etiqueta para feedback y errores
        self.feedback_label = Label(text='¡Introduce una expresión!', size_hint_y=0.3, color=(0.5, 0.5, 0.5, 1))
        self.add_widget(self.feedback_label)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_calculate_expression(self, instance):
        """Maneja el evento del botón y llama al controlador."""
        expression = self.expression_input.text
        if self.controller:
            self.feedback_label.text = "" 
            self.controller.calculate_expression(expression)

    def update_results(self, prefix_expression, result_text):
        """Actualiza los TextInputs con los resultados."""
        self.prefix_output.text = prefix_expression
        self.result_output.text = result_text

        # Actualiza el feedback
        if "Error" in result_text:
            self.feedback_label.color = (0.8, 0.2, 0.2, 1) # Rojo
            self.feedback_label.text = result_text
        else:
            self.feedback_label.color = (0.0, 0.5, 0.0, 1) # Verde
            self.feedback_label.text = "Operación completada con éxito."