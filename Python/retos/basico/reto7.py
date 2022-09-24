#------------------------------------------------
# Reto 7
# Escribe un programa que contenga dos variables. 
# Una de ellas representa la contraseña de un usuario y la otra un texto introducido.
# El programa debe poder mostrar por pantalla si las dos cadenas de texto son iguales sin tener en cuenta mayúsculas y minúsculas.
#------------------------------------------------


password:str = 'asbcs322#@'
texto:str  = 'asbcs322#@'

if password.lower() == texto.lower():
    print('Ambas string son iguales')
else:
    print('Las dos string son diferentes')
    
    
