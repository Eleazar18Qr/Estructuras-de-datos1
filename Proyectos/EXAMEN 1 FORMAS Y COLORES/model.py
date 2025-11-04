# model.py

# Definición de las 3 formas y los 3 colores (RGBA)
SHAPES = ['Circle', 'Rectangle', 'Triangle']
# ROJO, VERDE, AZUL
COLORS = [(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)] 

class Node:
    """Representa un estado (Forma + Color) en la lista circular."""
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.next = None
        self.prev = None # Usaremos un puntero doble para simplificar Back

    def get_state(self):
        """Retorna una tupla (forma, color_rgba)."""
        return (self.shape, self.color)

class ShapeCircularList:
    """
    Implementa la lista doblemente enlazada circular con 9 estados predefinidos.
    """
    def __init__(self):
        self.head = None
        self.current_node = None
        self._build_circular_list()

    def _build_circular_list(self):
        """
        Construye los 9 nodos (3 ciclos de 3 formas) y los enlaza circularmente.
        """
        nodes = []
        
        # Generar los 3 ciclos de color
        for cycle_start_index in range(3):
            # El orden de colores se desplaza en cada ciclo
            color_order = COLORS[cycle_start_index:] + COLORS[:cycle_start_index]
            
            for i, shape in enumerate(SHAPES):
                color = color_order[i]
                nodes.append(Node(shape, color))

        # Enlazar los 9 nodos circularmente
        num_nodes = len(nodes)
        if num_nodes == 0:
            return

        self.head = nodes[0]
        self.current_node = self.head

        for i in range(num_nodes):
            current = nodes[i]
            
            # El siguiente nodo
            next_index = (i + 1) % num_nodes
            current.next = nodes[next_index]
            
            # El nodo anterior
            prev_index = (i - 1 + num_nodes) % num_nodes
            current.prev = nodes[prev_index]
            
            # Verifica el último nodo para cerrar el ciclo (automático con el módulo %)
            
    def get_current_state(self):
        """Retorna el estado de la forma y color actual."""
        if self.current_node:
            return self.current_node.get_state()
        return ('Circle', COLORS[0]) # Estado por defecto si está vacía

    def next_state(self):
        """Avanza al siguiente nodo."""
        if self.current_node:
            self.current_node = self.current_node.next

    def previous_state(self):
        """Retrocede al nodo anterior (usando el puntero 'prev')."""
        if self.current_node:
            self.current_node = self.current_node.prev