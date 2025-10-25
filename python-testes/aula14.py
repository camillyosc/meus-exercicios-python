'''n = 1
while n != 0:
  n = int(input('Digite um valor:'))
  if n % 2 == 0:
    print(f'Foi digitado {n} números pares!')
  else:
    print(f'Foi digitado {n} números impares!')
print('Acabou')'''


n = 1
par = impar = 0
while n != 0:
  n = int(input('Digite um valor:'))
  if n != 0:
    if n % 2 == 0:
      par += 1
    else:
      impar += 1
print(f'Foi digitado {par} números pares!')
print(f'Foi digitado {impar} números impares!')
print('Acabou')
