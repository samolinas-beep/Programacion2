import random

def main():
    numero_secreto = random.randint(1, 100)
    intentos_max = 7
    intentos = 0

    print("Adivina un número entre 1 y 100. Tienes 7 intentos.")

    while intentos < intentos_max:
        try:
            entrada = input(f"Intento {intentos+1}/{intentos_max}: ")
            intento = int(entrada)
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")
            continue

        if intento < 1 or intento > 100:
            print("Número fuera de rango (1-100). Intenta de nuevo.")
            continue

        intentos += 1

        if intento < numero_secreto:
            print("Más alto.")
        elif intento > numero_secreto:
            print("Más bajo.")
        else:
            print(f"¡Correcto! Adivinaste en {intentos} intentos.")
            break
    else:
        print(f"Se agotaron los intentos. El número era {numero_secreto}.")


if __name__ == '__main__':
    main()