import random
import time
print('O computador está pensando um número de 0 a 5...')
numero_secreto = random.randint(0, 5)
descubra = int(input('Descubra o número que o computador pensou entre 0 e 5:'))
print('PROCESSANDO...')
time.sleep(3)
if descubra == numero_secreto:
  print('Parabéns! Você acertou!')
else:
  print('Não foi dessa vez!')