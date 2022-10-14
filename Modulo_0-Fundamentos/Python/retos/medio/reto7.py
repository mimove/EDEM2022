#------------------------------------------------
# Reto 7
# Escribe un programa que pida 5 precios al usuario y los almacene en una lista de precios. Al finalizar, deberá mostrar por consola la media de los precios introducidos.
#------------------------------------------------

def averagePrices():
    
    listPrices:list = list()
        
    [listPrices.append(str(input('Introduce precio {} de 5: '.format(i+1)))+'€') for i in range(5)]
    
    averagePrice = sum(list(map(float, map(lambda x: x[:-1],listPrices)))) / len(listPrices) # list(map(float,list)) converts all the list of strings in list of floats. map(lambda x: x[:-1], list) creates a list of the prices introduced without the € symbol.
    
    return listPrices, averagePrice
    
    