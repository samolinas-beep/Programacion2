def cifrar_caracter(c, desplazamiento):
    if c.isalpha():  # solo letras
        base = ord('a') if c.islower() else ord('A')
        # Convertimos a posición 0–25, aplicamos desplazamiento y volvemos
        nueva_pos = (ord(c) - base + desplazamiento) % 26
        return chr(base + nueva_pos)
    else:
        return c  # no cambia si no es letra


def cifrar_mensaje(mensaje, desplazamiento):
    resultado = ""
    for c in mensaje:
        resultado += cifrar_caracter(c, desplazamiento)
    return resultado


def descifrar_mensaje(mensaje, desplazamiento):
    return cifrar_mensaje(mensaje, -desplazamiento)


# BONUS
def fuerza_bruta(mensaje_cifrado):
    print("=== Fuerza bruta ===")
    for d in range(26):
        intento = descifrar_mensaje(mensaje_cifrado, d)
        print(f"Desplazamiento {d}: {intento}")


# Ejemplos
print(cifrar_mensaje("hola", 3))         # krod
print(descifrar_mensaje("krod", 3))      # hola

# Bonus
fuerza_bruta("krod")
