contador = 0
i = 1 
while i <= 10:
    if i % 2 == 0:
        contador += 1 
        print (f"contador: {contador}")
    else:
        print (f"impar {i}")
    i += 1
print (f"Pares: {contador}")
# Resultado: Pares: 5
