'''
EJERCICIO 
  - Por consola el usuario debe acertar un numero secreto
  - Si acierta en el primer intento: Sus puntos se suman 5 puntos y se multiplica por 2
  - Si acierta en el segundo intento: se suman 5 puntos
  - Si acierta a la tercera se suma 2 puntos
  - Si falla todas las veces se resta 2 puntos.
'''

numeroBuscado = 300
intento = 3
puntos = 0

numeroElegido = int(input(f'Intentos restantes: {intento}. Elige un numero: '))

while (numeroElegido != numeroBuscado) and intento > 1:
  intento -= 1
  if numeroElegido > numeroBuscado : 
    numeroElegido = int(input(f'Intentos restantes: {intento}. Elige otro numero más pequeño: ')) 
  else:
    numeroElegido = int(input(f'Intentos restantes: {intento}. Elige otro numero más grande: '))
      

if numeroElegido != numeroBuscado:
  puntos -= 2
  print(f'Te has quedado sin intentos. Has conseguido {puntos} puntos')
elif intento >= 2:
  puntos +=5
  puntos *= intento - 1
  print(f'Has ganado, el numero era {numeroBuscado}. Has conseguido {puntos} puntos')
else:
  puntos += 2    
  print(f'Has ganado, el numero era {numeroBuscado}. Has conseguido {puntos} puntos')
  
  
  
  
  
  