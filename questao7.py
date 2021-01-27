#-*- coding: UTF-8 -*-
print('********** Prestacoes **********\n')

def valor_pagamento(prestacao, dias):
    return (prestacao*1.03) + (0.001*dias)
qtd = 0
total = 0

while True:
  p = float(input('Valor da prestação: '))
  if p == 0:
    print(f'Total pago: {round(total,2)}. Quantidade paga: {qtd}')
    break
  d = int(input('Dia em atraso: '))
  print(f'Valor total a ser pago: {round(valor_pagamento(p, d),2)}')
  print('\n')
  qtd += 1
  total += valor_pagamento(p, d)