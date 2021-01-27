# -*- coding: UTF-8 -*-
print('******* Somar Imposto *******\n')


def somar_imposto(taxa_imposto, custo):
  return ((taxa_imposto / 100) * custo) + custo


taxa_imposto = float(input("Informe o valor da taxa do imposto: "))
custo = float(input('Informe o valor do custo: '))

print(f'O valor final do produto é: {somar_imposto(taxa_imposto, custo)}')