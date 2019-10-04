#!/usr/bin/python3
import sys

nombre_fichero = sys.argv[1]

with open(nombre_fichero + ".sim") as fichero:
    list_char = list(fichero.read())

with open(nombre_fichero + ".nvl") as fichero:
    c_nivel = fichero.read().split(",")
    c_nivel = [int(x) for x in c_nivel]
    nvl_min = c_nivel.pop(0)
    nvl_max = c_nivel.pop(0)

with open(nombre_fichero + ".cmp") as fichero:
    cadena = fichero.read()

counter = 0
niveles = []

for i in range(nvl_min,nvl_max + 1):
    niveles.extend([i] * c_nivel[counter])
    counter += 1

c = 0
codigos = [nvl_min * "0"]
nivel_anterior = nvl_min
for nivel in niveles[1:]:
    c = 2 ** (nivel - nivel_anterior)*(c + 1)
    bin_c = bin(c)[2:]
    if len(bin_c) < nivel:
        codigos.append("0" * (nivel - len(bin_c)) + bin_c)
    else:
        codigos.append(bin_c)
    nivel_anterior = nivel

dicc = {clave: valor for clave, valor in zip(codigos, list_char)}

largo_codigo = [i + nvl_min for i,j in enumerate(c_nivel) if j != 0]

cadena_desc = ""
i = 0
while i != len(cadena):
    for num_bits in largo_codigo:
        temp = dicc.get(cadena[i:i + num_bits])
        if temp != None:
            i += num_bits
            cadena_desc += temp
            break
    else:
        raise Exception("No se puede descomprimir")

print(cadena_desc)

