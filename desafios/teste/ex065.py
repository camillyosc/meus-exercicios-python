n = int(input('Digite um número:'))
continuar = input('Deseja inserir outro número? (s/n): ').lower()
numeros = [n]
while continuar == 's':
  n = int(input('Digite um número:'))
  numeros.append(n)
  continuar = input('Deseja inserir outro número? (s/n): ').lower()
media = sum (numeros) / len (numeros)
maior = max(numeros)
menor = min(numeros)
print(f'A média dos números inseridos são: {media} o maior número é {maior} e o menor número é {menor}')
if continuar == 'n':
  print('Seu programa encerrou, você não quis digitar nenhum número a mais!')