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

""" nombres_velocidades = pokemon_csv_df[['Name','Speed']] # Genera un df a partir de la lista con solo 2 columnas con 'Name' y 'Speed'

print(nombres_velocidades) """


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

print(pokemon_csv_df.iloc[:3])






