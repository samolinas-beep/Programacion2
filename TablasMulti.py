def tabla(n, hasta=10):  # BONUS: parámetro opcional
    print(f"\nTabla del {n}")
    for i in range(1, hasta + 1):
        print(f"{n} x {i} = {n * i}")


def es_primo(n):
    if n < 2:
        return False

    # Solo probamos hasta la raíz cuadrada de n
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


def tablas_primos(limite):
    for n in range(2, limite + 1):
        if es_primo(n):
            tabla(n)  # reutiliza la función


# Ejemplo
tablas_primos(10)
