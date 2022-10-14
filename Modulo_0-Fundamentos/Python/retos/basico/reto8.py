#------------------------------------------------
# Reto 8
# Escribe un programa que pueda decirte si un número (número entero) es primo o no
#------------------------------------------------

# Prime numbers are numbers greater than one with no positive divisors besides one and itself

def prime(n: int):
    if n <= 0:
        return print(f'{n} no es ni primo ni no primo')
    elif n == 1:
        return print(f'{n} es primo')
    
    for i in range(2,n):
        if n%i == 0 :
            return print(f'{n} no es primo')
    
    return print(f'{n} es primo')
        
