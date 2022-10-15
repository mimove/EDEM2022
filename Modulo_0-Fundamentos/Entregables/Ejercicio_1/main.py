import requests
import csv
import time

while True:
   
    URL = 'https://thesimpsonsquoteapi.glitch.me/quotes'


    respuesta = requests.get(URL)

    if respuesta.status_code >= 200 and respuesta.status_code < 300:

        # Extraemos los datos en formato JSON
        
        datosjson = respuesta.json()
        
        datos = {"Personaje": datosjson[0]["character"], "Frase": datosjson[0]["quote"]}
        
        print(datos)


        # Obtenemos valor en la clave 'value' del JSON que nos interesa
        
        
        # frase_simpsons = datos["Frase"]

        # personaje_simpsons = datos["Personaje"]

        print('La frase de {} es: {}'.format(datos["Personaje"], datos["Frase"]))

        with open('General/quotes_general.csv', 'a', encoding='UTF8') as f:
            w = csv.DictWriter(f, datos.keys())
            
            if f.tell() == 0:
               w.writeheader()

            # write the data
            w.writerow(datos)


        if 'Homer' in datos["Personaje"]:
          with open('Homer/quotes_homer.csv', 'a', encoding='UTF8') as f:
              w = csv.DictWriter(f, datos.keys())
              
              if f.tell() == 0:
                  w.writeheader()

              # write the data
              w.writerow(datos)

        elif 'Lisa' in datos["Personaje"]:

           with open('Lisa/quotes_lisa.csv', 'a', encoding='UTF8') as f:

              w = csv.DictWriter(f, datos.keys())
              
              if f.tell() == 0:  
                  w.writeheader()

              # write the data
              w.writerow(datos)
        
        time.sleep(1)

