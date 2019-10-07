#!/usr/bin/python3
from collections import OrderedDict
cadena = "abbabcabbabcb"

dicc = OrderedDict()
dicc[cadena[0]] = 1
largo_maximo = 2
fin_cadena = len(cadena) -1
i = 1 
contador = 1
resultado = []
with open("prueba.txt", "wt") as file:
    print(0, cadena[0])
    file.write(f"0 {cadena[0]}\n")

    while i + largo_maximo < fin_cadena:
        for j in range(largo_maximo,1,-1):
            temp = cadena[i: i + j - 1]
            if temp in dicc.keys():
                print(list(dicc.keys()).index(temp) + 1, cadena[i + j - 1])
                file.write(f"{list(dicc.keys()).index(temp) + 1} {cadena[i+j-1]}\n")
                contador += 1
                dicc[temp + cadena[i + j - 1]] = contador
                if largo_maximo >= j:
                    largo_maximo += 1
                i += j
                break
        else:
            print(0,cadena[i])
            file.write(f"0 {cadena[i]}\n")
            contador += 1
            dicc[cadena[i]] = contador
            i += 1

    print(dicc)
    largo_maximo = fin_cadena - i + 1
    while largo_maximo > 0:
        for j in range(largo_maximo,1,-1):
            temp = cadena[i: i + j -1]
            if temp in dicc.keys():
                largo_maximo -= j - 1
                if largo_maximo == 0:
                    print(list(dicc.keys()).index(temp) + 1, 'nada')
                    file.write(f"{list(dicc.keys()).index(temp) + 1} \n")
                    break
                else:
                    contador += 1
                    print(list(dicc.keys()).index(temp) + 1, cadena[i + j - 1])
                    file.write(f"{list(dicc.keys()).index(temp) + 1} {cadena[i+j-1]}\n")
                    dicc[temp + cadena[i + j - 1]] = contador
                    i += j
                    largo_maximo -= 1
                    break
        else:
            largo_maximo -= 1
            if largo_maximo == 0:
                if cadena[i] in dicc.keys():
                    print(list(dicc.keys()).index(cadena[i]) +1,"nada ")
                    file.write(f"{list(dicc.keys()).index(cadena[i])+1} \n")
                else:
                    print(0,cadena[i])
                    file.write(f"0 {cadena[i]}\n")
                    dicc[cadena[i]] = contador
            else:
                print(0,cadena[i])
                file.write(f"0 {cadena[i]}\n")
                contador += 1
                dicc[cadena[i]] = contador
            i += 1
