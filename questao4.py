# -*- coding: UTF-8 -*-
print('******* Positivo, Negativo ou Nulo *******\n')


def pn(x):
    if x <= 0:
        return "N"
    else:
        return "P"


x = int(input('Informe um número: '))
print(f'O número informado é: {pn(x)}')