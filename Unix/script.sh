#!/bin/bash

echo "hello world"

c=1
read var1
x=0
while [ $c -le 100 ]
do
  x=$(($(($var1*$c))+$x))
  c=$(($c+1))
done

echo $x