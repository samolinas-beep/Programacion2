def tiene_mayuscula(texto):
    for c in texto:
        if c.isupper():
            return True
    return False

def tiene_digito(texto):
    for c in texto:
        if c.isdigit():
            return True
    return False

def tiene_especial(texto):
    especiales = "!@#$%"
    for c in texto:
        if c in especiales:
            return True
    return False

def longitud_valida(texto):
    return len(texto) >= 8

# BONUS
def no_tres_iguales_seguidos(texto):
    for i in range(len(texto) - 2):
        if texto[i] == texto[i+1] == texto[i+2]:
            return False
    return True


def validar_password(password):
    return (
        longitud_valida(password) and
        tiene_mayuscula(password) and
        tiene_digito(password) and
        tiene_especial(password) and
        no_tres_iguales_seguidos(password)  # bonus incluido
    )


def diagnosticar_password(password):
    errores = []

    if not longitud_valida(password):
        errores.append("Debe tener al menos 8 caracteres")
    if not tiene_mayuscula(password):
        errores.append("Debe tener al menos una letra mayúscula")
    if not tiene_digito(password):
        errores.append("Debe tener al menos un dígito")
    if not tiene_especial(password):
        errores.append("Debe tener al menos un carácter especial (!, @, #, $, %)")
    if not no_tres_iguales_seguidos(password):
        errores.append("No debe contener 3 caracteres iguales seguidos")

    if len(errores) == 0:
        print("Password válida ✅")
        return True
    else:
        print("Password inválida ❌. Problemas:")
        for e in errores:
            print("-", e)
        return False
    