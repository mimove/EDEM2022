#------------------------------------------------
# Reto 8
# Escribe una función que reciba un número entero positivo y devuelva su factorial.
#------------------------------------------------

def factorialNumber(number: int) -> int:
    
    factorial:int = 1
    for i in range(number):
        factorial *= i+1
        
    return factorial