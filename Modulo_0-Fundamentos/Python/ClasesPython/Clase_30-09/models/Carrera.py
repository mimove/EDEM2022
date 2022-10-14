from models.Coche import Coche


class Carrera:
    coches = []
    
    def __init__(self, participantes):
        self.coches = participantes
        
    
    def iniciar_carrera(self):
        print('Ha iniciado la carrera los participantes son:')
        for coche in self.coches:
            print(f'-> {coche.matricula}')