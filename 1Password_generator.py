import random

letras = "lkjkjgsndvhabcjegdvakjudfygehdjiaueghdbjakshudghbendhchgjvhb gbdu "
numeros = "0123456789"

contrasena = []

while len(contrasena) < 8:
    s = random.choice(letras + numeros)
    contrasena.append(s)

print("".join(contrasena))

## RETO
## 1. Cambiar. La contraseña debe ser de 12 caracteres de longitud
## 2. La contraseña debe tener letras en mayusculas con .upper
## 3. Debe contener 1 sólo caracter especial ! @ # %
