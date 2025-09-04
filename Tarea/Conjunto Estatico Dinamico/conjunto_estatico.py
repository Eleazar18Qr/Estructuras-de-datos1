class ConjuntoEstatico:
    def __init__(self, capacidad):
        """Inicializa un conjunto estático con una capacidad fija."""
        self.capacidad = capacidad
        self.elementos = [False] * capacidad  #(Estructura estatica de un tamaño fijo) Usando vector booleano para representar el conjunto

    # Métodos Getter y Setter
    def get_capacidad(self):  
        """Devuelve la capacidad del conjunto."""
        return self.capacidad

    def get_elementos(self):  
        """Devuelve el vector booleano de elementos."""
        return self.elementos

    def set_elementos(self, nuevos_elementos):  
        """Establece un nuevo vector de elementos."""
        if len(nuevos_elementos) == self.capacidad:
            self.elementos = nuevos_elementos
        else:
            print("Error: El tamaño del nuevo vector no coincide con la capacidad.")

    # Operaciones básicas
    def agregar(self, elemento):  
        """Agrega un elemento al conjunto."""
        if 0 <= elemento < self.capacidad:
            self.elementos[elemento] = True
        else:
            print(f"El elemento {elemento} está fuera del rango permitido (0-{self.capacidad - 1}).")

    def eliminar(self, elemento):  
        """Elimina un elemento del conjunto."""
        if 0 <= elemento < self.capacidad:
            self.elementos[elemento] = False
        else:
            print(f"El elemento {elemento} está fuera del rango permitido (0-{self.capacidad - 1}).")

    def pertenece(self, elemento):  
        """Verifica si un elemento pertenece al conjunto."""
        if 0 <= elemento < self.capacidad:
            return self.elementos[elemento]
        return False

    def mostrar(self):  
        """Muestra los elementos actuales del conjunto."""
        elementos_presentes = [i for i in range(self.capacidad) if self.elementos[i]]
        print("Conjunto:", elementos_presentes)

    # Diferentes operaciones de conjuntos
    def union(self, otro_conjunto):  
        """Devuelve la unión de dos conjuntos."""
        if self.capacidad != otro_conjunto.get_capacidad():
            print("Error: Los conjuntos tienen capacidades diferentes.")
            return None
        resultado = ConjuntoEstatico(self.capacidad)
        resultado.set_elementos([self.elementos[i] or otro_conjunto.get_elementos()[i] for i in range(self.capacidad)])
        return resultado

    def interseccion(self, otro_conjunto):  # Línea 55
        """Devuelve la intersección de dos conjuntos."""
        if self.capacidad != otro_conjunto.get_capacidad():
            print("Error: Los conjuntos tienen capacidades diferentes.")
            return None
        resultado = ConjuntoEstatico(self.capacidad)
        resultado.set_elementos([self.elementos[i] and otro_conjunto.get_elementos()[i] for i in range(self.capacidad)])
        return resultado

    def diferencia(self, otro_conjunto):  # Línea 63
        """Devuelve la diferencia de dos conjuntos."""
        if self.capacidad != otro_conjunto.get_capacidad():
            print("Error: Los conjuntos tienen capacidades diferentes.")
            return None
        resultado = ConjuntoEstatico(self.capacidad)
        resultado.set_elementos([self.elementos[i] and not otro_conjunto.get_elementos()[i] for i in range(self.capacidad)])
        return resultado

    def complemento(self):  # Línea 71
        """Devuelve el complemento del conjunto."""
        resultado = ConjuntoEstatico(self.capacidad)
        resultado.set_elementos([not self.elementos[i] for i in range(self.capacidad)])
        return resultado


# Ejemplo de uso
if __name__ == "__main__":
    # Instanciación del objeto ConjuntoEstatico
    conjunto1 = ConjuntoEstatico(10)  # Conjunto con capacidad para 10 elementos
    conjunto2 = ConjuntoEstatico(10)

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
    union.mostrar()  # Conjunto: [2, 4, 5, 6]

    interseccion = conjunto1.interseccion(conjunto2)
    interseccion.mostrar()  # Conjunto: [4]

    diferencia = conjunto1.diferencia(conjunto2)
    diferencia.mostrar()  # Conjunto: [2, 6]

    complemento = conjunto1.complemento()
    complemento.mostrar()  # Conjunto: [0, 1, 3, 5, 7, 8, 9]