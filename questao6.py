# -*- coding: UTF-8 -*-
print('******* Conversão de Horas *******\n')


def hora(h, m):
  b = int(h) / 12

  if b <= 1:
    hh = str(h)
    print('Sua hora: ' + hh + ':', end='')
  elif 1 < b < 2:
    hhh = str(h - 12)
    print('Sua hora: ' + hhh + ':', end='')
  else:
    print('Formato de hora invalido\n')

  if b < 1 and m <= 60:
    print(m, 'a.m')
  elif b >= 1 and m <= 60:
    print(m, 'p.m')
  else:
    print('Formato de minutos invalidos\n')


while True:
    print('Para sair, digite "s" para sair!\n')
    h = input('Hora: ').upper()
    if h == 's'.upper():
        break
    m = int(input('Minuto: '))
    hora(h, m)
    print('='*12)