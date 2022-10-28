#------------------------------------------------
# Reto 21
# Haciendo uso de:
# colores = ["Negro", "Rojo", "Marrón", "Amarillo"]
# representacion = ["#000000", "#FF0000", "#800000", "#FFFF00"]
# e investigando acerca de zip() deberás entrelazar ambas listas para obtener un diccionario que tenga la clave color cuyos valores son los de la lista colores y otra clave code que tendrá como valor los datos de la lista representación.
#------------------------------------------------


colores = ["Negro", "Rojo", "Marrón", "Amarillo"]
representacion = ["#000000", "#FF0000", "#800000", "#FFFF00"]

dic1 = dict(zip(colores, representacion))

dic2 = dict()

dic3 = dict()

for a, b in zip(colores, representacion):
    dic2.setdefault('color', []).append(a)    
    dic3.setdefault('color', []).append(b)

   
print(dic1)
print(dic2)
print(dic3)