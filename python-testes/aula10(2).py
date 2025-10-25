'''n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digitee sua segunda nota:'))
m = (n1+n2)/2
print(f'A sua média foi {m:.1f}')
if m >= 6:
  print('PARABÉNS! Você atingiu a média!')
else:
  print('Infelizmente você não atingiu a média! Estude mais!')'''

#pode fazer assim também (de forma simplificada):
n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digitee sua segunda nota:'))
m = (n1+n2)/2
print(f'A sua média foi {m:.1f}')
print('PARABÉNS!' if m >= 6 else 'Estude mais!')
