import requests
import csv
import time
import os
import string
import pandas as pd

def word_count(str):
    # Obtained from https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-12.php
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


dictWords = dict()

while True:
   
    URL = 'https://thesimpsonsquoteapi.glitch.me/quotes'

    try:
      respuesta = requests.get(URL,timeout=3)
    except requests.exceptions.Timeout as err:
      print(err)
      time.sleep(1)
      
    if respuesta.status_code >= 200 and respuesta.status_code < 300:

      # Extraemos los datos en formato JSON
        
      datosjson = respuesta.json()
      
      # a_string.translate(str.maketrans('', '', string.punctuation)
      
      datos = {"Personaje": datosjson[0]["character"].translate(str.maketrans('', '', string.punctuation)).split(), "Frase": datosjson[0]["quote"]}
        
      

      img_personaje = datosjson[0]["image"]
      


      # Obtenemos valor en la clave 'value' del JSON que nos interesa
        
      print('La frase de {} es: {}'.format(" ".join(datos["Personaje"]), datos["Frase"]))
      
      
      dictWords.update(word_count(string.capwords(datos["Frase"].translate(str.maketrans('', '', '".,:!?')))))
      
      
      with open('countedWords.csv', 'w') as csv_file:  
        writer = csv.writer(csv_file)
        for key, value in dictWords.items():
          writer.writerow([key, value])  
        
        
      #Check if folder of character exist, if not create it.
        
      if not os.path.exists("_".join(datos["Personaje"])):
        os.makedirs("_".join(datos["Personaje"]))
        
        
        with open("_".join(datos["Personaje"]) + '/' + 'quotes' + '_' + "_".join(datos["Personaje"]) + '.csv', 'a', encoding='UTF8') as f:
          w = csv.DictWriter(f, datos.keys())
          
          if f.tell() == 0:
            w.writeheader()

          # write the data
          w.writerow({'Personaje':" ".join(datos["Personaje"]), 'Frase': datos["Frase"]})
        
        img_data = requests.get(img_personaje).content
        with open("_".join(datos["Personaje"]) + '/' + "_".join(datos["Personaje"]) +'.png', 'wb') as handler:
          if handler.tell() == 0:
            handler.write(img_data)

          
          
        

        # with open('Palabras/quotes_general.csv', 'a', encoding='UTF8') as f:
        #   w = csv.DictWriter(f, datos.keys())
            
        #   if f.tell() == 0:
        #     w.writeheader()

        #     # write the data
        #     w.writerow(datos)


       
        
        time.sleep(1)



