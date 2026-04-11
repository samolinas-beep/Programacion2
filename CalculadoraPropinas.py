def calcular_propina(subtotal, porcentaje):
    return subtotal * (porcentaje / 100)


def calcular_total(subtotal, propina):
    return subtotal + propina


def dividir_cuenta(total, personas):
    if personas <= 0:
        return "Error: número de personas inválido."
    return total / personas


def aplicar_descuento(subtotal, descuento_pct):
    return subtotal - (subtotal * (descuento_pct / 100))


def mostrar_menu():
    print("\n=== MENÚ RESTAURANTE ===")
    print("1. Calcular propina")
    print("2. Dividir la cuenta")
    print("3. Aplicar descuento + propina")
    print("4. Salir")
    print("5. Ver resumen")


# Función auxiliar para leer números de forma segura
def leer_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")


def main():
    historial = []

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            subtotal = leer_float("Subtotal: Q")
            print("Sugerencias: 10%, 15%, 20%")
            porcentaje = leer_float("Porcentaje de propina: ")

            propina = calcular_propina(subtotal, porcentaje)
            total = calcular_total(subtotal, propina)

            print(f"Propina: Q{propina:.2f}")
            print(f"Total: Q{total:.2f}")

            historial.append(f"Propina {porcentaje}% → Total Q{total:.2f}")

        elif opcion == "2":
            total = leer_float("Total de la cuenta: Q")
            personas = int(leer_float("Número de personas: "))

            resultado = dividir_cuenta(total, personas)

            print(f"Resultado: {resultado}")
            historial.append(f"Dividir Q{total:.2f} entre {personas} → {resultado}")

        elif opcion == "3":
            subtotal = leer_float("Subtotal: Q")
            descuento = leer_float("Descuento (%): ")

            nuevo_subtotal = aplicar_descuento(subtotal, descuento)
            porcentaje = leer_float("Propina (%): ")

            propina = calcular_propina(nuevo_subtotal, porcentaje)
            total = calcular_total(nuevo_subtotal, propina)

            print(f"Subtotal con descuento: Q{nuevo_subtotal:.2f}")
            print(f"Total con propina: Q{total:.2f}")

            historial.append(f"Desc {descuento}% + prop {porcentaje}% → Q{total:.2f}")

        elif opcion == "4":
            print("Gracias por usar el sistema 🍽️")
            break

        elif opcion == "5":  # BONUS
            print("\n=== RESUMEN ===")
            if not historial:
                print("No hay operaciones aún.")
            else:
                for h in historial:
                    print("-", h)

        else:
            print("Opción inválida.")


# Ejecutar programa
main()
