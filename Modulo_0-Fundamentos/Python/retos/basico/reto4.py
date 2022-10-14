#------------------------------------------------
# Reto 4
# Escribe un programa que sea capaz de mostrar los elementos de una lista en orden inverso al original.
# Por ejemplo: teniendo [1,2,3,4,5] el programa debe mostrar por pantalla [5,4,3,2,1]
#------------------------------------------------


# Reverse option function using ini, end, step

def invList(lst: list)->list:  return lst[len(lst)::-1]
    



# Reverse option function reversed and method reverse() function

def invListMethod(lst: list)->list:
    lst.reverse()
    return lst


def invListFunction(lst: list)->list:
    
    return reversed(lst)


    
