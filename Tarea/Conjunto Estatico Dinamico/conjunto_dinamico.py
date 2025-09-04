class ConjuntoDinamico:
    def __init__(self):
        """Inicializa un conjunto dinámico vacío."""
        self.elementos = []  # Lista dinámica para representar el conjunto (estructura dinamica)

    # Métodos Getter y Setter
    def get_elementos(self):  
        """Devuelve los elementos del conjunto."""
        return self.elementos

    def set_elementos(self, nuevos_elementos):  
        """Establece un nuevo conjunto de elementos."""
        self.elementos = list(set(nuevos_elementos))  # Elimina duplicados automáticamente

    # Operaciones básicas
    def agregar(self, elemento):  
        """Agrega un elemento al conjunto si no está presente."""
        if elemento not in self.elementos:
            self.elementos.append(elemento)

    def eliminar(self, elemento):  
        """Elimina un elemento del conjunto si está presente."""
        if elemento in self.elementos:
            self.elementos.remove(elemento)

    def pertenece(self, elemento):  
        """Verifica si un elemento pertenece al conjunto."""
        return elemento in self.elementos

    def mostrar(self):  
        """Muestra los elementos actuales del conjunto."""
        print("Conjunto:", self.elementos)

    # Operaciones de conjuntos
    def union(self, otro_conjunto):  
        """Devuelve la unión de dos conjuntos."""
        resultado = ConjuntoDinamico()
        resultado.set_elementos(self.elementos + otro_conjunto.get_elementos())
        return resultado

    def interseccion(self, otro_conjunto):  
        """Devuelve la intersección de dos conjuntos."""
        resultado = ConjuntoDinamico()
        resultado.set_elementos([elem for elem in self.elementos if elem in otro_conjunto.get_elementos()])
        return resultado

    def diferencia(self, otro_conjunto):  
        """Devuelve la diferencia de dos conjuntos."""
        resultado = ConjuntoDinamico()
        resultado.set_elementos([elem for elem in self.elementos if elem not in otro_conjunto.get_elementos()])
        return resultado

    def complemento(self, universo):  
        """Devuelve el complemento del conjunto con respecto a un universo."""
        resultado = ConjuntoDinamico()
        resultado.set_elementos([elem for elem in universo if elem not in self.elementos])
        return resultado


# Ejemplo de uso
if __name__ == "__main__":
    # Instanciación del objeto 
    conjunto1 = ConjuntoDinamico()
    conjunto2 = ConjuntoDinamico()

    # Operaciones básicas
    conjunto1.agregar(2)
    conjunto1.agregar(4)
    conjunto1.agregar(6)
    conjunto1.mostrar()  # Conjunto: [2, 4, 6]

    conjunto2.agregar(4)
    conjunto2.agregar(5)
    conjunto2.mostrar()  # Conjunto: [4, 5]

    # Operaciones de conjuntos
    union = conjunto1.union(conjunto2)
    union.mostrar()  # Conjunto: [2, 4, 6, 5]

    interseccion = conjunto1.interseccion(conjunto2)
    interseccion.mostrar()  # Conjunto: [4]

    diferencia = conjunto1.diferencia(conjunto2)
    diferencia.mostrar()  # Conjunto: [2, 6]

    universo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    complemento = conjunto1.complemento(universo)
    complemento.mostrar()  # Conjunto: [0, 1, 3, 5, 7, 8, 9]