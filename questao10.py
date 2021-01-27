#-*- coding: UTF-8 -*-
print('********** Jogo Craps **********\n')

from random import randint

primeira_jogada = 0
natural_list = [7,11]
craps_list = [2,3,12]
ponto_list = [4,5,6,8,9,10]

def craps():
  primeira_jogada = randint(2,13)
  if natural_list.__contains__(primeira_jogada):
    print('You are the master!! Congratulations!!', primeira_jogada)
  elif craps_list.__contains__(primeira_jogada):
    print('Craps!!! You lose!', primeira_jogada)
  elif ponto_list.__contains__(primeira_jogada):
    print('This is your number, lets play!! Number:', primeira_jogada)
    z = 0
    while primeira_jogada != z:
      s = input('Type "d" to roll the dice: ').upper()
      if s == 'D':
        z = randint(2,13)
        print('Your number was: ', z)
        if z == 7:
          print('You lose! Nobody said it was easy!!!')
          break
    if  z != 7:
      print('You win!!!')
craps()