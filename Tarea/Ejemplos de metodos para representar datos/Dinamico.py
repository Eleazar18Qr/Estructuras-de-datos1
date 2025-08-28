

transacciones = []

def depositar(monto):
    """Agrega un depósito al historial de transacciones."""
    transacciones.append({'tipo': 'depósito', 'monto': monto})
    print(f"Depósito de ${monto} registrado.")

def retirar(monto):
    """Agrega un retiro al historial de transacciones."""
    saldo_actual = consultar_saldo()
    if monto > saldo_actual:
        print("Fondos insuficientes para realizar el retiro.")
    else:
        transacciones.append({'tipo': 'retiro', 'monto': monto})
        print(f"Retiro de ${monto} registrado.")

def ver_historial():
    """Muestra el historial de transacciones."""
    if not transacciones:
        print("No hay transacciones registradas.")
    else:
        print("Historial de transacciones:")
        for i, transaccion in enumerate(transacciones, start=1):
            print(f"{i}. {transaccion['tipo'].capitalize()}: ${transaccion['monto']}")

def consultar_saldo():
    """Calcula y devuelve el saldo actual."""
    saldo = 0
    for transaccion in transacciones:
        if transaccion['tipo'] == 'depósito':
            saldo += transaccion['monto']
        elif transaccion['tipo'] == 'retiro':
            saldo -= transaccion['monto']
    return saldo

def menu():
    """Muestra el menú principal y gestiona las opciones del usuario."""
    while True:
        print("\n--- Menú Principal ---")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Ver historial de transacciones")
        print("4. Consultar saldo")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            monto = float(input("Ingrese el monto a depositar: "))
            depositar(monto)
        elif opcion == '2':
            monto = float(input("Ingrese el monto a retirar: "))
            retirar(monto)
        elif opcion == '3':
            ver_historial()
        elif opcion == '4':
            print(f"Saldo actual: ${consultar_saldo()}")
        elif opcion == '5':
            print("Gracias por usar el sistema. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecución del programa
menu()