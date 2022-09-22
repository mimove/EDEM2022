#!/bin/bash

echo "hello world"


# Script realizar calculo de var*x + x e imprimir resultado

c=1
read var1
x=0
while [ $c -le 100 ]
do
  x=$(($(($var1*$c))+$x))
  c=$(($c+1))
done

echo $x



# Ejercicio hecho el otro día en clase 16/09/2022


# La primera línea le dice a Unix qué tipo de interprete vamos a utilizar
# Comandos Ejercicio
# Crear carpeta
mkdir EjercicioRemember
# Dentro de EjercicioRemember crearr Ej1 y Ej2
# opcion A
mkdir EjercicioRemember/Ej1
mkdir EjercicioRemember/Ej1
# En ej1 crear un fichero primero.txt con permiso de lectura para el grupo solo
touch EjercicioRemember/Ej1/primero.txt
chmod 040 EjercicioRemember/Ej1/primero.txt
#En ej2 crear un fichero Segundo.txt con todos los permisos
touch EjercicioRemember/Ej2/segundo.txt
chmod 777 EjercicioRemember/Ej2/segundo.txt
# Copiad primero.txt a ej2 y moved Segundo.txt a ej1
cp EjercicioRemember/Ej1/primero.txt EjercicioRemember/Ej2
mv EjercicioRemember/Ej2/segundo.txt EjercicioRemember/Ej1
#Listar el contenido de ej1
ls EjercicioRemember/Ej1
#Escribir en primero.txt “El Data mola mogollón”
echo “El Data mola mogollón” > EjercicioRemember/Ej1/primero.txt
#Mostrar el contenido de primero.txt
cat EjercicioRemember/Ej1/primero.txt
