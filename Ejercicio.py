import math

def area_circulo(radio):
    """
    Calcula el área de un círculo.
    
    Args:
        radio (float): El radio del círculo.
    Returns:
        float: El área calculada usando π * r².
    """
    return math.pi * (radio ** 2)

def es_primo(n):
    """
    Determina si un número es primo.
    
    Args:
        n (int): El número a evaluar.
    Returns:
        bool: True si es primo, False en caso contrario.
    """
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    """
    Calcula el factorial de un número n.
    
    Args:
        n (int): El número entero no negativo.
    Returns:
        int: El resultado de n!.
    """
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def fibonacci(n):
    """
    Retorna los primeros n números de la serie de Fibonacci.
    
    Args:
        n (int): La cantidad de números a generar.
    Returns:
        list: Una lista con los n números de Fibonacci.
    """
    secuencia = []
    a, b = 0, 1
    for _ in range(n):
        secuencia.append(a)
        a, b = b, a + b
    return secuencia

def celsius_a_fahrenheit(c):
    """
    Convierte una temperatura de Celsius a Fahrenheit.
    
    Args:
        c (float): Temperatura en grados Celsius.
    Returns:
        float: Temperatura equivalente en Fahrenheit.
    """
    return (c * 9/5) + 32

def maximo(lista):
    """
    Encuentra el valor máximo en una lista sin usar la función max().
    
    Args:
        lista (list): Una lista de números.
    Returns:
        float/int: El valor más alto de la lista.
    """
    if not lista:
        return None
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor