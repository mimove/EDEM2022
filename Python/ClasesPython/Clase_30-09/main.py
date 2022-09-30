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



