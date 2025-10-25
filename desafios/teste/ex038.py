n1 = int(input('Digite um número:'))
n2 = int(input('Digite mais um número:'))
if n1 > n2:
  print(f'O primeiro valor {n1} é maior que {n2}')
elif n2 > n1:
  print(f'O segundo valor \033[34;2m{n2}\033[m  é maior que {n1}')
else:
  print('Não existe valor maior, os dois são iguais!')

