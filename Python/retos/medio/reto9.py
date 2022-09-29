#-------------------------------------#
# Reto 9
# Escribe una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.
#-------------------------------------#


def decToBin(number: int)->str:
    
    listBin: list = list()
    
    while number/2 > 0:
        listBin.append(str(number%2))
        number //= 2
         
    return ''.join(reversed(listBin))



def binToDec(number: str)->int:
    
    decNumber: int = 0
    
    
    
    for i in range(len(number)):
        decNumber += 2**i*int(number[-i-1])
        
    return decNumber