#------------------------------------------------
# Reto 16
# Partiendo de la siguiente lista de tuplas:
# miLista = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Actualiza la lista sin aquellas tuplas que estén vacías.
#------------------------------------------------


miLista = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d'),(),()]

for idx, i in reversed(list(enumerate(miLista))):

    if not len(i) or i[0]=='':  miLista.pop(idx)
       

print(miLista)