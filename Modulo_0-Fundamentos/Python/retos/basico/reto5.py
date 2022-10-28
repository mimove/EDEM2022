#------------------------------------------------
# Reto 5
# Escribe un programa que sea capaz de pedirle a un usuario por consola** que introduzca una contraseña y mientras que ésta no sea "admin", 
# el programa seguirá pidiéndola. Si la contraseña es errónea, deberá sacarle un mensaje de error y volver a pedirle la contraseña hasta 
# que la introduzca bien. Si el usuario introduce "admin" correctamente, el programa le deberá mostrar un mensaje "Bienvenido al programa señor ADMIN"
# y luego terminar.
#
# NOTA: Para pedir por pantalla y guardarlo en una variable llamada password debes hacer uso de password:str = input('Introduce una contraseña')
#------------------------------------------------

def correctPass():
    while True:
        password: str = input('Introduce contraseña: ')
        
        if password == 'admin':
            break
        else:
            print('Contraseña incorrecta. Vuelva a intentarlo') 

    print('Bienvenido al programa señor admin')