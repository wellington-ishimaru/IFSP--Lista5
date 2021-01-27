# -*- coding: UTF-8 -*-
print('******* Inverso do número *******\n')


def inverte_num(n):
    inverso = str(n)
    return inverso[::-1]


n = str(input('Informe um número: '))
print(f'O inverso do número é: {inverte_num(n)}')