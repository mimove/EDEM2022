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




class Clients:
    
    # Class atributes
    nif:str = ''
    name:str = ''
    surname:str = ''
    phone:str = ''
    email:str = ''
    vip:bool = False
    
    # Contstructor method
    def __init__(self, nif, name, surname, phone, email, vip):
        self.nif = nif
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.vip = vip
        
        
    
    
    # Methods
    
    def addCustomer(listCustomers: list):
        from re import search
        nif: str = input('(#1) Introduzca el NIF del nuevo cliente (6 volver al menú): ')
        
        if nif == '6': return # All the lines that include this condition allow to go back to main menu in case the user wants to do so. It avoids getting stuck
        
        
        # Checking if NIF contains 8 numbers and 1 letter. It could be improved by adding the equation to obtain the letter from the numbers of your DNI.
        
        while bool(search(r'^[0-9]{8}[A-Z]{1}',nif)) == False:
            
            print(bcolors.FAIL + '(#1) NIF introducido incorrecto' + bcolors.ENDC)
            nif: str = input('(#1) Introduzca el NIF del nuevo cliente (6 volver al menú): ')
            if nif == '6': return
        
        name: str = input('(#1) Introduzca el nombre del nuevo cliente (6 volver al menú): ')
        
        if name == '6': return
        
        # If the name or surname variable are empty don't allow the user to continue any further.
        
        while name == []:
            print(bcolors.FAIL + '(#1) El campo nombre no puede estar vacío' + bcolors.ENDC)
            name: str = input('(#1) Introduzca el nombre del nuevo cliente (6 volver al menú): ')
            if name == '6': return
            
        surname: str = input('(#1) Introduzca los apellidos del nuevo cliente (6 volver al menú): ')
        if surname == '6': return
        
        while surname == []:
            
            print(bcolors + '(#1) El campo apellidos no puede estar vacío' + bcolors.ENDC)
            surname: str = input('(#1) Introduzca los apellidos del nuevo cliente (6 volver al menú): ')
            if surname == '6': return
        
        phone: str = input('(#1) Introduzca el teléfono del nuevo cliente (Formato con guión cada 3 números: 000-000-000) (6 volver al menú): ')
        
        # Phone format has to be introduce as ***-***-***. This ensures consistency in the database that could be created out of this program.
        
        if phone == '6': return
        while bool(search(r'^[0-9]{3}-[0-9]{3}-[0-9]{3}',phone)) == False:
            print(bcolors.FAIL + '(#1) Formato de teléfono incorrecto' + bcolors.ENDC)
            phone: str = input('(#1) Introduzca el teléfono del nuevo cliente (Formato con guión cada 3 números: 000-000-000) (6 volver al menú): ')
            if phone == '6': return
            
        email: str = input('(#1) Introduzca el email del nuevo cliente (6 volver al menú): ')
        if email == '6': return
        
        # Regex expression to check if an email is correct. Obtained from Stackoverflow
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        
        while bool(search(regex,email)) == False:
            
            print(bcolors.FAIL + '(#1) Email introducido incorrecto' + bcolors.ENDC)
            email: str = input('(#1) Introduzca el email del nuevo cliente (6 volver al menú): ')
            if email == '6': return
            
        vip = input('(#1) ¿Es un cliene preferente? (si/no)? (6 volver al menú) ')
        if vip == '6': return
        
        # Only allow si or no answer from the user
        
        while True:
            if vip.lower() != 'si' and vip.lower() != 'no':
                print(bcolors.FAIL + '(#1) Lo siento, tiene que responder si o no'+ bcolors.ENDC)
                vip = input('(#1) ¿Es un cliene preferente? (si/no)? (6 volver al menú) ')
                if vip == '6': return
                continue
            elif vip.lower() == 'si':
                vip = True
                break
            else:
                vip = False
                break
        
        #Appending new customer to the existing list of dictionaries. It can't be included as a return because I've put a print command to tell the user that the new data was added correctly.
        
        customerNew = Clients(nif, name, surname, phone, email, vip)
        
        
        listCustomers.append(vars(customerNew))
        
        print(f'{bcolors.OKGREEN}(#1) El cliente con NIF {listCustomers[-1]["nif"]} ha sido añadido correctamente{bcolors.ENDC}')
        
        
        
        
    def removeCustomer(listCustomers: list):
        from re import search
        
        # If there are no customers, you can't delete/show anything.
        
        if listCustomers == []:
            return print(bcolors.WARNING + '(#2) Lista de clientes vacía' + bcolors.ENDC) 
            
            
        print(f'\n(#2) Los NIF de los clientes en la base de datos son:\n')
        
        # Show all the NIF available in the database.
        
        NIF: str = list(listCustomers[0].keys())[0] #Get the string value of the NIF from the list of Customers
        
        for i in range(len(listCustomers)):
            print('Cliente {} -> NIF: {}\n'.format(i+1,listCustomers[i][NIF]))       
        
    
        # This loop ensures that until a valid NIF that correspond to someone on the database is added, the user have to keep introducing NIF or press 6 to exit to main menu.
        # A similar loop is introduced in other functions below.
        
        while True:
            nifRemove: str = input('(#2) Introduzca el NIF del cliente que desea eliminar (6 volver al menú): ')
            if nifRemove == '6': return
            
            while bool(search(r'^[0-9]{8}[A-Z]{1}',nifRemove)) == False:
                
                
                print(bcolors.FAIL + '(#2) NIF introducido incorrecto' + bcolors.ENDC)
                nifRemove: str = input('(#2) Introduzca el NIF del cliente que desea eliminar (6 volver al menú): ')
                if nifRemove == '6': return
            
            # If the NIF of the customer introduced is found, remove the customer and exit to main menu.
                
            for i in range(len(listCustomers)):
                if nifRemove == listCustomers[i][NIF]:
                    print('{}El cliente con NIF {} ha sido eliminado correctamente{}'.format(bcolors.OKGREEN, listCustomers[i][NIF], bcolors.ENDC))
                    return listCustomers.pop(i)
                
            print(bcolors.FAIL + '(#2) NIF no encontrado, vuelva a intentarlo' + bcolors.ENDC)