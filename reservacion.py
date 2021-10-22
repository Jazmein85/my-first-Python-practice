

nombre1 = "Habitacion"
nombre2 = "Spa"
nombre3 = "Senderismo"
nombre4 = "Vuelo"
nombre5 = "Cena VIP"

precio1 = 10
precio2 = 20
precio3 = 30
precio4 = 40
precio5 = 50
total = precio1 + precio2 + precio3 + precio4 +precio5


print("-"*40)
print(f'{"Recibo de venta":^40}')
print("-"*40)
print(f"{nombre1:30}|{precio1:9}")
print(f"{nombre2:30}|{precio2:9}")
print(f"{nombre3:30}|{precio3:9}")
print(f"{nombre4:30}|{precio4:9}")
print(f"{nombre5:30}|{precio5:9}")
print("-"*40)
print(f"{'total':^30}|{total:9}")
