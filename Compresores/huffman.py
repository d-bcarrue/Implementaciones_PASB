#!/usr/bin/python3

def frecuencias(fichero):
    dicc = {}
    with open(fichero,'rt') as f:
        #TODO: PROBAR LAS DOS OPCIONES (LETRA A LETRA, LINEA A LINEA, EL FICHERO ENTERO, COUNTER DE COLLECTIONS 
        for linea in f:
            for caracter in linea:
                if not (caracter in dicc.keys()):
                    dicc[caracter] = 1
                else:
                    dicc[caracter] += 1
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
    codigos = [0]
    nivel_anterior = niveles[0]
    num_anterior = 0
    for nivel in niveles[1:]:
        if nivel == nivel_anterior:
            num_anterior += 1
            nivel_anterior = nivel
            codigos.append(num_anterior)
        else:
            nivel_anterior = nivel
            num_anterior = 2 * (num_anterior+1)
            codigos.append(num_anterior)
    codigos_bin = []
    for nivel, codigo in zip(niveles,codigos):
        c_bin = str(bin(codigo))[2:]
        if len(c_bin) < nivel:
            # El nivel de ese caracter debe coincidir con el largo de la cadena de bits, por ejemplo si el primer caracter esta en el nivel 2, le corresponde el 00 no el 0
            # Para solucionarlo añadimos ceros a la izquierda
            codigos_bin.append("0" * (nivel - len(c_bin)) + c_bin)
        else:
            codigos_bin.append(c_bin)
    return {simbolo: c_bin for simbolo,c_bin in zip(simbolos,codigos_bin) }

x = frecuencias("./dna.50MB/dna.50MB")
#cadena = "panamabanana"
#lista = frecuencias_ejemplo(cadena)
lista = frecuencias(x)
#lista = sorted(lista,key=lambda x: x[1],reverse=True)
simbolos, niveles = calculo_niveles(lista)
codigo = generador_codigos(simbolos, niveles)
codigos_por_nivel = []
min_nivel = min(niveles)
max_nivel = max(niveles)
for i in range(min_nivel,max_nivel + 1):
    codigos_por_nivel.append(str(niveles.count(i)))

with open("prueba.txt","wt") as fichero:
        #RECUERDA ESTO, CUANDO VAYAS A DECODIFICAR, EL RETORNO DE CARRO LO TIENES QUE TENER CUENTA
    fichero.write(''.join(simbolos)+'\n')
    fichero.write(','.join([str(min_nivel),str(max_nivel)])+ '\n')
    fichero.write(','.join(codigos_por_nivel)+'\n')
    for letra in cadena:
        fichero.write(codigo[letra])

