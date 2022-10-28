#-------------------------------------#
# Reto 30
# Investiga acerca de ast y convierte un String en una lista. Es decir, un string que representa una lista literalmente. Puedes usar este ejemplo:
# colores ="['Rojo', 'Verde', 'Blanco']"
# Se trata de una cadena de texto que dentro contiene una lista. La idea es que a través de ast lo conviertas en una lista como tal.
#-------------------------------------#


import ast


tree = ast.parse("['Rojo', 'Verde', 'Blanco']")

for node in ast.iter_child_nodes(tree):
    print(node)

print(ast.dump(ast.parse("['Rojo', 'Verde', 'Blanco']", mode='eval'), indent=4))
