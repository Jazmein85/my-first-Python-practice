import random

letras = "laaakjkjgsndvhabcjegdvakjudfymnbvhgtgehdjiaueghpppdbjakshuuuuuryryryryklklkaaudghbwwendhchgjvhbmmmgbdu "
letras = letras.upper() + letras.lower()
numeros = "0123456789"
caracteres = "!$%&/()"


contrasena = []


while len(contrasena) < 11:
    s = random.choice (letras + numeros)
    contrasena.append(s)
j = random.choice (caracteres)
contrasena.append(j)

random.shuffle(contrasena)
print("".join(contrasena))

## RETO
## 1. Cambiar. La contraseña debe ser de 12 caracteres de longitud
## 2. La contraseña debe tener letras en mayusculas con .upper
## 3. Debe contener 1 sólo caracter especial ! @ # %
