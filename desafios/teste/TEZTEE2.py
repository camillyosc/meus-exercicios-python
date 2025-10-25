'''import random
print('Sou seu computador. Acabei de pensar em um número entre 0 e 10 será que você consegue adivinhar?')
computador = random.randint(0,10)
numero = int(input('Qual é o seu palpite?'))
tentativas = 1
while numero != computador:
  numero = int(input('Tente novamente! Qual é o seu palpite?'))
  tentativas += 1
if numero == computador and tentativas == 0:
  print(f'Parabéns! Você acertou de primeira!')
else:
  print(f'Parabéns! Você acertou! Foram {tentativas} tentativas!')'''

import random
computador = random.randint(0,10)
print('Sou seu computador. Acabei de pensar em um número entre 0 e 10 será que você consegue adivinhar?')
acertou = False
tentativas = 0
while not acertou:
  numero = int(input('Qual é o seu palpite?'))
  tentativas += 1

  if numero == computador:
    acertou = True
  
  else:
    if numero > computador:
      print('Menos...Tente novamente')
    elif numero < computador:
      print('Mais...Tente novamente')
      
if numero == computador and tentativas == 1:   
  print(f'Parabéns você acertou de primeira!')
else:
  print(f'Parabéns! Você acertou com {tentativas} tentativas!')
  

