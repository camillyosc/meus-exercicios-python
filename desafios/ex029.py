velocidade = float(input('Digite quantos KM está a velocidade de seu carro:'))
if velocidade > 80:
  excesso = velocidade - 80
  multa = excesso * 7
  print(f'Você foi multado! Ultrapassou o limite em {excesso}')
  print(f'Pague {multa} de multa!')
else:
  print('Tudo está dentro dos conformes!')




