# view.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Rectangle
# Importar Mesh para dibujar el triángulo relleno
from kivy.graphics.vertex_instructions import Mesh 
from kivy.graphics import InstructionGroup
from kivy.app import App
from kivy.metrics import dp 

# --- Widget Personalizado para Dibujar la Forma ---

class ShapeDisplay(Widget):
    """
    Widget que utiliza el Canvas para dibujar la forma geométrica actual.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shape = 'Circle'
        self.color = (1, 0, 0, 1)
        self.shape_instructions = InstructionGroup()
        self.bind(size=self.draw_shape, pos=self.draw_shape) # Redibujar al cambiar tamaño/posición
        self.canvas.add(self.shape_instructions)

    def update(self, shape, color):
        """Método llamado por la Vista principal para cambiar el estado."""
        self.shape = shape
        self.color = color
        self.draw_shape()

    def draw_shape(self, *args):
        """Dibuja la forma actual en el centro del widget."""
        self.shape_instructions.clear()
        
        # Calcular el tamaño y la posición para centrar la forma
        # Reducir el tamaño un poco más para que no toque los bordes, incluso el círculo.
        size = min(self.width, self.height) * 0.6 
        x = self.center_x - size / 2
        y = self.center_y - size / 2

        self.shape_instructions.add(Color(*self.color))

        if self.shape == 'Circle':
            # Círculo (Ellipse)
            self.shape_instructions.add(Ellipse(pos=(x, y), size=(size, size)))
            
        elif self.shape == 'Rectangle':
            # Rectángulo (Rectangle)
            self.shape_instructions.add(Rectangle(pos=(x, y), size=(size, size)))
            
        elif self.shape == 'Triangle':
            # Triángulo (usando Mesh para un relleno adecuado)
            # Definir 3 puntos del triángulo
            # Ajustamos las coordenadas para que el triángulo sea equilátero y centrado.
            # Vértice superior
            p1_x = self.center_x
            p1_y = y + size 
            
            # Vértice inferior izquierdo
            p2_x = x 
            p2_y = y 
            
            # Vértice inferior derecho
            p3_x = x + size
            p3_y = y
            
            # Los vértices para Mesh se definen como una lista plana [x1, y1, u1, v1, x2, y2, u2, v2, ...]
            # u, v son coordenadas de textura, que podemos ignorar si no usamos textura.
            vertices = [
                p1_x, p1_y, 0, 0,  # Vértice 1
                p2_x, p2_y, 0, 0,  # Vértice 2
                p3_x, p3_y, 0, 0   # Vértice 3
            ]
            
            # Los índices para Mesh definen cómo se conectan los vértices para formar triángulos.
            # Para un solo triángulo, simplemente usamos los índices 0, 1, 2.
            indices = [0, 1, 2]
            
            self.shape_instructions.add(
                Mesh(vertices=vertices, indices=indices, mode='triangles')
            )

# --- Vista Principal ---

class ShapeView(BoxLayout):
    """
    Vista principal de la aplicación Kivy.
    """
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.controller = controller

        # Fondo Blanco Completo (Tal como se ve en la imagen)
        with self.canvas.before:
            Color(1, 1, 1, 1)  
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

        # Contenedor Central (Botones + Forma)
        self.center_container = BoxLayout(orientation='horizontal', size_hint_y=0.9, padding=dp(20))
        
        # 1. Botón BACK
        self.btn_back = Button(
            text='BACK',
            size_hint_x=0.2,
            background_color=(0, 0, 0, 1), # Fondo negro
            color=(1, 1, 1, 1),            # Texto blanco
            font_size='24sp',
            on_release=self.on_back_press
        )
        self.center_container.add_widget(self.btn_back)
        
        # 2. Widget de Visualización de la Forma (Panel Central)
        self.shape_display = ShapeDisplay(size_hint_x=0.6)
        self.center_container.add_widget(self.shape_display)
        
        # 3. Botón NEXT
        self.btn_next = Button(
            text='NEXT',
            size_hint_x=0.2,
            background_color=(0, 0, 0, 1), # Fondo negro
            color=(1, 1, 1, 1),            # Texto blanco
            font_size='24sp',
            on_release=self.on_next_press
        )
        self.center_container.add_widget(self.btn_next)

        self.add_widget(self.center_container)
        
        # Inicializar la visualización al cargar
        self.update_shape_display()

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    # --- Métodos de Interacción del Usuario (Delegación) ---

    def on_next_press(self, instance):
        """Llama al método del controlador para avanzar."""
        self.controller.move_next()

    def on_back_press(self, instance):
        """Llama al método del controlador para retroceder."""
        self.controller.move_back()

    # --- Método de Actualización de la Vista (Respuesta del Controlador) ---

    def update_shape_display(self):
        """
        Obtiene el estado actual del controlador y actualiza el widget de dibujo.
        """
        shape, color = self.controller.get_current_state()
        self.shape_display.update(shape, color)