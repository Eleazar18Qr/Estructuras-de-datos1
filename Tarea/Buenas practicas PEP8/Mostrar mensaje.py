def saludar(nombre):
    """Genera un mensaje de saludo personalizado.

    Args:
        nombre: El nombre de la persona a saludar.

    Returns:
        Una cadena con el mensaje de saludo.
    """
    if nombre:
        return f"¡Hola, {nombre}!"
    return "¡Hola, mundo!"


if __name__ == "__main__":
    nombre_usuario = input("Ingresa tu nombre: ")
    mensaje_saludos = saludar(nombre_usuario)
    print(mensaje_saludos)