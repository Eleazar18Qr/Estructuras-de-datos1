


FILENAME = "catalogo_libros.txt"

def cargar_catalogo(filename=FILENAME):
    """Carga el catálogo desde un archivo de texto."""
    catalogo = {}
    try:
        with open(filename, "r") as file:
            for linea in file:
                isbn, titulo, autor, genero = linea.strip().split(" | ")
                catalogo[isbn] = {'titulo': titulo, 'autor': autor, 'genero': genero}
    except FileNotFoundError:
        pass  # Si el archivo no existe, devuelve un catálogo vacío
    return catalogo

def guardar_catalogo(catalogo, filename=FILENAME):
    """Guarda el catálogo en un archivo de texto."""
    with open(filename, "w") as file:
        for isbn, datos in catalogo.items():
            file.write(f"{isbn} | {datos['titulo']} | {datos['autor']} | {datos['genero']}\n")

def agregar_libro(catalogo, titulo, autor, isbn, genero):
    """Agrega un nuevo libro al catálogo."""
    if isbn in catalogo:
        print("El libro con este ISBN ya existe en el catálogo.")
    else:
        catalogo[isbn] = {'titulo': titulo, 'autor': autor, 'genero': genero}
        print(f"Libro '{titulo}' agregado al catálogo.")

def buscar_libro(catalogo, criterio):
    """Busca libros por título, autor o ISBN."""
    resultados = []
    for isbn, datos in catalogo.items():
        if criterio.lower() in datos['titulo'].lower() or \
           criterio.lower() in datos['autor'].lower() or \
           criterio == isbn:
            resultados.append({'isbn': isbn, **datos})
    return resultados

def mostrar_catalogo(catalogo):
    """Muestra todos los libros en el catálogo."""
    if not catalogo:
        print("El catálogo está vacío.")
    else:
        print("\n--- Catálogo de Libros ---")
        for isbn, datos in catalogo.items():
            print(f"ISBN: {isbn}, Título: {datos['titulo']}, Autor: {datos['autor']}, Género: {datos['genero']}")

def menu():
    """Muestra el menú principal y gestiona las opciones del usuario."""
    catalogo = cargar_catalogo()
    while True:
        print("\n--- Menú del Catálogo de Biblioteca ---")
        print("1. Agregar un nuevo libro")
        print("2. Buscar un libro")
        print("3. Mostrar todos los libros")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            genero = input("Ingrese el género del libro: ")
            agregar_libro(catalogo, titulo, autor, isbn, genero)
        elif opcion == '2':
            criterio = input("Ingrese el título, autor o ISBN para buscar: ")
            resultados = buscar_libro(catalogo, criterio)
            if resultados:
                print("\n--- Resultados de la búsqueda ---")
                for libro in resultados:
                    print(f"ISBN: {libro['isbn']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Género: {libro['genero']}")
            else:
                print("No se encontraron libros que coincidan con el criterio.")
        elif opcion == '3':
            mostrar_catalogo(catalogo)
        elif opcion == '4':
            guardar_catalogo(catalogo)
            print("Catálogo guardado. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecución del programa
menu()