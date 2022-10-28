#------------------------------------------------
# Reto 10
# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.
#------------------------------------------------


def maxDiv(a: int, b: int) -> int:

    # Greateast common divisor by Euclidean Algorithm: https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
    
    if a == 0 or b == 0: 
        
        return max(a,b)
    
    elif max(a,b)%min(a,b) == 0:
        
        return min(a,b)
        
    while max(a,b)%min(a,b) != 0:      
               
        if max(a,b) == a:
            a = max(a,b)%min(a,b)
        else:
            b = max(a,b)%min(a,b)
    
    
    return min(a,b)


def minMult(a: int,  b: int) -> int:  return int((a*b)/maxDiv(a,b))