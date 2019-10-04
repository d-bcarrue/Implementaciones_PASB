#!/usr/bin/python3

import sys

def frecuencias(fichero):
    global cadena
    dicc = {}
    with open(fichero,'rt') as f:
        #TODO: PROBAR LAS DOS OPCIONES ( LINEA A LINEA, EL FICHERO ENTERO, COUNTER DE COLLECTIONS 
        #------------------OPCION 1---------------------
#        for linea in f:
#            for caracter in linea:
#                if not (caracter in dicc.keys()):
#                    dicc[caracter] = 1
#                else:
#                    dicc[caracter] += 1
        #------------------OPCION 2---------------------
#        cadena = f.read()
#        for caracter in set(cadena):
#            dicc[caracter] = cadena.count(caracter)
        #-----------------OPCION 3______________________
        from collections import Counter
        cadena = f.read()
        dicc = Counter(cadena)

    lista_frecuencias = sorted(dicc.items(),key = lambda x: x[1], reverse = True)
    return lista_frecuencias

def frecuencias_ejemplo(cadena):
    lista = []
    for i in sorted(list(set(cadena))):
        lista.append((i,cadena.count(i)))
    return lista

def calculo_niveles(lista):
    niveles = [0]*len(lista)
    simbolos = list(zip(*lista))[0]
    lista = [([i],j) for i,j in lista ]
    while(len(lista)>1):
        #Sacamos los dos valores mas pequeños entre los nodos y los eliminamos entre la lista de nodos
        x1 = min(lista, key = lambda x: x[1])
        lista.pop(lista.index(x1))
        x2 = min(lista, key = lambda x: x[1])
        lista.pop(lista.index(x2))
        #Generamos un nuevo nodo con ambas letras 
        nuevo_nodo = (x1[0]+x2[0],x1[1] + x2[1])
        lista.append(nuevo_nodo)
        # Por cada caracter que es hijo del nuevo nodo añadimos un nivel
        for caracter in x1[0] + x2[0]:
            i = simbolos.index(caracter)
            niveles[i] += 1
    resultado = list(zip(simbolos,niveles))
    resultado = sorted(resultado, key=lambda x: x[1],reverse = False)
    return list(zip(*resultado))

def generador_codigos(simbolos,niveles):
    #IMPORTANTE: SI UN NIVEL ESTA VACIO SE ROMPE LA NORMA QUE INFIERO DE LOS APUNTES, POR CADA NIVEL SE DEBE AÑADIR UN 0 A LA DERECHA AL NUMERO BINARIO O LO QUE ES LO MISMO MULTIPLICAR POR DOS EN DECIMAL.
    codigos = [0]
    nivel_anterior = niveles[0]
    num_anterior = 0
    for nivel in niveles[1:]:
        num_anterior = 2 ** (nivel - nivel_anterior) * (num_anterior + 1)
        nivel_anterior = nivel
        codigos.append(num_anterior)
    codigos_bin = []
    for nivel, codigo in zip(niveles,codigos):
        c_bin = str(bin(codigo))[2:]
        if len(c_bin) < nivel:
            # El nivel de ese caracter debe coincidir con el largo de la cadena de bits, por ejemplo si el primer caracter esta en el nivel 2, le corresponde el 00 no el 0
            # Para solucionarlo añadimos ceros a la izquierda
            # TODO: CAMBIAR ESTO A ALGO MAS ELEGANTE
            codigos_bin.append("0" * (nivel - len(c_bin)) + c_bin)
        else:
            codigos_bin.append(c_bin)
    return {simbolo: c_bin for simbolo,c_bin in zip(simbolos,codigos_bin) }

lista = frecuencias(sys.argv[1])
#cadena = "panamabanana"
#lista = frecuencias_ejemplo(cadena)

#lista = sorted(lista,key=lambda x: x[1],reverse=True)

simbolos, niveles = calculo_niveles(lista)
codigo = generador_codigos(simbolos, niveles)
codigos_por_nivel = []
min_nivel = min(niveles)
max_nivel = max(niveles)
for i in range(min_nivel,max_nivel + 1):
    codigos_por_nivel.append(str(niveles.count(i)))
# Solucion temporal, un archivo por lista
with open(sys.argv[1] + ".sim","wt") as fichero:
    fichero.write(''.join(simbolos))

with open(sys.argv[1] + ".nvl","wt") as fichero:
    fichero.write(','.join([str(min_nivel),str(max_nivel)])+ ',')
    fichero.write(','.join(codigos_por_nivel))

with open(sys.argv[1] + ".cmp","wt") as fichero:
    for letra in cadena:
        fichero.write(codigo[letra])
