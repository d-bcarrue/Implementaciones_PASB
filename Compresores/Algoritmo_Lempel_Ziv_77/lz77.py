#!/usr/bin/python3
import sys
import os

"""
HAY UN PROBLEMA CON EL ARCHIVO english.50MB, si lo paso por por diff hay cuatro lineas que cambian, sin embargo si antes lo leo en python y lo escribo de nuevo sin modificar esas se vuelven iguales.
"""
def input_cadena(ruta):
    with open(ruta,'rt',encoding='latin1') as file:
        cadena = file.read()
    return cadena

preventana = 10 
postventana = 10 
cadena = input_cadena(sys.argv[1])
posicion = 0
p = 0
l = 0
c = cadena[posicion]
i = 0
largo_cadena = len(cadena)
resultado = []
while i < largo_cadena:
    p = 0
    l = 0
    c = cadena[i]

    for k in range(i - 1, i - preventana - 1, - 1):
        if k<0:
            break
        if cadena[i] == cadena[k]:
            p_temp = i - k
            l_temp = 1
            while True:
                if l_temp + i < largo_cadena and l_temp + k < i and cadena[i + l_temp] == cadena[k + l_temp]:
                    l_temp += 1
                else:
                    break
            if l <= l_temp:
                p = p_temp
                l = l_temp
                c = cadena[i+l_temp] if i + l_temp < largo_cadena else "\0"
    resultado.append(",".join((str(p),str(l),c))+',')
    
    i += l + 1
with open(f'{sys.argv[1]}.lz1','wt+',encoding='latin1') as file:
    file.writelines(resultado)

