#------------------------------------------------
# Reto 17
# Crea un script que pueda mostrar la hora actual en milisegundos
#------------------------------------------------

from datetime import datetime

print(datetime.now().timestamp()*1000)