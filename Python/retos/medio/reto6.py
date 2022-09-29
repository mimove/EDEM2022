#------------------------------------------------
# Reto 6
# Escribe un programa que pida al usuario una palabra por consola y devuelva si se trata de un palíndormo**
# ** Palíndromo: Palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda
#------------------------------------------------


def palindrome(word = input('Introduce una palabra: ')) -> bool:   return word[::-1].lower() == word.lower()