#------------------------------------------------
# Reto 15
# Partiendo del siguiente snippet:
# numeros = [10,20,(1,3),30,50,69,(10,20),40]
# cantidad = 0
# Realiza un script que permita encontrar dentro de la lista aquellos elementos que sean tuplas. Cada vez que encuentre una tupla, deberá incrementarse la variable cantidad.
# *** Pista: Haz uso de isinstance()
#------------------------------------------------


numeros = [10,20,(1,3),30,50,69,(10,20),40]
cantidad = 0

for i in numeros:
    if isinstance(i,tuple):
        cantidad += 1
        

print(cantidad)
    

