def celsius_a_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def celsius_a_kelvin(c):
    return c + 273.15

def kelvin_a_celsius(k):
    return k - 273.15

# Bonus: Escala Rankine
def celsius_a_rankine(c):
    # R = F + 459.67. Primero pasamos C a F.
    return celsius_a_fahrenheit(c) + 459.67

def rankine_a_celsius(r):
    # F = R - 459.67. Luego pasamos F a C.
    f = r - 459.67
    return fahrenheit_a_celsius(f)

def convertir(valor, origen, destino):
    origen = origen.upper()
    destino = destino.upper()

    if origen == destino:
        return valor

    # 1. Convertir cualquier origen a Celsius primero (Punto de anclaje)
    temp_c = None
    if origen == 'C':
        temp_c = valor
    elif origen == 'F':
        temp_c = fahrenheit_a_celsius(valor)
    elif origen == 'K':
        temp_c = kelvin_a_celsius(valor)
    elif origen == 'R':
        temp_c = rankine_a_celsius(valor)
    
    if temp_c is None:
        return None

    # 2. Convertir de Celsius al destino final
    if destino == 'C':
        return temp_c
    elif destino == 'F':
        return celsius_a_fahrenheit(temp_c)
    elif destino == 'K':
        return celsius_a_kelvin(temp_c)
    elif destino == 'R':
        return celsius_a_rankine(temp_c)
    
    return None

# --- Pruebas de funcionamiento ---
print(f"32°F a Celsius: {convertir(32, 'F', 'C')}°C")
print(f"100°C a Kelvin: {convertir(100, 'C', 'K')}K")
print(f"0°F a Kelvin: {convertir(0, 'F', 'K'):.2f}K") # F -> C -> K
print(f"20°C a Rankine: {convertir(20, 'C', 'R'):.2f}R")
