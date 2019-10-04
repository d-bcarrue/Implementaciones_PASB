#!/usr/bin/python3
import sys

with open(sys.argv[1], 'rt',encoding='latin1') as file:
    comprimido = file.read()

i = 0
cadena = ''
while i < len(comprimido):
    i2 = comprimido.find(',', i)
    p = int(comprimido[i:i2])
    i3 = comprimido.find(',',i2 + 1)
    l = int(comprimido[i2 + 1: i3])
    c = comprimido[i3 + 1]
    i = i3 + 3
    if p != 0 and -p + l == 0:
        cadena += cadena[-p:] + c
    else:   
        cadena += cadena[-p:(-p + l)] + c
with open('prueba.txt','wt+',encoding='latin1') as file:
    file.write(cadena)
    file.write('\n')
