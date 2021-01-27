#-*- coding: UTF-8 -*-

def imprime_valores(n):
    for i in range (0, n):
        print(f'{i + 1}' * (i + 1))

n = int(input("Digite um numero inteiro: "))
imprime_valores(n)
