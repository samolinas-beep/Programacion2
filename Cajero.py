def calcular_billetes(monto):
    # Verificar si es múltiplo de 20
    if monto % 20 != 0:
        print("Error: el monto debe ser múltiplo de 20.")
        return None

    billetes = [200, 100, 50, 20]
    resultado = {}

    for b in billetes:
        cantidad = monto // b
        if cantidad > 0:
            resultado[b] = cantidad
            monto = monto % b

    # Imprimir resultado
    salida = ", ".join([f"{v}x Q{k}" for k, v in resultado.items()])
    print(salida)
    return resultado