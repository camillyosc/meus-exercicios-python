import time
from random import randint
itens = ('pedra', 'papel', 'tesoura')
computadorescolha = randint(0, 2)
print('''SUAS OPÇÕES:
  [0] PEDRA
  [1] PAPEL
  [2] TESOURA ''')
jogador = int(input('Qual é a sua jogada?'))
print('JO') 
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
print('-=' * 20)
print(f'O computador escolheu {(itens[computadorescolha])}')
print(f'Você escolheu {(itens[jogador])}')
print('-=' * 20)
if computadorescolha == 0:
    if jogador == 0:
        print('EMPATE!' )
    elif jogador == 1:
        print('VOCÊ VENCEU!')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU!')      
    else:
        print('JOGADA INVÁLIDA!')

elif computadorescolha == 1:
    if jogador == 0:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCÊ VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')

elif computadorescolha == 2:
    if jogador == 0:
        print('VOCÊ VENCEU!')
    elif jogador == 1:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')


