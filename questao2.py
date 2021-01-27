#-*- coding: UTF-8 -*-

def imprime_valores(n):
    lista = []
    for i in range(0, n):
        lista.append(i+1)
        print(*lista, sep = ' ')

n = int(input("Digite um numero inteiro: "))
imprime_valores(n)
