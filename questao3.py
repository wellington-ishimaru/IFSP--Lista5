#-*- coding: UTF-8 -*-

def soma (num1, num2, num3):
    return num1 + num2 + num3

numeros = []
for i in range(0, 3):
    numeros.append(float(input(f"Digite o numero {i + 1} de 3: ")))

print(f'A soma dos 3 numeros e igual: {soma(numeros[0], numeros[1], numeros[2])}')
