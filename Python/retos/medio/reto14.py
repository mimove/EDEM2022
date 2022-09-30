#------------------------------------------------
# Reto 14
# Partiendo de las siguientes cadenas de texto:
# miCodigo = 'print("Hola Mundo")'
# otroCodigo = """
# def multiplicar(x,y):
#     return x*y

# print('Multiplica: 2 * 4: ',multiplicar(2,4))
# """
# Haz uso de exec() para ejecutar ambas operaciones
#------------------------------------------------

program = ('miCodigo = print("Hola Mundo")\notroCodigo = "Otro codigo"\nprint(otroCodigo)\n \ndef multiplicar(x,y): return x*y\nx = 5\ny = 6\nprint(multiplicar(x,y))')


exec(program)