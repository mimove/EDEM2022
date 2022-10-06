#------------------------------------------------
# Reto 23
# Investiga acerca de Counter del módulo collections y haciendo uso del siguiente diccionario, encuentra la moda en las puntuaciones de películas:
# misPeliculas = {'PeliculaA':81, 'PeliculaB':83, 'PeliculaC':87}
#------------------------------------------------

# https://www.guru99.com/python-counter-collections-example.html


from collections import Counter


misPeliculas = {'PeliculaA':81, 'PeliculaB':83, 'PeliculaC':87}

count = Counter(misPeliculas)

print(f'La pelicula de moda es: {count.most_common(1)[0][0]} con una puntuación de {count.most_common(1)[0][1]}')
