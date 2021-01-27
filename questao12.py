# -*- coding: UTF-8 -*-
import random

print('******* Embaralha Palavra *******\n')


def palavra(x):
    embaralha = random.sample(x, len(x))
    a = ''.join(embaralha)
    print(a)


x = input('Digite algo: ')
palavra(x)