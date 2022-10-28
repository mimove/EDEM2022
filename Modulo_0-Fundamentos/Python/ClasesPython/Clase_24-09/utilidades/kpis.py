#Archivo utilidades/kpis.py
 
def puntuacion(objetivos: int) -> int:
  puntuacion: int = 0
  
  if(objetivos <= 0):
    pass
  elif(objetivos >0 and objetivos <=5):
    puntuacion = 2
  elif(objetivos>5 and objetivos <=7):
    puntuacion = 4
  else:
    puntuacion = 6
  return puntuacion