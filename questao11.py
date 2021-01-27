#-*- coding: UTF-8 -*-
import re
data = input('Digite a data no formato DD/MM/AAAA: ')

def valida_data(data):
    padrao_mes = re.compile('[0-3]?\d/([0-1]?\d)/[1-2]\d{3}')
    padrao_dia = re.compile('([0-3]?\d)/[0-1]?\d/[1-2]\d{3}')
    padrao_ano = re.compile('[0-3]?\d/[0-1]?\d/([1-2]\d{3})')
    resultado_mes = re.findall(padrao_mes, data)
    resultado_dia = re.findall(padrao_dia, data)
    resultado_ano = re.findall(padrao_ano, data)


    return [resultado_dia,resultado_mes, resultado_ano]

print(valida_data(data))
dia = int(''.join(valida_data(data)[0]))
mes = int(''.join(valida_data(data)[1]))
ano = int(''.join(valida_data(data)[2]))

if mes == 1:
    print(f'{dia} de janeiro de {ano}')
elif mes == 2:
    print(f'{dia} de fevereiro de {ano}')
elif mes == 3:
    print(f'{dia} de marco de {ano}')
elif mes == 4:
    print(f'{dia} de abril de {ano}')
elif mes == 5:
    print(f'{dia} de maio de {ano}')
elif mes == 6:
    print(f'{dia} de junho de {ano}')
elif mes == 7:
    print(f'{dia} de julho de {ano}')
elif mes == 8:
    print(f'{dia} de agosto de {ano}')
elif mes == 9:
    print(f'{dia} de setembro de {ano}')
elif mes == 10:
    print(f'{dia} de outubro de {ano}')
elif mes == 11:
    print(f'{dia} de novembro de {ano}')
elif mes == 12:
    print(f'{dia} de dezembro de {ano}')
else:
    print('mes invalido')

