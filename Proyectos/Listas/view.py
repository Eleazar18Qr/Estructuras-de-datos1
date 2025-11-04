# view.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle
from kivy.metrics import dp 

# Colores de la paleta
COLOR_BEIGE = (0.95, 0.9, 0.85, 1)      
COLOR_DARK_GREEN = (0.1, 0.25, 0.25, 1) 
COLOR_WHITE = (1, 1, 1, 1)              
COLOR_PENDING = (0.8, 0.4, 0, 1)        
COLOR_COMPLETED = (0, 0.6, 0, 1)        

class TodoListView(BoxLayout):
    """
    Vista (Interfaz de Usuario) de la aplicación de Lista de Tareas con Kivy.
    Diseño funcional.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.controller = None 

        # 1. Fondo Beige Suave (Canvas del widget principal)
        with self.canvas.before:
            Color(*COLOR_BEIGE)  
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

        # Contenedor Principal
        self.main_container = BoxLayout(orientation='horizontal', size_hint_y=0.9, padding=dp(10))
        
        # === Panel Izquierdo (Input y Display) ===
        self.left_panel = BoxLayout(orientation='vertical', size_hint_x=0.75, spacing=dp(10))

        # Campo de Texto (Nueva Tarea)
        self.task_input = TextInput(
            text='Nueva tarea',
            size_hint_y=None, height=dp(40),
            multiline=False,
            padding=[dp(10), dp(10), dp(10), dp(10)],
            background_color=COLOR_WHITE,
            foreground_color=(0,0,0,1)
        )
        self.left_panel.add_widget(self.task_input)

        # Recuadro Grande para Mostrar Tareas (ScrollView)
        self.tasks_list_layout = BoxLayout(
            orientation='vertical',
            spacing=dp(5), 
            size_hint_y=None, 
            padding=dp(10)
        )
        self.tasks_list_layout.bind(minimum_height=self.tasks_list_layout.setter('height'))
        
        self.scroll_view = ScrollView() 
        self.scroll_view.add_widget(self.tasks_list_layout)
        
        # Contenedor para dibujar el fondo blanco (solución al error de ScrollView)
        list_background = BoxLayout(padding=dp(1), size_hint_y=1)
        
        with list_background.canvas.before:
            Color(*COLOR_WHITE)
            self.list_bg_rect = Rectangle(size=list_background.size, pos=list_background.pos)
        
        # Vinculación corregida usando lambda/setattr
        list_background.bind(size=lambda instance, value: setattr(self.list_bg_rect, 'size', value), 
                             pos=lambda instance, value: setattr(self.list_bg_rect, 'pos', value))
            
        list_background.add_widget(self.scroll_view)
        
        self.left_panel.add_widget(list_background)
        self.main_container.add_widget(self.left_panel)


        # === Panel Derecho (Botones) ===
        self.right_panel = BoxLayout(orientation='vertical', size_hint_x=0.25, spacing=dp(10), padding=(dp(10), dp(5), dp(10), dp(5)))

        def create_styled_button(text, on_press_handler):
            btn = Button(
                text=text,
                size_hint_y=None, height=dp(50),
                color=COLOR_DARK_GREEN, 
                background_normal='',
                background_color=COLOR_WHITE,
                border=[dp(1), dp(1), dp(1), dp(1)],
                # border_color fue eliminado para corregir el error de inicialización
            )
            btn.bind(on_press=on_press_handler)
            return btn

        # Botones
        self.btn_add = create_styled_button('Añadir Tarea', self.on_add_task)
        self.right_panel.add_widget(self.btn_add)
        
        self.btn_display = create_styled_button('Mostrar lista de tareas', self.update_task_list)
        self.right_panel.add_widget(self.btn_display)

        self.btn_search = create_styled_button('Buscar Tarea', self.on_search_task)
        self.right_panel.add_widget(self.btn_search)
        
        self.btn_delete = create_styled_button('Eliminar Tarea', self.on_delete_task)
        self.right_panel.add_widget(self.btn_delete)

        self.btn_mark_complete = create_styled_button('Marcar Completada', self.on_mark_completed)
        self.right_panel.add_widget(self.btn_mark_complete)
        
        self.main_container.add_widget(self.right_panel)
        self.add_widget(self.main_container)

        # Etiqueta para mensajes de feedback (abajo del todo)
        self.feedback_label = Label(
            text='Por favor, introduce una descripción de la tarea', 
            size_hint_y=None, height=dp(30),
            color=(0.1, 0.1, 0.1, 1),
            font_size='18sp'
        )
        self.add_widget(self.feedback_label)
        

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    # --- Métodos de Interacción con el Controlador ---

    def on_add_task(self, instance):
        description = self.task_input.text
        if self.controller and self.controller.add_task(description, to_start=False):
            self.task_input.text = ''
            self.feedback_label.text = f'Tarea "{description}" añadida. Presione "Mostrar lista..." para verla.'
        else:
            self.feedback_label.text = 'Por favor, introduce una descripción de la tarea.'

    def on_mark_completed(self, instance):
        description = self.task_input.text
        if self.controller and self.controller.mark_completed(description):
            self.update_task_list()
            self.feedback_label.text = f'Tarea "{description}" marcada como COMPLETADA.'
        else:
            self.feedback_label.text = f'Error: Tarea "{description}" no encontrada.'

    def on_delete_task(self, instance):
        description = self.task_input.text
        if self.controller and self.controller.delete_task(description):
            self.update_task_list()
            self.task_input.text = ''
            self.feedback_label.text = f'Tarea "{description}" eliminada.'
        else:
            self.feedback_label.text = f'Error: Tarea "{description}" no encontrada para eliminar.'

    def on_search_task(self, instance):
        description = self.task_input.text
        result = self.controller.search_task(description)
        if result:
            desc, status = result
            self.feedback_label.text = f'¡Tarea Encontrada! Estado: {status}'
        else:
            self.feedback_label.text = f'Error: Tarea "{description}" no encontrada.'

    # --- Actualización de la Interfaz (Llamada por el botón Mostrar lista) ---

    def update_task_list(self, instance=None):
        self.tasks_list_layout.clear_widgets()
        
        if self.controller is None:
            return

        tasks = self.controller.get_all_tasks()
        
        for description, status in tasks:
            status_color = COLOR_COMPLETED if status == 'Completada' else COLOR_PENDING
            
            task_widget = BoxLayout(size_hint_y=None, height=dp(40))
            
            task_label = Label(text=description, size_hint_x=0.7, color=(0, 0, 0, 1), halign='left', valign='middle', font_size='18sp')
            task_label.bind(size=task_label.setter('text_size'))
            task_widget.add_widget(task_label)

            status_label = Label(text=status, size_hint_x=0.3, color=status_color, font_size='18sp')
            task_widget.add_widget(status_label)
            
            self.tasks_list_layout.add_widget(task_widget)
        
        self.feedback_label.text = "Lista