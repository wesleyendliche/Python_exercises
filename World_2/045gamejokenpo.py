from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('Suas opções:')
print('[ 0 ] PEDRA \n[ 1 ] PAPEL \n[ 2 ] TESOURA')
op = int(input('Qual é a sua jogada?'))
print('JO ')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=-' * 20)
print('Computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}.'.format(itens[op]))
print('-=-' * 20)
if pc == 0: #computador jogou PEDRA
    if op == 0:
        print('EMPATE!')
    elif op == 1:
        print('JOGADOR VENCE')
    elif op == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 1: #computador jogou PAPEL
    if op == 0:
        print('COMPUTADOR VENCE')
    elif op == 1:
        print('EMPATE!')
    elif op == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif pc ==2: #computador jogou TESOURA
    if op == 0:
        print('JOGADOR VENCE')
    elif op == 1:
        print('COMPUTADOR VENCE')
    elif op == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
