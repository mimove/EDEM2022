# Uso the APIs


""" from HTTP_Requests.chuck_norris_dice import obtenerChiste

chiste = obtenerChiste()


print('****chistecito****')
print(chiste)
print('****chistecito****') """





# PROGRAMACION ORIENTADA A OBJETOS



""" from models.Coche import Coche


coche1: Coche = Coche(marca='Audi', 
                      modelo='A3', 
                      matricula='1234BBB', 
                      color='BLANCO', 
                      titular='Martín')


coche2: Coche = Coche(marca='BMW', 
                      modelo='i5', 
                      matricula='4567LMG', 
                      color='NEGRO', 
                      titular='Lara')


print(f'La matricula es {coche1.matricula}')


print(f'La velocidad del coche actual es: {coche1.velocidad} km/h') # 0
print(f'La velocidad del coche actual es: {coche2.velocidad} km/h') # 0



coche1.arrancar()
print(f'La velocidad del coche actual es: {coche1.velocidad} km/h') # 10

print(f'La velocidad del coche actual es: {coche2.velocidad} km/h') # 0

coche1.acelerar(10)
print(f'La velocidad del coche actual es: {coche1.velocidad} km/h')

miTaller = [coche1, coche2]





print('Coches en mi taller')

for coche in miTaller:
    print(f'- {coche.matricula}')
    
    
    
def velocidadDeUnCoche(miTaller, matricula:str):
    for coche in miTaller:
        if coche.matricula == matricula:
            print(f'La velocidad del coche con matrícula {coche.matricula} es {coche.velocidad} km/h')
            
            
velocidadDeUnCoche(miTaller, '4567LMG')


carrera = [coche1, coche2]

def buscarCoche(carrera, matricula: str) -> Coche:
    for coche in carrera:
        if(coche.matricula == matricula):
            return coche
        


cocheEncontrado = buscarCoche(carrera, '4567LMG')

print(f'El coche {cocheEncontrado.matricula} va a una velocidad de {cocheEncontrado.velocidad} km/h') """



# LIBRERÍA PANDAS

import pandas as pd
import chunk
import re

# Leer CSV

pokemon_csv_df = pd.read_csv('G:\Mi unidad\Personal\MASTER DATA\GitHub\EDEM2022\Python\ClasesPython\Clase_30-09\pokemon_data.csv', #_df hace referencia a data frame
                         dtype={"Name": str, # El dtype es opcional
                                "Type 1":str, 
                                "Type 2": str,
                                "Speed": int,
                                "Generation": int
                                }) 


# Leer de un Excel

pokemon_excel_df = pd.read_excel('G:\Mi unidad\Personal\MASTER DATA\GitHub\EDEM2022\Python\ClasesPython\Clase_30-09\pokemon_data.xlsx')


# Leer de un TXT

pokemon_txt_df = pd.read_csv('G:\Mi unidad\Personal\MASTER DATA\GitHub\EDEM2022\Python\ClasesPython\Clase_30-09\pokemon_data.txt',delimiter='\t')



# Imprimir los valores

""" print(pokemon_csv_df) """

# Imprimir los 5 primeros

""" print(pokemon_csv_df.head(5)) """


# Imprimir los 5 ultimos

""" print(pokemon_csv_df.tail(5)) """


# Obtener nombres de columnas

""" print(pokemon_csv_df.columns) """

# Obtener nombres de los pokemon

""" nombres = pokemon_csv_df['Name']

print(*nombres) """

# Obtener todos los nombres y sus velocidades

# Opción 1

nombres_velocidades = pokemon_csv_df[['Name','Speed']] # Genera un df a partir de la lista con solo 2 columnas con 'Name' y 'Speed'

print(nombres_velocidades)


# Opción 2 **Opción recomendada


""" lista_columnas = ['Name', 'Speed']

nombres_velocidades = pokemon_csv_df[lista_columnas] # Genera un df a partir de la lista con solo 2 columnas con 'Name' y 'Speed'

print(nombres_velocidades) """


# Obtener los primeros 5 nombres 

""" primeros_5 = pokemon_csv_df['Name'][:5]

print(primeros_5) """


# Obtener primera fila

""" print(pokemon_csv_df.iloc[0]) """


# Obtener las 3 primeras filas

""" print(pokemon_csv_df.iloc[:3]) """


# LIBRERÍA CSV

""" import csv

#list with 21 discs

longListDiscs: list = [{'album':'AMERICAN IDIOT' , 'artista':'GREEN DAY' , 'año': 2004, 'precio': 51.64, 'genero': 'Pop'}, 
                   {'album':'BACK TO BLACK' , 'artista':'AMY WINEHOUSE' , 'año': 2006, 'precio': 23.99, 'genero': 'Pop'},
                   {'album':'IS THIS IT' , 'artista':'THE STROKES' , 'año': 2001, 'precio': 17.88, 'genero': 'Pop'},
                   {'album':'KID A' , 'artista':'RADIOHEAD' , 'año': 2000, 'precio': 31.37, 'genero': 'Electro'},
                   {'album':'RANDOM ACCESS MEMORIES' , 'artista':'DAFT PUNK' , 'año': 2013, 'precio': 11.99, 'genero': 'Electro'},
                   {'album':'DUMMY' , 'artista':'PORTISHEAD' , 'año': 1994, 'precio': 23.99, 'genero': 'Electro'},
                   {'album':'TALENTO DE BARRIO' , 'artista':'DADDY YANKEE' , 'año': 2008, 'precio': 11.99, 'genero': 'Reggaeton'},
                   {'album':'THE LAST DON' , 'artista':'DON OMAR' , 'año': 2003, 'precio': 30.14, 'genero': 'Reggaeton'},
                   {'album':'YHLQMDLG' , 'artista':'BAD BUNNY' , 'año': 2020, 'precio': 21.86, 'genero': 'Reggaeton'},
                   {'album':'UNTITLED (IV)' , 'artista':'LED ZEPPELIN' , 'año': 1971, 'precio': 14.99, 'genero': 'Rock'},
                   {'album':'APPETITE FOR DESTRUCTION' , 'artista':"GUNS N'ROSES" , 'año': 1987, 'precio': 30.11, 'genero': 'Rock'},
                   {'album':'DARK SIDE OF THE MOON' , 'artista':'PINK FLOYD' , 'año': 1973, 'precio': 21.99, 'genero': 'Rock'},
                   {'album':'HIGHWAY TO HELL' , 'artista':'AC/DC' , 'año': 1979, 'precio': 20.50, 'genero': 'Metal'},
                   {'album':'THE NUMBER OF THE BEAST' , 'artista':'IRON MAIDEN' , 'año': 1982, 'precio': 17.99, 'genero': 'Metal'},
                   {'album':'MASTER OF PUPPETS' , 'artista':'METALLICA' , 'año': 1986, 'precio': 36.80, 'genero': 'Metal'},
                   {'album':'ALTARS OF MADNESS' , 'artista':'MORBID ANGEL' , 'año': 1989, 'precio': 26.09, 'genero': 'Death Metal'},
                   {'album':'DIVUS DE MORTUUS' , 'artista':'NECROVORE' , 'año': 1987, 'precio': 36.80, 'genero': 'Death Metal'},
                   {'album':'MASTER OF PUPPETS' , 'artista':'METALLICA' , 'año': 1986, 'precio': 15.00, 'genero': 'Death Metal'},
                   {'album':'BLACK METAL' , 'artista':'VENOM' , 'año': 1982, 'precio': 17.95, 'genero': 'Black Metal'},
                   {'album':'FILOSOFEM' , 'artista':'BURZUM' , 'año': 1996, 'precio': 17.22, 'genero': 'Black Metal'},
                   {'album':'BATHORY' , 'artista':'BATHORY' , 'año': 1984, 'precio': 16.29, 'genero': 'Black Metal'}]


shortListDiscs: list = [{'album':'AMERICAN IDIOT' , 'artista':'GREEN DAY' , 'año': 2004, 'precio': 51.64, 'genero': 'Pop'}, 
                   {'album':'BACK TO BLACK' , 'artista':'AMY WINEHOUSE' , 'año': 2006, 'precio': 23.99, 'genero': 'Pop'},
                   {'album':'KID A' , 'artista':'RADIOHEAD' , 'año': 2000, 'precio': 31.37, 'genero': 'Electro'},
                   {'album':'RANDOM ACCESS MEMORIES' , 'artista':'DAFT PUNK' , 'año': 2013, 'precio': 11.99, 'genero': 'Electro'},
                   {'album':'TALENTO DE BARRIO' , 'artista':'DADDY YANKEE' , 'año': 2008, 'precio': 11.99, 'genero': 'Reggaeton'},
                   {'album':'YHLQMDLG' , 'artista':'BAD BUNNY' , 'año': 2020, 'precio': 21.86, 'genero': 'Reggaeton'},
                   {'album':'UNTITLED (IV)' , 'artista':'LED ZEPPELIN' , 'año': 1971, 'precio': 14.99, 'genero': 'Rock'},
                   {'album':'APPETITE FOR DESTRUCTION' , 'artista':"GUNS N'ROSES" , 'año': 1987, 'precio': 30.11, 'genero': 'Rock'},
                   {'album':'HIGHWAY TO HELL' , 'artista':'AC/DC' , 'año': 1979, 'precio': 20.50, 'genero': 'Metal'},
                   {'album':'THE NUMBER OF THE BEAST' , 'artista':'IRON MAIDEN' , 'año': 1982, 'precio': 17.99, 'genero': 'Metal'},
                   {'album':'ALTARS OF MADNESS' , 'artista':'MORBID ANGEL' , 'año': 1989, 'precio': 26.09, 'genero': 'Death Metal'},
                   {'album':'DIVUS DE MORTUUS' , 'artista':'NECROVORE' , 'año': 1987, 'precio': 36.80, 'genero': 'Death Metal'},
                   {'album':'BLACK METAL' , 'artista':'VENOM' , 'año': 1982, 'precio': 17.95, 'genero': 'Black Metal'},
                   {'album':'FILOSOFEM' , 'artista':'BURZUM' , 'año': 1996, 'precio': 17.22, 'genero': 'Black Metal'}]



try:
    with open("./medio/discos_long.csv", 'w',newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=shortListDiscs[0].keys())
        writer.writeheader()
        for key in longListDiscs:
            writer.writerow(key)
except IOError:
    print("I/O error") """


