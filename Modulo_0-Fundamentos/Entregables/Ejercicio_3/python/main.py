import requests
import csv
import time
import os
import string

def writeData(path, mode, datos):
    with open(path, mode, encoding='UTF8') as f:
        w = csv.DictWriter(f, datos.keys())
        
        # If file doesn't exist, create header
        if f.tell() == 0:
            w.writeheader()

        # write the data
        w.writerow(datos)

def word_count(str,dictCount):
  
    # Modified from https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-12.php
    
    counts = dictCount
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

    # Trying several times to connect to the API to avoid a freezing problem that occurs every now and then.
    try:
      respuesta = requests.get(URL,timeout=3)
    except requests.exceptions.Timeout as err:
      print(err)
      time.sleep(1)
      
    if respuesta.status_code >= 200 and respuesta.status_code < 300:

      # Extract data in json format
        
      datosjson = respuesta.json()
      
      
      # Store data in a dict, but name of character as a list of words for using them later in dynamic directory creation
      
      datos = {"Personaje": datosjson[0]["character"].translate(str.maketrans('', '', string.punctuation)).split(), "Frase": datosjson[0]["quote"]}
        
      
      # URL of image of the character
      
      img_personaje = datosjson[0]["image"]
      
      
      # Printing values in dict as a checking step
        
      print('La frase de {} es: {}'.format(' '.join(datos["Personaje"]), datos["Frase"]))
      
      
      # Updating dictionary with the word count. Removing punctuation characters except single quotation marks (') to avoid mixing words like we're with were.
      
      dictWords.update(word_count(string.capwords(datos["Frase"].translate(str.maketrans('', '', '".,:!?'))),dictWords))
      
      
      # Writing words as a list of key, value in a csv file in every row
      
      with open('results/countedWords.csv', 'w') as csv_file:  
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Palabra", "Cuenta"])
        for key, value in dictWords.items():
          writer.writerow([key, value])  
        
        
      # To create a directory for every character, we need to first check if it already exists. If it doesn't, the directory is created
      
      if not os.path.exists('results/'+'_'.join(datos["Personaje"])):
        os.makedirs('results/'+'_'.join(datos["Personaje"]))
        
        
        # Storing the word of the character in a csv file with its name
        
        writeData('results/'+'_'.join(datos["Personaje"]) + '/' + 'quotes' + '_' + '_'.join(datos["Personaje"]) + '.csv', 'a', {'Personaje':' '.join(datos["Personaje"]), 'Frase': datos["Frase"]})
        
        
        # Download the image of the character in its folder
        
        with open('results/'+'_'.join(datos["Personaje"]) + '/' + '_'.join(datos["Personaje"]) +'.png', 'wb') as handler:
          if handler.tell() == 0:
            img_data = requests.get(img_personaje).content
            handler.write(img_data)

       
        # I choose 1 second so that the verification steps are much faster
        
        time.sleep(1)



