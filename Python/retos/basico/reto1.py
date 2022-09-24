#------------------------------------------------
# Reto 1
# Desde tu cuenta de replit.com crea un nuevo proyecto. En dicho proyecto, dentro del archivo main.py crea variables que representen los siguientes datos de un contacto:
# Nombre
# Apellidos
# Edad
# Email
# Teléfono
# Casado (verdadero o falso)
# Con Hijos (verdadero o falso)
# Lista de amigos
# Películas vistas (diccionario con clave y valor. El valor será el título de la película)
# Una vez hayas creado todas las variables, muéstralas por consola haciendo uso de la función print()
#------------------------------------------------


name:str = 'Manuel'
surname:str = 'Lopez'
age:int = 22
email:str = 'manuel.lopez@gmail.com'
phone:int = 666111222
married:bool = False
kids:bool = False
amigos:list = ['Juan', 'Pepe', 'Jose', 'Paco', 'Javi']
films:dict = {'film1':'El señor de los anillos', 'film2':'Harry Potter', 'film3':'Inside Out', 'film4':'Toy Story'}

print(f"""Los datos del contacto son
Nombre: {name}
Apellido: {surname}
Edad: {age}
Email: {email}
Tlf: {phone}
¿Casado?: {married}
¿Hijos?: {kids}
Lista amigos: {amigos}
Películas: {films}""")