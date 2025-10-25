primo = 0
numero = int(input('Digite um número e descubra se ele é primo:'))
for c in range(1,11):
  if numero % c == 0:
    print(f"\033[33m{c}\033[0m", end=' ')
    primo += 1
  else:
    print(f"\033[31m{c}\033[0m",  end=' ' )
if primo > 2:
  print(f'\nEsse número foi divisível {primo} vezes, portanto ele não é primo!')
else:
  print(f'Esse número é primo! foi divisível somente {primo} vezes!')
    







