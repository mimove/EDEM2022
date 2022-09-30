class Coche():
    
    # Atributos de clase
    marca:str
    modelo:str
    color:str
    matricula:str    
    id_seguro:str
    titular:str
    velocidad:float = 0 # Velocidad por defecto 0 km/h
    
    
    # Método constructor
    def __init__(self, marca, modelo, color, matricula, titular): # La velocidad no se pone porque ya está inicializada
      self.marca = marca
      self.modelo = modelo
      self.color = color
      self.matricula = matricula
      self.titular = titular
    
    
    def arrancar(self):
      self.velocidad = 10
      print(f'El coche con matricula {self.matricula} ha arrancado')
      
    def frenar(self, presion: float):
      self.velocidad -= (presion - 10)
      print(f'El coche ha frenado. Su velocidad ahora es {self.velocidad}km/h')
    
    def acelerar(self, presion: float):
      self.velocidad += (presion + 10)
      print(f'El coche ha acelerado. Su velocidad ahora es {self.velocidad}km/h')
