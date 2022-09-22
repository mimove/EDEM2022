
#------------------------------------------------

# EJERCICIO PARA JUEVES:

# Hacer aplicación de consola que vaya pidiendo datos: Nombre, email, contraseña, edad y aceptar. Crear un diccionario del usuario con estos datos

#------------------------------------------------


################################################
#  función para comprobar si contraseña valida #
################################################

def is_valid(password):
    import string
    alpha = set(string.ascii_lowercase + string.ascii_uppercase)
    digits = set(string.digits)
    non_alpha = set('#@%.?!')
    password_chars = set(password)

    # We substract the set of letters (resp. digits, non_alpha)
    # from the set of chars used in password
    # If any of the letters is used in password, this should be
    # smaller than the original set 
    all_classes_used = all([len(password_chars - char_class) != len(password_chars) 
                            for char_class in [alpha, digits, non_alpha] ])

    # We remove all letters, digits and non_alpha from the
    # set of chars composing the password, nothing should be left.
    all_chars_valid = len(password_chars - alpha - digits - non_alpha) == 0

    return all_classes_used and all_chars_valid

################################################

while True:

    name = input('Dime tu nombre: ')

    email = input('Introduce email: ')

    while '@' not in email or '.' not in email:
        print('Email introducido incorrecto: ')
        email = input('Introduce email: ')
        
    from getpass import getpass

    password = getpass(prompt='Introduce contraseña: ')
    
    

    while len(password) < 8 or is_valid(password) == False:
        print('La contraseña tiene que tener al menos 8 caracteres, 1 minúscula, 1 mayúscula, 1 número y un caracter especial')
        password = getpass(prompt='Introduce contraseña: ')
    
    passhow = ''
    for i in range(len(password)):
        if i > 1 and i < len(password) - 2:
            passhow += '*' 
        else:
            passhow += password[i]

    age = 0

    while True: 
        try:
            age = int(input('Introduce tu edad: '))
        except:
            print('Introduce un número')
            continue
        else:
            if age > 5 and age < 100:
                break
            else:
                print('Edad introducida fuera de rango (5 a 100 años)')
            
    
    check = input('¿Estás seguro que los datos son correctos? (Si/No): ')
   
    
    while check.lower() != 'si' and check.lower() != 'no':
        print('Responde con Si o No')
        check = input('¿Estás seguro de que los datos son correctos? (Si/No): ')
        
    if check.lower() == 'si':
        break 
    elif check.lower() == 'no':
        continue
          



datos = {'nombre':name.capitalize(), 'email':email, 'contraseña': passhow, 'edad':age}
        
        

print(f'''Los datos introducidos son:
      Nombre: {datos["nombre"]}
      Email: {datos["email"]}
      Contraseña: {datos["contraseña"]}
      Edad: {datos["edad"]}''')




    