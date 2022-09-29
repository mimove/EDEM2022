#-------------------------------------#
# Reto 2
# El programa debe preguntar el artículo y su precio y añadirlo a una variable (diccionario u objeto literal), hasta que el usuario decida terminar
# ("Introducir otro elemento al carrito (Si / No)".
# Una vez el usuario decida no introducir más elementos al carrito, debe mostrar por pantalla la lista de la compra y el coste total.
#-------------------------------------#


def reto2():
    from re import match
    
    dictGroceries: dict = {'producto': [], 'precio':[]}
    
    while True:
        

        item = input('¿Qué artículo quieres añadir? ')
        
       
        
        if bool(match('[a-zA-Z]', item)) == False:
            print('El nombre del artículo es incorrecto')
            continue
        
        elif item in dictGroceries['producto']:
            print('Artículo ya añadido. Prueba con otro')
            continue
        
        
        while True:
            try:
            
                price = float(input('¿Qué precio tiene? '))
                
                if price == 0:
                    print('El artículo no puede tener un precio de 0€')
                    continue
                
                break
            
            except ValueError:
                print('Precio incorrecto, tienes que introducir el precio de nuevo')
                continue
        
        
        
        dictGroceries['producto'].append(item)
        dictGroceries['precio'].append(price)
        
        
        
        while True:
            finish = input('¿Quieres terminar? (si/no) ')
            
            if finish.lower() == 'si' or finish.lower() == 'no':
                
                break
        
            print('No te entiendo, vuelve a intentarlo.')
        
        
        if finish == 'si':
            break
 
            

            
    
    
    
    
    print('\nLos productos en la lista de la compra son:\n')
    
    for i in range(len(dictGroceries['producto'])):
        print('Artículo: {}. Precio: {}€\n'.format(dictGroceries["producto"][i].capitalize(), dictGroceries["precio"][i] ))
              
              
   
        