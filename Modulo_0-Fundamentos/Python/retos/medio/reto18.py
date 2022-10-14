#------------------------------------------------
# Reto 18
# A partir de la siguiente lista:
# colores = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
# Crea un script que pueda almacenar cada uno de los elementos (tuplas) de la lista en variable1, variable2 y variable3 para después imprimirlas por consola.
#------------------------------------------------


colores = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),("Yellow", "#FFFF00", "rgb(255, 255, 0)")]

# This is not the recommended way to store variables in Python, but it's shown here as an example.

for idx, i in enumerate(colores):
    globals()['variable' + str(idx + 1)] = i
    print(globals()['variable' + str(idx + 1)])
    



""" # Alternative

variableAlt1 = colores[0]
variableAlt2 = colores[1]
variableAlt3 = colores[2]    

for idx, i in enumerate(colores):
    print(eval('variableAlt' + str(idx + 1))) """