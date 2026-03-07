# Crear un diamante completo con asteriscos

# Solicitamos el tamaño del diamante
n = int(input("Ingresa el tamaño del diamante (número impar, ej: 5, 7, 9): "))

# Aseguramos que es un número impar
if n % 2 == 0:
    n = n + 1

mitad = n // 2

print()
print("=" * 40)
print("DIAMANTE CON ASTERISCOS")
print("=" * 40)
print()

# Mitad superior del diamante (incluyendo la línea del medio)
for i in range(mitad + 1):
    espacios = " " * (mitad - i)
    asteriscos = "*" * (2 * i + 1)
    print(espacios + asteriscos)

# Mitad inferior del diamante
for i in range(mitad - 1, -1, -1):
    espacios = " " * (mitad - i)
    asteriscos = "*" * (2 * i + 1)
    print(espacios + asteriscos)

print()
print("=" * 40)
