
class AutomovilDinamico:
    def __init__(self, marca, modelo, anio, color):
        
        self.datos = {
            "marca": marca,
            "modelo": modelo,
            "anio": anio,
            "color": color
        }

    # Getters
    def get_marca(self):
        return self.datos["marca"]

    def get_modelo(self):
        return self.datos["modelo"]

    def get_anio(self):
        return self.datos["anio"]

    def get_color(self):
        return self.datos["color"]

    # Setters
    def set_marca(self, marca):
        self.datos["marca"] = marca

    def set_modelo(self, modelo):
        self.datos["modelo"] = modelo

    def set_anio(self, anio):
        self.datos["anio"] = anio

    def set_color(self, color):
        self.datos["color"] = color


auto_dinamico = AutomovilDinamico("Honda", "Civic", 2021, "Negro")
print(auto_dinamico.get_modelo())  # Civic
auto_dinamico.set_anio(2022)
print(auto_dinamico.get_anio())  # 2022