class ConjuntosModel:
    """
    El Modelo se encarga de realizar las operaciones entre conjuntos.
    No sabe nada sobre cómo se mostrarán estos datos.
    """

    @staticmethod
    def union(conjunto_a, conjunto_b):
        """
        Realiza la unión de dos conjuntos.
        """
        return conjunto_a | conjunto_b

    @staticmethod
    def interseccion(conjunto_a, conjunto_b):
        """
        Realiza la intersección de dos conjuntos.
        """
        return conjunto_a & conjunto_b

    @staticmethod
    def diferencia(conjunto_a, conjunto_b):
        """
        Realiza la diferencia de dos conjuntos (A - B).
        """
        return conjunto_a - conjunto_b

    @staticmethod
    def diferencia_simetrica(conjunto_a, conjunto_b):
        """
        Realiza la diferencia simétrica de dos conjuntos.
        """
        return conjunto_a ^ conjunto_b