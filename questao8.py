# -*- coding: UTF-8 -*-
print('******* Quantidade Dígitos *******\n')


def digito(n):
    s = str(n)
    return len(s)


n = str(input('Informe um número: '))
print(f'Esse número tem {digito(n)} dígitos!')