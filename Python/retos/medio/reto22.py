#------------------------------------------------
# Reto 22
# A partir de:
# listaTuplas = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
# miDiccionario = {}
# Realiza una iteración para poder pasar de una lista de tuplas a un diccionario llamado miDiccionario
#------------------------------------------------


listaTuplas = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]

miDiccionario = dict()

#for a, b in listaTuplas:  miDiccionario.setdefault(a,[]).append(b)

[miDiccionario.setdefault(a,[]).append(b) for a, b in listaTuplas]
    
print(miDiccionario)


