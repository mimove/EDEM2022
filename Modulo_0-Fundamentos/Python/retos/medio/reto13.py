#------------------------------------------------
# Reto 13
# Escribe un programa que sea capaz de encontrar la diferencia completa entre dos fechas, mostrando días, horas, minutos y segundos.
#------------------------------------------------

def diffDateTime(a,b):
    
    from datetime import datetime

    if (a-b).days < 0: a, b = b, a # Swap in case the end date before the start date
    
        
    diffDays: int = (a-b).days
    diffHour: int = a.hour-b.hour
    diffMinute: int = a.minute-b.minute
    diffSecond: int = a.second-b.second
    
    
    if diffHour < 0:
        diffHour = 24 + (a.hour-b.hour)

    if diffMinute < 0:
        diffMinute = 60 + ((a.minute-b.minute))
        diffHour -= 1
    
    if diffSecond < 0:
        diffSecond = 60 + ((a.second-b.second))
        diffMinute -= 1
        
    return diffDays, diffHour, diffMinute, diffSecond
    
    


