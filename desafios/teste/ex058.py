import random
import time
adivinhar = 0
adivinharcont = 0
print('O computador está pensando em número...')
numeropc = random.randint(0, 10)
while adivinhar != numeropc:
  adivinhar = int(input('Tente adivinhar o número que o computador está pensando:'))
  print('PROCESSANDO...')
  time.sleep(1)
  adivinharcont += 1 
  if adivinhar == numeropc:
    print(f'Parabéns você acertou! Foram {adivinharcont} tentativas!  ')