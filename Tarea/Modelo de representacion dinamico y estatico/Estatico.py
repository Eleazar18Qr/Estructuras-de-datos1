
class AutomovilEstatico:
    def __init__(self, marca, modelo, anio, color):
        # Estructura estática: lista con tamaño fijo
        self.datos = [None] * 4
        self.datos[0] = marca
        self.datos[1] = modelo
        self.datos[2] = anio
        self.datos[3] = color

    # Getters
    def get_marca(self):
        return self.datos[0]

    def get_modelo(self):
        return self.datos[1]

    def get_anio(self):
        return self.datos[2]

    def get_color(self):
        return self.datos[3]

    # Setters
    def set_marca(self, marca):
        self.datos[0] = marca

    def set_modelo(self, modelo):
        self.datos[1] = modelo

    def set_anio(self, anio):
        self.datos[2] = anio

    def set_color(self, color):
        self.datos[3] = color

# Ejemplo de uso
auto_estatico = AutomovilEstatico("Toyota", "Corolla", 2020, "Rojo")
print(auto_estatico.get_marca())  # Toyota
auto_estatico.set_color("Azul")
print(auto_estatico.get_color())  # Azul