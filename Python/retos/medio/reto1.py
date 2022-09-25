#-------------------------------------#
# Reto 1 ****OBLIGATORIO****
# Una tienda vende Discos de música (unos muñecos muy graciosos). Con la idea de vender un stock almacenado durante meses, 
# se decide que discos de género "Black Metal" y "Electro" tienen un descuento del 30%.
# Cada disco (usa un diccionario para esto) tendrá:
# Nombre
# Artista
# Año
# Precio
# Género (solo pueden ser de los siguientes)
# Pop
# Electro
# Reggaeton
# Rock
# Metal
# Death Metal
# Black Metal
# Escribe un programa que, disponiendo de una lista de discos disponibles en la tienda el usuario pueda elegir el disco a comprar.
# Al acabar la compra (pulsando la tecla 0) se deberá mostrar el ticket de compra indicando la fecha de compra (puedes coger la fecha actual a través de datetime), 
# el dinero que se ahorra el usuario y el coste final de la compra.
#-------------------------------------#


def buyMusic(discs: list):
    
    from datetime import datetime
    orderDiscs: list = list()
    orderTotal: float = 0.00
    savedMoney: float = 0.00
    discAdded: list = list()
    
    print('#######################################################')
    print('                  DISCOS DISPONIBLES                   ')
    for i in range(len(discs)):
        print(f'Disco {i+1}: {discs[i]}\n')
    
    print(f'*** Los discos de género Electro y Black Metal tienen un {30}% de descuento sobre el precio indicado ***')
    print('#######################################################\n')
    
    while True:
        discNum = int(input('Introduce el numero del disco que quieres comprar (0 para terminar compra): '))
        
        if discNum == 0:
            break
        
        if discNum in discAdded:
            print('Disco ya añadido al carrito, por favor selecciona otro disco')
            continue
        elif discNum > len(discs) or discNum < 0:
            print('Numero introducido erróneo')
            continue
        
            
        confirmed = input(f'Ha seleccionado el disco {discs[discNum-1]}, ¿es correcto? (si/no): ')
        
        while confirmed.lower() != 'si':
            if confirmed.lower() == 'no':
                break
            else:
                print('Lo siento no le entiendo, vuelva a intentarlo')
                confirmed = input(f'Ha seleccionado el disco {discs[discNum-1]}, ¿es correcto? (si/no): ')
                  
            
        discAdded.append(discNum) # Stored number of the disc added to check in next iteration if disc already added.
            
        discNum -= 1 # I have to substract 1 becuase the disc selected by the user is discNum-1 in the list discs due to the indexing of Python.
            
        orderDiscs.append(discs[discNum]) 
            
        if discs[discNum]['genero'] == 'Black Metal' or discs[discNum]['genero'] == 'Electro':
            orderTotal += 0.70*discs[discNum]['precio']
            savedMoney += 0.30*discs[discNum]['precio']
        else:
            orderTotal += discs[discNum]['precio']
    

            
    print('\n###############################################')
    print('Compra realizada el {}'.format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
    print(f'Total de la compra: {round(orderTotal,2)}€')
    print(f'Total dinero rebajado: {round(savedMoney,2)}€')
    
    print('Los discos comprados son:\n')
    for i in range(len(orderDiscs)):
        print(f'Disco {i+1}: {orderDiscs[i]}\n')
    print('###############################################')
        
        