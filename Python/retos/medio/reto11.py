#------------------------------------------------
# Reto 11  ****OBLIGATORIO****
# Una empresa quiere gestionar su cartera de clientes. Escribe un programa que guarde los clientes en un diccionario u objeto literal en el que disponga de:
# NIF (string), nombre (string), apellidos (string), teléfono (string), email (string) y preferente (boolean)
# El programa debe mostrar las siguientes opciones para que escoja el usuario:
# (1) Añadir un cliente
# (2) Eliminar cliente por NIF
# (3) Mostrar Cliente por NIF
# (4) Listar TODOS os clientes
# (5) Mostrar ÚNICAMENTE los clientes preferentes
# (6) Finalizar Programa
#------------------------------------------------


def addCustomer(listCustomers: list)->list:
    from re import search
    nif: str = input('(#1) Introduzca el NIF del nuevo cliente (6 volver al menú): ')
    
    if nif == '6': return
    
    while bool(search(r'^[0-9]{8}[A-Z]{1}',nif)) == False:
        
        print('(#1) NIF introducido incorrecto')
        nif: str = input('(#1) Introduzca el NIF del nuevo cliente (6 volver al menú): ')
        if nif == '6': return
    
    name: str = input('(#1) Introduzca el nombre del nuevo cliente (6 volver al menú): ')
    
    if name == '6': return
    
    while name == []:
        print('(#1) El campo nombre no puede estar vacío')
        name: str = input('(#1) Introduzca el nombre del nuevo cliente (6 volver al menú): ')
        if name == '6': return
        
    surname: str = input('(#1) Introduzca los apellidos del nuevo cliente (6 volver al menú): ')
    if surname == '6': return
    
    while surname == []:
        
        print('(#1) El campo apellidos no puede estar vacío')
        name: str = input('(#1) Introduzca los apellidos del nuevo cliente (6 volver al menú): ')
        if surname == '6': return
    
    phone: str = input('(#1) Introduzca el teléfono del nuevo cliente (Formato: ***-***-***) (6 volver al menú): ')
    if phone == '6': return
    while bool(search(r'^[0-9]{3}-[0-9]{3}-[0-9]{3}',phone)) == False:
        print('(#1) Formato de teléfono incorrecto')
        phone: str = input('(#1) Introduzca el teléfono del nuevo cliente (Formato: ***-***-***) (6 volver al menú): ')
        if phone == '6': return
        
    email: str = input('(#1) Introduzca el email del nuevo cliente (6 volver al menú): ')
    if email == '6': return
    
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    while bool(search(regex,email)) == False:
        
        print('(#1) Email introducido incorrecto')
        email: str = input('(#1) Introduzca el email del nuevo cliente (6 volver al menú): ')
        if email == '6': return
        
    vip = input('(#1) ¿Es un cliene preferente? (si/no)? (6 volver al menú) ')
    if vip == '6': return
    
    while True:
        if vip.lower() != 'si' and vip.lower() != 'no':
            print('(#1) Lo siento, tiene que responder si o no')
            vip = input('(#1) ¿Es un cliene preferente? (si/no)? (6 volver al menú) ')
            if vip == '6': return
            continue
        elif vip.lower() == 'si':
            vip = True
            break
        else:
            vip = False
            break
    
    listCustomers.append({'NIF': nif,'nombre': name, 'apellidos': surname, 'telefono': phone, 'email': email, 'preferente': vip})
    print(f'(#1) El cliente con NIF {listCustomers[-1]["NIF"]} ha sido añadido correctamente')
     
    
    
    
    
def removeCustomer(listCustomers: list) -> list:
    from re import search
    
    if listCustomers == []:
        return print('(#2) Lista de clientes vacía') 
        
        
    print(f'\n(#2) Los NIF de los clientes en la base de datos son:\n')
    
    for i in range(len(listCustomers)):
        print('Cliente {} -> NIF: {}\n'.format(i+1,listCustomers[i]['NIF']))       
      
   
 
    while True:
        nifRemove: str = input('(#2) Introduzca el NIF del cliente que desea eliminar (6 volver al menú): ')
        if nifRemove == '6': return
        
        while bool(search(r'^[0-9]{8}[A-Z]{1}',nifRemove)) == False:
            
            
            print('(#2) NIF introducido incorrecto')
            nifRemove: str = input('(#2) Introduzca el NIF del cliente que desea eliminar (6 volver al menú): ')
            if nifRemove == '6': return
            
        for i in range(len(listCustomers)):
            if nifRemove == listCustomers[i]['NIF']:
                print('El cliente con NIF {} ha sido eliminado correctamente'.format(listCustomers[i]['NIF']))
                return listCustomers.pop(i)
            
        print('(#2) NIF no encontrado, vuelva a intentarlo')





def showCustomerNIF(listCustomers: list):
    
    from re import search
    
    if listCustomers == []:
        return print('(#3) Lista de clientes vacía') 
        
        
    print(f'\n(#3) Los NIF de los clientes en la base de datos son:\n')
    
    for i in range(len(listCustomers)):
        print('Cliente {} -> NIF: {}\n'.format(i+1,listCustomers[i]['NIF']))       
      
   
   
    while True:
        
        nifShow: str = input('(#3) Introduzca el NIF del cliente del que desea ver todos sus datos (6 volver al menú): ')
        if nifShow == '6': return
        
        while bool(search(r'^[0-9]{8}[A-Z]{1}',nifShow)) == False:

            print('(#3) NIF introducido incorrecto')
            nifShow: str = input('(#3) Introduzca el NIF del cliente del que desea ver todos sus datos (6 volver al menú): ')
            if nifShow == '6': return
        
        for i in range(len(listCustomers)):
            if nifShow == listCustomers[i]['NIF']:
                
                return print('''(#3) El cliente con NIF {} tiene los siguientes datos:\n
    Nombre: {}
    Apellidos: {}
    Teléfono: {}
    Email: {}
    ¿Es preferente?: {}'''.format(listCustomers[i]['NIF'], listCustomers[i]['nombre'], listCustomers[i]['apellidos'], listCustomers[i]['telefono'], listCustomers[i]['email'], listCustomers[i]['preferente']))
                
            
        print('NIF no encontrado, vuelva a intentarlo')
 
        



def showAll(listCustomers: list):
    from time import sleep
    if listCustomers == []:
        return print('(#4) Lista de clientes vacía') 
        
    for i in range(len(listCustomers)):
        if i == 0:
            print(f'Hay un total de {len(listCustomers)} clientes. Imprimiendo datos a continuación...\n')
            sleep(1)
        print('''(#4) Cliente {}, con NIF {} tiene los siguientes datos:\n
        Nombre: {}
        Apellidos: {}
        Teléfono: {}
        Email: {}
        ¿Es preferente?: {}\n'''.format(i+1,listCustomers[i]['NIF'], listCustomers[i]['nombre'], listCustomers[i]['apellidos'], listCustomers[i]['telefono'], listCustomers[i]['email'], listCustomers[i]['preferente']))
        print('***********************\n')
        sleep(2)
        
        
        



def preferCustomer(listCustomers: list):
    from time import sleep

    if listCustomers == []:
        return print('(#5) Lista de clientes vacía') 
        
        
    chk = False #chk variable is necessary to print header text just for the first time
    
    for i in range(len(listCustomers)):
        if listCustomers[i]['preferente'] == True:
            if chk == False:
                print('***********************************')
                print('(#5) Los clientes preferentes son: ')
                print('***********************************')
                sleep(1)
                chk = True
            print('''(#5) Cliente {}, con NIF {} tiene los siguientes datos:\n
    Nombre: {}
    Apellidos: {}
    Teléfono: {}
    Email: {}
    ¿Es preferente?: {}\n'''.format(i+1,listCustomers[i]['NIF'], listCustomers[i]['nombre'], listCustomers[i]['apellidos'], listCustomers[i]['telefono'], listCustomers[i]['email'], listCustomers[i]['preferente']))
            print('***********************\n')
            sleep(2)
            
