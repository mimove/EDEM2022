#------------------------------------------------
# Reto 29
# Crea una función capaz de devolver el segundo valor numérico más pequeño de una lista de números
#------------------------------------------------


def secondSmaller(listNum:list)->int:  return list(set(sorted(listNum)))[1] 


