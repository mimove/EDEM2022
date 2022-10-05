#------------------------------------------------
# Reto 19
# Escribe un programa capaz de imprimir los próximos tres días a partir de la fecha actual (haz uso de datetime.datetime.today() para obtener la fecha actual).
# Pista: investiga acerca de datetime.timedelta()
#------------------------------------------------

from datetime import datetime, timedelta

for i in range(3): print('Fecha {}: {}'.format(i+1, datetime.strftime(datetime.today()+timedelta(i+1),'%d/%m/%Y')))
