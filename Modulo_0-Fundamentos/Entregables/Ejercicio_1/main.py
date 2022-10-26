import requests
import csv
import time


def writeData(path, mode, datos):
    with open(path, mode, encoding='UTF8') as f:
        w = csv.DictWriter(f, datos.keys())
        
        # If file doesn't exist, create header
        if f.tell() == 0:
            w.writeheader()

        # write the data
        w.writerow(datos)
    


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
        
        # Store data in a dict with the name of the character and the quote
        datos = {"Personaje": datosjson[0]["character"], "Frase": datosjson[0]["quote"]}


        # Printing values in dict as a checking step
        print('La frase de {} es: {}'.format(datos["Personaje"], datos["Frase"]))


        # Use of writeData function to write quotes in a csv file
        writeData('General/quotes_general.csv', 'a', datos)


        if 'Homer' in datos["Personaje"]:
            writeData('Homer/quotes_homer.csv', 'a', datos)

        elif 'Lisa' in datos["Personaje"]:
            writeData('Lisa/quotes_lisa.csv', 'a', datos)


        # I choose 1 second so that the verification steps are much faster 
        time.sleep(1)