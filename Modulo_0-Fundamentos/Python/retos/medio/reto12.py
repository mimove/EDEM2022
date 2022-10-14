#------------------------------------------------
# Reto 12
# Escribe un script de código que haga al usuario introducir 8 alturas de edificios (deben ser float) y que saque por consola las 3 más altas (haz uso de sorted).
#------------------------------------------------

heights: list = list()



for i in range(8):
    
    heights.append(float(input(f'Introduce {i+1} de 8 alturas de edificios: ')))
    

heights.sort(reverse=True)


print(f'Las tres alguras más altas son: {heights[:3]}')