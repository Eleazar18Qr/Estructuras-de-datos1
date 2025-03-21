import time


class Temporizador:
    """Clase para medir el tiempo de ejecución de un bloque de código."""

    def __enter__(self):
        self.tiempo_inicio = time.time()
        return self

    def __exit__(self, tipo_excepcion, valor_excepcion, traza_excepcion):
        tiempo_fin = time.time()
        print(f"Tiempo transcurrido: {tiempo_fin - self.tiempo_inicio:.6f} segundos")


with Temporizador():
    # Aquí va el código cuyo tiempo de ejecución deseas medir
    for _ in range(1000000):
        pass