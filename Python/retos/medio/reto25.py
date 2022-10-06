#------------------------------------------------
# Reto 25
# Partiendo de la lista:
# comunidades = ["Madrid", "Aragón",
#                     "Valencia", "Cataluña",
#                     "Extremadura", "Castilla y León",
#                     "Castilla La Mancha", "Asturias",
#                     "Murcia", "Cantabria", "País Vasco",
#                     "Andalucia"]
# Crea una función que sea capaz de devolver una lista ordenada según la longitud de su nombre.
#------------------------------------------------


def sortLenList(listUnsort: list)->list:

    newListIdx = list() 
    newList = list()
    
    for idx, i in enumerate(listUnsort):
        newListIdx.append((len(i),idx))
        
    
    for i in sorted(newListIdx, reverse=True):
        newList.append(listUnsort[i[1]])
    
        
    return newList



def sortLenList1line(listUnsort:list)->list: return sorted(listUnsort, key=len, reverse=True)
    
    
