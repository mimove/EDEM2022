#------------------------------------------------
# Reto 10
# Escribe un programa que guarde en una variable el siguiente contenido:
# {'titulo':'El Más Allá','aka':'E tu vivrai nel terrore - Laldilà','director':'Lucio Fulci', 'año':1981, 'país':'Italia'}
#------------------------------------------------

def printContent():
    variable = {'titulo':'El Más Allá','aka':'E tu vivrai nel terrore - Laldilà','director':'Lucio Fulci', 'año':1981, 'país':'Italia'}
    contenido = variable['titulo'] + ' ' + variable['aka'] + ' ' + variable['director'] + ' ' + str(variable['año']) + ' ' + variable['país']
    print(contenido)