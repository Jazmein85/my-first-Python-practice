#oreo = "19"
#oreo = int(oreo)
#fresa = "22"
#fresa = int(fresa)
#mm = "25"
#mm = int(mm)
#brownie = "28"
#brownie = int(brownie)



print("-"*70)
print(f'{"HELADERÍA ROMA. ¡Bienvenidos!":^70}')
print("-"*70)
precio_helado = input ('¡Hola!¿Qué sabor con tu helado quieres? (oreo/fresa/m&m/brownie):')
precio_helado = precio_helado.lower()

if precio_helado == 'oreo':
    print ('El costo es $19')

elif precio_helado == 'fresa':
    print ('El costo es $22')

elif precio_helado == 'm&m':
    print ('El costo es $25')

elif precio_helado == 'brownie':
    print ('El costo es $28')

else:
    print('Por el momento sólo tenemos sabor oreo, m&m, brownie y fresa. ¿Qué sabor te damos?')