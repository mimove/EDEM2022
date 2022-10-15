import requests
import csv
import time

while True:
   
    URL = 'https://thesimpsonsquoteapi.glitch.me/quotes'


    respuesta = requests.get(URL)

    if respuesta.status_code >= 200 and respuesta.status_code < 300:

        # Extraemos los datos en formato JSON

        datos = respuesta.json()

        # Obtenemos valor en la clave 'value' del JSON que nos interesa
        
        frase_simpsons = datos[0]["quote"]

        personaje_simpsons = datos[0]["character"]


        print('La frase de {} es: {}'.format(personaje_simpsons, frase_simpsons))

        # with open('General/quotes_general.csv', 'a', encoding='UTF8') as f:
        #   writer = csv.writer(f)

        #   # write the data
        #   writer.writerow([personaje_simpsons, frase_simpsons])


        if 'Homer' in personaje_simpsons:
          with open('Homer/quotes_homer.csv', 'a', encoding='UTF8') as f:

                writer = csv.writer(f)

                # write the data
                writer.writerow([personaje_simpsons, frase_simpsons])

        elif 'Lisa' in personaje_simpsons:

           with open('Lisa/quotes_lisa.csv', 'a', encoding='UTF8') as f:

                writer = csv.writer(f)

                # write the data
                writer.writerow([personaje_simpsons, frase_simpsons])
        
        time.sleep(1)

