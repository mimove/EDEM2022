#------------------------------------------------
# Reto 3
# El nuevo gobierno ha decidido replantear el sistema de pago de impuestos. Ha pensado que a partir de ahora:
# si una persona es mayor de 16 años y menor de 70 ésta debe pagar impuestos.
# En caso de no tener ingresos iguales o superiores a 800€ se acumulará una deuda mensual del 10%.
# Si supera los 800€, pero no llega a los 2000€, deberá pagar un impuesto del 30% mensual
# Si supera los 2000€ esta persona deberá pagar el 50% en concepto de impuestos
# si la persona es menor de 16 años, no tiene que pagar impuestos
# Escribe un programa capaz de calcular la cantidad de impuestos, o endeudamiento, de una lista de personas** durante un año entero (12 meses)
#------------------------------------------------


def payTax(listTaxPayers: list):
    
    for i in range(len(listTaxPayers)):
        
        listTaxPayers[i]['impuestos']: float = 0
        
        if listTaxPayers[i]['edad'] < 16 or listTaxPayers[i]['edad'] > 70:
            continue
            
        elif listTaxPayers[i]['salario'] / 12 <= 800:
            
            listTaxPayers[i]['impuestos'] = listTaxPayers[i]['salario'] * 0.1 
        
        elif listTaxPayers[i]['salario'] / 12 > 800 and listTaxPayers[i]['salario'] / 12 < 2000:
            
            listTaxPayers[i]['impuestos'] = listTaxPayers[i]['salario'] * 0.3 
            
        else:
            
            listTaxPayers[i]['impuestos'] = listTaxPayers[i]['salario'] * 0.5 
        

    