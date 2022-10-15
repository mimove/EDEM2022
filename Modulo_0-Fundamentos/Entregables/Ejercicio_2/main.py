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
        
        img_personaje = datosjson[0]["image"]
        
        print(datos)


        # Obtenemos valor en la clave 'value' del JSON que nos interesa
        
        print('La frase de {} es: {}'.format(datos["Personaje"], datos["Frase"]))

        with open('/home/ttmam/GitHub/EDEM2022/Modulo_0-Fundamentos/Entregables/Ejercicio_2/quotes_general.csv', 'a', encoding='UTF8') as f:
            w = csv.DictWriter(f, datos.keys())
            
            if f.tell() == 0:
               w.writeheader()

            # write the data
            w.writerow(datos)


        if 'Homer' in datos["Personaje"]:
          with open('/home/ttmam/GitHub/EDEM2022/Modulo_0-Fundamentos/Entregables/Ejercicio_2/Homer/quotes_homer.csv', 'a', encoding='UTF8') as f:
              w = csv.DictWriter(f, datos.keys())
              
              if f.tell() == 0:
                w.writeheader()

              # write the data
              w.writerow(datos)
              
              img_data = requests.get(img_personaje).content
              with open('Homer/Homer.png', 'wb') as handler:
                if handler.tell() == 0:
                   handler.write(img_data)

        elif 'Lisa' in datos["Personaje"]:

           with open('/home/ttmam/GitHub/EDEM2022/Modulo_0-Fundamentos/Entregables/Ejercicio_2/Lisa/quotes_lisa.csv', 'a', encoding='UTF8') as f:

              w = csv.DictWriter(f, datos.keys())
              
              if f.tell() == 0:  
                w.writeheader()

              # write the data
              w.writerow(datos)
        
        time.sleep(1)



