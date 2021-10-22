n = input('¿Tamaño de la lista que deseas? escríbelo aquí:')
n = int(n)

m = input('¿Valor en la lista que deseas? escríbelo aquí:')
m = float(m)

if n >=500_000:
    print('Por favor sólo escribe hasta 50,000 valores numéricos. Intenta nuevamente:')
    quit()

lista = [m] * n
print(lista)
