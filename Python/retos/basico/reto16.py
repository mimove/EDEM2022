#------------------------------------------------
# Reto 16
# Crea un script que sea capaz de restar dos fechas y muestra el resultado por consola
#------------------------------------------------

def diffDates(d1, d2):
    from datetime import date
    return abs(d2-d1).days
    
    