#------------------------------------------------
# Reto 9
# Escribe un programa que pueda decirte si un año (número entero) es bisiesto o no
#------------------------------------------------


# Explanation of leap year:

# In the Gregorian calendar, a normal year consists of 365 days. Because the actual length of a sidereal year 
# (the time required for the Earth to revolve once about the Sun) is actually 365.2425 days, a "leap year" of 366 days
# is used once every four years to eliminate the error caused by three normal (but short) years. Any year that is evenly
# divisible by 4 is a leap year: for example, 1988, 1992, and 1996 are leap years.

# However, there is still a small error that must be accounted for. To eliminate this error, the Gregorian calendar stipulates
# that a year that is evenly divisible by 100 (for example, 1900) is a leap year only if it is also evenly divisible by 400.


def leapYear(year: int): 
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
         print(f'El año {year} es bisiesto')
    
    else:
         print(f'El año {year} no es bisiesto')
    



 