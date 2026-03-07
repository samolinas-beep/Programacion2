# Mostrar todas las tablas de multiplicar del 1 al 12
# Usando bucles anidados

print("=" * 50)
print("TABLAS DE MULTIPLICAR DEL 1 AL 12")
print("=" * 50)

# Bucle externo: recorre las tablas del 1 al 12
for tabla in range(1, 13):
    print(f"\n--- Tabla del {tabla} ---")
    
    # Bucle interno: recorre los multiplicadores del 1 al 10
    for multiplicador in range(1, 11):
        resultado = tabla * multiplicador
        print(f"{tabla} x {multiplicador} = {resultado}")

print("\n" + "=" * 50)
print("¡Fin de las tablas de multiplicar!")
print("=" * 50)
