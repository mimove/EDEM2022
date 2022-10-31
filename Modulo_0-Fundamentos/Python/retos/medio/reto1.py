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


# Defining colors for print function 
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def buyMusic(discs: list, listType: str):
    
    import pandas as pd
    from datetime import datetime
    
    orderDiscs: list = list()
    orderTotal: float = 0.00
    savedMoney: float = 0.00
    listRemove: list = list()
    
    # Printing list of discs available.
    
    print('#######################################################')
    print('##                DISCOS DISPONIBLES                 ##')
    print('#######################################################\n')
    for i in range(len(discs)):
        
        # If 'genero' of disc is 'Electro or 'Black Metal' apply 30% discount
        
        if discs[i]['genero'] == 'Electro' or discs[i]['genero'] == 'Black Metal' :
            print('## Disco {} **DESCUENTO 30%** : Album: {} | Artista: {} | Año: {} | Precio: {}€ | **Precio con descuento**: {}€ | Género: {}\n'.format(i+1, discs[i]["album"], discs[i]["artista"], discs[i]["año"], strike(str(discs[i]["precio"])), round(discs[i]["precio"]*0.7,2), discs[i]["genero"]))
        
        else:
            print('## Disco {}: Album: {} | Artista: {} | Año: {} | Precio: {}€  | Género: {}\n'.format(i+1, discs[i]["album"], discs[i]["artista"], discs[i]["año"], discs[i]["precio"], discs[i]["genero"]))
    
    
    print('#######################################################\n')
    
    # Loop until the user selects a valid number from the list
    
    while True:
        try:
            discNum = int(input('Introduce el numero del disco que quieres comprar (0 para ir al checkout): '))
        except ValueError:
            print('Lo siento, no has introducido un número')
            continue
        
        
        if discNum == 0:
            break
        
        discNum -= 1 # I have to substract 1 becuase the disc selected by the user is discNum-1 in the list discs due to the indexing of Python.
        
        # Condition to check if disc already added to the cart or if the number chose is within the list
        
        
        if discNum >= len(discs) or discNum < 0:
            print(bcolors.FAIL+'\nNumero introducido erróneo\n'+bcolors.ENDC)
            continue
        
        elif discs[discNum]['stock'] == 0:
            print('\n**Disco '+bcolors.FAIL+'OUT OF STOCK' + bcolors.ENDC+', por favor selecciona otro disco**\n')
            continue
        
        
        # Disc added to the cart
        orderDiscs.append(discs[discNum]) 
        print(bcolors.OKGREEN + '\nDisco añadido correctamente\n' + bcolors.ENDC)
        discs[discNum]['stock'] -= 1
    
    
    
    if orderDiscs == []:
        print(bcolors.WARNING + '###############################################')
        print('##  Carrito vacío. Vuelva a iniciar compra   ##')
        print('###############################################' + bcolors.ENDC)
        quit()
    
    # Print the list of disc in the shopping cart
    print('\n###############################################')            
    print('\nLos discos en el carrito son: \n')
    print('###############################################\n')
    for i in range(len(orderDiscs)):
            
        if orderDiscs[i]['genero'] == 'Electro' or orderDiscs[i]['genero'] == 'Black Metal' :
            print('## Artículo {} con **DESCUENTO 30%** : Album: {} | Artista: {} | Año: {} | Precio: {}€ | **Precio con descuento**: {}€ | Género: {}\n'.format(i+1, orderDiscs[i]["album"], orderDiscs[i]["artista"], orderDiscs[i]["año"], strike(str(orderDiscs[i]["precio"])), round(orderDiscs[i]["precio"]*0.7,2), orderDiscs[i]["genero"]))
            
        else:
            print('## Artículo {}: Album: {} | Artista: {} | Año: {} | Precio: {}€  | Género: {}\n'.format(i+1, orderDiscs[i]["album"], orderDiscs[i]["artista"], orderDiscs[i]["año"], orderDiscs[i]["precio"], orderDiscs[i]["genero"])) 
   
    
    
    # Condition at the checkout to let the user decide if they want to purchase all the discs in the cart
    
    while True:
        try:
            confirmed = int(input('Si quieres quitar algún disco del carrito indica el nº del artículo. (0 para finalizar compra): '))
            
            if confirmed == 0:
                break
            elif confirmed > len(orderDiscs) or confirmed < 0:
                print(bcolors.FAIL + '\nLo siento, el número seleccionado no está en la lista\n' + bcolors.ENDC)
                continue
                
            elif confirmed-1 in listRemove:
                print(bcolors.WARNING + '\n**Disco ya eliminado**\n' + bcolors.ENDC)
                continue
            
            else:
                listRemove.append(confirmed-1)
                if len(listRemove) == len(orderDiscs):
                    print(bcolors.WARNING + '###############################################')
                    print('##  Carrito vacío. Vuelva a iniciar compra   ##')
                    print('###############################################' + bcolors.ENDC)
                    quit()
                print('\nDisco eliminado correctamente\n')
                
                # Next two lines return the stock of the disc remove to +1
                index = next((i for i, item in enumerate(discs) if item["album"] == orderDiscs[listRemove[-1]]["album"]), None)
                discs[index]['stock'] += 1

                        
        except ValueError:
            print(bcolors.FAIL + 'Lo siento, no has introducido un número' + bcolors.ENDC)
            continue
    
                
    
    deleteMultipleElements(orderDiscs, listRemove)
    

    # Loop to calculate the final price that the customer has to pay. If 'genero' of the disc is 'Black Metal' or 'Electro' apply 30% discount and calculate the money saved.
    for i in range(len(orderDiscs)):
        if orderDiscs[i]['genero'] == 'Black Metal' or orderDiscs[i]['genero'] == 'Electro':
            orderTotal += round(0.70*orderDiscs[i]['precio'],2)
            savedMoney += round(0.30*orderDiscs[i]['precio'],2)
        else:
            orderTotal += orderDiscs[i]['precio']
    
    
    # If there are no discs in the shopping cart print a message of empty cart.
    
    
    print('\n###############################################')
    print('Compra realizada el {} a las {}'.format(datetime.now().strftime("%d/%m/%Y"),datetime.now().strftime("%H:%M:%S")))
    print(f'Total de la compra: {round(orderTotal,2)}€')
    print(f'Total dinero rebajado: {round(savedMoney,2)}€')
        
    print('Los discos comprados son:\n')
        
    for i in range(len(orderDiscs)):
            
        if orderDiscs[i]['genero'] == 'Electro' or orderDiscs[i]['genero'] == 'Black Metal' :
            print('## Artículo {} comprado con **DESCUENTO 30%** : Album: {} | Artista: {} | Año: {} | Precio: {}€ | **Precio con descuento**: {}€ | Género: {}\n'.format(i+1, orderDiscs[i]["album"], orderDiscs[i]["artista"], orderDiscs[i]["año"], strike(str(orderDiscs[i]["precio"])), round(orderDiscs[i]["precio"]*0.7,2), orderDiscs[i]["genero"]))
        
        else:
            print('## Artículo {}: Album: {} | Artista: {} | Año: {} | Precio: {}€  | Género: {}\n'.format(i+1, orderDiscs[i]["album"], orderDiscs[i]["artista"], orderDiscs[i]["año"], orderDiscs[i]["precio"], orderDiscs[i]["genero"]))
        
    print('###############################################')
    print('######      GRACIAS POR SU COMPRA      ########')    
    print('###############################################')

    # Updating csv file with new stock of discs.
    updateStock = pd.json_normalize(discs)
    updateStock.to_csv('discos_' + listType + '.csv',index=False)  

# Function to cross original price when a disc has a discount (obtained from Stack Overflow)
def strike(text):
    return ''.join([u'\u0336{}'.format(c) for c in text])


# Function to remove multiple elements from a list and avoid the error from trying to remove index positions that are not in the list after removing some elements
def deleteMultipleElements(listOrg, listIndices):
    listIndices = sorted(listIndices, reverse=True) # Sort the list of indeces to remove in reversed order to avoid conflict after removing some elements from the original list
    for idx in listIndices:
        if idx < len(listOrg): # Condition to avoid exemption if index position not in listOrg
            listOrg.pop(idx)