edad = input ('Cual es tu edad? ')
edad = int(edad)

if edad < 1 or edad > 121:
    print('ERROR: Edad invalida')
    quit()

credencial = input('¿Tienes credencial? (s/n)')

if edad >=18 and credencial == 's':
    print('Puedes votar!')

elif edad == 17 and credencial == 'n':
    print('Tramita tu credencial para votar')
else:
    print('No puedes votar')
print('adios.')