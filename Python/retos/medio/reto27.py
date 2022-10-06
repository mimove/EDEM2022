#------------------------------------------------
# Reto 27
# Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set).
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.
#------------------------------------------------

listCountries = input("Introduce una lista de países separados por comas (ej: España,Portugal,Francia:) ")

tmp = listCountries.replace(" ","")

listNew = set(tmp.split(','))


print(listNew)