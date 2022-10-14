#------------------------------------------------
# Reto 5
# Escribe un programa que realice lo mismo que el programa del reto 4, pero que elimine de la lista aquellos lenguajes que el usuario conoce y únicamente muestre aquellos que no conoce.
#------------------------------------------------



def languageUnknown(listLanguage:dict)->list:
    
    knownLanguage: list = list()
    
    for i in listLanguage.items():
        if i[1] == 'no':
            knownLanguage.append(i[0])
            
    
    return knownLanguage
            
        
        
            