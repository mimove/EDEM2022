#------------------------------------------------
# Reto 28
# Crea un script que solicite al usuario que escriba una frase que contenga las palabras Madrid y Valencia.
# Una vez lo haya introducido, se debe mostrar la frase, habiendo sustituido Madrid por Valencia y Valencia por Madrid.
# Por ejemplo: Si el usuario introduce Vivo en Madrid y viajo a Valencia la salida del programa debe ser Vivo en Valencia y viajo a Madrid.
#------------------------------------------------

sentence = input('Introduce una frase con las palabras Madrid y Valencia: ')

sentenceNew = sentence.replace("Valencia", "{Valencia}").replace("Madrid", "{Madrid}").format(Madrid = 'Valencia', Valencia = 'Madrid')


print(sentence)
print(sentenceNew)