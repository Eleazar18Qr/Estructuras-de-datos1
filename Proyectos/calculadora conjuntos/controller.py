class ConjuntosController:
    """
    El Controlador conecta la Vista con el Modelo.
    Maneja las interacciones del usuario y actualiza la vista
    cuando los datos en el modelo cambian.
    """
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def obtener_conjuntos(self):
        """
        Obtiene los conjuntos ingresados por el usuario desde la vista.
        """
        conjunto_a = self.view.ids.conjunto_a.text
        conjunto_b = self.view.ids.conjunto_b.text

        # Convertir las cadenas de texto en conjuntos
        conjunto_a = set(e.strip() for e in conjunto_a.split(',')) if conjunto_a else set()
        conjunto_b = set(e.strip() for e in conjunto_b.split(',')) if conjunto_b else set()


        return conjunto_a, conjunto_b

    def realizar_union(self):
        """
        Realiza la unión de los conjuntos y actualiza la vista.
        """
        conjunto_a, conjunto_b = self.obtener_conjuntos()
        resultado = self.model.union(conjunto_a, conjunto_b)
        self.view.ids.resultado.text = f"Resultado: {resultado}"

    def realizar_interseccion(self):
        """
        Realiza la intersección de los conjuntos y actualiza la vista.
        """
        conjunto_a, conjunto_b = self.obtener_conjuntos()
        resultado = self.model.interseccion(conjunto_a, conjunto_b)
        self.view.ids.resultado.text = f"Resultado: {resultado}"

    def realizar_diferencia(self):
        """
        Realiza la diferencia de los conjuntos y actualiza la vista.
        """
        conjunto_a, conjunto_b = self.obtener_conjuntos()
        resultado = self.model.diferencia(conjunto_a, conjunto_b)
        self.view.ids.resultado.text = f"Resultado: {resultado}"

    def realizar_diferencia_simetrica(self):
        """
        Realiza la diferencia simétrica de los conjuntos y actualiza la vista.
        """
        conjunto_a, conjunto_b = self.obtener_conjuntos()
        resultado = self.model.diferencia_simetrica(conjunto_a, conjunto_b)
        self.view.ids.resultado.text = f"Resultado: {resultado}"

    def verificar_subconjunto(self):
        """
        Verifica si un conjunto es subconjunto del otro y actualiza la vista.
        """
        conjunto_a, conjunto_b = self.obtener_conjuntos()
        resultado = conjunto_a.issubset(conjunto_b)
        self.view.ids.resultado.text = f"Resultado: {'Sí' if resultado else 'No'}"

    def verificar_superconjunto(self):
        """
        Verifica si un conjunto es superconjunto del otro y actualiza la vista.
        """
        conjunto_a, conjunto_b = self.obtener_conjuntos()
        resultado = conjunto_a.issuperset(conjunto_b)
        self.view.ids.resultado.text = f"Resultado: {'Sí' if resultado else 'No'}"